from tkinter import *
from tkinter import messagebox
import os
import csv
import locale
import pandas as pd
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)

FILES = ["ProDomSalesExport.csv","ThreeWheelers.csv","Multiutility.csv","CommercialVehicals.csv","PassengersVehicals.csv","TwoWheelers.csv"]
CWD = os.getcwd()
CSVDATADIR = "CsvYearlyData"
YEARNOW = 2020
CATAGORIES=['Commercial Vehicles','Multiutility Vehicles','Passenger Vehicles','Three Wheelers','Two Wheelers','Over All Production , Salse , Export per Year','Investment And Profit per Year']
CATEDICT ={
'Commercial Vehicles': "CommercialVehicals.csv",
'Multiutility Vehicles': "Multiutility.csv",
'Passenger Vehicles':"PassengersVehicals.csv",
'Three Wheelers':"ThreeWheelers.csv",
'Two Wheelers':"TwoWheelers.csv",
'Over All Production , Salse , Export per Year':"ProDomSalesExport.csv",
"Investment And Profit per Year": "PriceOverallAvg.csv"
}

class Root(Tk):
  def __init__(self):
    super(Root,self).__init__()
    self.title("Yearly Growth Analizer App")
    self.minsize(640,700)
    self.mainScreen()
    #self.createButtons()
    #self.wm_iconbitmap()
    #self.configure(background="#4d4d4d")
  def loadSettings(self):
    #self.Year = 2020
    pass
  def mainScreen(self):
    Root.container = Frame(self)
    Root.container.pack(side="top",fill="both",expand=True) 
    Root.container.grid_rowconfigure(0,weight=1)
    Root.container.grid_columnconfigure(0,weight=1)
    self.frames={} 
    for F in (MainScreen,ChoiceScreen):
      frame = F(Root.container,self)
      self.frames[F] = frame
      frame.grid(row=0,column=0,sticky='nsew')
    self.showFrames(MainScreen)
  def showFrames(self,cont):
    frame=self.frames[cont]
    frame.tkraise()
  def showDataFrame(self,data):
    frame = DataFrame(Root.container,self,data)
    frame.grid(row=0,column=0,sticky='nsew')
    frame.tkraise()
  def showScatterPlot(self,data):
    frame = ScatterPlot(Root.container,self,data)
    frame.grid(row=0,column=0,sticky='nsew')
    frame.tkraise()
  def showProductionPlot(self,data,sett):
    frame = ProductionPlot(Root.container,self,data,sett)
    frame.grid(row=0,column=0,sticky='nsew')
    frame.tkraise()
  def showPriceFrame(self,data):
    frame = PriceFrame(Root.container,self,data)
    frame.grid(row=0,column=0,sticky='nsew')
    frame.tkraise()
  def showScatterPriceFrame(self,data):
    frame = ScatterPriceFrame(Root.container,self,data)
    frame.grid(row=0,column=0,sticky='nsew')
    frame.tkraise()
  def showProfitGraph(self,data,stt):
    frame = ProfitGraphFrame(Root.container,self,data,stt)
    frame.grid(row=0,column=0,sticky='nsew')
    frame.tkraise()
class MainScreen(Frame):
  global FILES,CWD,CSVDATADIR
  def __init__(self,parent,controller):
    Frame.__init__(self,parent)
    self.mainScreen(controller)
  def mainScreen(self,controller):
    locale.setlocale(locale.LC_ALL,'en_IN.utf-8')
    data = self.getData()
    Label(self,text="").pack()
    Label(self,text="Welcome To Analizer",font="Times 20",padx=10,pady=10).pack()
    wrapper = LabelFrame(self,text="Automobile Company Name")
    wrapper.pack(fill="both",padx=20,pady=10,expand='yes')
    wrapper2 = LabelFrame(self,text=f"Statistics Year {YEARNOW}")
    wrapper2.pack(fill="both",padx=20,pady=10,expand='yes')
    Label(wrapper,text="HinDustaan Automobiles",bg = "white",padx=10,pady=5).pack(side="left",padx=20,pady=10)
    Label(wrapper,text="Since",padx=10,pady=5).pack(side="left",padx=20,pady=10)
    Label(wrapper,text="1990",bg = "white",padx=10,pady=5).pack(side="left",padx=20,pady=10)
    inner = LabelFrame(wrapper2,text="Total Production Count")
    inner1 = LabelFrame(wrapper2,text="Total Sales ")
    inner2 = LabelFrame(wrapper2,text="Total Export ")
    inner.pack(fill="both",padx=20,pady=10)
    inner1.pack(fill="both",padx=20,pady=10)
    inner2.pack(fill="both",padx=20,pady=10)
    Label(inner,text="Number Of Automobiles Produced",bg = "white",padx=10,pady=5).pack(side="left",padx=20,pady=10)
    Label(inner,text=f"{locale.format_string('%d',int(data[1]),grouping=True)}",bg = "white",padx=10,pady=5).pack(side="right",padx=20,pady=10)
    Label(inner1,text="Automobiles Sold",bg = "white",padx=10,pady=5).pack(side="left",padx=20,pady=10)
    Label(inner1,text=f"{locale.format_string('%d',int(data[2]),grouping=True)}",bg = "white",padx=10,pady=5).pack(side="right",padx=20,pady=10)
    Label(inner2,text="Automobiles Exported",bg = "white",padx=10,pady=5).pack(side="left",padx=20,pady=10)
    Label(inner2,text=f"{locale.format_string('%d',int(data[3]),grouping=True)}",bg = "white",padx=10,pady=5).pack(side="right",padx=20,pady=10)
    Label(self,text="App by Yatharth").pack(side="right",anchor="se",padx=5,pady=5)
    analyse = Button(self,text='Analyse',command=lambda:controller.showFrames(ChoiceScreen))
    analyse.pack(side='left',padx=20,pady=10)

  def getData(self):
    name = os.path.join(CWD,CSVDATADIR,FILES[0])
    if os.path.isfile(name):
      if os.stat(name).st_size != 0:
        with open(name,'r') as file:
          data = csv.reader(file,delimiter=',')
          for row in data:
            #print(row)
            if row[0] == str(YEARNOW):
              return row
          else:
            ans = messagebox.showerror("Current Year Data Not Found ",f"Filename :{FILES[0]} Not Found for {YEARNOW}")
            self.quit()            
      else:
        ans = messagebox.showerror("No Data in File",f"Filename :{FILES[0]} is Empty")
        if ans == 'ok':
         self.destroy()
    else:
      ans = messagebox.showerror("Not Found",f"Data File Not Found in {CSVDATADIR} Directory Filename :{FILES[0]}")
      if ans == 'ok':
        self.destroy()


class ChoiceScreen(Frame):
   global CATAGORIES
   def __init__(self,parent,controller):
    Frame.__init__(self,parent)
    self.choiceScreen(controller)
   def choiceScreen(self,controller):
    Label(self,text="").pack()
    Label(self,text="Analiyse Options",font="Times 20",padx=10,pady=10).pack()
    wrapper = LabelFrame(self,text="Over All")
    wrapper.pack(fill="both",padx=20,pady=10)
    Label(wrapper,bg='white',pady=5,padx=5,text='Overall Analysis of Production , Sales and Export from \nTotal Anual Data of each year. ').pack(padx=10,pady=10,side='left')
    Totalbutton =  Button(wrapper,text='Analyse Yearly',command=lambda:controller.showDataFrame(CATAGORIES[-2]))
    Totalbutton.pack(side='right',padx=20,pady=10)
    wrapper2 = LabelFrame(self,text="Catagories")
    wrapper2.pack(fill="both",padx=20,pady=10)
    Label(wrapper2,text='Analyse according to Following Categories.',bg='white',padx=5,pady=5).pack(padx=10,pady=10,anchor='nw',side ='left')
    Button(wrapper2,text=CATAGORIES[0],width=20,command=lambda:controller.showDataFrame(CATAGORIES[0])).pack(padx=20,pady=10)
    Button(wrapper2,text=CATAGORIES[1],width=20,command=lambda:controller.showDataFrame(CATAGORIES[1])).pack(padx=20,pady=10)
    Button(wrapper2,text=CATAGORIES[2],width=20,command=lambda:controller.showDataFrame(CATAGORIES[2])).pack(padx=20,pady=10)
    Button(wrapper2,text=CATAGORIES[3],width=20,command=lambda:controller.showDataFrame(CATAGORIES[3])).pack(padx=20,pady=10)
    Button(wrapper2,text=CATAGORIES[4],width=20,command=lambda:controller.showDataFrame(CATAGORIES[4])).pack(padx=20,pady=10)
    wrapper3 = LabelFrame(self,text="Total Amount")
    wrapper3.pack(fill="both",padx=20,pady=10,expand='yes')
    Label(wrapper3,text='Analyse according total Investment and Total Gain per Year',bg='white',padx=5,pady=5).pack(padx=10,pady=10,anchor='nw',side ='left')
    Button(wrapper3,text='Analyse Profit',width=20,command=lambda:controller.showPriceFrame(CATAGORIES[-1])).pack(padx=20,pady=10)
    back = Button(self,text='Back',command=lambda:controller.showFrames(MainScreen))
    back.pack(side='left',padx=20,pady=10)
    Label(self,text="App by Yatharth").pack(side="right",anchor="se",padx=5,pady=5)
   def setGlobalCate(self,name,controller):
    global CATNAME
    CATNAME = name
    print(CATNAME,name)
    controller.showFrames(DataFrame)

class DataFrame(Frame):
  global CATEDICT
  def __init__(self,parent,controller,data):
    Frame.__init__(self,parent)
    self.plotGraph(controller,data)
  def getTableData(self,data):
    filename = data
    name = os.path.join(CWD,CSVDATADIR,filename)
    if os.path.isfile(name):
      if os.stat(name).st_size != 0:
        with open(name,'r') as file:
          data = pd.read_csv(file)
          return data      
      else:
        ans = messagebox.showerror("No Data in File",f"Filename :{FILES[0]} is Empty")
        if ans == 'ok':
         self.quit()
    else:
      ans = messagebox.showerror("Not Found",f"Data File Not Found in {CSVDATADIR} Directory Filename :{FILES[0]}")
      if ans == 'ok':
        self.quit()
  def plotGraph(self,controller,data):
    Label(self,text="").pack()
    Label(self,text=data,font="Times 20",padx=10,pady=10).pack()
    back = Button(self,text='Back',command=lambda:controller.showFrames(ChoiceScreen))
    back.pack(padx=20,pady=10,anchor='nw')
    wrapper = LabelFrame(self,text="Other Graphs")
    wrapper.pack(side='right',padx=20,pady=10,expand='yes',fill='both')
    back = Button(wrapper,text='Production Count Graph',command=lambda:controller.showProductionPlot(data,0))
    back.pack(padx=20,pady=10,anchor='nw')
    back = Button(wrapper,text='Scatter Plot',command=lambda: controller.showScatterPlot(data))
    back.pack(padx=20,pady=10,anchor='nw')
    datasheet = self.getTableData(CATEDICT[data])
    self.makePlot(datasheet,data)

  def makePlot(self,data,name):
    fig = Figure(figsize = (7,5),dpi =100)
    plot1 = fig.add_subplot(111)
    plot1.plot(data.Year,data.Sales,'g',label='Sales')
    plot1.plot(data.Year,data.Exports,'b',label='Exports')
    plot1.set_xlabel('Year')
    plot1.set_ylabel('Number Of Automobiles')
    plot1.set_title(f'Analysing {name}')
    plot1.legend()
    canvas = FigureCanvasTkAgg(fig,master=self)
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas,self)
    toolbar.update()
    canvas.get_tk_widget().pack(padx=10,pady=10)    
    Label(self,text="App by Yatharth").pack(side="right",anchor="se",padx=5,pady=5)
 
class ScatterPlot(Frame):
  global CATEDICT
  def __init__(self,parent,controller,data):
    Frame.__init__(self,parent)
    self.plotGraph(controller,data)
  def getTableData(self,data):
    filename = data
    name = os.path.join(CWD,CSVDATADIR,filename)
    if os.path.isfile(name):
      if os.stat(name).st_size != 0:
        with open(name,'r') as file:
          data = pd.read_csv(file)
          return data      
      else:
        ans = messagebox.showerror("No Data in File",f"Filename :{FILES[0]} is Empty")
        if ans == 'ok':
         self.quit()
    else:
      ans = messagebox.showerror("Not Found",f"Data File Not Found in {CSVDATADIR} Directory Filename :{FILES[0]}")
      if ans == 'ok':
        self.quit()
  def plotGraph(self,controller,data):
    Label(self,text="").pack()
    Label(self,text=data,font="Times 20",padx=10,pady=10).pack()
    back = Button(self,text='Back',command=lambda:controller.showFrames(ChoiceScreen))
    back.pack(padx=20,pady=10,anchor='nw')
    wrapper = LabelFrame(self,text="Other Graphs")
    wrapper.pack(side='right',padx=20,pady=10,expand='yes',fill='both')
    back = Button(wrapper,text='Production Count Graph',command=lambda:controller.showProductionPlot(data,1))
    back.pack(padx=20,pady=10,anchor='nw')
    back = Button(wrapper,text='Line Plot',command=lambda: controller.showDataFrame(data))
    back.pack(padx=20,pady=10,anchor='nw')
    datasheet = self.getTableData(CATEDICT[data])
    self.makePlot(datasheet,data)

  def makePlot(self,data,name):
    fig = Figure(figsize = (7,5),dpi =100)
    plot1 = fig.add_subplot(111)
    plot1.scatter(data.Year,data.Sales,c='g',label='Sales')
    plot1.scatter(data.Year,data.Exports,c='b',label='Exports')
    plot1.set_xlabel('Year')
    plot1.set_ylabel('Number Of Automobiles')
    plot1.set_title(f'Analysing {name}')
    plot1.legend()
    canvas = FigureCanvasTkAgg(fig,master=self)
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas,self)
    toolbar.update()
    canvas.get_tk_widget().pack(padx=10,pady=10)    
    Label(self,text="App by Yatharth").pack(side="right",anchor="se",padx=5,pady=5)

class ProductionPlot(Frame):
  global CATEDICT
  def __init__(self,parent,controller,data,sett):
    Frame.__init__(self,parent)
    self.plotGraph(controller,data,sett)
  def getTableData(self,data):
    filename = data
    name = os.path.join(CWD,CSVDATADIR,filename)
    if os.path.isfile(name):
      if os.stat(name).st_size != 0:
        with open(name,'r') as file:
          data = pd.read_csv(file)
          return data      
      else:
        ans = messagebox.showerror("No Data in File",f"Filename :{FILES[0]} is Empty")
        if ans == 'ok':
         self.quit()
    else:
      ans = messagebox.showerror("Not Found",f"Data File Not Found in {CSVDATADIR} Directory Filename :{FILES[0]}")
      if ans == 'ok':
        self.quit()
  def plotGraph(self,controller,data,sett):
    Label(self,text="").pack()
    Label(self,text=data,font="Times 20",padx=10,pady=10).pack()
    back = Button(self,text='Back',command=lambda:controller.showFrames(ChoiceScreen))
    back.pack(padx=20,pady=10,anchor='nw')
    wrapper = LabelFrame(self,text="Other Graphs")
    wrapper.pack(side='right',padx=20,pady=10,expand='yes',fill='both')
    back = Button(wrapper,text='Production Count Graph',command=lambda:controller.showFrames(ChoiceScreen))
    back.pack(padx=20,pady=10,anchor='nw')
    back = Button(wrapper,text='Line Plot',command=lambda: controller.showDataFrame(data))
    back.pack(padx=20,pady=10,anchor='nw')
    datasheet = self.getTableData(CATEDICT[data])
    self.makePlot(datasheet,data,sett)

  def makePlot(self,data,name,sett):
    if sett == 1:
      fig = Figure(figsize = (7,5),dpi =100)
      plot1 = fig.add_subplot(111)
      plot1.scatter(data.Year,data.Sales,c='g',label='Sales')
      plot1.scatter(data.Year,data.Exports,c='y',label='Exports')
      plot1.scatter(data.Year,data.Production,c='b',label='Total Production')
      plot1.set_xlabel('Year')
      plot1.set_ylabel('Number Of Automobiles')
      plot1.set_title(f'Analysing {name}')
      plot1.legend()
      canvas = FigureCanvasTkAgg(fig,master=self)
      canvas.draw()
      canvas.get_tk_widget().pack()
      toolbar = NavigationToolbar2Tk(canvas,self)
      toolbar.update()
      canvas.get_tk_widget().pack(padx=10,pady=10)    
      Label(self,text="App by Yatharth").pack(side="right",anchor="se",padx=5,pady=5)
    if sett == 0:
      fig = Figure(figsize = (7,5),dpi =100)
      plot1 = fig.add_subplot(111)
      plot1.plot(data.Year,data.Sales,c='g',label='Sales')
      plot1.plot(data.Year,data.Exports,c='y',label='Exports')
      plot1.plot(data.Year,data.Production,c='b',label='Total Production')
      plot1.set_xlabel('Year')
      plot1.set_ylabel('Number Of Automobiles')
      plot1.set_title(f'Analysing {name}')
      plot1.legend()
      canvas = FigureCanvasTkAgg(fig,master=self)
      canvas.draw()
      canvas.get_tk_widget().pack()
      toolbar = NavigationToolbar2Tk(canvas,self)
      toolbar.update()
      canvas.get_tk_widget().pack(padx=10,pady=10)    
      Label(self,text="App by Yatharth").pack(side="right",anchor="se",padx=5,pady=5)

class PriceFrame(Frame):
  global CATEDICT
  def __init__(self,parent,controller,data):
    Frame.__init__(self,parent)
    self.plotGraph(controller,data)
  def getTableData(self,data):
    filename = data
    name = os.path.join(CWD,CSVDATADIR,filename)
    if os.path.isfile(name):
      if os.stat(name).st_size != 0:
        with open(name,'r') as file:
          data = pd.read_csv(file)
          return data      
      else:
        ans = messagebox.showerror("No Data in File",f"Filename :{FILES[0]} is Empty")
        if ans == 'ok':
         self.quit()
    else:
      ans = messagebox.showerror("Not Found",f"Data File Not Found in {CSVDATADIR} Directory Filename :{FILES[0]}")
      if ans == 'ok':
        self.quit()
  def plotGraph(self,controller,data):
    Label(self,text="").pack()
    Label(self,text=data,font="Times 20",padx=10,pady=10).pack()
    back = Button(self,text='Back',command=lambda:controller.showFrames(ChoiceScreen))
    back.pack(padx=20,pady=10,anchor='nw')
    wrapper = LabelFrame(self,text="Other Graphs")
    wrapper.pack(side='right',padx=20,pady=10,expand='yes',fill='both')
    back = Button(wrapper,text='Scatter Plot',command=lambda: controller.showScatterPriceFrame(data))
    back.pack(padx=20,pady=10,anchor='nw')
    back = Button(wrapper,text='Profit Graph',command=lambda: controller.showProfitGraph(data,0))
    back.pack(padx=20,pady=10,anchor='nw')
    datasheet = self.getTableData(CATEDICT[data])
    self.makePlot(datasheet,data)

  def makePlot(self,data,name):
    fig = Figure(figsize = (7,5),dpi =100)
    plot1 = fig.add_subplot(111)
    plot1.plot(data.Year,data.Production,c='b',label='Total Investment')
    plot1.plot(data.Year,data.Exports + data.Sales,c='g',label='Gained by Sales + Exports')
    plot1.set_xlabel('Year')
    plot1.set_ylabel('Amount in Rupees ( 100 Crore)')
    plot1.set_title(f'Analysing {name}')
    plot1.legend()
    canvas = FigureCanvasTkAgg(fig,master=self)
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas,self)
    toolbar.update()
    canvas.get_tk_widget().pack(padx=10,pady=10)    
    Label(self,text="App by Yatharth").pack(side="right",anchor="se",padx=5,pady=5)

class ScatterPriceFrame(Frame):
  global CATEDICT
  def __init__(self,parent,controller,data):
    Frame.__init__(self,parent)
    self.plotGraph(controller,data)
  def getTableData(self,data):
    filename = data
    name = os.path.join(CWD,CSVDATADIR,filename)
    if os.path.isfile(name):
      if os.stat(name).st_size != 0:
        with open(name,'r') as file:
          data = pd.read_csv(file)
          return data      
      else:
        ans = messagebox.showerror("No Data in File",f"Filename :{FILES[0]} is Empty")
        if ans == 'ok':
         self.quit()
    else:
      ans = messagebox.showerror("Not Found",f"Data File Not Found in {CSVDATADIR} Directory Filename :{FILES[0]}")
      if ans == 'ok':
        self.quit()
  def plotGraph(self,controller,data):
    Label(self,text="").pack()
    Label(self,text=data,font="Times 20",padx=10,pady=10).pack()
    back = Button(self,text='Back',command=lambda:controller.showFrames(ChoiceScreen))
    back.pack(padx=20,pady=10,anchor='nw')
    wrapper = LabelFrame(self,text="Other Graphs")
    wrapper.pack(side='right',padx=20,pady=10,expand='yes',fill='both')
    back = Button(wrapper,text='Profit Graph',command=lambda: controller.showProfitGraph(data,1))
    back.pack(padx=20,pady=10,anchor='nw')
    back = Button(wrapper,text='Line Plot',command=lambda: controller.showPriceFrame(data))
    back.pack(padx=20,pady=10,anchor='nw')
    datasheet = self.getTableData(CATEDICT[data])
    self.makePlot(datasheet,data)

  def makePlot(self,data,name):
    fig = Figure(figsize = (7,5),dpi =100)
    plot1 = fig.add_subplot(111)
    plot1.scatter(data.Year,data.Production,c='b',label='Total Investment')
    plot1.scatter(data.Year,data.Exports + data.Sales,c='g',label='Gained by Sales + Exports')
    plot1.set_xlabel('Year')
    plot1.set_ylabel('Amount in Rupees ( 100 Crore)')
    plot1.set_title(f'Analysing {name}')
    plot1.legend()
    canvas = FigureCanvasTkAgg(fig,master=self)
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas,self)
    toolbar.update()
    canvas.get_tk_widget().pack(padx=10,pady=10)    
    Label(self,text="App by Yatharth").pack(side="right",anchor="se",padx=5,pady=5)

class ProfitGraphFrame(Frame):
  global CATEDICT
  def __init__(self,parent,controller,data,sett):
    Frame.__init__(self,parent)
    self.plotGraph(controller,data,sett)
  def getTableData(self,data):
    filename = data
    name = os.path.join(CWD,CSVDATADIR,filename)
    if os.path.isfile(name):
      if os.stat(name).st_size != 0:
        with open(name,'r') as file:
          data = pd.read_csv(file)
          return data      
      else:
        ans = messagebox.showerror("No Data in File",f"Filename :{FILES[0]} is Empty")
        if ans == 'ok':
         self.quit()
    else:
      ans = messagebox.showerror("Not Found",f"Data File Not Found in {CSVDATADIR} Directory Filename :{FILES[0]}")
      if ans == 'ok':
        self.quit()
  def plotGraph(self,controller,data,sett):
    Label(self,text="").pack()
    Label(self,text=data,font="Times 20",padx=10,pady=10).pack()
    back = Button(self,text='Back',command=lambda:controller.showFrames(ChoiceScreen))
    back.pack(padx=20,pady=10,anchor='nw')
    wrapper = LabelFrame(self,text="Other Graphs")
    wrapper.pack(side='right',padx=20,pady=10,expand='yes',fill='both')
    back = Button(wrapper,text='Scatter Plot',command=lambda:controller.showScatterPriceFrame(data))
    back.pack(padx=20,pady=10,anchor='nw')
    back = Button(wrapper,text='Line Plot',command=lambda: controller.showPriceFrame(data))
    back.pack(padx=20,pady=10,anchor='nw')
    datasheet = self.getTableData(CATEDICT[data])
    self.makePlot(datasheet,data,sett)

  def makePlot(self,data,name,sett):
    if sett == 1:
      fig = Figure(figsize = (7,5),dpi =100)
      plot1 = fig.add_subplot(111)
      plot1.scatter(data.Year,((((data.Sales+data.Exports)-data.Production)/data.Production)*100),c='g',label='Profit')
      plot1.set_xlabel('Year')
      plot1.set_ylabel('Profit in Percentage (%)')
      plot1.set_title(f'Analysing {name}')
      plot1.legend()
      canvas = FigureCanvasTkAgg(fig,master=self)
      canvas.draw()
      canvas.get_tk_widget().pack()
      toolbar = NavigationToolbar2Tk(canvas,self)
      toolbar.update()
      canvas.get_tk_widget().pack(padx=10,pady=10)    
      Label(self,text="App by Yatharth").pack(side="right",anchor="se",padx=5,pady=5)
    if sett == 0:
      fig = Figure(figsize = (7,5),dpi =100)
      plot1 = fig.add_subplot(111)
      plot1.plot(data.Year,((((data.Sales+data.Exports)-data.Production)/data.Production)*100),c='g',label='Profit')
      plot1.set_xlabel('Year')
      plot1.set_ylabel('Profit in Percentage (%)')
      plot1.set_title(f'Analysing {name}')
      plot1.legend()
      canvas = FigureCanvasTkAgg(fig,master=self)
      canvas.draw()
      canvas.get_tk_widget().pack()
      toolbar = NavigationToolbar2Tk(canvas,self)
      toolbar.update()
      canvas.get_tk_widget().pack(padx=10,pady=10)    
      Label(self,text="App by Yatharth").pack(side="right",anchor="se",padx=5,pady=5)

if __name__ == "__main__":
  root = Root()
  root.mainloop()
