#!/bin/bash

ls $1 > temp_data_files.txt

parallel -q './B-single-docking.sh' $1/{} $2{} :::: temp_data_files.txt

rm temp_data_files.txt