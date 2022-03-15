#include <opencv2\opencv.hpp> 
#include <opencv2\highgui\highgui.hpp>
#include<opencv2\imgproc.hpp>
#include <iostream>

using namespace cv;
using namespace std;

void main() {
	string path = "resources/lena.bmp";
	Mat img = imread(path, IMREAD_GRAYSCALE);
	Mat img_clone;
	img.copyTo(img_clone);
	int row = img.rows - 1;
	int col = img.cols - 1;

	for (int i = 0; i <= col; i++) {
		for (int j = 0; j <= row; j++) {
			img.at<uchar>(i, j) = img_clone.at<uchar>(i, col - j);
		}
	}
	imshow("Image", img);
	imwrite("resources/Rightleft.bmp", img);
	waitKey(0);
}