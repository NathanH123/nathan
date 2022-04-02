import pandas as pd
import csv
import statistics

df = pd.read_csv("index.csv")
weightlist = df["Weight(Pounds)"].to_list()
weightmean = statistics.mean(weightlist)
weightmedian = statistics.median(weightlist)
weightmode = statistics.mode(weightlist)
standardde = statistics.stdev(weightlist)
print(weightlist)
print(weightmean)
print(weightmedian)
print(weightmode)
print(standardde)

wfsd_start,wfsd_end = weightmean -standardde,weightmean +standardde
wssd_start,wssd_end = weightmean -(2*standardde),weightmean +(2*standardde)
wtsd_start,wtsd_end = weightmean -(3*standardde),weightmean +(3*standardde)

weightdata1 = [result for result in weightlist if result >wfsd_start and result <wfsd_end]
weightdata2 = [result for result in weightlist if result >wssd_start and result <wssd_end]
weightdata3 = [result for result in weightlist if result >wtsd_start and result <wtsd_end]

print("{}% of data for height lies within 1 standard deviation".format(len(weightdata1)*100/len(weightlist)))
print("{}% of data for height lies within 2 standard deviation".format(len(weightdata2)*100/len(weightlist)))
print("{}% of data for height lies within 3 standard deviation".format(len(weightdata3)*100/len(weightlist)))