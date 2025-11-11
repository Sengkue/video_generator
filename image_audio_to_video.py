#!/usr/bin/env python3
"""
Simple Video Creator
Automatically processes files from a 'data' folder and saves to 'output' folder
"""

import os
import glob
from pathlib import Path
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
from PIL import Image, ImageOps
import argparse

# Video presets (width, height, description)
VIDEO_PRESETS = {
    'youtube': (1920, 1080, 'YouTube HD (16:9)'),
    'youtube_short': (1080, 1920, 'YouTube Shorts (9:16)'),
    'tiktok': (1080, 1920, 'TikTok (9:16)'),
    'instagram_post': (1080, 1080, 'Instagram Post (1:1)'),
    'instagram_story': (1080, 1920, 'Instagram Story (9:16)'),
    'facebook': (1280, 720, 'Facebook (16:9)')
}

def find_files_in_data():
    """Find image and audio files in the data folder"""
    data_dir = Path('data')
    if not data_dir.exists():
        data_dir.mkdir(parents=True, exist_ok=True)
        raise FileNotFoundError("'data' folder not found. I've created it for you. Please add your files and run again.")
    
    # Find all image files
    image_exts = ('*.jpg', '*.jpeg', '*.png', '*.bmp')
    image_files = []
    for ext in image_exts:
        image_files.extend(sorted(glob.glob(str(data_dir / ext), recursive=True)))
    
    # Find first audio file
    audio_exts = ('*.mp3', '*.wav', '*.m4a')
    audio_file = None
    for ext in audio_exts:
        audio_files = glob.glob(str(data_dir / ext))
        if audio_files:
            audio_file = audio_files[0]  # Use first audio file found
            break
    
    if not image_files:
        raise FileNotFoundError("No image files found in the 'data' folder.")
    if not audio_file:
        raise FileNotFoundError("No audio file found in the 'data' folder.")
    
    return image_files, audio_file

def resize_image(image_path, target_size):
    """Resize image to fit target size while maintaining aspect ratio"""
    img = Image.open(image_path)
    img = ImageOps.contain(img, target_size, method=Image.Resampling.LANCZOS)
    
    # Create new image with target size and paste the resized image
    new_img = Image.new('RGB', target_size, (0, 0, 0))  # Black background
    new_img.paste(
        img, 
        ((target_size[0] - img.size[0]) // 2, (target_size[1] - img.size[1]) // 2)
    )
    return new_img

def create_video(image_paths, audio_path, output_path, preset='youtube', custom_size=None, duration_per_image=5, transition_duration=0.5):
    """Create a video from multiple images and audio"""
    # Get dimensions
    if preset == 'custom' and custom_size and len(custom_size) == 2:
        width, height = custom_size
        preset_name = f'Custom ({width}x{height})'
    else:
        width, height, preset_name = VIDEO_PRESETS.get(preset, VIDEO_PRESETS['youtube'])
    
    print(f"🎥 Creating {preset_name} video: {width}x{height}")
    print(f"📸 Found {len(image_paths)} images")
    print(f"🔊 Using audio: {os.path.basename(audio_path)}")
    
    # Load audio
    audio = AudioFileClip(audio_path)
    audio_duration = audio.duration
    print(f"⏱️  Audio duration: {audio_duration:.1f} seconds")
    
    # Calculate duration per image
    if duration_per_image == 0:  # Auto-calculate duration
        duration_per_image = max(3, audio_duration / len(image_paths))
        print(f"⏱️  Auto-calculated {duration_per_image:.1f} seconds per image")
    
    # Create video clips from images
    clips = []
    for i, img_path in enumerate(image_paths, 1):
        print(f"🖼️  Processing image {i}/{len(image_paths)}: {os.path.basename(img_path)}")
        
        # Resize image
        resized_img = resize_image(img_path, (width, height))
        temp_img_path = f'temp_img_{i}.jpg'
        resized_img.save(temp_img_path, 'JPEG', quality=95)
        
        # Create clip
        clip = ImageClip(temp_img_path).set_duration(duration_per_image)
        
        # Add crossfade transition (except for first clip)
        if i > 1 and transition_duration > 0:
            clip = clip.crossfadein(transition_duration)
        
        clips.append(clip)
    
    # Concatenate all clips
    print("🎬 Combining images...")
    video = concatenate_videoclips(clips, method="compose")
    video = video.set_audio(audio)
    
    # Create output directory if it doesn't exist
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Export
    print(f"🚀 Exporting video to: {output_path}")
    video.write_videofile(
        str(output_path),
        fps=24,
        codec='libx264',
        audio_codec='aac',
        temp_audiofile='temp-audio.m4a',
        remove_temp=True,
        logger='bar',  # Show progress bar
        threads=4,     # Use multiple threads for faster encoding
        preset='fast', # Faster encoding with slightly larger file size
        ffmpeg_params=['-pix_fmt', 'yuv420p']  # Better compatibility
    )
    
    # Clean up
    for i in range(1, len(image_paths) + 1):
        temp_img = f'temp_img_{i}.jpg'
        if os.path.exists(temp_img):
            os.remove(temp_img)
    
    print(f"✅ Video saved to: {output_path}")

def list_presets():
    """List all available video presets"""
    print("\nAvailable video presets:")
    for name, (w, h, desc) in VIDEO_PRESETS.items():
        print(f"  {name:15} - {w}x{h}: {desc}")
    print("\nExample: --preset tiktok")
    print("Or use custom size: --preset custom --width 800 --height 1200")

def main():
    parser = argparse.ArgumentParser(description='Create video from images and audio in data folder')
    
    # Main arguments
    default_output = str(Path('output') / 'video.mp4')
    parser.add_argument('--output', default=default_output, 
                      help=f'Output video file (default: {default_output})')
    
    # Video size options
    parser.add_argument('--preset', default='youtube',
                      help='Video size preset (youtube, tiktok, instagram_post, etc.)')
    parser.add_argument('--width', type=int, help='Custom width (use with --preset custom)')
    parser.add_argument('--height', type=int, help='Custom height (use with --preset custom)')
    parser.add_argument('--list-presets', action='store_true',
                      help='List all available video size presets and exit')
    
    # Timing options
    parser.add_argument('--duration', type=float, default=5,
                      help='Duration to show each image (seconds). 0 = auto-calculate based on audio length')
    parser.add_argument('--transition', type=float, default=0.5,
                      help='Crossfade transition duration between images (seconds)')
    
    args = parser.parse_args()
    
    # List presets if requested
    if args.list_presets:
        return list_presets()
    
    # Validate preset
    if args.preset.lower() not in VIDEO_PRESETS and args.preset.lower() != 'custom':
        print(f"❌ Error: Unknown preset '{args.preset}'. Use --list-presets to see available options.")
        return 1
    
    # Validate custom size if using custom preset
    custom_size = None
    if args.preset.lower() == 'custom':
        if not args.width or not args.height:
            print("❌ Error: --width and --height are required when using --preset custom")
            return 1
        custom_size = (args.width, args.height)
    
    try:
        # Find files in data folder
        image_paths, audio_path = find_files_in_data()
        
        print(f"📁 Found in 'data' folder:")
        print(f"   - Images: {len(image_paths)} files")
        print(f"   - Audio: {os.path.basename(audio_path)}")
        
        # Create the video
        create_video(
            image_paths,
            audio_path,
            args.output,
            preset=args.preset.lower(),
            custom_size=custom_size,
            duration_per_image=args.duration,
            transition_duration=args.transition
        )
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    main()