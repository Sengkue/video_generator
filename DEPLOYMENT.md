# 🚀 Deployment Guide - Auto Video Generator

## 📥 Installation Steps

### Step 1: System Requirements

**Operating System:**
- Linux (Ubuntu 20.04+ recommended)
- macOS (10.14+)
- Windows 10/11

**Software:**
- Python 3.7 or higher
- FFmpeg (for video encoding)
- Git (optional, for version control)

### Step 2: Install FFmpeg

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

**macOS (with Homebrew):**
```bash
brew install ffmpeg
```

**Windows:**
1. Download from: https://ffmpeg.org/download.html
2. Extract to C:\ffmpeg
3. Add to PATH: `C:\ffmpeg\bin`
4. Verify: Open CMD and type `ffmpeg -version`

### Step 3: Install Python Dependencies

```bash
cd auto-video-generator
pip install -r requirements.txt
```

**If you encounter issues:**
```bash
# Use virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Step 4: Verify Installation

```bash
python setup_test.py
```

This will:
- ✅ Check Python version
- ✅ Verify FFmpeg installation
- ✅ Test Python dependencies
- ✅ Create sample assets
- ✅ Test video generation

## 🎬 First Video Generation

### Quick Test

```bash
# 1. Add an audio file
cp your_audio.mp3 assets/audio/

# 2. Add some images
cp your_images/* assets/images/

# 3. Generate video
python main.py -a "assets/audio/your_audio.mp3" -i assets/images -p youtube
```

### Expected Output

```
Creating video: Your Audio
Preset: youtube (1920x1080)
Audio duration: 30.5s
Number of images: 5
Duration per image: 6.1s
Rendering video to: output/your_audio_youtube.mp4
✓ Video created successfully: output/your_audio_youtube.mp4
```

## 🏢 Production Deployment

### Option 1: Local Server

**Setup as a system service (Linux):**

1. Create service file:
```bash
sudo nano /etc/systemd/system/video-generator.service
```

2. Add content:
```ini
[Unit]
Description=Auto Video Generator Service
After=network.target

[Service]
Type=simple
User=your_user
WorkingDirectory=/path/to/auto-video-generator
ExecStart=/usr/bin/python3 /path/to/auto-video-generator/main.py --batch -af /path/to/audio -i /path/to/images -p youtube
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

3. Enable and start:
```bash
sudo systemctl enable video-generator
sudo systemctl start video-generator
```

### Option 2: Docker Deployment

**Create Dockerfile:**
```dockerfile
FROM python:3.9-slim

# Install FFmpeg
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Create necessary directories
RUN mkdir -p assets/audio assets/images output

# Set entrypoint
ENTRYPOINT ["python", "main.py"]
```

**Build and run:**
```bash
# Build image
docker build -t auto-video-generator .

# Run container
docker run -v $(pwd)/assets:/app/assets -v $(pwd)/output:/app/output auto-video-generator -a "assets/audio/song.mp3" -i assets/images -p youtube
```

### Option 3: Cloud Deployment (AWS)

**Using AWS Lambda (for batch processing):**

1. Create Lambda function
2. Package project with dependencies
3. Set up S3 buckets for input/output
4. Configure triggers (S3 upload events)

**Using AWS EC2:**
```bash
# SSH into EC2 instance
ssh ubuntu@your-ec2-ip

# Install dependencies
sudo apt-get update
sudo apt-get install python3-pip ffmpeg git

# Clone/upload project
git clone your-repo-url
cd auto-video-generator

# Install Python packages
pip3 install -r requirements.txt

# Run
python3 main.py --batch -af assets/audio -i assets/images -p youtube
```

## 🔄 Automated Workflows

### Cron Job (Linux/Mac)

**Edit crontab:**
```bash
crontab -e
```

**Add job (runs daily at 2 AM):**
```bash
0 2 * * * cd /path/to/auto-video-generator && python3 main.py --batch -af assets/audio -i assets/images -p youtube >> logs/cron.log 2>&1
```

### Task Scheduler (Windows)

1. Open Task Scheduler
2. Create Basic Task
3. Set trigger (daily, weekly, etc.)
4. Set action: Run program
   - Program: `python.exe`
   - Arguments: `C:\path\to\main.py --batch -af assets/audio -i assets/images -p youtube`
   - Start in: `C:\path\to\auto-video-generator`

## 📊 Monitoring and Logging

### Enable Logging

**Add to main.py:**
```python
import logging

logging.basicConfig(
    filename='logs/video_generator.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
```

### Monitor Output

```bash
# Watch logs in real-time
tail -f logs/video_generator.log

# Check recent errors
grep ERROR logs/video_generator.log | tail -n 20
```

## 🔐 Security Best Practices

### File Permissions

```bash
# Restrict configuration files
chmod 600 config/presets.json

# Protect output directory
chmod 755 output/
```

### Input Validation

The project includes basic validation:
- File type checking
- Path sanitization
- Size limits (configurable)

### Production Recommendations

1. **Run as non-root user**
2. **Limit file upload sizes**
3. **Sanitize filenames**
4. **Use environment variables for sensitive config**
5. **Regular security updates**

## 🎯 Performance Optimization

### For High Volume Processing

**1. Use SSD storage for faster I/O**

**2. Optimize image loading:**
```python
# In video_generator.py, use PIL.Image.open with mode
from PIL import Image
img = Image.open(path).convert('RGB')
```

**3. Multi-threading for batch:**
```python
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=4) as executor:
    executor.map(process_video, audio_files)
```

**4. GPU acceleration (if available):**
Install GPU-enabled MoviePy and FFmpeg with NVIDIA codec support

### Memory Management

```python
# Clear memory after each video
import gc
gc.collect()
```

## 🔧 Troubleshooting Production Issues

### Issue: Out of Memory

**Solution:**
- Process videos sequentially instead of batch
- Reduce image resolution before processing
- Increase system swap space

### Issue: Slow Rendering

**Solution:**
- Use lower FPS (24 instead of 30)
- Reduce bitrate for faster encoding
- Process smaller batches

### Issue: Font Not Found

**Solution:**
```bash
# Install common fonts (Ubuntu)
sudo apt-get install fonts-liberation fonts-dejavu

# Or update config to use available font
python preset_manager.py title
```

## 📈 Scaling

### Horizontal Scaling

**Multiple Workers:**
```bash
# Worker 1
python main.py --batch -af batch1/ -i images/ -p youtube

# Worker 2
python main.py --batch -af batch2/ -i images/ -p youtube
```

**Queue System (with Redis):**
- Use Celery for task queue
- Distribute processing across multiple servers
- Monitor with Flower dashboard

### Vertical Scaling

- Increase CPU cores for parallel processing
- Add more RAM for larger videos
- Use faster storage (NVMe SSD)

## 🎬 Ready for Production!

Your auto video generator is now:
- ✅ Installed and tested
- ✅ Configured for your needs
- ✅ Deployed and running
- ✅ Monitored and optimized

**Start generating amazing videos!** 🚀

---

**Need help?** Check the README.md or PROJECT_OVERVIEW.md for detailed information.
