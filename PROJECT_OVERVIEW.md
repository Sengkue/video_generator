# 📋 Project Overview - Auto Video Generator

## 🎯 Project Purpose

This project automatically generates professional videos by combining:
- 🎵 Audio files (MP3, WAV, etc.)
- 🖼️ Images (JPG, PNG, etc.)
- 📝 Auto-generated titles from audio filenames

**Key Feature**: Audio filename "for love.mp3" automatically becomes video title "For Love" displayed at top center!

## 📦 Project Structure

```
auto-video-generator/
│
├── main.py                      # Main CLI entry point
├── examples.py                  # Usage examples
├── setup_test.py               # Setup and testing script
├── preset_manager.py           # Configuration manager
├── requirements.txt            # Python dependencies
├── README.md                   # Full documentation
├── QUICKSTART.md              # Quick start guide
├── .gitignore                 # Git ignore rules
│
├── config/
│   └── presets.json           # Video presets (YouTube, TikTok, etc.)
│
├── src/
│   └── video_generator.py    # Core video generation logic
│
├── assets/
│   ├── audio/                 # Your audio files (.mp3, .wav, etc.)
│   ├── images/                # Your images (.jpg, .png, etc.)
│   └── videos/                # Optional video clips
│
└── output/                    # Generated videos output
```

## 🏗️ Architecture

### Core Components

1. **VideoGenerator Class** (`src/video_generator.py`)
   - Main video creation engine
   - Handles image resizing and positioning
   - Creates title overlays
   - Manages audio synchronization
   - Supports batch processing

2. **Configuration System** (`config/presets.json`)
   - Platform presets (YouTube, TikTok, Instagram, etc.)
   - Title styling configuration
   - Video encoding settings
   - Easily customizable

3. **CLI Interface** (`main.py`)
   - Command-line argument parsing
   - Single and batch video generation
   - Preset management
   - User-friendly error messages

### Key Technologies

- **MoviePy**: Video editing and composition
- **Pillow (PIL)**: Image processing
- **NumPy**: Array operations
- **FFmpeg**: Video encoding (system dependency)
- **Pydub**: Audio processing

## 🔄 Video Generation Workflow

```
1. Load Audio File
   ↓
2. Extract Title from Filename
   ↓
3. Load Configuration & Preset
   ↓
4. Load Images
   ↓
5. Calculate Timing
   ↓
6. Resize & Position Images
   ↓
7. Create Image Clips
   ↓
8. Generate Title Overlay
   ↓
9. Composite All Elements
   ↓
10. Add Audio Track
   ↓
11. Render Final Video
   ↓
12. Save to Output
```

## 📝 Title Generation Logic

```python
# Example: "for love.mp3" → "For Love"

1. Extract filename without extension: "for love"
2. Split by spaces/underscores: ["for", "love"]
3. Capitalize each word: ["For", "Love"]
4. Join with spaces: "For Love"
5. Display at video top center
```

## 🎬 Supported Platforms

| Platform | Preset | Resolution | Aspect | Use Case |
|----------|--------|------------|--------|----------|
| YouTube | `youtube` | 1920x1080 | 16:9 | Standard videos |
| YouTube Shorts | `youtube_short` | 1080x1920 | 9:16 | Vertical shorts |
| TikTok | `tiktok` | 1080x1920 | 9:16 | TikTok videos |
| Instagram | `instagram_story` | 1080x1920 | 9:16 | Stories/Reels |
| Instagram | `instagram_post` | 1080x1080 | 1:1 | Feed posts |
| Facebook | `facebook` | 1280x720 | 16:9 | Facebook videos |

## 🔧 Configuration Options

### Preset Configuration
```json
{
  "width": 1920,
  "height": 1080,
  "fps": 30,
  "aspect_ratio": "16:9",
  "description": "YouTube Standard HD"
}
```

### Title Style Configuration
```json
{
  "font": "Arial-Bold",
  "fontsize": 60,
  "color": "white",
  "stroke_color": "black",
  "stroke_width": 3,
  "position": "top"
}
```

### Video Encoding Settings
```json
{
  "codec": "libx264",
  "audio_codec": "aac",
  "bitrate": "5000k",
  "audio_bitrate": "192k"
}
```

## 🚀 Usage Modes

### 1. Single Video Generation
```bash
python main.py -a "audio.mp3" -i images/ -p youtube
```

### 2. Batch Processing
```bash
python main.py --batch -af audio_folder/ -i images/ -p tiktok
```

### 3. Custom Configuration
```bash
python main.py -a "audio.mp3" -i images/ -p youtube -t "Custom Title" -d 3
```

## 📊 Performance Considerations

- **Image Processing**: Images are resized to fit preset dimensions
- **Memory Usage**: Depends on number and size of images
- **Rendering Time**: Varies with video length and complexity
- **Output Quality**: Configurable via bitrate settings

## 🔐 Best Practices

1. **Image Quality**: Use high-resolution images (1920x1080+)
2. **Image Count**: 5-20 images for smooth transitions
3. **Audio Format**: MP3 or WAV for best compatibility
4. **Filename Convention**: Use descriptive names (they become titles!)
5. **Batch Processing**: Organize files by platform/project

## 🎨 Customization Guide

### Add New Preset
```bash
python preset_manager.py add
# Follow interactive prompts
```

### Modify Title Style
```bash
python preset_manager.py title
# Edit font size, color, stroke, etc.
```

### Custom Video Settings
Edit `config/presets.json` directly for advanced options

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| FFmpeg not found | Install FFmpeg on system |
| No images found | Check images folder path |
| Title not showing | Verify font is installed |
| Poor video quality | Increase bitrate in config |
| Slow rendering | Reduce image count or size |

## 📈 Future Enhancements

Potential features for future versions:
- ✨ Video effects and transitions
- 🎞️ Video clip support (not just images)
- 🎬 Animated title effects
- 🎵 Background music mixing
- 🖼️ Watermark support
- 📱 Web interface
- 🤖 AI-powered image selection
- 📊 Progress bars and previews

## 📄 License

MIT License - Free for personal and commercial use

## 🤝 Contributing

Contributions welcome! Areas to improve:
- Add more presets
- Improve title animations
- Add video effects
- Create web interface
- Optimize performance

## 📞 Support

For issues or questions:
1. Check README.md documentation
2. Review examples in examples.py
3. Test setup with setup_test.py
4. Check configuration with preset_manager.py

---

**Built for content creators who want automated, professional video generation!** 🎬
