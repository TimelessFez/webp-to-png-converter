# Imports
from PIL import Image
import os.path

while True:
    image = input("\nPlease enter the directory of the image file ending with .webp: \n")

    # Check if dir ends with .webp
    if image.endswith(".webp"):
        break
    else:
        print("\nError: Incorrect image format. Only .webp is supported. Please try again.")

# Convert to RGB
im = Image.open(image).convert("RGB")

# Change file format (replaces string; dir path)
output = image.replace(".webp", ".png")

# Check if file already exists in path
path = (output)
checkFile = os.path.isfile(path)

  # For debug (prints T/F)
  # print(f"{checkFile}")

while True:
    if checkFile:
        print("\nFile has already been converted.")
        break
    else:
        # Save as .png
        im.save(output, "png")
        # Fin
        print(f"\nThe image has been saved in: \n{output}")
        break
