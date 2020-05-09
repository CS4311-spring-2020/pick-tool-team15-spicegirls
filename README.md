# Prevent, Mitigate, and Recover (PMR) Insight Collective Knowledge System (PICK) tool-team15-spicegirls

## Table of Contents  
* [Product Perspective](#product-perspective)  
* [Scope of Product](#scope-of-product)  
* [Github Structure](#github-structure)
* [Installation](#installation)
* [How to Run](#how-to-run)
* [Collaborators](#collaborators) 
  
<Product Perspective="product-perspective"/>

## Product Perspective

Prevent, Mitigate, and Recover (PMR) Insight Collective Knowledge System (PICK) is an interactive system that facilitates correlations between red team’s activities and blue team’s responses and generates graphical representation of events that took place during an adversarial assessment.  

<Scope of Product="scope-of-product"/>

## Scope of Product

The Lethality, Survivability, and HSI Directorate (LSH) recognizes the complexity and the time it takes to analyze the applicable logs, observation notes, and other artifacts gathered from an adversarial assessment from the red, blue, and white teams and generate a report that presents the events that took place during the adversarial assessment.  They want a system that would aid their analysts in correlating red team’s activities to blue team’s responses and represent the events that took place during an adversarial assessment graphically.  

The University of Texas at El Paso (UTEP) and LSH are collaborating to develop Prevent, Mitigate, and Recover (PMR) Insight Collective Knowledge System (PICK) that will provide the ability to correlate red team’s activities to blue team’s responses and graphically represent the events that took place during an adversarial assessment. 

<Github Structure="github-structure"/>

## Github Structure

This repository contains 3 folders (src, doc, Libraries, Resouces, and ui). 

  * The src folder contains all source code regarding the PICK project.
  
  * The doc folder contains all documents regarding the PICK project (SRS and SCM).
  
  * The ui folder contains the .ui files for the PICK project.
  
  * The Resouces folder contains all images, icons, and Audios used in the PICK ui
  
  * The Libraries folder contains all libraries used in the code.
  

## Installation

Run the following commands on the terminal:

### pyqt5
   
    sudo apt-get install python3-pyqt5
    
### datetime

    pip3 install DateTime
    
### datefinder

    pip3 install datefinder
    
### speech recognition

    pip3 install SpeechRecognition
    
### bson

    pip3 install bson
    
 ### mongodb
 
    pip3 install pymongo
    
    brew tap mongodb/brew
    
    brew install mongodb-community@4.2
    
    brew services start mongodb-community@4.2
    
 ### PIL
 
    sudo pip3 install Pillow
    
    pip3 install image
    
 ### Image
 
    pip3 install image
    
### pytesseract

    pip3 install pytesseract
    
### pymongo

    pip3 install pymongo
    
### asyncio

    pip3 install asyncio
    
### splunk

    pip3 install splunklib
    
    pip3 install splunk-sdk
    
### moviepy

    pip3 install moviepy
    
 ### pydub
 
    pip3 install pydub
    


<How to Run="how-to-run"/>
  
## How to Run

First, make sure you have already downloaded MongoDB server onto your computer.

Clone the repository:
    
      git clone https://github.com/CS4311-spring-2020/pick-tool-team15-spicegirls.git
      
Then, once you're inside pick-tool-team15-spicegirls, go to src

      cd src
      
Next, run pickStartPage.py

   ##### Run: 
      
        python3 pickStartPage.py
       


## Collaborators

  * Dima AbdelJaber

  * Ricardo Sanchez

  * Ana Zepeda

  * Scott Honaker

  * Luis Ochoa
