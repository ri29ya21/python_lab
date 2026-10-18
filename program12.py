#Program 12: Digital Image Filter and Color Converter Utility

from PIL import Image, ImageFilter, ImageOps


def process_image():
    filename = input("Enter image filename (e.g. photo.jpg): ")

    try:
        image = Image.open(filename).convert("RGB")

        print("\nImage Processing Menu")
        print("1. Grayscale")
        print("2. Black and White")
        print("3. Blur")
        print("4. Edge Detection")
        print("5. Invert Colors")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            result = ImageOps.grayscale(image)

        elif choice == "2":
            grayscale = ImageOps.grayscale(image)
            result = grayscale.point(
                lambda pixel: 255 if pixel >= 128 else 0
            )

        elif choice == "3":
            result = image.filter(
                ImageFilter.GaussianBlur(radius=3)
            )

        elif choice == "4":
            result = image.filter(ImageFilter.FIND_EDGES)

        elif choice == "5":
            result = ImageOps.invert(image)

        else:
            print("Invalid choice.")
            return

        output_file = "processed_image.png"
        result.save(output_file)
        result.show()

        print("Image processed successfully.")
        print("Saved as:", output_file)

    except FileNotFoundError:
        print("Error: Image file not found.")

    except Exception as error:
        print("Error processing image:", error)


if __name__ == "__main__":
    process_image()