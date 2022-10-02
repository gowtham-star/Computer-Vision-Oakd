# Computer-Vision-Oakd
 Computer Vision Assignments

Assignment 1) All the files related to each task in their respective folders.

Part A) 
Written the script parta.py
Firstly, I used the images from part 4 to calibrate using the given  opencv toolbox script tutorial to find the camera matrix ausing  opencv.caliberateCamera() and calculated the camera matrix = Intrinsic matrix * Extrinsic matrix. Calibration results are:

Intrinsic Matrix:

[[462.56484414   0.         305.97412997]
 [  0.         623.96855446 267.16069973]
 [  0.           0.           1.        ]]


Part B) partb.py is the script created and used. Here we find the real world co ordinates using prespective projection. The answer is in negative as the mirrored image is taken by oakd-camera.

We take the calculate camera matrix part a and caluate real world co ordinates using prespective projection equation.

The real world co ordainates
x axis length -  -9.458911910179621
y axis length -  -15.388305710245824
z axis length -  -57.055634097823884

Part C) It is achievable and rgb_stero_camera.py is the script created and used.

Stereo Camera:
Max Resolution: 720P
Max Frame Rate: 120 FPS

Color Camera:
Max Resolution: 13 MP
Max Frame Rate: 60 FPS



Part D)

 Used the calibrate.py script from depthai folder in  github repository to capture images in 13 different angles and found the calibration results below:

Intrinsic Matrix

[[457.1668    0.      320.9126]
[    0.     556.0823  240.56018]
[   0.          0.        1.]]
