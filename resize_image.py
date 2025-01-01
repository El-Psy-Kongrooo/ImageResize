from PIL import Image
import sys

def resize_image(input_path, output_path, size):
    try:
        # Open the image file
        with Image.open(input_path) as img:
            # Resize the image
            img_resized = img.resize(size, Image.LANCZOS)
            # Save the resized image
            img_resized.save(output_path)
            print(f"Image resized and saved to {output_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python resize_image.py <input_path> <output_path> <width> <height>")
    else:
        input_path = sys.argv[1]
        output_path = sys.argv[2]
        width = int(sys.argv[3])
        height = int(sys.argv[4])
        resize_image(input_path, output_path, (width, height))
