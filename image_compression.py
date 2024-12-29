from PIL import Image

def compress_image(input_path, output_path, quality=85):
    """
    Compress an image to reduce its file size.

    Parameters:
        input_path (str): Path to the input image.
        output_path (str): Path to save the compressed image.
        quality (int): Compression quality (1-100, higher means better quality but larger size). Default is 85.
    """
    try:
        # Open the image using PIL
        image = Image.open(input_path)

        # Print original file size and dimensions
        print(f"Original size: {image.size}, Format: {image.format}")
        
        # Save the image with reduced quality
        image.save(output_path, quality=quality, optimize=True)

        # Print success message
        print(f"Compressed image saved to {output_path} with quality={quality}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_image_path = ""  # Replace with your input image path
output_image_path = ""  # Replace with desired output path
compression_quality = 70  # Compression quality (lower for smaller file size)

compress_image(input_image_path, output_image_path, compression_quality)
