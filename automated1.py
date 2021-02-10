
# how to run the script
# python automated.py -inImgDir <inImgDir> -outImgDir <outImgDir> -inExt <inExtension> -outExt <outExtension> -graph <graph.xml>  > "commands.bat"

# Example on how to run the script: (Do not forget the "." in the extensions)
# python automated1.py -inImgDir "D:\ASTARTE_Data\Level2_discardedData\ERS-1" -outImgDir "D:\ASTARTE_Data\Level2\ERS-1" -inExt .tif -outExt .tif -graph "D:\Scripts\Feb2020\myGraph.xml"  > "D:\Scripts\Feb2020\exampleOut.bat"

# import libraries
import os
import FoldersManager
import argparse

# define directory where to be saved
# satelliteDir="E:/ReProcessed/Sentinel1"
# parsing command line inputs
parser = argparse.ArgumentParser()
parser.add_argument("-inImgDir",
     required=True,
     help="Input directory of images",
     metavar='<string>')
parser.add_argument("-outImgDir",
     required=True,
     help="Output directory for exporting pre-processed images",
     metavar='<string>')
parser.add_argument("-graph",
     required=True,
     help="Directory of the SNAP graph to use in massive processing",
     metavar='<string>')
parser.add_argument("-inExt",
     required=True,
     help="Extension of input image",
     metavar='<string>')
parser.add_argument("-outExt",
     required=True,
     help="Extension of output image",
     metavar='<string>')

params       = vars(parser.parse_args())
inImgDir     = params["inImgDir" ]
outImgDir    = params["outImgDir"]
graphDir     = params["graph"    ]
inExt        = params["inExt"    ]
outExt       = params["outExt"   ]

print ("inImgDir     = ", inImgDir ) 
print ("outImgDir    = ", outImgDir)
print ("graphDir     = ", graphDir    )
print ("inExt        = ", inExt    )
print ("outExt       = ", outExt   )

dirs=FoldersManager.creatFolders(inImgDir,outImgDir)

print (dirs)

os.chdir(inImgDir)
for d in dirs:
   print (d)
   # get a list of images from a given direction
   os.chdir(inImgDir)
   imgs=FoldersManager.getFilesNames(d,inExt)

   for img in imgs:
      imgInDir1 = inImgDir+"/"+d[2:len(d)]+"/"+img
      imgOutDir1 = outImgDir+"/"+d[2:len(d)]+"/"+img
      
      # if not os.path.isfile(imgOutDir1 + outExt):
      print ("gpt \""  + graphDir +"\" -Pin=\""+ imgInDir1 + "\" -Pout=\""+ imgOutDir1 + outExt + "\"\n")



# gpt C:\Users\milto\Documents\TEPAK\ASTARTE\D3\myGraphSentinel7x7toDIM.xml -Pin="D:\Pre-processing\Level0\Sentinel-1\Sentinel-1 Original\05-02-2019 with 01-01-2020\S1A_IW_GRDH_1SDV_20190205T035116_20190205T035141_025789_02DE41_13F2.zip" -Pout="C:\Users\milto\Documents\TEPAK\ASTARTE\D3\Tests\hello.dim"

# python automated.py -inImgDir "D:\ASTARTE_Data\Level2_discardedData\ERS-1" -outImgDir "D:\ASTARTE_Data\Level2\ERS-1" > "D:\Scripts\Feb2020\reprojectERS1.bat"
# python automated.py -inImgDir "D:\ASTARTE_Data\Level2_discardedData\ERS-2" -outImgDir "D:\ASTARTE_Data\Level2\ERS-2" > "D:\Scripts\Feb2020\reprojectERS2.bat"


