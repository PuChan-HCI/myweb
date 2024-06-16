import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
import cv2
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def main():
    selected_box = st.sidebar.selectbox(
        'Choose one of the following',
        ('Welcome', 'Image Processing','Graph','Map')
    )
    if selected_box == 'Welcome':
        welcome()
    if selected_box == 'Image Processing':
        photo()
    if selected_box == 'Graph':
        graph()
    if selected_box == 'Map':
        tokyo()

def welcome():
    st.title('Streamlitで画像処理を実演する')
    st.header('～何でもやってみましょう～')
    st.text('Webで簡単にグラフを書いたり，映像を表示しタイルすることもできるため'
                 + '研究打ち合わせが楽になる' +
                 '\nYou are free to add stuff to this app.')

class VideoProcessor:
    def __init__(self) -> None:
        self.threshold1 = 100
        self.threshold2 = 200

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        img = cv2.cvtColor(cv2.Canny(img, self.threshold1, self.threshold2), cv2.COLOR_GRAY2BGR)
        return av.VideoFrame.from_ndarray(img, format="bgr24")

def photo():
    ctx = webrtc_streamer(key="example", video_processor_factory=VideoProcessor)
    if ctx.video_processor:
        ctx.video_processor.threshold1 = st.slider("Threshold1", min_value=0, max_value=1000, step=1, value=100)
        ctx.video_processor.threshold2 = st.slider("Threshold2", min_value=0, max_value=1000, step=1, value=200)

def graph():
    fig = plt.figure(figsize=(10, 5))
    ax = plt.axes()
    x = [105, 210, 301, 440, 500]
    y = [10, 20, 30, 50, 60]
    ax.plot(x, y)
    st.pyplot(fig)

def tokyo():
    tokyo_lat = 35.69
    tokyo_lon = 139.69
    df_tokyo = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [tokyo_lat, tokyo_lon],
        columns=['lat', 'lon']
    )
    st.map(df_tokyo)

if __name__ == "__main__":
    main()
