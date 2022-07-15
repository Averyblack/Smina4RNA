#!/bin/bash

#Master script for

# 1 - path to training data
# 2 - path to output dir

#Creates the files with the names of the data folders to loop over
ls $1 > temp_data_files.txt


# Runs B-single-docking.sh parallelly for all training data folders
parallel xz --decompress $1/{}/rna.pdbqt.xz :::: temp_data_files.txt
parallel --jobs 3 --progress -q './B-single-docking.sh' $1/{} $2/{} :::: temp_data_files.txt

# Removes the temp file
rm temp_data_files.txt

# Calculate the mean of the results
python3 compute_mean.py -p $2/
