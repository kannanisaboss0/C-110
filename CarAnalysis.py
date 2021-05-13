#-----------------------------------------------------CarAnalysis.py-----------------------------------------------------#
'''
Importing modules:
-plotly.figure_factory (ff)
-pandas (pd)
-statistics (st)
-plotly.graph_objects (go)
-random
-time
'''
import plotly.figure_factory as ff
import pandas as pd
import statistics as st
import plotly.graph_objects as go
import random
import time

#Defining a function to run a loop over the given data for a thousand times
def Run1000LoopOverListData(list_arg_1,data_label_arg):
  new_mean_list=[]
  for value_2 in range(1000):
    new_mean_list.append(GenerateRandomValuesFromListData(list_arg_1))
  PlotDistributionGraph(new_mean_list,data_label_arg)

#Defining a function to generate random values pertaining to the given data and finding the mean of the new list of values produced  
def GenerateRandomValuesFromListData(list_arg_2):
  new_list=[]
  for value in range(100):
    random_index=random.randint(0,(len(list_arg_2)-1))
    new_list.append(int(list_arg_2[random_index]))
  mean_list=st.mean(new_list)  
  return mean_list

 
#Defining a function to plot a distribution graph for modified data
def PlotDistributionGraph(graph_data,graph_label):
  graph_data_mean=st.mean(graph_data)
  graph_data_st_dev=st.stdev(graph_data)
  graph_data_median=st.median(graph_data)

  st_dev_1_start,st_dev_1_end=graph_data_mean-(1*graph_data_st_dev),graph_data_mean+(1*graph_data_st_dev)
  st_dev_2_start,st_dev_2_end=graph_data_mean-(2*graph_data_st_dev),graph_data_mean+(2*graph_data_st_dev)
  st_dev_3_start,st_dev_3_end=graph_data_mean-(3*graph_data_st_dev),graph_data_mean+(3*graph_data_st_dev)
  x=graph_label
  value=0
  if(x=="Horsepower"):
    value=0.0654
  elif(x=="MSRP"):
    value=0.2697
  elif(x=="Weight"):
    value=0.0061
  elif(x=="MPG_City"):
    value=0.9229  
  elif(x=="MPG_Highway"):
    value=0.8925

  graph_plot=ff.create_distplot([graph_data],[graph_label],show_hist=False)
  graph_plot.update_layout(title=str(article_stat_choice)+":Sample Data")
  graph_plot.add_trace(go.Scatter(x=[st_dev_1_start,st_dev_1_start],y=[0,value],mode="lines",name="Standard Deviation 1"))
  graph_plot.add_trace(go.Scatter(x=[st_dev_2_start,st_dev_2_start],y=[0,value],mode="lines",name="Standard Deviation 2"))
  graph_plot.add_trace(go.Scatter(x=[st_dev_3_start,st_dev_3_start],y=[0,value],mode="lines",name="Standard Deviation 3"))
  graph_plot.add_trace(go.Scatter(x=[st_dev_1_end,st_dev_1_end],y=[0,value],mode="lines",name="Standard Deviation 1"))
  graph_plot.add_trace(go.Scatter(x=[st_dev_2_end,st_dev_2_end],y=[0,value],mode="lines",name="Standard Deviation 2"))
  graph_plot.add_trace(go.Scatter(x=[st_dev_3_end,st_dev_3_end],y=[0,value],mode="lines",name="Standard Deviation 3"))
  
     
  graph_plot.update_yaxes(range=[0,value],rangemode="nonnegative")
  graph_plot.show()
  percentage_data_1=[value for value in graph_data if st_dev_1_start<value<st_dev_1_end]
  percentage_data_2=[value for value in graph_data if st_dev_2_start<value<st_dev_2_end]
  percentage_data_3=[value for value in graph_data if st_dev_3_start<value<st_dev_3_end]

  print("{}% of the total {} lies between the first standard deviation".format(round((len(percentage_data_1)*100)/len(graph_data),2),graph_label))
  print("{}% of the total {} lies between the second standard deviation".format(round((len(percentage_data_2)*100)/len(graph_data),2),graph_label))
  print("{}% of the total {} lies between the third standard deviation".format(round((len(percentage_data_3)*100)/len(graph_data),2),graph_label))
  print("The middle value of the data is {}.".format(round(graph_data_median,2)))
  print("The average value of the data is {}.".format(round(graph_data_mean,2)))
  print("The total standard deviation of the data is {}.".format(round(graph_data_st_dev,2)))

#Defining a function to plot a distribution graph for given data
def PlotDistributionGraphFromRawData(graph_data,graph_label):
  graph_data_mean=st.mean(graph_data)
  graph_data_st_dev=st.stdev(graph_data)
  graph_data_median=st.median(graph_data)
  

  st_dev_1_start,st_dev_1_end=graph_data_mean-(1*graph_data_st_dev),graph_data_mean+(1*graph_data_st_dev)
  st_dev_2_start,st_dev_2_end=graph_data_mean-(2*graph_data_st_dev),graph_data_mean+(2*graph_data_st_dev)
  st_dev_3_start,st_dev_3_end=graph_data_mean-(3*graph_data_st_dev),graph_data_mean+(3*graph_data_st_dev)
  x=graph_label
  value=0
  if(x=="Horsepower"):
    value=0.0089
  elif(x=="MSRP"):
    value=0.04303
  elif(x=="Weight"):
    value=0.000912343
  elif(x=="MPG_City"):
    value=0.2103 
  elif(x=="MPG_Highway"):
    value=0.0971

  graph_plot=ff.create_distplot([graph_data],[graph_label],show_hist=False)
  graph_plot.update_layout(title=str(article_stat_choice)+":Original Data")
  graph_plot.add_trace(go.Scatter(x=[st_dev_1_start,st_dev_1_start],y=[0,value],mode="lines",name="Standard Deviation 1"))
  graph_plot.add_trace(go.Scatter(x=[st_dev_2_start,st_dev_2_start],y=[0,value],mode="lines",name="Standard Deviation 2"))
  graph_plot.add_trace(go.Scatter(x=[st_dev_3_start,st_dev_3_start],y=[0,value],mode="lines",name="Standard Deviation 3"))
  graph_plot.add_trace(go.Scatter(x=[st_dev_1_end,st_dev_1_end],y=[0,value],mode="lines",name="Standard Deviation 1"))
  graph_plot.add_trace(go.Scatter(x=[st_dev_2_end,st_dev_2_end],y=[0,value],mode="lines",name="Standard Deviation 2"))
  graph_plot.add_trace(go.Scatter(x=[st_dev_3_end,st_dev_3_end],y=[0,value],mode="lines",name="Standard Deviation 3"))
  
     
  graph_plot.update_yaxes(range=[0,value],rangemode="nonnegative")
  graph_plot.show()
  percentage_data_1=[value for value in graph_data if st_dev_1_start<value<st_dev_1_end]
  percentage_data_2=[value for value in graph_data if st_dev_2_start<value<st_dev_2_end]
  percentage_data_3=[value for value in graph_data if st_dev_3_start<value<st_dev_3_end]

  print("{}% of the total {} lies between the first standard deviation".format(round((len(percentage_data_1)*100)/len(graph_data),2),graph_label))
  print("{}% of the total {} lies between the second standard deviation".format(round((len(percentage_data_2)*100)/len(graph_data),2),graph_label))
  print("{}% of the total {} lies between the third standard deviation".format(round((len(percentage_data_3)*100)/len(graph_data),2),graph_label))
  print("The middle value of the data is {}.".format(round(graph_data_median,2)))
  print("The average value of the data is {}.".format(round(graph_data_mean,2)))
  print("The total standard deviation of the data is {}.".format(round(graph_data_st_dev,2)))

 #Defining a function to print the ending message 
def PrintEndingMessage():
  print("Thank you or using CarAnalysis.py")

#Reading data from the file
df=pd.read_csv("data.csv")

#Introductory message and user inputs
print("Wlcome to CarAnalysis.py.We provide collective statistical data on cars present in a particular area.")
print("Loading choices...")
time.sleep(2.0)
article_stat_list=["Unusable_Element","Weight","MSRP","Horsepower","MPG_City","MPG_Highway"]
article_stat_count=0

#Displaying all choices
for article_stat in article_stat_list[1:]:
  article_stat_count+=1
  print(str(article_stat_count)+":"+article_stat)
user_input=input("Please enter the index of the statistic desired to visualise:")

#Verifying the user's input
#Case-1
if(int(user_input)>5 or int(user_input)==0):
  print("Request Terminated.")
  print("Invalid Input.")
  PrintEndingMessage()
#Case-2  
else:
  print("Input Accepted")
  article_stat_choice=article_stat_list[int(user_input)]
  graph_data=df[article_stat_choice].tolist()
  print("Creating graph...")
  time.sleep(2.3)
  print("Graph created:-")
  time.sleep(0.5)
  PlotDistributionGraphFromRawData(graph_data,article_stat_choice)
  print("Sampling data...")
  time.sleep(3.1)
  print("Creating graph...")
  time.sleep(2.1)
  print("Graph created:-")
  time.sleep(0.5)
  Run1000LoopOverListData(graph_data,article_stat_choice)
  PrintEndingMessage()
#-----------------------------------------------------CarAnalysis.py-----------------------------------------------------#


  





