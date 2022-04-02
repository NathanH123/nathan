import pandas as pd
import csv
import statistics 

df = pd.read_csv("index.csv")
heightlist = df["Height(Inches)"].to_list()
heightmean = statistics.mean(heightlist)
heightmedian = statistics.median(heightlist)
heightmode = statistics.mode(heightlist)
standarddi = statistics.stdev(heightlist)
print(heightlist)
print(heightmean)
print(heightmedian)
print(heightmode)
print(standarddi)

hfsd_start,hfsd_end = heightmean -standarddi,heightmean + standarddi
hssd_start,hssd_end = heightmean -(2* standarddi),heightmean +(2* standarddi)
htsd_start,htsd_end = heightmean -(3* standarddi),heightmean +(3* standarddi)

heightdata1 = [result for result in heightlist if result > hfsd_start and result < hfsd_end]
heightdata2 = [result for result in heightlist if result > hssd_start and result < hssd_end]
heightdata3 = [result for result in heightlist if result > htsd_start and result < htsd_end]

print("{}% of data for height lies within 1 standard deviation".format(len(heightdata1)*100/len(heightlist)))
print("{}% of data for height lies within 2 standard deviation".format(len(heightdata2)*100/len(heightlist)))
print("{}% of data for height lies within 3 standard deviation".format(len(heightdata3)*100/len(heightlist)))