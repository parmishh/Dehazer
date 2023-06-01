import streamlit as st
st.set_page_config(
    page_title = "Dehazer",
    page_icon = "🌐",
    layout = "wide",
)
st.title(""" Dehazer
[![](https://private-user-images.githubusercontent.com/91942072/241233617-852ecf78-e684-438e-b53a-5944261b9aa3.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJrZXkxIiwiZXhwIjoxNjg1MTA4MzI1LCJuYmYiOjE2ODUxMDgwMjUsInBhdGgiOiIvOTE5NDIwNzIvMjQxMjMzNjE3LTg1MmVjZjc4LWU2ODQtNDM4ZS1iNTNhLTU5NDQyNjFiOWFhMy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBSVdOSllBWDRDU1ZFSDUzQSUyRjIwMjMwNTI2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDIzMDUyNlQxMzMzNDVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT03ODU4MWJlOTRmNzM0YTFiZGJmZThjMTcxMzJjYzJjNDgzY2QwMTgzNjM1MGQyNjgyOTBiNTZkNjgzZmNiZDA1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.q6-S0rDvqITNe7_xFLI3OcgzQsGc3wro53Ihy8fY3vw)](https://github.com/parmishh)""")



st.subheader("Problem Identified:")
st.write(""" **Haze & Fog causes several Road and Plane accidents.** Survey By Times of INDIA Shows about **11000 people died** because of accidents met due to Fog/Haze during the year 2017 and the number keeps on increasing
every year. Article By TOI: [LINK ](https://timesofindia.indiatimes.com/india/over-10000-lives-lost-in-fog-related-road-crashes/articleshow/67391588.cms)""")

st.image("stats.jpg")
st.write("""Several Plane and Chopper crashes has been reported due to low visibility caused by Fog and Haze.In 2019 we lost Chief of Defence Staff, General Bipin Rawat during a chopper crash caused by low visibility caused by haze. Another accident in which **234 people died** during a indonesian Jet crash due to reduced visibility caused by Fog and Haze Article By NewYork Times: [LINK ](https://www.nytimes.com/1997/09/27/world/indonesia-jet-crash-kills-all-234-aboard-haze-was-a-possible-cause.html)""")
st.write("""We now have a solution thanks to the breakthroughs in **Image processing Algorithms and Deep Learning techniques**. With this project we hope to come one step closer to Prevent **Accidents due to reduced visibilty caused by Fog and Haze** for good!""")
st.subheader("Solution:")

st.image("Capture.jpg")
st.write("we have used the Efficient Image Dehazing with Boundary Constraint and Contextual Regularization Research papers as our base thanks to Gaofeng MENG, Ying WANG, Jiangyong DUAN, Shiming XIANG, Chunhong which helped to produce a image Dehazer Algorithm the next step I took is to take a input video and split it into frames and apply image Dehazing on each frame and merge them back to produce our output video.")
st.subheader("PyPi Packages Published as a part of this Project:")
st.write("""
    I Published some PyPi packages while Developing this Project. Now this Project can be used by installing it via simple pip command
    1. Dehazer: [LINK]() 
      ```pip install Dehazer```
    """)
col1, col2 = st.columns(2)
with col1:
    st.subheader("Steps to use this project:")
    st.write("""
    1. open the page for which operation you want to perform
    2. Upload images or videos
    3. You will get the Processed output""")
st.subheader("Features:")
st.write("""
    1. Image Dehazer
    2. Video Dehazer
    3. Image Bg Remover
    4. Video Bg Remover""")
st.subheader("Acknowledgement:")
st.write(""" Thanks to Ying WANG, Jiangyong DUAN, Shiming XIANG, Chunhong PAN for their paper "Efficient Image Dehazing with Boundary Constraint and Contextual Regularization""")
