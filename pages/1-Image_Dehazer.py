import streamlit as st
from PIL import Image
from io import BytesIO
from Dehaze_module import remove_haze
import numpy as np

st.set_page_config(layout="wide", page_title="Image Haze Remover")

st.write("## Remove Haze from your image")
st.write(
    "😎 Try uploading an image to watch the Haze magically removed. Full quality images can be downloaded from the sidebar. This code is avaliable on my account [here](https://github.com/parmishh)"
)
st.sidebar.write("## Upload and download :gear:")


# Download the fixed image
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im


def fix_image(upload):
    image = Image.open(upload)
    col1.write("Original Image :camera:")
    col1.image(image)
    						# read input image -- (**must be a color image**)
    pix = np.array(image)
    fixed, haze_map = remove_haze(pix, showHazeTransmissionMap=False)	
    PIL_image = Image.fromarray(pix.astype('uint8'), 'RGB')
    col2.write("Fixed Image :wrench:")
    col2.image(fixed)
    st.sidebar.markdown("\n")
    st.sidebar.download_button("Download fixed image", convert_image(PIL_image), "fixed.png", "image/png")


col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if my_upload is not None:
    fix_image(upload=my_upload)
