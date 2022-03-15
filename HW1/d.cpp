#include <opencv2\opencv.hpp> 
#include <opencv2\highgui\highgui.hpp>
#include<opencv2\imgproc.hpp>
#include <iostream>
#include<stdio.h>

using namespace cv;
using namespace std;

void main() {
	string path = "resources/lena.bmp";
	Mat img = imread(path, IMREAD_GRAYSCALE);
	double angle = 45;
	double width = img.cols - 1, height = img.rows - 1;
	Point center(width/2,height/2);
	Mat rotate_mat = getRotationMatrix2D(center, angle, 1.0);
	Mat rotate_img;
	warpAffine(img, rotate_img, rotate_mat, img.size());
	imshow("Rotation Image", rotate_img);
	imwrite("resources/Rotation.bmp", rotate_img);
	waitKey(0);
}
