# DE-TECHT DOCUMENTATION
## What is it?
This is a pretty basic motion detection project.
It can be used to perform two elaborate tasks if implemented and applied with proper infrastructure: 
Detecting and tracking cars in traffic as well as detecting faces and tracking any type of motion.

## What do I need to install for it?
You will need the Python3 installed on your system along with [OpenCV](https://docs.opencv.org/master/) , [bokeh](https://docs.bokeh.org/en/latest/index.html) and [pandas](https://pandas.pydata.org/docs/)
### To install OpenCV
Open the system's command prompt and type in the following command `pip install opencv-python`

### To install Bokeh
Open the system's command prompt and type in the following command `pip install bokeh`

### To install Pandas
Open the system's command prompt and type in the following command `pip install pandas`


## How do I run it?

### Face and Motion detector
To run the face and motion detector program, open the command prompt and type in the following command after going to the appropriate directory: `python plotting.py` . This will run the face-detector and  motion tracker program using the video feed from your computer system's web camera. To exit web camera and view the motion monitoring plot, press `q`

### Car detector
To run the car-detector program, open the command prompt and type in the following command after going to the appropriate directory: `python car_detector.py` .This will run the car detector program using the provided video file [vehicles.mp4](https://github.com/Saswata13/De-Techt/blob/master/vehicles.mp4?raw=true) . If you wish to run it using another mp4 file, copy it into the appropriate directory and replace the code in line **11** of [car_detector.py](https://github.com/Saswata13/De-Techt/blob/master/car_detector.py) with `cap = cv2.VideoCapture('_filename_.mp4')` where '_filename_' is the name of your  video file. In reality video should be captured from a camera installed in an appropriate location near roadways. To exit the video file press `esc`.

### NOTE
MAC users should use `pip3 install package_name` for installing packages and `python3 file_name.py` to run the files

### For a detailed explanation on the usage and application of the above programs please watch the following video: ['De-Techt.mp4'](https://github.com/Saswata13/De-Techt/blob/master/De-Techt.mp4?raw=true) from the above directory.

### For a detailed explanation about the idea, working and the 3 main applications, please see the presentation:['De-Techt.pptx'] (https://drive.google.com/drive/u/0/folders/1fPy1Sed5TweSfuhY6DOTFi9bGT65hKQy) in google drive.

### MADE BY:
* SASWATA MUKHERJEE  
* SHUBHAM GANDHI
