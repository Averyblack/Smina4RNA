#!/bin/bash

# master low level script to dock with smina
# Filip Stefaniak

# -----------------------------#

# Ligand to dock
ligand_to_dock="ligand.sdf"

# Reference ligand
native_ligand="ligand.sdf"

# RNA receptor pdbqt file
rnaFile="rna.pdbqt"

# -----------------------------#

# smina fixed parameters
exh=8
ile_poz=10
seed="2022"
autobox_add=8

# -----------------------------#

inputDir="$1"
outputDir="$2"

mkdir -p "$outputDir"


# ------------- docking

## copying config to the destination output dir

cp custom-sf.score $outputDir/

## docking
./smina.static -r "$inputDir/$rnaFile" -l "$inputDir/$ligand_to_dock" --autobox_ligand="$inputDir/$native_ligand" --autobox_add $autobox_add --exhaustiveness $exh -o $outputDir/output.sdf \
--log $outputDir/log.txt --num_modes $ile_poz --energy_range 50 --seed $seed --custom_scoring $outputDir/custom-sf.score


## calculate rmsd
python3 rmsd-calculate.py -x $inputDir/$native_ligand -f $outputDir/output.sdf > $outputDir/rmsds.csv

## return the best RMSD in top scored 3 poses:

bestRMSD3=$(cat $outputDir/rmsds.csv  | head -3 | sort -k 2 -n | head -1 | cut -f 2)

echo "$bestRMSD3" | tee $outputDir/bestRMSD3.txt
cat $outputDir/rmsds.csv | wc -l | tee $outputDir/howManyPosesGenerated.txt

# extract affinities
cat $outputDir/output.sdf | grep -A 1 "minimizedAffinity" --no-group-separator | grep -v "minimizedAffinity" > $outputDir/affinities.csv

# get the lowest value (the best value)
cat $outputDir/affinities.csv | sort -n | tee $outputDir/lowestAffinity.txt



## compress the output
xz $outputDir/output.sdf $outputDir/log.txt $outputDir/custom-sf.score
