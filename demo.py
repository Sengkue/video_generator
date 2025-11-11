#!/usr/bin/env python3
"""
Demo: ສ້າງວິດີໂອຈາກຮູບມົ້ງທີ່ອັບໂຫຼດ + dummy audio
"""

from moviepy.editor import ImageClip, AudioFileClip, CompositeAudioClip
from moviepy.audio.AudioClip import AudioArrayClip
import numpy as np
from tqdm import tqdm
import sys

def create_simple_tone(duration, frequency=440, sample_rate=44100):
    """ສ້າງສຽງງ່າຍໆ ສຳລັບທົດສອບ"""
    t = np.linspace(0, duration, int(sample_rate * duration))
    audio_data = np.sin(2 * np.pi * frequency * t)
    return AudioArrayClip(audio_data, fps=sample_rate)

def demo_with_hmong_image():
    """Demo ດ້ວຍຮູບມົ້ງທີ່ອັບໂຫຼດ"""
    
    print("🎬 ກຳລັງສ້າງ demo video...")
    
    # ໃຊ້ຮູບມົ້ງທີ່ອັບໂຫຼດ
    image_path = "/mnt/user-data/uploads/Generated_Image_November_10__2025_-_10_16AM.png"
    
    # ສ້າງວິດີໂອຄວາມຍາວ 5 ວິນາທີ
    duration = 5
    
    print(f"   📸 ໃຊ້ຮູບ: {image_path}")
    print(f"   ⏱️  ຄວາມຍາວ: {duration} ວິນາທີ")
    
    # ສ້າງ image clip
    video = ImageClip(image_path).set_duration(duration)
    
    # ສ້າງສຽງງ່າຍໆ (ສຽງ tone)
    audio = create_simple_tone(duration, frequency=440)
    video = video.set_audio(audio)
    
    # Export
    output_path = "/mnt/user-data/outputs/demo_hmong_video.mp4"
    print(f"   💾 ກຳລັງບັນທຶກ: {output_path}")
    
    # ສ້າງ progress bar
    pbar = tqdm(total=100, desc="🚀 ກຳລັງສ້າງວິດີໂອ", unit="%", ncols=100, file=sys.stdout)
    
    def progress_callback(progress):
        pbar.update(int(progress * 100) - pbar.n)
        if progress >= 1:  # ເມື່ອສຳເລັດ 100%
            pbar.close()
    
    video.write_videofile(
        output_path,
        fps=24,
        codec='libx264',
        audio_codec='aac',
        preset='medium',
        logger=None,
        bitrate='5000k',
        threads=4,
        progress_callback=progress_callback
    )
    
    print(f"✅ ສຳເລັດ! Demo video ໄດ້ຖືກສ້າງແລ້ວ")
    print(f"📁 ທ່ານສາມາດເບິ່ງໄດ້ທີ່: {output_path}")
    
    return output_path

if __name__ == "__main__":
    try:
        demo_with_hmong_image()
    except Exception as e:
        print(f"❌ ເກີດຂໍ້ຜິດພາດ: {e}")
        print("\n💡 ກະລຸນາກວດສອບວ່າ:")
        print("   1. ໄດ້ຕິດຕັ້ງ moviepy ແລ້ວ: pip install moviepy")
        print("   2. ໄດ້ຕິດຕັ້ງ ffmpeg ແລ້ວ")
        print("   3. ໄດ້ຕິດຕັ້ງ tqdm ແລ້ວ: pip install tqdm"
