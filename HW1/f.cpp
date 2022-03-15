#include <opencv2\opencv.hpp> 
#include <opencv2\highgui\highgui.hpp>
#include<opencv2\imgproc.hpp>
#include <iostream>


using namespace cv;
using namespace std;

void main() {
	string path = "resources/lena.bmp";
	Mat img = imread(path, IMREAD_GRAYSCALE);
	Mat binary_img;
	int th = 128;
	threshold(img, binary_img, th, 255, THRESH_BINARY);
	imshow("Binary", binary_img);
	imwrite("resources/Binary.bmp", binary_img);

	waitKey(0);
}
