import numpy as np
import cv2 as cv
from scipy.spatial.transform import Rotation
from math import cos, sin, radians
import parta

rvecs = parta.rvecs
tvecs = parta.tvecs
r_obj = Rotation.from_rotvec(np.array(rvecs[0]).reshape(1,3))
rot_matrix = r_obj.as_matrix()
nprvecs = np.array(rvecs)
nptvecs = np.array(tvecs)
# Creation of rotation matrix from rotation vector
xc, xs = cos(radians(nprvecs[0][0][0])), sin(radians(nprvecs[0][0][0]))
yc, ys = cos(radians(nprvecs[0][1][0])), sin(radians(nprvecs[0][1][0]))
zc, zs = cos(radians(nprvecs[0][2][0])), sin(radians(nprvecs[0][2][0]))
# Translated matrix
tx = nptvecs[0][0][0]
ty = nptvecs[0][1][0]
tz = nptvecs[0][2][0]
translation_mtx = np.array([[1,0,0,tx],[0,1,0,ty],[0,0,1,tz],[0,0,0,1]])
#Creation of  rotation matrices along x,y and z
rot_x_mtx = np.array([[1,0,0,0],[0,xc,-xs,0],[0,xs,-xc,0],[0,0,0,1]])
rot_y_mtx = np.array([[yc,0,ys,0],[0,1,0,0],[-ys,0,yc,0],[0,0,0,1]])
rot_z_mtx = np.array([[zc,-zs,0,0],[zs,zc,0,0],[0,0,1,0],[0,0,0,1]])
ext_mtx = np.dot(rot_z_mtx, np.dot(rot_y_mtx, np.dot(rot_x_mtx, translation_mtx)))
int_mtx = np.append( np.append(parta.mtx, [[0],[0],[1]], axis=1), [np.array([0,0,0,1])], axis=0)
print('Intrinsinc mtx: ', int_mtx)
print('Extrinsinc mtx, ', ext_mtx)

# Camera Matrix
camera_matrix = np.dot(int_mtx, ext_mtx)
print("Camera mtx: ", camera_matrix)
cv.destroyAllWindows()

inverse_mat = np.linalg.inv(camera_matrix) 
project_points = np.array([[5],[10],[30],[1]])
real_dim = inverse_mat.dot(project_points)

print("Here are the dimension")
print(real_dim)
print("x axis length - ", real_dim[0][0])
print("y axis length - ", real_dim[1][0])
print("z axis length - ", real_dim[2][0])