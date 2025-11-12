# ❓ Frequently Asked Questions (FAQ)

## 📋 General Questions

### Q: What does this project do?
**A:** It automatically creates videos from audio files and images, with the audio filename displayed as a title at the top center of the video. Perfect for creating content for YouTube, TikTok, Instagram, and more!

### Q: Why would I use this?
**A:** 
- ⏱️ Save time on repetitive video creation
- 📱 Create platform-optimized videos automatically
- 🎨 Consistent branding across all videos
- 📦 Batch process multiple videos at once

### Q: Do I need programming experience?
**A:** No! Just install the requirements and use simple command-line commands. Examples are provided.

---

## 🔧 Installation & Setup

### Q: What do I need to install?
**A:** 
1. Python 3.7 or higher
2. FFmpeg (video encoder)
3. Python packages (via `pip install -r requirements.txt`)

### Q: How do I know if everything is installed correctly?
**A:** Run the test script:
```bash
python setup_test.py
```
It will check all requirements and create sample assets.

### Q: FFmpeg installation failed. What should I do?
**A:** 
- **Ubuntu/Debian:** `sudo apt-get install ffmpeg`
- **macOS:** `brew install ffmpeg`
- **Windows:** Download from ffmpeg.org and add to PATH

### Q: Can I use Python 2?
**A:** No, Python 3.7+ is required. MoviePy and other libraries need Python 3.

---

## 🎬 Video Generation

### Q: How does the title extraction work?
**A:** The title is automatically extracted from the audio filename:
- File: `for love.mp3` → Title: "For Love"
- File: `summer_vibes.mp3` → Title: "Summer Vibes"
- File: `MY-SONG.wav` → Title: "My-Song"

Spaces and underscores become spaces, and each word is capitalized.

### Q: Can I use a custom title instead of the filename?
**A:** Yes! Use the `-t` or `--title` flag:
```bash
python main.py -a "audio.mp3" -i images/ -p youtube -t "My Custom Title"
```

### Q: How many images do I need?
**A:** At least 1 image, but 5-10 images work best for smooth transitions. More images = smoother video.

### Q: What image formats are supported?
**A:** JPG, JPEG, PNG, GIF, and BMP

### Q: What audio formats are supported?
**A:** MP3, WAV, M4A, AAC, and OGG

### Q: How long does it take to generate a video?
**A:** Depends on:
- Video length (30s video: ~30-60 seconds)
- Number of images
- Video resolution
- Computer performance

### Q: Can I see a preview before rendering?
**A:** Not currently. This is a planned feature for future versions.

---

## 📱 Platform-Specific Questions

### Q: What's the difference between presets?
**A:**
- `youtube`: 1920x1080 (16:9) - Standard YouTube videos
- `youtube_short`: 1080x1920 (9:16) - YouTube Shorts
- `tiktok`: 1080x1920 (9:16) - TikTok videos
- `instagram_story`: 1080x1920 (9:16) - Instagram Reels/Stories
- `instagram_post`: 1080x1080 (1:1) - Instagram feed posts
- `facebook`: 1280x720 (16:9) - Facebook videos

### Q: Can I create videos for multiple platforms at once?
**A:** Yes! Run the command multiple times with different presets:
```bash
python main.py -a "audio.mp3" -i images/ -p youtube
python main.py -a "audio.mp3" -i images/ -p tiktok
python main.py -a "audio.mp3" -i images/ -p instagram_story
```

### Q: How do I add a new platform preset?
**A:** Use the preset manager:
```bash
python preset_manager.py add
```
Follow the interactive prompts.

---

## 🎨 Customization

### Q: Can I change the title style (font, color, size)?
**A:** Yes! Use the preset manager:
```bash
python preset_manager.py title
```
Or edit `config/presets.json` directly.

### Q: Can I change the title position?
**A:** Currently, titles are positioned at top center. Custom positioning is planned for future versions.

### Q: Can I add a watermark?
**A:** Not yet, but this is a planned feature. You can manually add watermarks to images before processing.

### Q: Can I change video quality?
**A:** Yes! Edit the bitrate in `config/presets.json`:
```json
"video_settings": {
  "bitrate": "5000k",  // Higher = better quality
  "audio_bitrate": "192k"
}
```

---

## 📦 Batch Processing

### Q: How do I process multiple audio files at once?
**A:** Use the `--batch` flag:
```bash
python main.py --batch -af assets/audio -i assets/images -p youtube
```

### Q: Can I use different images for each audio file?
**A:** Currently, no. The same image set is used for all videos in batch mode. This feature may be added in future versions.

### Q: What happens if one video fails during batch processing?
**A:** The process continues with the next file. Failed videos are reported at the end with error messages.

---

## 🐛 Troubleshooting

### Q: Error: "No images found"
**A:** Check that:
1. Images folder exists: `assets/images/`
2. Contains supported formats (JPG, PNG, etc.)
3. Path is correct in command

### Q: Error: "FFmpeg not found"
**A:** FFmpeg is not installed or not in system PATH. Install FFmpeg and verify with:
```bash
ffmpeg -version
```

### Q: Title doesn't appear in video
**A:** The font might not be installed. Install Arial or edit `config/presets.json` to use an available font:
```bash
# Ubuntu: Install common fonts
sudo apt-get install fonts-liberation
```

### Q: Video quality is poor
**A:** Increase bitrate in `config/presets.json`:
```json
"bitrate": "8000k"  // Increase from 5000k
```

### Q: Rendering is very slow
**A:** Try:
1. Reduce FPS (30 → 24)
2. Lower bitrate
3. Use fewer/smaller images
4. Close other programs

### Q: Error: "Memory error" or "Out of memory"
**A:** 
1. Process fewer videos at once
2. Use smaller images
3. Close other programs
4. Increase system RAM/swap

---

## 💾 File Management

### Q: Where are output videos saved?
**A:** In the `output/` folder by default. You can specify a custom path with `-o`:
```bash
python main.py -a "audio.mp3" -i images/ -p youtube -o "my_folder/video.mp4"
```

### Q: What's the output filename format?
**A:** `{audio_name}_{preset}.mp4`
- Example: `for love_youtube.mp4`

### Q: Can I change the output format (not MP4)?
**A:** Currently only MP4 is supported. Other formats may be added in future versions.

### Q: How do I organize my assets?
**A:** Recommended structure:
```
assets/
├── audio/
│   ├── project1/
│   └── project2/
└── images/
    ├── project1/
    └── project2/
```

---

## 🚀 Performance

### Q: How can I speed up video generation?
**A:** 
1. Use lower FPS (24 instead of 30)
2. Reduce bitrate slightly
3. Use fewer images
4. Use SSD for storage
5. Close unnecessary programs

### Q: Can I use GPU acceleration?
**A:** Not by default, but you can install GPU-enabled FFmpeg for faster encoding.

### Q: Can I process multiple videos in parallel?
**A:** The batch processor is sequential. For parallel processing, run multiple instances manually or modify the code.

---

## 🔄 Updates & Features

### Q: How do I update to the latest version?
**A:** If using Git:
```bash
git pull origin main
pip install -r requirements.txt --upgrade
```

### Q: Can I request a feature?
**A:** Yes! Create an issue on GitHub or fork and implement it yourself.

### Q: Is there a GUI version?
**A:** Not yet, but a web interface is planned for future versions.

---

## 🤝 Contributing

### Q: Can I contribute to this project?
**A:** Yes! Contributions are welcome:
- Add features
- Fix bugs
- Improve documentation
- Add new presets
- Optimize performance

### Q: How do I report a bug?
**A:** Create an issue with:
- Description of the problem
- Steps to reproduce
- Error messages
- System information (OS, Python version)

---

## 📄 License & Usage

### Q: Is this free to use?
**A:** Yes! MIT License - free for personal and commercial use.

### Q: Can I use this for commercial projects?
**A:** Yes! No restrictions under MIT License.

### Q: Do I need to credit this project?
**A:** Not required, but appreciated!

---

## 💡 Tips & Best Practices

### Q: What's the best image-to-audio ratio?
**A:** For smooth videos:
- 30-second audio: 5-10 images
- 60-second audio: 10-15 images
- 3-minute audio: 30-40 images

### Q: Should I use high-resolution images?
**A:** Yes! Use at least:
- 1920x1080 for horizontal videos
- 1080x1920 for vertical videos
Images will be automatically resized.

### Q: How should I name my audio files?
**A:** Use descriptive names that work as titles:
- ✅ Good: "summer vibes.mp3" → "Summer Vibes"
- ✅ Good: "for love.mp3" → "For Love"
- ❌ Avoid: "audio123.mp3" → "Audio123"

### Q: Can I use the same images for all my videos?
**A:** Yes, but varying images creates more interesting content!

---

## 🎓 Learning Resources

### Q: Where can I learn more about MoviePy?
**A:** Official docs: https://zulko.github.io/moviepy/

### Q: Where can I learn about FFmpeg?
**A:** Official site: https://ffmpeg.org/documentation.html

### Q: How do I improve my command-line skills?
**A:** Try running `python main.py --help` to see all available options!

---

**Still have questions? Check the README.md or PROJECT_OVERVIEW.md for more details!**
