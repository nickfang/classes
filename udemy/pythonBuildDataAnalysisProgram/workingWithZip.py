#pip install patool
import patoolib
import glob
import os

def extractFiles(indir="in", out="extracted"):
	os.chdir(indir)
	archives=glob.glob("*.gz")
	print(archives)
	if not os.path.exists(out):
		os.makedirs(out)
	files=os.listdir("extracted")
	for archive in archives:
		if archive[:-3] not in files:
		   patoolib.extract_archive(archive,outdir=out)

extractFiles()