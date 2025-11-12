# 🎬 Auto Video Generator

Automatically generate videos from audio and images with customizable presets for different social media platforms (YouTube, TikTok, Instagram, Facebook, etc.). The title is automatically extracted from the audio filename and displayed at the top center of the video.

## ✨ Features

- 🎵 **Auto Title from Audio**: Automatically uses audio filename as video title (e.g., "for love.mp3" → "For Love")
- 📱 **Platform Presets**: Pre-configured for YouTube, TikTok, Instagram, Facebook
- 🎨 **Customizable**: Full control over video size, title style, transitions
- 📦 **Batch Processing**: Process multiple audio files at once
- 🎬 **Professional Output**: High-quality MP4 videos with proper encoding

## 📋 Supported Platforms

| Platform | Preset Name | Resolution | Aspect Ratio |
|----------|-------------|------------|--------------|
| YouTube Standard | `youtube` | 1920x1080 | 16:9 |
| YouTube Shorts | `youtube_short` | 1080x1920 | 9:16 |
| TikTok | `tiktok` | 1080x1920 | 9:16 |
| Instagram Post | `instagram_post` | 1080x1080 | 1:1 |
| Instagram Story/Reels | `instagram_story` | 1080x1920 | 9:16 |
| Facebook | `facebook` | 1280x720 | 16:9 |
| Custom | `custom` | Configurable | Any |

## 🚀 Installation

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Install FFmpeg (Required)

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

**Windows:**
Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH

## 📁 Project Structure

```
auto-video-generator/
├── main.py                 # Main entry point
├── requirements.txt        # Python dependencies
├── config/
│   └── presets.json       # Video presets configuration
├── src/
│   └── video_generator.py # Core video generation logic
├── assets/
│   ├── audio/             # Place your audio files here
│   ├── images/            # Place your images here
│   └── videos/            # Sample videos (optional)
└── output/                # Generated videos output folder
```

## 🎯 Quick Start

### 1. Prepare Your Assets

Place your files in the appropriate folders:
- **Audio**: `assets/audio/` (MP3, WAV, M4A, AAC, OGG)
- **Images**: `assets/images/` (PNG, JPG, JPEG, GIF, BMP)

### 2. Generate a Video

**Basic Example:**
```bash
python main.py -a "assets/audio/for love.mp3" -i assets/images -p youtube
```

This will create a YouTube video with the title "For Love" displayed at the top center.

**TikTok Video:**
```bash
python main.py -a "assets/audio/my song.mp3" -i assets/images -p tiktok
```

**Instagram Reels:**
```bash
python main.py -a "assets/audio/trending sound.mp3" -i assets/images -p instagram_story
```

### 3. Advanced Usage

**Custom Title:**
```bash
python main.py -a "assets/audio/song.mp3" -i assets/images -p youtube -t "My Custom Title"
```

**Specify Output Path:**
```bash
python main.py -a "assets/audio/song.mp3" -i assets/images -p tiktok -o "my_tiktok_video.mp4"
```

**Custom Image Duration:**
```bash
python main.py -a "assets/audio/song.mp3" -i assets/images -p youtube -d 3.5
```
(Each image will display for 3.5 seconds)

**Use Specific Images:**
```bash
python main.py -a "assets/audio/song.mp3" -i "img1.jpg,img2.jpg,img3.jpg" -p youtube
```

## 🔄 Batch Processing

Process multiple audio files at once:

```bash
python main.py --batch -af assets/audio -i assets/images -p youtube
```

This will:
1. Find all audio files in `assets/audio/`
2. Generate a video for each using images from `assets/images/`
3. Save output to `output/` folder with format: `{audio_name}_{preset}.mp4`

## 🎨 Customization

### List Available Presets

```bash
python main.py --list-presets
```

### Modify Title Style

Edit `config/presets.json` to customize title appearance:

```json
{
  "title_style": {
    "font": "Arial-Bold",
    "fontsize": 60,
    "color": "white",
    "stroke_color": "black",
    "stroke_width": 3,
    "position": "top"
  }
}
```

### Add Custom Preset

Add a new preset to `config/presets.json`:

```json
{
  "presets": {
    "my_custom": {
      "width": 1920,
      "height": 1080,
      "fps": 60,
      "aspect_ratio": "16:9",
      "description": "My Custom Preset"
    }
  }
}
```

## 📖 Usage Examples

### Example 1: Create YouTube Video

```bash
# Audio file: "for love.mp3"
# Output: Video with title "For Love" at top center
python main.py -a "assets/audio/for love.mp3" -i assets/images -p youtube
```

### Example 2: Create Multiple TikTok Videos

```bash
# Process all audio files in folder
python main.py --batch -af assets/audio -i assets/images -p tiktok
```

### Example 3: Instagram Reels with Custom Title

```bash
python main.py -a "assets/audio/summer vibes.mp3" -i assets/images -p instagram_story -t "Summer Vibes 2025"
```

### Example 4: YouTube Shorts

```bash
python main.py -a "assets/audio/quick tip.mp3" -i assets/images -p youtube_short
```

## 🛠️ Command Line Options

```
Required Arguments:
  -a, --audio          Path to audio file
  -i, --images         Path to images folder or comma-separated image paths

Optional Arguments:
  -o, --output         Output video path (default: auto-generated)
  -p, --preset         Video preset (default: youtube)
  -t, --title          Custom title (default: from audio filename)
  -d, --duration       Duration for each image in seconds

Batch Processing:
  --batch             Enable batch processing mode
  -af, --audio-folder  Folder containing audio files

Utility:
  --list-presets      List all available presets
  -c, --config        Path to config file (default: config/presets.json)
```

## 🎵 Title Extraction Rules

The title is automatically extracted from the audio filename:

| Audio Filename | Displayed Title |
|----------------|-----------------|
| `for love.mp3` | For Love |
| `my_song.mp3` | My Song |
| `SUMMER VIBES.wav` | Summer Vibes |
| `best-song-ever.mp3` | Best-Song-Ever |

**Note**: Underscores and spaces are converted to spaces, and each word is capitalized.

## 🎬 Video Output

Generated videos will have:
- ✅ Audio from source file
- ✅ Images displayed sequentially (with smooth transitions)
- ✅ Title text at top center (white with black outline)
- ✅ High-quality encoding (H.264 video, AAC audio)
- ✅ Proper aspect ratio for selected platform

## 📝 Tips & Best Practices

1. **Image Quality**: Use high-resolution images (1920x1080 or higher)
2. **Image Count**: More images = smoother video transitions
3. **Audio Format**: MP3 or WAV recommended for best compatibility
4. **File Naming**: Use descriptive audio filenames (they become titles!)
5. **Batch Processing**: Organize audio files in one folder for efficiency

## 🐛 Troubleshooting

**Error: "No images found"**
- Check that images folder exists and contains supported formats (PNG, JPG, etc.)

**Error: "FFmpeg not found"**
- Install FFmpeg and ensure it's in your system PATH

**Video quality is low**
- Edit `config/presets.json` and increase `bitrate` value

**Title doesn't appear**
- Check that font "Arial-Bold" is installed on your system
- Or change font in `config/presets.json`

## 📄 License

MIT License - Free to use for personal and commercial projects.

## 🤝 Contributing

Feel free to submit issues, fork the repository, and create pull requests!

## 💡 Future Features

- [ ] Add video effects and filters
- [ ] Support for video clips (not just images)
- [ ] Multiple title positions and animations
- [ ] Background music mixing
- [ ] Watermark support
- [ ] Real-time preview
- [ ] Web interface

---

**Made with ❤️ for content creators**
