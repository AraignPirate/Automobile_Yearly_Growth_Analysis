# Automobile Yearly Growth Analysis

A Python Software Project to visualize and Analyze Yearly growth of Automobile Company.


- Buid on **Python Version (3.9.5)**
- **Tkinter** for **GUI**
- **Matplotlib** for *Visualization*

TESTED ON : Linux (Debian) , Windows 10
DEVELOPED ON : Kali Linux

## Clone Repo

Download and extract this software or use git in terminal / cmd  as follows

> `git clone https://github.com/AraignPirate/Automobile_Yearly_Growth_Analysis.git`

Change directory to this project directory cloned.

> `cd Automobile_Yearly_Growth_Analysis`

## Installing Requirements

Required **Python version (3.9.5)**

#### Installing Dependencies

- run this command to install dependencies
  - > `python3 -m pip install -r requirements.txt`
- Alternate way to install.
  - > `pip3 install -r requirements.txt`

If no error occurs then all the dependencies are installed successfully

## Run Software

- run this program with python in terminal / cmd
  - > `python3 Analysedata.py`

## Software Demo 

#### Home Screen

Home screen of software displays overall stats of the company.

![Image of Home page](https://github.com/AraignPirate/Automobile_Yearly_Growth_Analysis/blob/main/Demo/home_screen.png)

Click on **Analyse button** to switch on next screen

#### Options Screen

This screen shows all the automobile categories to choose.

![Main Screen](https://github.com/AraignPirate/Automobile_Yearly_Growth_Analysis/blob/main/Demo/Analyse_options.png)

Click on their respective button to Analyse data graphically.

#### Graph Screen

Each data can be shown in 2 Types of Graphs 
  - Line Graph
  - Scatter Plot Graph

**Line graph is shown as**

![Line Graph](https://github.com/AraignPirate/Automobile_Yearly_Growth_Analysis/blob/main/Demo/graph_line.png)

**Scatter Plot Graph** is shown as

![Scatter Plot Graph](https://github.com/AraignPirate/Automobile_Yearly_Growth_Analysis/blob/main/Demo/graph%20scatter.png)

## Settings.json File

This settings file have following constant values 

- Company_name
- Current_year
- Establishment_year

These values are displayed on home screen and can be changed in settings.json file.

## CsvYearlyData Folder

This folder contains CSV files and a **createPDE.py** file to generate test data values for visualization.

run this createPDE.py file to generate logically correct Dummy data.

> `cd CsvYearlyData`

> `python3 createPDE.py`

This will prompt for **starting year** and **ending year** till which we want our dummy data.

This will also create a **YearlyData.db** file which cane be connect to the software (by Default data is taken from csv files)




