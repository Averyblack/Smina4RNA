# SMINA4RNA

Tuning simna to work well with the RNA


# Training

## `B-single-docking.sh`

Parameters:
1. single directory with RNA and native ligand
1. output directory for this particular docking

To test: `./B-single-docking.sh ../data/sample_data/training/1AJU/ ../outputs/test_output/trial-1/1AJU/`


Outputs:
```
├── affinities.csv              -- score values for all poses
├── bestRMSD3.txt               -- best RMSD in top 3 scored poses
├── custom-sf.score.xz
├── howManyPosesGenerated.txt   -- the number of generated poses
├── log.txt.xz
├── lowestAffinity.txt          -- best affinity value
├── output.sdf.xz
└── rmsds.csv                   -- RMSD values for all poses
```
