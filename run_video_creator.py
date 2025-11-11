import os
import sys
from pathlib import Path

def main():
    # Create output directory if it doesn't exist
    output_dir = Path('output')
    output_dir.mkdir(exist_ok=True)
    
    # Define paths
    data_dir = Path('data')
    output_file = output_dir / 'my_video.mp4'
    
    # Check if data directory exists
    if not data_dir.exists():
        print("Error: 'data' directory not found. Please create it and add your files.")
        return 1
    
    # Find image and audio files
    image_exts = ('.jpg', '.jpeg', '.png', '.bmp')
    audio_exts = ('.mp3', '.wav', '.m4a')
    
    image_files = sorted([f for f in data_dir.iterdir() if f.suffix.lower() in image_exts])
    audio_files = [f for f in data_dir.iterdir() if f.suffix.lower() in audio_exts]
    
    if not image_files:
        print("Error: No image files found in the 'data' folder.")
        return 1
        
    if not audio_files:
        print("Error: No audio files found in the 'data' folder.")
        return 1
    
    # Use the first audio file found
    audio_file = audio_files[0]
    
    print(f"Found {len(image_files)} images and audio file: {audio_file.name}")
    print(f"Creating video: {output_file}")
    
    # Import moviepy here to show where it fails if there's an issue
    try:
        from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
        from PIL import Image, ImageOps
    except ImportError as e:
        print(f"Error importing required libraries: {e}")
        print("Please install the required packages with: pip install moviepy pillow")
        return 1
    
    try:
        # Load audio
        audio = AudioFileClip(str(audio_file))
        audio_duration = audio.duration
        
        # Create video clips from images
        clips = []
        duration_per_image = 5  # seconds per image
        
        for i, img_path in enumerate(image_files, 1):
            print(f"Processing image {i}/{len(image_files)}: {img_path.name}")
            
            # Create clip from image
            clip = ImageClip(str(img_path)).set_duration(duration_per_image)
            
            # Add crossfade transition (except for first clip)
            if i > 1:
                clip = clip.crossfadein(1.0)  # 1 second crossfade
                
            clips.append(clip)
        
        # Concatenate all clips
        print("Combining clips...")
        video = concatenate_videoclips(clips, method="compose")
        video = video.set_audio(audio)
        
        # Export video
        print(f"Exporting video to: {output_file}")
        video.write_videofile(
            str(output_file),
            fps=24,
            codec='libx264',
            audio_codec='aac',
            temp_audiofile=str(output_dir / 'temp_audio.m4a'),
            remove_temp=True,
            logger='bar'
        )
        
        print(f"✅ Video created successfully: {output_file}")
        return 0
        
    except Exception as e:
        print(f"❌ Error creating video: {str(e)}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())
