"""
#pip install pandas
import pandas

#dataframe is the object that holds the data acquired through panda
df=pandas.read_csv("test.csv",index_col=0)

#get just a column
df["col1"]

#get row
df.loc["row1"]

#get subset
df.loc["row2":"row4","col3":"col7"]

#get location by integer
df.iloc[2,4]

df=df.loc[]

"""

import os
import glob
import pandas

def addField(indir="in\\extracted"):
	os.chdir(indir)
	filelist=glob.glob("*")
	for filename in filelist:
		df=pandas.read_csv(filename, sep='\s+', header=None)
		df["Station"]=[filename.rsplit("-",1)[0]]*df.shape[0]
		df.to_csv(filename+".csv", index=None, header=None)

def concatenate(indir="in\\extracted",outfile="out\\concatenated.csv"):
	os.chdir(indir)
	fileList=glob.glob("*.csv")
	dfList=[]
	colnames=["Year","Month","Day","Hour","Temp","DewTemp","Pressure","WindDir","WindSpeed","Sky","Precip1","Precip6","ID"]
	for fileName in fileList:
		print(fileName)
		df=pandas.read_csv(fileName,header=None)
		dfList.append(df)
	concatDf=pandas.concat(dfList, axis=0)
	concatDf.columns=colnames
	os.chdir("..\\..")
	concatDf.to_csv(outfile,index=None)

def merge(left="out\\concatenated.csv", right="station-info.txt", output="out\\concatenated-merged.csv"):
	leftDF=pandas.read_csv(left)
	rightDF=pandas.read_fwf(right,converters={"USAF":str,"WBAN":str})
	rightDF["USAF_WBAN"]=rightDF["USAF"]+"-"+rightDF["WBAN"]
	mergedDF=pandas.merge(leftDF,rightDF.ix[:,["USAF_WBAN","STATION NAME","LAT","LON"]],left_on="ID",right_on="USAF_WBAN")
	mergedDF.to_csv(output)



# addField()
# concatenate()
merge()

