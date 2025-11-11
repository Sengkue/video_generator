#!/usr/bin/env python3
"""
Simple Video Creator
Create videos from images and audio files with different size presets
"""

import os
from pathlib import Path
from moviepy.editor import ImageClip, AudioFileClip
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

def create_video(image_path, audio_path, output_path, preset='youtube', custom_size=None):
    """Create a video from image and audio"""
    # Get dimensions
    if preset == 'custom' and custom_size and len(custom_size) == 2:
        width, height = custom_size
        preset_name = f'Custom ({width}x{height})'
    else:
        width, height, preset_name = VIDEO_PRESETS.get(preset, VIDEO_PRESETS['youtube'])
    
    print(f"🎥 Creating {preset_name} video: {width}x{height}")
    
    # Load and resize image
    print(f"🖼️  Processing image...")
    resized_img = resize_image(image_path, (width, height))
    
    # Save resized image to temporary file
    temp_img_path = 'temp_resized_image.jpg'
    resized_img.save(temp_img_path, 'JPEG')
    
    # Load audio
    print(f"🔊 Loading audio...")
    audio = AudioFileClip(audio_path)
    
    # Create video from image
    video = ImageClip(temp_img_path, duration=audio.duration)
    video = video.set_audio(audio)
    
    # Export
    print(f"🚀 Exporting video...")
    video.write_videofile(
        output_path,
        fps=24,
        codec='libx264',
        audio_codec='aac',
        temp_audiofile='temp-audio.m4a',
        remove_temp=True,
        logger='bar'  # Show progress bar
    )
    
    # Clean up
    if os.path.exists(temp_img_path):
        os.remove(temp_img_path)
    
    print(f"✅ Video saved to: {output_path}")

def list_presets():
    """List all available video presets"""
    print("\nAvailable video presets:")
    for name, (w, h, desc) in VIDEO_PRESETS.items():
        print(f"  {name:15} - {w}x{h}: {desc}")
    print("\nExample: --preset tiktok")
    print("Or use custom size: --preset custom --width 800 --height 1200")

def main():
    parser = argparse.ArgumentParser(description='Create video from image and audio')
    
    # Required arguments
    parser.add_argument('--image', required=True, help='Path to image file')
    parser.add_argument('--audio', required=True, help='Path to audio file')
    parser.add_argument('--output', default='output.mp4', help='Output video file')
    
    # Video size options
    parser.add_argument('--preset', default='youtube',
                      help='Video size preset (youtube, tiktok, instagram_post, etc.)')
    parser.add_argument('--width', type=int, help='Custom width (use with --preset custom)')
    parser.add_argument('--height', type=int, help='Custom height (use with --preset custom)')
    parser.add_argument('--list-presets', action='store_true',
                      help='List all available video size presets and exit')
    
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
    
    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(args.output)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Create the video
    try:
        create_video(
            args.image,
            args.audio,
            args.output,
            preset=args.preset.lower(),
            custom_size=custom_size
        )
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    main()
