# 👋🏻 Scribbled Notebook
The following records the activities of the seminars, such as basics of computer vision, deep learning, 3D programming, and 3D content creation. The code and operating techniques described are updated to ensure that they can be executed in the current environment as much as possible.
- Pytorch for dummies
- OpenCV for beginners
- Object detection & Segmentattion with OpenMMlab
- Tutorials (for students)

The code in this repository can be run on Google Colaboratory. If you want to reduce the time it takes to train a neural network, you can simply connect Google Colaboratory to your local runtime. Below is how to setup your local server.
```
conda create -n colab python=3.8.3
conda activate colab
pip install -U scikit-learn==1.2.2 --user
pip install albumentations==1.3.1 --user
pip install pandas==1.5.3 --user
pip install segmentation-models-pytorch
pip install opencv-python==4.8.0.76
pip install matplotlib
pip install seaborn
pip install torchsummary

[gpu/cuda]
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

Run notebook and copy the URLs
```
jupyter notebook --NotebookApp.allow_origin='https://colab.research.google.com' --port=8888 --NotebookApp.port_retries=0
```
Ex: the URL may be like below.
```
http://127.0.0.1:8888/?token=78e3af624806cef63cfc125a8b388c96f1a786659ff2eb5f
```

<div align="center">
	<br>
	<img src="https://raw.githubusercontent.com/Aniket965/Aniket965/master/pacman.svg?sanitize=true" width="200" height="200">
</div>
