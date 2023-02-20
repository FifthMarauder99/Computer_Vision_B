# svujjin-apore-dbharton-sajairam-a1

# Part  1:  Hough Transforms

## Statement : 

We are given an image consisting of 5 lines that are (approximately) parallel and (approximately) evenly-spaced, but you don’t know the spacing of the lines ahead of time and we don’t know their orientation in the image. There may be noise so that not all of the lines are completely visible, there may be distracting objects, etc.
We need to write program called staff finder.py that takes an image as input and then finds the best fit of the model to the image data. 

## Approach Explanation :

To detect the lines in the given image, we implemented hough transform

- To ensure that the algorithm can identify the lines in the image correctly, converted to binary image in which the edges are clearly defined, i.e., loaded the input image, converted it to gray scale and detected edges using FIND_EDGES from the ImageFilter library.

- Using the accumulator two-dimensional numpy array, we defined the hough space. The largest possible values of rho (the distance of a line from the origin) and the total number of possible angles theta determine the accumulator's dimensions (angle of straight line w.r.t. the horizontal axis).

- Voting scheme was used to further increase the cells' initial values in the accumulator, which was initialized with zeroes. This allowed the points in the parameter space that correspond to the lines in the image to be accumulated.

- Computed the value of rho for each potential angle and increased the associated cell in the accumulator. This process looped through all edge points and potential angles in the image between 80 and 180 degrees.
- For each line, found the maximum value in the accumulator and extracted the corresponding rho and theta values and stored them in the list of peaks in the accumulator, representing the most prominent lines in the image. 

- Once a peak is detected in the accumulator, zeroed out the adjacent cells to ensure that the same line is not detected again in order to avoid overlapping lines.

- Finally, traced the lines found on the original image.
 
## Problems Faced :

 - Selecting the appropriate values for these parameters such as theta values and rho step size was challenging and required lot of trial and error.
 
 - Correctly identifying the shape of the lines as the detected lines were overlapping with each other. 

## Hough Transform :

- We got the following image as the hough transform after the successful run of the program. 

![image](files:part1/Hough Transform.png)



### References Used :

https://www.youtube.com/watch?v=M43yXpp2qW8 <br/>
https://medium.com/@tomasz.kacmajor/hough-lines-transform-explained-645feda072ab <br/>
https://www.youtube.com/watch?v=5zAT6yTHvP0 <br/>
https://www.youtube.com/watch?v=XRBc_xkZREg <br/>
https://www.cs.cmu.edu/~16385/s17/Slides/5.3_Hough_Transform.pdf <br/>
