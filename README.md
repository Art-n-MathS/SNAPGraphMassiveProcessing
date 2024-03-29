# SNAPGraphMassiveProcessing

This is a script used for massive processing of images using Graphs from SNAP. It takes as input, 
(1) an input directory with an undefined number of image. The directory may contain subdirectories with images and the images within the subdirectories are also processed, 
(2) an output directory, where the processed images will be exported and inside that directory it creates the same subdirectories as the input directory, 
(3) the directory with name of the SNAP graph to be used for processing the images, 
(4) the extension of the input images (e.g. ".tif"), 
(5) the extension of the output images
Notes: 
(a) Do not forget the "." while defining the extension of the images e.g. ".tif" is a valid extension to be inserted.
(b) Make sure that inputs and outputs of the graph files are changed to allow definition from the Command prompt. Use ${in} for input and ${out} for output. Se example of graph included in the repository.  

compursory arguments:
  -inImgDir <string>   Input directory of images
  -outImgDir <string>  Output directory for exporting pre-processed images
  -graph <string>      Directory of the SNAP graph to use in massive processing
  -inExt <string>      Extension of input image
  -outExt <string>     Extension of output image

for help use the following arguments:
  -h, --help           show this help message and exit

How to run the script:
python automated1.py -inImgDir <inImgDir> -outImgDir <outImgDir> -inExt <inExtension> -outExt <outExtension> -graph <graph.xml>  > "commands.bat"

Example on how to run the script: 
python automated1.py -inImgDir "D:\ASTARTE_Data\Level2_discardedData\ERS-1" -outImgDir "D:\ASTARTE_Data\Level2\ERS-1" -inExt .tif -outExt .tif -graph "D:\Scripts\Feb2020\myGraph.xml"  > "D:\Scripts\Feb2020\reprojectERS1_1.bat"

The ">" writes the generated commands into the ".bat" file. Once the executable ".bat" file is created, you may run it to execute the commands. 

Additional Notes:
(a) Make sure that Python is added to the Path during installation of SNAP, alternatively add it manually in the Path Variables so tha you can run the command "gpt" from command prompt.


Acknoledgements:
These scripts were developed as part of the "ASTARTE" project (EXCELLENCE/0918/0341), which is co-financed by the European Regional Development Fund and the Republic of Cyprus through the Research Innovation Foundation. 

This video tutorial will help you use it efficiently:
https://www.youtube.com/watch?v=iEEMn7h35nU
