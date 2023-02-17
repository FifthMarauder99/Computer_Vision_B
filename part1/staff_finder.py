import sys
import numpy as np
from PIL import Image, ImageDraw

def hough_transform(img):
    gray = np.array(img.convert('L'))
    # Detect edges using Canny edge detector
    edges = gray.filter(ImageFilter.FIND_EDGES)
    
    # Define the Hough space
    w, h = edges.size
    max_rho = np.ceil(np.sqrt(h**2 + w**2))
    theta_res = np.pi/180
    rho_res = 1
    accumulator = np.zeros((int(2 * max_rho // rho_res), int(180 // theta_res)))

    # Loop over all edge points
    edge_pixels = edges.load()
    for x in range(w):
        for y in range(h):
            if edge_pixels[x, y] == 255:
                # Loop over all possible angles in range of -45 to 45 degrees
                for theta_idx in range(80, 180, 24):
                    theta = (theta_idx - 90) * theta_res
                    rho = x * np.cos(theta) + y * np.sin(theta)
                    rho_idx = int(round(rho / rho_res)) + int(max_rho // rho_res)
                    accumulator[rho_idx, theta_idx] += 1
                
    return accumulator, max_rho, theta_res, rho_res


def hough_show_lines(img, n_lines=5):
    accumulator, max_rho, theta_res, rho_res = hough_transform(img)
    
    # Find the peaks in the Hough space
    peaks = []
    for i in range(n_lines):
        rho_idx, theta_idx = np.unravel_index(np.argmax(accumulator), accumulator.shape)
        rho = (rho_idx - int(max_rho // rho_res)) * rho_res
        theta = (theta_idx - 90) * theta_res
        peaks.append((rho, theta))
        
        # Zero-out the surrounding cells in the accumulator to avoid overlapping lines
        for j in range(-10, 11):
            for k in range(-10, 11):
                if rho_idx+j >= 0 and rho_idx+j < accumulator.shape[0] and theta_idx+k >= 0 and theta_idx+k < accumulator.shape[1]:
                    accumulator[rho_idx+j, theta_idx+k] = 0
                    
    # Draw the detected lines on the original image
    img = img.convert('RGB')
    draw = ImageDraw.Draw(img)
    for rho, theta in peaks:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        
        draw.line((x1, y1, x2, y2), fill="red", width=2)
        


    img.save("detected staff.png")

if __name__ == '__main__':
    
    if(len(sys.argv) < 2):
        raise Exception("error: please give an input image name as a parameter, like this: \n"
                        "python3 staff_finder.py sample-input.png")
    
    img = Image.open(sys.arv[1])
    hough_show_lines(img)
                                        
