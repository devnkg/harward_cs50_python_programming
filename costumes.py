"""
HARVARD CS50 PYTHON - Week 4: Pillow Library (Image Processing)
=================================================================
Concepts: PIL (Pillow), Image.open(), sys.argv, image processing, GIF creation

Author: David J. Malan (CS50)
Learning Level: Advanced | Best Practice: ✅
"""

import sys
from PIL import Image


def create_costume_gif(image_paths: list[str], output: str = "costume.gif") -> None:
    """Create an animated GIF from two images.

    Args:
        image_paths: List of paths to images (at least 2)
        output: Output GIF filename (default: "costume.gif")

    💡 Uses Pillow (PIL) - Install: pip install Pillow
    """
    images = []

    for path in image_paths:
        try:
            image = Image.open(path)
            images.append(image)
            print(f"✅ Loaded: {path}")
        except FileNotFoundError:
            print(f"❌ File not found: {path}")
            sys.exit(1)
        except Exception as e:
            print(f"❌ Error loading {path}: {e}")
            sys.exit(1)

    if len(images) < 2:
        print("❌ Need at least 2 images to create a GIF")
        sys.exit(1)

    # Save as animated GIF
    # 💡 save_all=True = include all frames
    # 💡 append_images = additional frames after first
    # 💡 duration = time per frame in milliseconds
    # 💡 loop = 0 means loop forever (0 = infinite)
    images[0].save(
        output,
        save_all=True,
        append_images=images[1:],  # 💡 All images after first
        duration=200,               # 200ms per frame = 5 FPS
        loop=0,
    )

    print(f"✅ GIF created: {output}")


def main() -> None:
    """Convert command-line images to animated GIF."""
    if len(sys.argv) < 3:
        sys.exit("Usage: python3 costumes.py <image1.jpg> <image2.jpg> [...]")

    create_costume_gif(sys.argv[1:])


if __name__ == "__main__":
    main()


# 💡 KEY TAKEAWAYS:
#   ✅ PIL/Pillow = Python Imaging Library
#   ✅ Image.open(path) = load an image file
#   ✅ image[0] (OLD) → images[0] (FIXED: list variable name)
#   ✅ images[1:] = slice from index 1 to end (all images after first)
#   ✅ GIF parameters: duration (ms), loop (0=forever), save_all=True
#   ✅ Always handle file loading with try/except

