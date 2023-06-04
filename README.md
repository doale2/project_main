###### PE02_Team D

<img src="https://capsule-render.vercel.app/api?type=waving&color=auto&height=200&section=header&text=Analyze+Wafer&fontSize=90" />

*****

# Contents  
- [Overview](#overview)     
- [Installation](#installation)  
- [Usage](#usage)  
- [Contributor](#contributor)
- [Environment](#environment)
- [Enquiry](#enquiry)  

*****

## Overview   
*Wafer-scale data* processing refers to a technology that efficiently manages and utilizes 
vast amounts of data of elements in each die at the wafer scale. 
This requires the use of appropriate data formats and processing tools. 


So our team created **a module that can efficiently extract and analyze the data**
provided by the customer, it also shows and saves information in graphs and csv files.


Customers can select and analyze **files, lots, wafers, column&row** which they want.


### What you can analyze

**IV graph**

A graph that represents the voltage-current curve of a semiconductor device. 
This graph is used to analyze the electrical characteristics of the device.

**IV fitting**

The process of mathematically modeling the characteristics of a device 
based on the data obtained from the IV graph. 
We selected 8th function to fit it.


**Transmission graph**

 A graph that shows how much light is transmitted through a semiconductor device
 or structure. This graph is used to analyze the optical properties of the device or structure.

**Transmission fitting**

The process of modeling the optical properties of a semiconductor device
or structure based on the data obtained from the transmission graph.
We selected both exponential and polynomial function to fit it.

**Flat Transmission graph**

 A graph that shows how much light is transmitted through a semiconductor 
 device or structure at a constant rate over a specific wavelength range. 
 This graph is used to analyze important optical properties, such as the bandgap,
 of the device or structure.

**Flat flat transmission graph**

A graph that shows how much light is transmitted through a semiconductor
device or structure at an even more constant rate than the flat transmission graph.
This graph is used to more accurately analyze important optical properties,
such as the bandgap, of the device or structure.

*****

## Installation  
First, clone our project files in your repository  
 ```{.python}
git clone https://github.com/PE02teamD/project_main.git
 ```
Install requirements to run our code  
 ```{.python}
pip install -r requirements.txt
 ```
Run "run.py"

## Usage
  <img src="https://user-images.githubusercontent.com/93698770/241849695-c743f132-67c9-4671-956d-3e4eb0eaf088.png" height="300">
  
  1. set data saving style. <br> you can select data save style _.png_ and _.csv_ both.

  2. select files as _LOT ID, Wafer ID, Location, Date_. <br> when select nothing at list, select all automatically

  3. show selected files. <br> after click _set scale_, show filename in this area.

  4. UI settings. <br> change Appearance Mode _Light, Dark, System_ <br> change UI Scaling _80%, 90%, 100%, 110%, 120%_

  5. set scale <br> save select files and show Number of Files.

  6. progress bar <br> show progress ratio as the ratio which files are completed

  7. analyze & exit <br> start analyze & exit button. <br> please check (1.)data saving style and (3.)selected XML files after analyze.
  <br><img src="https://user-images.githubusercontent.com/119747175/243174250-1e3d9134-54a9-400e-bf1b-bb5474c8c8f9.gif" height="300">

## Contributor  
_Department of Photonics and Nanoelectronics_

_In HANYANG University ERICA Campus_

- **Jungwan Noh**
  
  <img src="https://github.com/PE02teamD/project_main/assets/127360946/742c4597-5dca-40e8-8199-88ec694cd15a" width="195" height="240"/>

  **A principal developer👑**
  
  Implemented Tkinter GUI
  
  Extracted to XML files

  Saved to CSV, PNG files 
  
  Graph fitting

  Modulization python files
  
  [npower220@hanyang.ac.kr](npower220@hanyang.ac.kr)

<br/>

- **Kyusik Kim**
 
  <img src="https://github.com/PE02teamD/project_main/assets/127360946/41083b56-6cdd-48a7-b609-101b4abdb7a1" width="190" height="250"/>

  Diversification of data file selection

  [kimq6@hanyang.ac.kr](kimq6@hanyang.ac.kr)

<br/>

- **Yujeong Kim**

  <img src="https://github.com/PE02teamD/project_main/assets/127360946/371677b4-9e92-412f-aa83-78b35d472eb9" width="195" height="240"/>

  implemented I-V Curve graph

  implemented transmission spectra graph
  
  [govldjsgovl@hanyang.ac.kr](govldjsgovl@hanyang.ac.kr)
 
 <br/>

- **Dohyeon Lee**

  <img src="https://github.com/PE02teamD/project_main/assets/127360946/9e2c72d5-4ae3-4784-a986-ffe3a2cbe16b" width="240" height="180"/>

  Modulization some python files

  [ehgus9806@hanyang.ac.kr](ehgus9806@hanyang.ac.kr)

## Environment  
<div align=center>
	<h3>📚 Tech Stack 📚</h3>
	<p>💻 Platforms & Languages 💻</p>
</div>
<div align=center>
<img src="https://img.shields.io/badge/Python3.10-3776AB?style=flat&logo=python&logoColor=white"/>  
<img src="https://img.shields.io/badge/Window10-0078D6?style=flat&logo=Windows&logoColor=white"/>
</div>
<div align=center>
    <p>🔨 Tools 🔨</p>
    <img src="https://img.shields.io/badge/Github-181717?style=flat&logo=Github&logoColor=white"/>
</div>

## Enquiry  
If you have any questions or suggestions about this repository, please contact us using the contributors' information.  

Also, before submitting any questions or suggestions, please check if there is already something related to this repository.
