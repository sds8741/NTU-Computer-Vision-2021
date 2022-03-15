#include <opencv2\opencv.hpp> 
#include <opencv2\highgui\highgui.hpp>
#include<opencv2\imgproc.hpp>
#include <iostream>

using namespace cv;
using namespace std;

void main() {
	string path = "resources/lena.bmp";
	Mat img = imread(path, IMREAD_GRAYSCALE);
	double width = img.cols - 1, height = img.rows - 1;
	Mat resize_img;
	resize(img, resize_img, Size(width/2, height/2), 0, 0, INTER_LINEAR);
	imshow("Original", img);
	imshow("Resize", resize_img);
	imwrite("resources/Resize.bmp", resize_img);
	waitKey(0);
}
