## @package Manager
#  It manages files and folders
#  @author Dr Milto Miltiadou
#  @date Oct 2020
#  @version 1.0
import os

## this function taks as input a directory and returns all its sub-directories
# @param[in] i_inDir input directory
# @return a list with sub-directories
def getDirs(i_inDir):
   return [d[0] for d in os.walk(i_inDir)]

## this function that copies a folder structure
# @param[in] i_inDir directory with folder structure to be copied
# @param[in] i_outDir directory of folder where structure will be copied
# @returns a list with the paths of the sub-directories
def creatFolders(i_inDir,i_outDir):
   os.chdir(i_inDir)
   #dirs=[d[0] for d in os.walk(".")]
   dirs = getDirs(".")
   os.chdir(i_outDir)
   for d in dirs:
      if not os.path.exists(d):
         os.makedirs(d)
   return dirs
   
## this function returns the names of all the files with a given extension 
#  within a given directory
#  @param[in] i_inDir the directory of our interest
#  @param[in} i_ext the extension of our interest
#  @return a list with the names of the files that have the given extension
def getFilesNames(i_inDir,i_ext):    
    cdir=os.getcwd()
    os.chdir(i_inDir)
    images=[f for f in os.listdir(".")if f.endswith(i_ext)] 
    os.chdir(cdir)
    return images



