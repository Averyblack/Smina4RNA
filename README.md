# SMINA4RNA

Tuning simna to work well with the RNA


# Training

## `A-optuna-do.py`

The master script for optimization.

Input:
- reads docking summary from the text files

Ouptuts:
- the trial name
- writes the config file


## `B-single-docking.sh`

Parameters:
1. single directory with RNA and native ligand
1. output directory for this particular docking

To test: `./B-single-docking.sh ../data/sample_data/training/1AJU/ ../outputs/test_output/trial-1/1AJU/`


Outputs:
```
├── affinities.csv              -- score values for all poses
├── custom-sf.score.xz
├── log.txt.xz
├── output.sdf.xz
├── return_bestRMSD1.txt        -- best RMSD in top 1 scored poses
├── return_bestRMSD3.txt        -- best RMSD in top 3 scored poses
├── return_bestRMSD5.txt        -- best RMSD in top 5 scored poses
├── return_howManyPosesGenerated.txt   -- the number of generated poses
├── return_lowestAffinity.txt    -- best affinity value
└── rmsds.csv                   -- RMSD values for all poses
```

The important values to prostprocess are in `return_*.txt` files.

## `B-looper.sh`

Master script for handling the docking result files. It uses GNU-parallel to loop through the outpup files of the `B-single-docking.sh` and calculates mean for `return_*.txt` files uing `compute_mean.py` script.

Parameters:
1. Directory of the data folders
2. Direcotory for the output files

# Prerequisites
1. GNU-parallel
2. Numpy 
3. Smina

# How to run

In command line type:

`./B-looper.sh ../data/sample_data/training ../outputs`
