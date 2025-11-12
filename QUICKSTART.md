# 🚀 Quick Start Guide

## 1. Install Dependencies

```bash
pip install -r requirements.txt
```

**Important**: Make sure FFmpeg is installed on your system!
- Ubuntu/Debian: `sudo apt-get install ffmpeg`
- macOS: `brew install ffmpeg`
- Windows: Download from ffmpeg.org

## 2. Add Your Files

### Add Audio Files
Place your audio files in `assets/audio/`:
```
assets/audio/
├── for love.mp3
├── summer vibes.mp3
└── my song.wav
```

### Add Images
Place your images in `assets/images/`:
```
assets/images/
├── image1.jpg
├── image2.jpg
├── image3.png
└── image4.jpg
```

**Tip**: Use at least 5-10 images for smoother videos!

## 3. Generate Your First Video

### Simple YouTube Video
```bash
python main.py -a "assets/audio/for love.mp3" -i assets/images -p youtube
```

**Result**: Creates `output/for love_youtube.mp4` with title "For Love" at top center!

### TikTok Video
```bash
python main.py -a "assets/audio/for love.mp3" -i assets/images -p tiktok
```

### Instagram Reels
```bash
python main.py -a "assets/audio/for love.mp3" -i assets/images -p instagram_story
```

## 4. Check Your Output

Find your video in the `output/` folder!

## 5. Advanced: Batch Processing

Process all audio files at once:
```bash
python main.py --batch -af assets/audio -i assets/images -p youtube
```

## Common Commands Cheat Sheet

```bash
# List all presets
python main.py --list-presets

# Custom title
python main.py -a audio.mp3 -i assets/images -p youtube -t "My Title"

# Custom output path
python main.py -a audio.mp3 -i assets/images -p tiktok -o my_video.mp4

# Set image duration (3 seconds per image)
python main.py -a audio.mp3 -i assets/images -p youtube -d 3

# Use specific images only
python main.py -a audio.mp3 -i "img1.jpg,img2.jpg,img3.jpg" -p youtube
```

## Platform Presets

| Preset | Size | Best For |
|--------|------|----------|
| `youtube` | 1920x1080 | YouTube videos |
| `youtube_short` | 1080x1920 | YouTube Shorts |
| `tiktok` | 1080x1920 | TikTok videos |
| `instagram_story` | 1080x1920 | IG Reels/Stories |
| `instagram_post` | 1080x1080 | IG Feed posts |
| `facebook` | 1280x720 | Facebook videos |

## Need Help?

Check the full README.md for detailed documentation!
