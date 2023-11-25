import os
import cv2
import torch
from skimage.metrics import peak_signal_noise_ratio
import lpips
from torchvision import transforms

def calculate_psnr(img1, img2):
    # Read images
    image1 = cv2.imread(img1)
    image2 = cv2.imread(img2)

    # Convert images to grayscale
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Calculate PSNR
    psnr = peak_signal_noise_ratio(gray1, gray2)

    return psnr

def calculate_lpips(img1, img2, lpips_model):
    # Read images
    image1 = cv2.imread(img1)
    image2 = cv2.imread(img2)

    # Convert images to PyTorch tensors
    transform = transforms.ToTensor()
    image1_tensor = transform(image1).unsqueeze(0)
    image2_tensor = transform(image2).unsqueeze(0)

    # Calculate LPIPS
    lpips_value = lpips_model(image1_tensor, image2_tensor).item()

    return lpips_value

def calculate_average_scores(folder1, folder2):
    # Create LPIPS model
    lpips_model = lpips.LPIPS(net='vgg')  # You can choose a different model if needed

    psnr_scores = []
    lpips_scores = []

    # Iterate over files with the same filenames in both folders
    for filename in os.listdir(folder1):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img1_path = os.path.join(folder1, filename)
            img2_path = os.path.join(folder2, filename)

            # Check if the corresponding image exists in the second folder
            if os.path.exists(img2_path):
                # Calculate PSNR and LPIPS
                psnr = calculate_psnr(img1_path, img2_path)
                lpips_score = calculate_lpips(img1_path, img2_path, lpips_model)

                psnr_scores.append(psnr)
                lpips_scores.append(lpips_score)

    # Calculate average scores
    avg_psnr = sum(psnr_scores) / len(psnr_scores) if psnr_scores else 0
    avg_lpips = sum(lpips_scores) / len(lpips_scores) if lpips_scores else 0

    print(f"Average PSNR: {avg_psnr}")
    print(f"Average LPIPS: {avg_lpips}")

if __name__ == "__main__":
    # Replace 'folder1' and 'folder2' with your folder names
    folder1 = './Obama_val_450'
    folder2 = './Obama_groundtruth'

    calculate_average_scores(folder1, folder2)

