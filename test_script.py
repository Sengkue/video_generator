
import os
from pathlib import Path

def test_data_folder():
    data_dir = Path('data')
    print(f"Checking directory: {data_dir.absolute()}")
    
    if not data_dir.exists():
        print("❌ Error: 'data' folder does not exist")
        return False
    
    print("✅ 'data' folder exists")
    
    # List all files in data directory
    print("\nFiles in data folder:")
    files = list(data_dir.glob('*'))
    if not files:
        print("❌ No files found in 'data' folder")
        return False
    
    for file in files:
        print(f"- {file.name} ({file.stat().st_size / 1024:.1f} KB)")
    
    # Check for required files
    has_audio = any(f.suffix.lower() in ['.mp3', '.wav', '.m4a'] for f in files)
    has_images = any(f.suffix.lower() in ['.jpg', '.jpeg', '.png', '.bmp'] for f in files)
    
    print("\nRequired files check:")
    print(f"✅ Audio file: {'Found' if has_audio else '❌ Not found'}")
    print(f"✅ Image files: {'Found' if has_images else '❌ Not found'}")
    
    return has_audio and has_images

if __name__ == "__main__":
    test_data_folder()
