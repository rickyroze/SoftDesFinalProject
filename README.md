# SoftDesFinalProject
Satelite Image Processing
By Aiden Carley-Clopton, Grace Montagnino, and Richard run_docstring_examples

#Dependencies
 PIL, os, numpy, cv2

# Image Repo
The small to medium sized images in this project are stored in a second github
repo. You can clone it here: https://github.com/aidenclpt/Final_Project_Image_Repo
The file path in which you locate it doesn't matter, except for a line in
image_load.py which references the landsat bands stored within it.

# image_load.py

This file contains the functions used to make color images out of multiple
channels obtained from satellite imagery. It balances the levels to account for
the fact that raw sensor data provides very dim images. It creates a directory
