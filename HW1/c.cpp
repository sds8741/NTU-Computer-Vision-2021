#include <opencv2\opencv.hpp> 
#include <opencv2\highgui\highgui.hpp>
#include<opencv2\imgproc.hpp>
#include <iostream>

using namespace cv;
using namespace std;

void main() {
	string path = "resources/lena.bmp";
	Mat img = imread(path, IMREAD_GRAYSCALE);
	int height = img.rows -1 ;
	int width = img.cols - 1;
	Mat dia_img(height+1,width+1,CV_8UC1);
	for (int i = 0; i <= height; i++) {
		for (int j = 0; j <= width; j++) {
			dia_img.at<uchar>(i, j) = img.at<uchar>(j, i);
			
		}
	}
	imshow("Image", dia_img);
	imwrite("resources/Diagonal.bmp", dia_img);
	waitKey(0);
}