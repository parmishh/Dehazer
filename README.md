# Dehazer

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)                 
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)   

## Problem statement
**Haze & Fog causes several Road and Plane accidents:** Survey By Times of INDIA Shows about **11000 people died** because of accidents met due to Fog/Haze during the year 2017 and the number keeps on increasing every year. Several Plane and Chopper crashes has been reported due to low visibility caused by Fog and Haze.In 2019 we lost Chief of Defence Staff,during a chopper crash caused by low visibility caused by haze. Another accident in which **234 people died** during a indonesian Jet crash due to reduced visibility caused by Fog and Haze.

## Solution
With the advancement in Image Processing Algorithms and Technology. We now have a solution the Dehaze_module implements the **"Boundary Constraint and Contextual Regularization algorithm"** which refers to theory and equations of the research by Gaofeng MENG. The module thus developed helps us to dehaze images. We can futher make use of the fact that video is made up of frames, we extract frames and process each frame and append it to a array and finally combine the processed frames to give Dehazed video output. It can be used to have a clear view in Haze/Foggy weather and reduce chances of road accidents and plane crashes.
## Functionality of the Dehazer

- Removes Haze and Fog and enhances quality of Videos/Images.
- Removes Background and enhances quality of Videos/Images.


## Working
<table align="center">
<tr>
    <td align="center">&nbsp;<img src="https://user-images.githubusercontent.com/91942072/243196291-fe4b85fd-1a5c-44d9-81e0-3a0fb73690fc.png" alt="parmishh" />Image Dehazing Algorithm</td>
 <td align="center">&nbsp;<img src="https://user-images.githubusercontent.com/91942072/243196277-0257b2bb-815a-421c-9b1c-4fdeeca7267e.PNG"  alt="parmishh" />Video Dehazing Implementation</td>
</tr>
</table>

## How to use and Contribute

`fork the repository`

```
git clone https://github.com/{your github username here}/Dehazer
```

`cd Dehazer`



```
pip install -r requirements.txt

```

```
streamlit run Homepage.py
```

`Project will start running in localhost`

## Now This Project is Published on PyPi🎉
This project is now Published on PyPi and its the first Video Dehazer on PyPi that provides Video Dehazing,Video Bgremoval and other image processing tools!
Just use: 
```
pip install Dehaze
```
How to use it: https://pypi.org/project/Dehaze/


## Outputs
<table align="center">
<tr>
    <td align="center">&nbsp;<img src="https://user-images.githubusercontent.com/91942072/243181999-362477ea-db0d-4d80-975e-61cb1a4913b8.gif" alt="parmishh" /></td>
 <td align="center">&nbsp;<img src="https://user-images.githubusercontent.com/91942072/243198402-ea0557ec-372b-43c1-85b1-745c2434582c.gif"  alt="parmishh" /></td>
</tr>
</table>
<table align="center">
<tr>
    <td align="center">&nbsp;<img  src="https://user-images.githubusercontent.com/91942072/240655359-cf2f5724-d91f-4874-a761-459835c15a24.jpg" alt="parmishh" /></td>
 <td align="center">&nbsp;<img  src="https://user-images.githubusercontent.com/91942072/240655369-b30aeb4f-c2bc-4ffa-9a8a-3a9b31444130.jpg"  alt="parmishh" /></td>
</tr>
</table>

**Additional Bg removal feature**

<table align="center">
<tr>
    <td align="center">&nbsp;<img  src="https://user-images.githubusercontent.com/91942072/243181847-c1d718f0-a113-45d2-87b1-3f9dff1655da.gif" alt="parmishh" /></td>
 <td align="center">&nbsp;<img  src="https://user-images.githubusercontent.com/91942072/243181777-f1479bd7-5496-49dd-b80a-159bd90639ee.gif"  alt="parmishh" /></td>
</tr>
</table>
<table align="center">
<tr>
    <td align="center">&nbsp;<img  src="https://user-images.githubusercontent.com/91942072/243198637-f02e4cd3-3ada-4a3c-b0d6-92aa08682444.jpg" alt="parmishh" /></td>
 <td align="center">&nbsp;<img  src="https://user-images.githubusercontent.com/91942072/243198643-bf08d068-a9dd-44bf-81fd-735f71f5aefd.png"  alt="parmishh" /></td>
</tr>
</table>

## Acknowledgements
Thanks to Gaofeng MENG, Ying WANG, Jiangyong DUAN, Shiming XIANG, Chunhong PAN for their paper "Efficient Image Dehazing with Boundary Constraint and Contextual Regularization"(https://ieeexplore.ieee.org/document/6751186)



