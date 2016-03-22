# Load Cells

This was a work project where I attempted to compile into one document the serial numbers and calibration data from a bunch of separate documents.

Original data was .pdf.  Used tabula to get table data out of .pdf into separate .csv files.  

This script walks through the directory and subdirectories looking for .csv files and strips out the relevant information.  It then writes the info into a single tab delimited text file (filename hard-coded).

Ideas to make this more useful:
* ability to define filename as a command line argument
* ability to point to a specific folder to search
* is there a way to make this more general?
