import os
import cv2

# Define the image path (update if needed)
image_path = r"C:\Users\Sahar\MA-AGIQA\dataset\AGIQA_3k\sd1.5_lowcorr_189.jpg"



# ✅ Check if the file exists
if os.path.exists(image_path):
    print("✅ File exists!")

    # Try to load the image with OpenCV
    img = cv2.imread(image_path)

    if img is None:
        print("❌ ERROR: OpenCV could not read the image. The file might be corrupted.")
    else:
        print("✅ SUCCESS: Image loaded successfully!")
        print("Image shape:", img.shape)  # Should print (height, width, channels)

        # Show the image in a window
        cv2.imshow("Loaded Image", img)
        cv2.waitKey(0)  # Wait for a key press
        cv2.destroyAllWindows()  # Close the window

else:
    print("❌ File NOT found! Check the path.")
    print("📂 Current working directory:", os.getcwd())
    print("🛠 Try running this command before executing the script:")
    print(f'os.chdir(r"{os.path.dirname(image_path)}")')
