#!/usr/bin/env python3
"""
Example script demonstrating how to use the VideoGenerator class directly
"""

import sys
import os
sys.path.insert(0, 'src')

from video_generator import VideoGenerator


def example_basic():
    """Basic example: Create a single video"""
    print("=" * 50)
    print("Example 1: Basic Video Generation")
    print("=" * 50)
    
    generator = VideoGenerator()
    
    # Create YouTube video
    generator.create_video(
        audio_path="assets/audio/for love.mp3",
        images_path="assets/images",
        preset="youtube"
    )


def example_custom_title():
    """Example with custom title"""
    print("\n" + "=" * 50)
    print("Example 2: Custom Title")
    print("=" * 50)
    
    generator = VideoGenerator()
    
    # Create TikTok video with custom title
    generator.create_video(
        audio_path="assets/audio/song.mp3",
        images_path="assets/images",
        preset="tiktok",
        custom_title="My Amazing Song"
    )


def example_batch():
    """Example: Batch processing"""
    print("\n" + "=" * 50)
    print("Example 3: Batch Processing")
    print("=" * 50)
    
    generator = VideoGenerator()
    
    # Process all audio files
    results = generator.batch_create(
        audio_folder="assets/audio",
        images_folder="assets/images",
        preset="youtube_short"
    )
    
    # Print results
    for result in results:
        if result['status'] == 'success':
            print(f"✓ {result['audio']} -> {result['output']}")
        else:
            print(f"✗ {result['audio']} - Error: {result['error']}")


def example_all_presets():
    """Example: Create video in all presets"""
    print("\n" + "=" * 50)
    print("Example 4: Generate for All Platforms")
    print("=" * 50)
    
    generator = VideoGenerator()
    
    presets = ['youtube', 'tiktok', 'instagram_story', 'facebook']
    
    for preset in presets:
        print(f"\nCreating {preset} video...")
        try:
            generator.create_video(
                audio_path="assets/audio/for love.mp3",
                images_path="assets/images",
                preset=preset
            )
            print(f"✓ {preset} done!")
        except Exception as e:
            print(f"✗ {preset} failed: {e}")


def example_list_presets():
    """Example: List all available presets"""
    print("\n" + "=" * 50)
    print("Example 5: List Available Presets")
    print("=" * 50)
    
    generator = VideoGenerator()
    generator.list_presets()


if __name__ == "__main__":
    print("\n🎬 Auto Video Generator - Examples\n")
    
    # Check if assets exist
    if not os.path.exists("assets/audio"):
        print("⚠️  Warning: 'assets/audio' folder not found!")
        print("Please create it and add audio files before running examples.\n")
    
    if not os.path.exists("assets/images"):
        print("⚠️  Warning: 'assets/images' folder not found!")
        print("Please create it and add image files before running examples.\n")
    
    # Uncomment the examples you want to run:
    
    # example_basic()
    # example_custom_title()
    # example_batch()
    # example_all_presets()
    example_list_presets()
    
    print("\n✓ Examples completed!")
    print("\nTo run other examples, uncomment them in examples.py")
