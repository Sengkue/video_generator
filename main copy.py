#!/usr/bin/env python3
"""
Auto Video Generator - Main Entry Point

Generate videos automatically from audio and images with customizable presets
for different social media platforms (YouTube, TikTok, Instagram, etc.)
"""

import sys
import os
import argparse

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from video_generator import VideoGenerator


def main():
    parser = argparse.ArgumentParser(
        description='Auto Video Generator - Create videos from audio and images',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Create YouTube video from audio and images folder
  python main.py -a "assets/audio/for love.mp3" -i assets/images -p youtube
  
  # Create TikTok video with custom title
  python main.py -a "assets/audio/song.mp3" -i assets/images -p tiktok -t "My Custom Title"
  
  # Batch process all audio files
  python main.py --batch -af assets/audio -i assets/images -p youtube_short
  
  # List all available presets
  python main.py --list-presets
        """
    )
    
    # Main arguments
    parser.add_argument('-a', '--audio', type=str, help='Path to audio file')
    parser.add_argument('-i', '--images', type=str, help='Path to images folder or comma-separated image paths')
    parser.add_argument('-o', '--output', type=str, help='Output video path (optional)')
    parser.add_argument('-p', '--preset', type=str, default='youtube', 
                       help='Video preset: youtube, youtube_short, tiktok, instagram_post, instagram_story, facebook, custom (default: youtube)')
    parser.add_argument('-t', '--title', type=str, help='Custom title (optional, defaults to audio filename)')
    parser.add_argument('-d', '--duration', type=float, help='Duration for each image in seconds (optional)')
    
    # Batch processing
    parser.add_argument('--batch', action='store_true', help='Batch process multiple audio files')
    parser.add_argument('-af', '--audio-folder', type=str, help='Folder containing audio files for batch processing')
    
    # Utility
    parser.add_argument('--list-presets', action='store_true', help='List all available presets')
    parser.add_argument('-c', '--config', type=str, default='config/presets.json', 
                       help='Path to config file (default: config/presets.json)')
    
    args = parser.parse_args()
    
    # Initialize generator
    generator = VideoGenerator(config_path=args.config)
    
    # List presets
    if args.list_presets:
        generator.list_presets()
        return
    
    # Batch processing
    if args.batch:
        if not args.audio_folder:
            print("Error: --audio-folder required for batch processing")
            sys.exit(1)
        if not args.images:
            print("Error: --images required for batch processing")
            sys.exit(1)
        
        print(f"\n=== Batch Processing ===")
        print(f"Audio folder: {args.audio_folder}")
        print(f"Images folder: {args.images}")
        print(f"Preset: {args.preset}\n")
        
        results = generator.batch_create(
            audio_folder=args.audio_folder,
            images_folder=args.images,
            preset=args.preset
        )
        
        print("\n=== Batch Results ===")
        success = sum(1 for r in results if r['status'] == 'success')
        print(f"Successful: {success}/{len(results)}")
        
        for result in results:
            status_icon = "✓" if result['status'] == 'success' else "✗"
            print(f"{status_icon} {result['audio']}")
            if result['status'] == 'failed':
                print(f"  Error: {result['error']}")
        
        return
    
    # Single video processing
    if not args.audio:
        print("Error: --audio required (or use --batch for batch processing)")
        parser.print_help()
        sys.exit(1)
    
    if not args.images:
        print("Error: --images required")
        parser.print_help()
        sys.exit(1)
    
    print(f"\n=== Creating Video ===")
    print(f"Audio: {args.audio}")
    print(f"Images: {args.images}")
    print(f"Preset: {args.preset}")
    if args.title:
        print(f"Custom Title: {args.title}")
    print()
    
    # Process images argument (folder or comma-separated paths)
    if ',' in args.images:
        images = [img.strip() for img in args.images.split(',')]
    else:
        images = args.images
    
    try:
        output_path = generator.create_video(
            audio_path=args.audio,
            images_path=images,
            output_path=args.output,
            preset=args.preset,
            custom_title=args.title,
            image_duration=args.duration
        )
        print(f"\n✓ Success! Video saved to: {output_path}")
    except Exception as e:
        print(f"\n✗ Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
