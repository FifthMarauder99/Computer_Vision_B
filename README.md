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

<img width="200" alt="Hough Transform" src="https://media.github.iu.edu/user/21707/files/a48f5723-529e-4f86-b745-efc99d454d13">



### References Used :

https://www.youtube.com/watch?v=M43yXpp2qW8 <br/>
https://medium.com/@tomasz.kacmajor/hough-lines-transform-explained-645feda072ab <br/>
https://www.youtube.com/watch?v=5zAT6yTHvP0 <br/>
https://www.youtube.com/watch?v=XRBc_xkZREg <br/>
https://www.cs.cmu.edu/~16385/s17/Slides/5.3_Hough_Transform.pdf <br/>


# Part  2:  Optical Music Recognition

## Statement:

Given the music notes and image of three objects (filled note, quarter rest, and eight rest), we are asked to detect those object and predict the pitch tone for each filled note.

## Assumption:
- Staff lines are assumed to be perfectly horizontal
- Ignoring sharp note symbol & flat note symbol
- We only detect 3 objects: filled note, quarter rest, and eight rest

## Approach Explanation:

- Firstly, we binarize the input image by replacing each pixel's value with 0 if it is greater or equal to 127.5 and 0 otherwise. 127.5 is chosen as it is the middle value of the range [0,255].

- Finding staff lines and their coordinate. In this step, we assume that staff lines are horizontal. Instead of using hough transform and search for various angle, we use the simpler approach where the program will scan through image horizontally on each row. Since we are finding staff lines which are black pixels (value of 0), the program will give one point every time it finds 0 value. This point will be stored in accumulator to be aggregated. With some threshold, we decide that a row is considered to have a staff if the black pixels occupy 45% of the input image's width. After finding those lines, we record the row coordinates in which staff is detected.

- For noisy image, we found that the previous step detected multiple line in a single staff. Therefore, we have to choose a single line that well represents a staff. We use 1D non maximum suppression algorithm to perform this task. 1D is because we only considers the y axis since staves are assumed to be horizontal, x axis is constant. This algorithm check an accumulator value to its neighbors, if that value is bigger then it will keep the value. However if it is lower, the value will be replaced with 0. To find how many neighbors should be checked, we use trial and error method and we found that checking 10 neighbors (5 at the beginning and 5 after) gives the best result.

- After processing the staff lines, we estimate the distance between them. We calculated the gap on each pair of lines and store the results, then we picked one by using mode of those gaps. This gap will later be used to estimate the size of 3 objects that we are going to detect in the image.

- In the subsquent process, we determine the location of the first staff in each set of tone row / note row. To do so, we are using the representative gap to determine this first staff. We estimated that each tone row has distance not less than 3 times of the gap. Visually, they look like having the distance of 5 times or more of the gap, but we considered there might be some pitches in lower and high octave that rest outside the 5 staff lines.

- This gap also is used to determined the pitch of filled notes where the distance between pitch is half of the gap. As we do not consider '#'(sharp note symbol) and '♭' (flat note symbol) sign on music note which tells if notes should be played 1 or more pitch higher or lower, we determine the pitch label based on the regular note (without # and ♭). In this process, we create a dictionary that consists of the pitch coordinate as key and pitch label as value.

- After preparing all those references, we start to detect the objects. Beforehand, we make adjustment to the reference image. Input images (music note) is not standardized where they come with different sizes. Hence, we need to rescale the reference image based on the detected staff gap. For filled notes, we use the reference image height the same as the staff gap, eight rest is twice of the gap, and quarter rest is thrice of the gap. During rescaling, we keep the width & heighr ratio the same. As an example, assuming that we have reference size 5x5 and wanting to rescale it such that the height is 8. By keeping the ratio the same, in this case is 1, the new image will have size of 8x8.

- Then, we convolve this new reference image through all the pixels in the image.

- During the convolution, we apply correlation coefficient algorithm where it find the correlation value, ranging [-1, 1], between the reference image and the sub image. The figure below is the formula to calculate the correlation coefficient. 'I' is sub image, while 'R' is reference image.
<img width="569" alt="Screenshot 2023-02-21 at 14 58 08" src="https://media.github.iu.edu/user/20652/files/2bb06ad0-cd84-4d84-aada-49bbf9e0b371">

- 
- 


