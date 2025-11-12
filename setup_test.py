#!/usr/bin/env python3
"""
Setup and Test Script for Auto Video Generator
This script helps verify installation and creates sample assets for testing
"""

import os
import sys
import subprocess
from pathlib import Path


def check_python_version():
    """Check if Python version is adequate"""
    print("Checking Python version...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print(f"❌ Python 3.7+ required. You have {version.major}.{version.minor}")
        return False
    print(f"✓ Python {version.major}.{version.minor}.{version.micro}")
    return True


def check_ffmpeg():
    """Check if FFmpeg is installed"""
    print("\nChecking FFmpeg...")
    try:
        result = subprocess.run(
            ['ffmpeg', '-version'],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            version_line = result.stdout.split('\n')[0]
            print(f"✓ {version_line}")
            return True
        else:
            print("❌ FFmpeg not working properly")
            return False
    except FileNotFoundError:
        print("❌ FFmpeg not found!")
        print("\nPlease install FFmpeg:")
        print("  Ubuntu/Debian: sudo apt-get install ffmpeg")
        print("  macOS: brew install ffmpeg")
        print("  Windows: Download from https://ffmpeg.org/download.html")
        return False
    except subprocess.TimeoutExpired:
        print("❌ FFmpeg check timed out")
        return False


def check_dependencies():
    """Check if required Python packages are installed"""
    print("\nChecking Python dependencies...")
    required = [
        'moviepy',
        'PIL',
        'numpy',
        'cv2'
    ]
    
    missing = []
    for module in required:
        try:
            if module == 'PIL':
                __import__('PIL')
            elif module == 'cv2':
                __import__('cv2')
            else:
                __import__(module)
            print(f"✓ {module}")
        except ImportError:
            print(f"❌ {module}")
            missing.append(module)
    
    if missing:
        print(f"\n❌ Missing packages: {', '.join(missing)}")
        print("Run: pip install -r requirements.txt")
        return False
    
    return True


def create_sample_images():
    """Create sample images for testing"""
    print("\nCreating sample images...")
    try:
        from PIL import Image, ImageDraw, ImageFont
        import random
        
        images_dir = Path("assets/images")
        images_dir.mkdir(parents=True, exist_ok=True)
        
        colors = [
            (255, 99, 71),   # Tomato
            (60, 179, 113),  # Medium Sea Green
            (30, 144, 255),  # Dodger Blue
            (255, 215, 0),   # Gold
            (218, 112, 214), # Orchid
        ]
        
        for i, color in enumerate(colors, 1):
            img = Image.new('RGB', (1920, 1080), color)
            draw = ImageDraw.Draw(img)
            
            # Draw text
            text = f"Sample Image {i}"
            try:
                font = ImageFont.truetype("arial.ttf", 80)
            except:
                font = ImageFont.load_default()
            
            # Calculate text position (center)
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            x = (1920 - text_width) // 2
            y = (1080 - text_height) // 2
            
            # Draw text with shadow
            draw.text((x+3, y+3), text, fill=(0, 0, 0), font=font)
            draw.text((x, y), text, fill=(255, 255, 255), font=font)
            
            # Save
            img_path = images_dir / f"sample_{i}.jpg"
            img.save(img_path, quality=95)
            print(f"✓ Created {img_path}")
        
        return True
    except Exception as e:
        print(f"❌ Error creating sample images: {e}")
        return False


def create_sample_audio():
    """Create a sample audio file for testing"""
    print("\nCreating sample audio...")
    try:
        from pydub.generators import Sine
        from pydub import AudioSegment
        
        audio_dir = Path("assets/audio")
        audio_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate a simple melody (C major scale)
        notes = [262, 294, 330, 349, 392, 440, 494, 523]  # C D E F G A B C
        duration = 500  # milliseconds per note
        
        melody = AudioSegment.silent(duration=100)
        
        for note in notes:
            tone = Sine(note).to_audio_segment(duration=duration)
            melody += tone
        
        # Repeat for longer duration
        full_audio = melody * 2
        
        # Export
        audio_path = audio_dir / "for love.mp3"
        full_audio.export(audio_path, format="mp3", bitrate="192k")
        print(f"✓ Created {audio_path}")
        return True
    except Exception as e:
        print(f"⚠️  Could not create sample audio: {e}")
        print("   You can add your own audio files to assets/audio/")
        return False


def test_video_generation():
    """Test video generation"""
    print("\n" + "=" * 50)
    print("Testing Video Generation")
    print("=" * 50)
    
    # Check if we have assets
    audio_files = list(Path("assets/audio").glob("*.mp3"))
    image_files = list(Path("assets/images").glob("*.jpg"))
    
    if not audio_files:
        print("❌ No audio files found in assets/audio/")
        return False
    
    if not image_files or len(image_files) < 3:
        print("❌ Need at least 3 images in assets/images/")
        return False
    
    print(f"✓ Found {len(audio_files)} audio file(s)")
    print(f"✓ Found {len(image_files)} image file(s)")
    
    # Try to import our module
    try:
        sys.path.insert(0, 'src')
        from video_generator import VideoGenerator
        
        generator = VideoGenerator()
        print("✓ VideoGenerator initialized")
        
        # List presets
        print("\nAvailable presets:")
        generator.list_presets()
        
        return True
    except Exception as e:
        print(f"❌ Error testing video generation: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Main setup and test function"""
    print("=" * 50)
    print("🎬 Auto Video Generator - Setup & Test")
    print("=" * 50)
    
    checks = [
        ("Python Version", check_python_version),
        ("FFmpeg", check_ffmpeg),
        ("Python Dependencies", check_dependencies),
    ]
    
    all_passed = True
    for name, check_func in checks:
        if not check_func():
            all_passed = False
    
    if not all_passed:
        print("\n" + "=" * 50)
        print("❌ Setup incomplete. Please fix the issues above.")
        print("=" * 50)
        sys.exit(1)
    
    # Create sample assets
    print("\n" + "=" * 50)
    print("Creating Sample Assets")
    print("=" * 50)
    
    create_sample_images()
    create_sample_audio()
    
    # Test video generation
    test_video_generation()
    
    print("\n" + "=" * 50)
    print("✓ Setup Complete!")
    print("=" * 50)
    print("\nYou can now:")
    print("1. Add your own audio files to: assets/audio/")
    print("2. Add your own images to: assets/images/")
    print("3. Run: python main.py -a 'assets/audio/for love.mp3' -i assets/images -p youtube")
    print("\nSee README.md for full documentation!")


if __name__ == "__main__":
    main()
