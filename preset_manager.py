#!/usr/bin/env python3
"""
Preset Manager - Easy configuration editing for Auto Video Generator
"""

import json
import sys
from pathlib import Path


class PresetManager:
    """Manage video presets configuration"""
    
    def __init__(self, config_path="config/presets.json"):
        self.config_path = config_path
        self.load_config()
    
    def load_config(self):
        """Load configuration from file"""
        with open(self.config_path, 'r') as f:
            self.config = json.load(f)
    
    def save_config(self):
        """Save configuration to file"""
        with open(self.config_path, 'w') as f:
            json.dump(self.config, f, indent=2)
        print(f"✓ Configuration saved to {self.config_path}")
    
    def list_presets(self):
        """List all presets"""
        print("\n=== Available Presets ===\n")
        for name, preset in self.config['presets'].items():
            print(f"📹 {name}")
            print(f"   Size: {preset['width']}x{preset['height']}")
            print(f"   FPS: {preset['fps']}")
            print(f"   Aspect Ratio: {preset['aspect_ratio']}")
            print(f"   Description: {preset['description']}\n")
    
    def show_title_style(self):
        """Show current title style settings"""
        print("\n=== Title Style Settings ===\n")
        style = self.config['title_style']
        for key, value in style.items():
            print(f"  {key}: {value}")
    
    def add_preset(self, name, width, height, fps=30, aspect_ratio=None, description=""):
        """Add a new preset"""
        if name in self.config['presets']:
            print(f"⚠️  Preset '{name}' already exists!")
            overwrite = input("Overwrite? (y/n): ").lower()
            if overwrite != 'y':
                print("Cancelled.")
                return
        
        if aspect_ratio is None:
            aspect_ratio = f"{width}:{height}"
        
        self.config['presets'][name] = {
            "width": width,
            "height": height,
            "fps": fps,
            "aspect_ratio": aspect_ratio,
            "description": description
        }
        
        self.save_config()
        print(f"✓ Added preset '{name}'")
    
    def remove_preset(self, name):
        """Remove a preset"""
        if name not in self.config['presets']:
            print(f"❌ Preset '{name}' not found!")
            return
        
        confirm = input(f"Remove preset '{name}'? (y/n): ").lower()
        if confirm == 'y':
            del self.config['presets'][name]
            self.save_config()
            print(f"✓ Removed preset '{name}'")
        else:
            print("Cancelled.")
    
    def update_title_style(self, **kwargs):
        """Update title style settings"""
        for key, value in kwargs.items():
            if key in self.config['title_style']:
                self.config['title_style'][key] = value
                print(f"✓ Updated {key} = {value}")
            else:
                print(f"⚠️  Unknown setting: {key}")
        
        self.save_config()
    
    def interactive_add_preset(self):
        """Interactive preset creation"""
        print("\n=== Add New Preset ===\n")
        
        name = input("Preset name: ").strip()
        if not name:
            print("❌ Name required!")
            return
        
        try:
            width = int(input("Width (px): "))
            height = int(input("Height (px): "))
            fps = int(input("FPS (default 30): ") or "30")
            description = input("Description: ").strip()
            
            self.add_preset(name, width, height, fps, description=description)
        except ValueError:
            print("❌ Invalid input!")
    
    def interactive_title_style(self):
        """Interactive title style editor"""
        print("\n=== Edit Title Style ===\n")
        self.show_title_style()
        print()
        
        print("Available settings:")
        print("  fontsize (int)")
        print("  color (string)")
        print("  stroke_color (string)")
        print("  stroke_width (int)")
        
        setting = input("\nSetting to change (or 'q' to quit): ").strip()
        if setting == 'q':
            return
        
        if setting not in self.config['title_style']:
            print(f"❌ Unknown setting: {setting}")
            return
        
        value = input(f"New value for {setting}: ").strip()
        
        # Convert to appropriate type
        if setting in ['fontsize', 'stroke_width']:
            try:
                value = int(value)
            except ValueError:
                print("❌ Must be a number!")
                return
        
        self.update_title_style(**{setting: value})


def main():
    """Main CLI interface"""
    manager = PresetManager()
    
    if len(sys.argv) < 2:
        print("🎬 Preset Manager - Auto Video Generator")
        print("\nUsage:")
        print("  python preset_manager.py list              # List all presets")
        print("  python preset_manager.py add               # Add preset (interactive)")
        print("  python preset_manager.py remove <name>     # Remove preset")
        print("  python preset_manager.py title             # Edit title style")
        print("  python preset_manager.py show-title        # Show title settings")
        sys.exit(0)
    
    command = sys.argv[1].lower()
    
    if command == 'list':
        manager.list_presets()
    
    elif command == 'add':
        if len(sys.argv) == 6:
            # Non-interactive mode
            name, width, height, fps = sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
            manager.add_preset(name, width, height, fps)
        else:
            # Interactive mode
            manager.interactive_add_preset()
    
    elif command == 'remove':
        if len(sys.argv) < 3:
            print("❌ Usage: python preset_manager.py remove <preset_name>")
            sys.exit(1)
        manager.remove_preset(sys.argv[2])
    
    elif command == 'title':
        manager.interactive_title_style()
    
    elif command == 'show-title':
        manager.show_title_style()
    
    else:
        print(f"❌ Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
