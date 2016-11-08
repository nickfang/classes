import seaborn as sns
import os
import glob
import pandas
import numpy
import patoolib

def extractFiles(indir="logs", outdir="logs\\extracted"):
	# archives=glob.glob.(os.path.join(indir,"*.gz"))
	archive=[]
	for dir,_,_ in os.walk(indir):
		archives=glob.glob(os.path.join(dir,"*.gz"))
		print(os.cwd)