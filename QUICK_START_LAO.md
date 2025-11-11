# 🚀 ເລີ່ມຕົ້ນດ່ວນ - Quick Start Guide

## ⚡ ຕິດຕັ້ງດ່ວນ (5 ນາທີ)

### Windows:

```powershell
# 1. ຕິດຕັ້ງ Python (ຖ້າຍັງບໍ່ມີ)
# ດາວໂຫຼດຈາກ: https://www.python.org/downloads/
# ✅ ຕິກໃສ່ "Add Python to PATH" ເວລາຕິດຕັ້ງ!

# 2. ຕິດຕັ້ງ FFmpeg
# ດາວໂຫຼດຈາກ: https://www.gyan.dev/ffmpeg/builds/
# ແຕກໄຟລ໌ໃສ່ C:\ffmpeg
# ເພີ່ມ C:\ffmpeg\bin ເຂົ້າໃນ PATH

# 3. ແຕກໄຟລ໌ video_generator_package.zip
# 4. ເປີດ Command Prompt ໃນໂຟລເດີນັ້ນ
# 5. ຕິດຕັ້ງ Python libraries:
pip install moviepy Pillow numpy

# 6. ທົດສອບ:
python image_audio_to_video.py --help
```

### Mac:

```bash
# 1. ຕິດຕັ້ງ Homebrew (ຖ້າຍັງບໍ່ມີ):
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 2. ຕິດຕັ້ງ Python ແລະ FFmpeg:
brew install python ffmpeg

# 3. ແຕກໄຟລ໌ video_generator_package.zip
# 4. ເປີດ Terminal ໃນໂຟລເດີນັ້ນ
# 5. ຕິດຕັ້ງ Python libraries:
pip3 install moviepy Pillow numpy

# 6. ທົດສອບ:
python3 image_audio_to_video.py --help
```

### Linux (Ubuntu/Debian):

```bash
# 1. ອັບເດດ system:
sudo apt update

# 2. ຕິດຕັ້ງທຸກຢ່າງພ້ອມກັນ:
sudo apt install python3 python3-pip ffmpeg

# 3. ແຕກໄຟລ໌ video_generator_package.zip
# 4. ເປີດ Terminal ໃນໂຟລເດີນັ້ນ
# 5. ຕິດຕັ້ງ Python libraries:
pip3 install moviepy Pillow numpy

# 6. ທົດສອບ:
python3 image_audio_to_video.py --help
```

---

## 🎬 ໃຊ້ງານທັນທີ - 3 ຄຳສັ່ງ

### ຮູບດຽວ + ເພງ MP3:

```bash
# Windows:
python image_audio_to_video.py --image ຮູບ.jpg --audio ເພງ.mp3

# Mac/Linux:
python3 image_audio_to_video.py --image ຮູບ.jpg --audio ເພງ.mp3
```

### ຫຼາຍຮູບ + ເພງ (Slideshow):

```bash
# Windows:
python image_audio_to_video.py --images ຮູບ1.jpg ຮູບ2.jpg ຮູບ3.jpg --audio ເພງ.mp3

# Mac/Linux:
python3 image_audio_to_video.py --images ຮູບ1.jpg ຮູບ2.jpg ຮູບ3.jpg --audio ເພງ.mp3
```

---

## 📁 ວາງໄຟລ໌ແນວໃດ:

```
video_generator/
├── image_audio_to_video.py
├── requirements.txt
├── README_LAO.md
├── ຮູບຂອງທ່ານ.jpg          ← ວາງຮູບພາບທີ່ນີ້
├── ເພງຂອງທ່ານ.mp3          ← ວາງ MP3 ທີ່ນີ້
└── output/
    └── video.mp4            ← ວິດີໂອທີ່ສຳເລັດຈະຢູ່ທີ່ນີ້
```

---

## ❓ ແກ້ບັນຫາດ່ວນ

### ບັນຫາ: "python is not recognized"
**ແກ້:** ກວດສອບວ່າໄດ້ຕິກ "Add Python to PATH" ເວລາຕິດຕັ້ງ Python

### ບັນຫາ: "FFmpeg not found"
**ແກ້:** 
- Windows: ກວດສອບວ່າ FFmpeg ຢູ່ໃນ PATH
- Mac: `brew install ffmpeg`
- Linux: `sudo apt install ffmpeg`

### ບັນຫາ: "No module named 'moviepy'"
**ແກ້:** `pip install moviepy`

---

## 🎯 ຕົວຢ່າງຈິງ

ສົມມຸດວ່າທ່ານມີ:
- ຮູບຊື່ `wedding.jpg`
- ເພງຊື່ `love_song.mp3`

```bash
# ສ້າງວິດີໂອ:
python image_audio_to_video.py --image wedding.jpg --audio love_song.mp3 --output wedding_video.mp4

# ວິດີໂອຈະໄດ້ຢູ່ທີ່: output/wedding_video.mp4
```

---

## 💡 Tips:

1. **ຮູບຄວນມີຂະໜາດດຽວກັນ**: 1920x1080 ຫຼື 1280x720
2. **MP3 ຄວນມີຄຸນນະພາບດີ**: 192kbps ຂຶ້ນໄປ
3. **ຫຼາຍຮູບ = ວິດີໂອດີກວ່າ**: ແນະນຳ 3-10 ຮູບຕໍ່ເພງ

---

## 📧 ຕ້ອງການຄວາມຊ່ວຍເຫຼືອ?

ອ່ານຄູ່ມືຄົບຖ້ວນໃນ **README_LAO.md** 📖

ຫຼື ຖາມຂ້ອຍໄດ້ເລີຍ! 🚀
