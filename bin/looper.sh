#!/bin/bash

ls $1 > temp_data_files.txt

parallel -q './B-single-docking.sh' $1/{} $2/{} :::: temp_data_files.txt

rm temp_data_files.txt

#ls $2 > temp_output_files.txt

#parallel python3 compute.py -p $2{} :::: temp_output_files.txt
python3 compute_mean.py -p $2/