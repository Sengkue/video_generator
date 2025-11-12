import os
import json
from pathlib import Path
from moviepy.editor import (
    ImageClip, AudioFileClip, CompositeVideoClip, 
    concatenate_videoclips
)
from PIL import Image, ImageDraw, ImageFont
import numpy as np


class VideoGenerator:
    """
    Automated video generator that creates videos from images and audio
    with automatic title overlay from audio filename.
    """
    
    def __init__(self, config_path="config/presets.json"):
        """Initialize the video generator with configuration."""
        self.config_path = config_path
        self.load_config()
        
    def load_config(self):
        """Load configuration from JSON file."""
        with open(self.config_path, 'r') as f:
            self.config = json.load(f)
    
    def get_title_from_audio(self, audio_path):
        """
        Extract title from audio filename.
        Example: 'for love.mp3' -> 'For Love'
        """
        filename = Path(audio_path).stem
        # Capitalize each word
        title = ' '.join(word.capitalize() for word in filename.split())
        return title
    
    def create_title_image(self, title, width, height):
        """
        Create title overlay image using Pillow.
        
        Parameters:
        -----------
        title : str
            Title text to display
        width : int
            Video width
        height : int
            Video height
        """
        style = self.config['title_style']
        
        # Create transparent image
        img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Try to load font, fall back to default if not available
        try:
            # Try common Windows fonts first
            font_paths = [
                "C:/Windows/Fonts/arialbd.ttf",  # Arial Bold
                "C:/Windows/Fonts/Arial.ttf",     # Arial
                "C:/Windows/Fonts/calibrib.ttf",  # Calibri Bold
                "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",  # Linux
                "/System/Library/Fonts/Helvetica.ttc",  # macOS
            ]
            
            font = None
            for font_path in font_paths:
                if os.path.exists(font_path):
                    try:
                        font = ImageFont.truetype(font_path, style['fontsize'])
                        break
                    except:
                        continue
            
            if font is None:
                # Try to load any available TrueType font
                font = ImageFont.truetype("arial.ttf", style['fontsize'])
        except:
            # Fall back to default font
            print("⚠️  Using default font (custom font not found)")
            font = ImageFont.load_default()
        
        # Get text bounding box
        bbox = draw.textbbox((0, 0), title, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        # Calculate position (top center)
        x = (width - text_width) // 2
        y = 50  # 50 pixels from top
        
        # Draw text with stroke (outline)
        stroke_width = style['stroke_width']
        
        # Draw stroke (outline)
        if stroke_width > 0:
            for adj_x in range(-stroke_width, stroke_width + 1):
                for adj_y in range(-stroke_width, stroke_width + 1):
                    if adj_x != 0 or adj_y != 0:
                        draw.text((x + adj_x, y + adj_y), title, 
                                 font=font, fill=style['stroke_color'])
        
        # Draw main text
        draw.text((x, y), title, font=font, fill=style['color'])
        
        return np.array(img)
    
    def create_video(
        self,
        audio_path,
        images_path,
        output_path=None,
        preset="youtube",
        custom_title=None,
        transition_duration=1.0,
        image_duration=None
    ):
        """
        Create video from audio and images.
        
        Parameters:
        -----------
        audio_path : str
            Path to audio file
        images_path : str or list
            Path to folder containing images or list of image paths
        output_path : str, optional
            Output video path. If None, auto-generated
        preset : str
            Video preset (youtube, tiktok, instagram_story, etc.)
        custom_title : str, optional
            Custom title. If None, uses audio filename
        transition_duration : float
            Duration of transitions between images (seconds)
        image_duration : float, optional
            Duration each image is shown. If None, calculated from audio length
        """
        
        # Get preset configuration
        if preset not in self.config['presets']:
            raise ValueError(f"Preset '{preset}' not found. Available: {list(self.config['presets'].keys())}")
        
        preset_config = self.config['presets'][preset]
        width = preset_config['width']
        height = preset_config['height']
        fps = preset_config['fps']
        
        # Load audio
        print(f"Loading audio: {audio_path}")
        audio = AudioFileClip(audio_path)
        audio_duration = audio.duration
        
        # Get title
        title = custom_title if custom_title else self.get_title_from_audio(audio_path)
        
        # Get images
        if isinstance(images_path, str):
            # If it's a folder path
            image_files = sorted([
                os.path.join(images_path, f) 
                for f in os.listdir(images_path)
                if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))
            ])
        else:
            # If it's a list of paths
            image_files = images_path
        
        if not image_files:
            raise ValueError("No images found!")
        
        # Calculate duration for each image
        if image_duration is None:
            image_duration = audio_duration / len(image_files)
        
        print(f"Creating video: {title}")
        print(f"Preset: {preset} ({width}x{height})")
        print(f"Audio duration: {audio_duration:.2f}s")
        print(f"Number of images: {len(image_files)}")
        print(f"Duration per image: {image_duration:.2f}s")
        
        # Create title overlay using Pillow
        print("Creating title overlay...")
        title_array = self.create_title_image(title, width, height)
        title_clip = (ImageClip(title_array, transparent=True)
                     .set_duration(audio_duration)
                     .set_position('center'))
        
        # Create video clips from images
        print("Processing images...")
        clips = []
        for i, img_path in enumerate(image_files):
            print(f"  Processing image {i+1}/{len(image_files)}: {os.path.basename(img_path)}")
            # Create image clip
            img_clip = (ImageClip(img_path)
                       .set_duration(image_duration)
                       .resize(height=height)  # Resize to fit height
                       .on_color(size=(width, height), 
                                color=(0, 0, 0), 
                                pos='center'))
            clips.append(img_clip)
        
        # Concatenate all image clips
        print("Combining images...")
        video = concatenate_videoclips(clips, method="compose")
        
        # Trim video to match audio duration
        if video.duration > audio_duration:
            video = video.subclip(0, audio_duration)
        
        # Composite video with title
        print("Adding title overlay...")
        final_video = CompositeVideoClip([video, title_clip])
        
        # Add audio
        print("Adding audio track...")
        final_video = final_video.set_audio(audio)
        
        # Generate output path if not provided
        if output_path is None:
            audio_name = Path(audio_path).stem
            output_path = f"output/{audio_name}_{preset}.mp4"
        
        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Write video file
        print(f"Rendering video to: {output_path}")
        print("This may take a while...")
        final_video.write_videofile(
            output_path,
            fps=fps,
            codec=self.config['video_settings']['codec'],
            audio_codec=self.config['video_settings']['audio_codec'],
            bitrate=self.config['video_settings']['bitrate'],
            audio_bitrate=self.config['video_settings']['audio_bitrate'],
            preset='medium',
            threads=4
        )
        
        print(f"✓ Video created successfully: {output_path}")
        return output_path
    
    def batch_create(self, audio_folder, images_folder, preset="youtube"):
        """
        Batch create videos for all audio files in a folder.
        
        Parameters:
        -----------
        audio_folder : str
            Folder containing audio files
        images_folder : str
            Folder containing images (used for all videos)
        preset : str
            Video preset to use
        """
        audio_files = [
            f for f in os.listdir(audio_folder)
            if f.lower().endswith(('.mp3', '.wav', '.m4a', '.aac', '.ogg'))
        ]
        
        print(f"Found {len(audio_files)} audio files")
        
        results = []
        for audio_file in audio_files:
            audio_path = os.path.join(audio_folder, audio_file)
            try:
                output_path = self.create_video(
                    audio_path=audio_path,
                    images_path=images_folder,
                    preset=preset
                )
                results.append({
                    'audio': audio_file,
                    'status': 'success',
                    'output': output_path
                })
            except Exception as e:
                print(f"Error processing {audio_file}: {str(e)}")
                results.append({
                    'audio': audio_file,
                    'status': 'failed',
                    'error': str(e)
                })
        
        return results
    
    def list_presets(self):
        """List all available presets."""
        print("\n=== Available Presets ===")
        for preset_name, preset_config in self.config['presets'].items():
            print(f"\n{preset_name}:")
            print(f"  Size: {preset_config['width']}x{preset_config['height']}")
            print(f"  FPS: {preset_config['fps']}")
            print(f"  Aspect Ratio: {preset_config['aspect_ratio']}")
            print(f"  Description: {preset_config['description']}")
