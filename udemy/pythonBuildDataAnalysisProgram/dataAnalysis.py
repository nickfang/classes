from ftplib import FTP, error_perm
import seaborn as sns
import os
import glob
import pandas
import numpy
import patoolib

def ftpDownloader(stationId, startYear, endYear, url="ftp.pyclass.com", user="student@pyclass.com", passwd="student123"):
	ftp=FTP(url)
	ftp.login(user,passwd)
	loc="in"
	if not os.path.exists(loc):
		os.makedirs(loc)
	for year in range(startYear, endYear+1):
		fullPath="Data/%s/%s-%s.gz" % (year, stationId, year)
		filename=os.path.basename(fullPath)
		try:
			with open(os.path.join(loc,filename), 'wb') as file:
				ftp.retrbinary('RETR %s' % fullPath, file.write)
			print("%s successfully downloaded" % filename)
		except error_perm:
			print("%s is not available" % filename)
			os.remove(os.path.join(loc,filename))
	ftp.close()

def extractFiles(indir="in", out="extracted"):
	archives=glob.glob(os.path.join(indir,"*.gz"))
	print(archives)
	out=os.path.join(indir,out)
	if not os.path.exists(out):
		os.makedirs(out)
	files=os.listdir(out)
	for archive in archives:
		if archive[:-3] not in files:
		   patoolib.extract_archive(archive,outdir=out)

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

def pivot(infile="out\\concatenated-merged.csv", outfile="out\\pivoted.csv"):
	df=pandas.read_csv(infile)
	df=df.replace(-9999,numpy.nan)
	df["Temp"]=df["Temp"]/10.0
	table=pandas.pivot_table(df,index=["ID","LON","LAT","STATION NAME"],columns="Year",values="Temp")
	table.to_csv(outfile)
	return table

def plot(outfigure="out\\plotted.png"):
	df=pivot()
	df.T.plot(subplots=True,kind="bar")
	sns.plt.savefig(outfigure, dpi=200)

def kml(input="out\\pivoted.csv", out="out\\weather.kml"):
	kml=simple.kml.Kml()
	df=pandas.read_csv(input, index_col=["ID","LON","LAT","STATION NAME"])
	for lon, lat, name in zip(df.index.get_level_values("LON"),df.index.get_level_values("LAT"),df.index.get_level_values("STATION NAME")):
		kml.newpoint(name-name, coords[lon,lat])
		kml.save(out)


# ids=["010010-99999","010014-99999","010020-99999","010030-99999"]

# for name in ids:
# 	ftpDownloader(name,1950,2014)
# extractFiles()
# addField()
# concatenate()
# merge()
# df=pivot()
# print(df)
# fig=sns.heatmap(df).get_figure()
# fig=sns.heatmap(df,mask=df.isnull()).get_figure()
# fig.savefig("out\\heatmap.png",dpi=200)
plot()