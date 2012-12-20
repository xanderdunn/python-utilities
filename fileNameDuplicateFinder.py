import sys, os

# Description
# Take three command-line arguments: A directory of files to look through,
#   a filetype to throw away, and a filetype to keep
# Find files with the same filename and different filetype and move the
#   throw away filetype version to a ./duplicates folder

# Get files in folder given as a command-line argument

# Iterate through the files.  Check if filename is in dictionary.
#   If not, add filename to dictionary.
#   If yes, then mv "FILENAME.JPG"

def function():
    directory = sys.argv[1]
    os.chdir(directory) # Change to this directory
    filetype1 = sys.argv[2].upper()
    filetype2 = sys.argv[3].upper()
    keepFilesSet = set() # set of filenames which are to be kept
    os.system("mkdir duplicates") # duplicates will go into this folder
    print("Searching for duplicate filenames of type %s and %s in %s" %
          (filetype1, filetype2, directory))
    print("The following files will be moved to %s/duplicates/" % (directory))
    for file in os.listdir(directory): # First pass for wanted files
        if file.endswith(filetype2):
            keepFilesSet.add(os.path.splitext(file)[0]) # Add to set
    for file in os.listdir(directory): # Second pass for unwanted files
        if file.endswith(filetype1) and os.path.splitext(file)[0] in keepFilesSet:
            os.system("mv ./%s ./duplicates/%s" % (file, file))
            print("%s" % (file))

function()

# FIXME: There should be a main function, and the usual if statements guard