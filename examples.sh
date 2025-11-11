#!/bin/bash
# ຕົວຢ່າງການໃຊ້ງານ Image + Audio to Video Generator

echo "🎬 ຕົວຢ່າງການໃຊ້ງານ Video Generator"
echo "======================================"
echo ""

echo "📋 ກຳລັງກວດສອບ dependencies..."
python --version
ffmpeg -version | head -n 1
echo ""

echo "ຕົວຢ່າງທີ່ 1: ສ້າງວິດີໂອຈາກຮູບດຽວ + audio"
echo "-------------------------------------------"
echo "python image_audio_to_video.py --image photo.jpg --audio song.mp3 --output video1.mp4"
echo ""

echo "ຕົວຢ່າງທີ່ 2: ສ້າງ slideshow ຈາກຫຼາຍຮູບ + audio"
echo "-------------------------------------------"
echo "python image_audio_to_video.py --images img1.jpg img2.jpg img3.jpg --audio music.mp3 --output slideshow.mp4"
echo ""

echo "ຕົວຢ່າງທີ່ 3: ປັບແຕ່ງ FPS ແລະ transition"
echo "-------------------------------------------"
echo "python image_audio_to_video.py --images photo1.jpg photo2.jpg photo3.jpg --audio bg_music.mp3 --fps 30 --transition 2 --output custom.mp4"
echo ""

echo "💡 ດູລາຍລະອຽດເພີ່ມເຕີມໃນ README_LAO.md"
