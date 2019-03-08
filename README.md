# FE_intensity
## master project: recognising facial expression intensity

time: 05/2018 - 08/2018

quantify the facial expression of one person

### using virtualenv to create isolate python environment in this project

### using openCV

### using local binary pattern algorithm(LBP)

### using principal component analysis algorithm(PCA) to reduce the dimensionality

### using support vector machine(SVM) to get a linear regression function

This project does not make the graphical user interface because of time limits. All programs are executed in the command line in PyCharm. Figure 5.10 shows the beginning of the program when it is executed.<Br/>
![image](https://github.com/XiaozhengHe/FE_intensity/blob/master/src/test/data/img/testing_results/begining.png)<Br/>
Figure 5.10: The beginning of the program<Br/>

Then, users could input an integer between 1 and 6 to make the program do the corresponding work. We only consider the situation when the user inputs “6”, because this is what the program is analysing. After inputting 6, the program will show the intensity of the person’s facial expressions in the video which is accepted by the program (the video can be changed to another one by change the path to it), and the intensity will be shown using a percentage. Figure 5.11 shows the first selected frame’s facial expression intensity of the person’s facial expression in the video, and the happy intensity is 30.12%.<Br/>
![image](https://github.com/XiaozhengHe/FE_intensity/blob/master/src/test/data/img/testing_results/1.png)<Br/>
Figure 5.11 The happy level of the first selected frame<Br/><Br/>
For a video, it is not essential to process all frames of it because it will be time-consuming and meaningless to process. We choose to process every tenth frame. What is more, the intensity of the facial expression of that frame is expressed as a percentage. Figure 5.12 shows the percentage of the happy facial expressions in the third selected frame, and the happy intensity is 60.58%.<Br/>
![image](https://github.com/XiaozhengHe/FE_intensity/blob/master/src/test/data/img/testing_results/2.png)<Br/>
Figure 5.12: The happy level of the third selected frame<Br/><Br/>
Figure 5.13 shows the percentage of the happy facial expressions in the seventh selected frame, and the happy intensity is 77.56%.<Br/>
![image](https://github.com/XiaozhengHe/FE_intensity/blob/master/src/test/data/img/testing_results/3.png)<Br/>
Figure 5.13: The happy level of the seventh selected frame<Br/>

Figure 5.14 shows the percentage of the happy facial expressions in the ninth selected frame, and the happy intensity is 53.20%.<Br/>
![image](https://github.com/XiaozhengHe/FE_intensity/blob/master/src/test/data/img/testing_results/4.png)<Br/>
Figure 5.14: The happy level of the ninth selected frame<Br/>

Figure 5.15 shows the percentage of the happy facial expressions in the eleventh selected frame, and the happy intensity is 37.02%.<Br/>
![image](https://github.com/XiaozhengHe/FE_intensity/blob/master/src/test/data/img/testing_results/5.png)<Br/>
Figure 5.15: The happy level of the eleventh selected frame
