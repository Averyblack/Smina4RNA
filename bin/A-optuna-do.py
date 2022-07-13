#!/usr/bin/env python
# -*- coding: utf-8 -*-

import optuna
##from optuna.integration import CatBoostPruningCallback
from optuna.samplers import TPESampler
#from optuna.samplers import RandomSampler
#from optuna.samplers import CmaEsSampler

import subprocess
import datetime
import math


time_budget=48*60*60
n_trials=None


study_name='test7' # no spaces!
storage="sqlite:///optimize.db"


def file_write(filename, content):
  f = open( filename, 'w' )
  f.write(content)
  f.close() 


def objective(trial):

    trialNumber=trial.number

    # trial ID
    today = datetime.datetime.today()
    trial_id = today.strftime('%Y-%m-%d_%H%M%S') + "__" + study_name + "__" + str(trialNumber)
    outDir="results/%s/" % (trial_id)
    print("\n\ntrial_id:", trial_id)

    # trial parameters

    param_1 = trial.suggest_float('param_1', -5, 5)
    param_2 = trial.suggest_float('param_2', -5, 5)
    param_3 = trial.suggest_float('param_3', -5, 5)
    param_4 = trial.suggest_float('param_4', -5, 5)
    param_5 = trial.suggest_float('param_5', -5, 5)
    param_6 = trial.suggest_float('param_6', -5, 5)
    param_7 = trial.suggest_float('param_7', -5, 5)
    param_8 = trial.suggest_float('param_8', -5, 5)
    param_9 = trial.suggest_float('param_9', -5, 5)
    param_10 = trial.suggest_float('param_10', -5, 5)
    param_11 = trial.suggest_float('param_11', -5, 5)
    param_12 = trial.suggest_float('param_12', -5, 5)
    param_13 = trial.suggest_float('param_13', -5, 5)
    param_14 = trial.suggest_float('param_14', -5, 5)
    param_15 = trial.suggest_float('param_15', -5, 5)
    param_16 = trial.suggest_float('param_16', -5, 5)
    param_17 = trial.suggest_float('param_17', -5, 5)
    param_18 = trial.suggest_float('param_18', -5, 5)
    param_19 = trial.suggest_float('param_19', -5, 5)
    param_20 = trial.suggest_float('param_20', -5, 5)
    param_21 = trial.suggest_float('param_21', -5, 5)
    param_22 = trial.suggest_float('param_22', -5, 5)
    param_23 = trial.suggest_float('param_23', -5, 5)
    param_24 = trial.suggest_float('param_24', -5, 5)
    param_25 = trial.suggest_float('param_25', -5, 5)
    param_26 = trial.suggest_float('param_26', -5, 5)
    param_27 = trial.suggest_float('param_27', -5, 5)
    param_28 = trial.suggest_float('param_28', -5, 5)
    param_29 = trial.suggest_float('param_29', -5, 5)
    param_30 = trial.suggest_float('param_30', -5, 5)
    param_31 = trial.suggest_float('param_31', -5, 5)
    param_32 = trial.suggest_float('param_32', -5, 5)
    param_33 = trial.suggest_float('param_33', -5, 5)
    param_34 = trial.suggest_float('param_34', -5, 5)
    param_35 = trial.suggest_float('param_35', -5, 5)
    param_36 = trial.suggest_float('param_36', -5, 5)
    param_37 = trial.suggest_float('param_37', -5, 5)
    param_38 = trial.suggest_float('param_38', -5, 5)
    param_39 = trial.suggest_float('param_39', -5, 5)
    param_40 = trial.suggest_float('param_40', -5, 5)
    param_41 = trial.suggest_float('param_41', -5, 5)
    param_42 = trial.suggest_float('param_42', -5, 5)
    param_43 = trial.suggest_float('param_43', -5, 5)
    param_44 = trial.suggest_float('param_44', -5, 5)
    param_45 = trial.suggest_float('param_45', -5, 5)
    param_46 = trial.suggest_float('param_46', -5, 5)

    custom_score = """#This is an example of an input that can be used to create and calibrate
%.5f  ad4_solvation(d-sigma=3.6,_s/q=0.01097,_c=8)  desolvation, q determines whether value is charge dependent
%.5f  ad4_solvation(d-sigma=3.6,_s/q=0.01097,_c=8)  in all terms, c is a distance cutoff
%.5f  electrostatic(i=1,_^=100,_c=8)	i is the exponent of the distance, see everything.h for details
%.5f  electrostatic(i=2,_^=100,_c=8)
%.5f  gauss(o=0,_w=0.5,_c=8)		o is offset, w is width of gaussian
%.5f  gauss(o=3,_w=2,_c=8)
%.5f  gauss(o=1.5,_w=0.3,_c=8)
%.5f  gauss(o=2,_w=0.9,_c=8)
%.5f  gauss(o=1,_w=0.9,_c=8)
%.5f  gauss(o=1,_w=0.5,_c=8)
%.5f  gauss(o=1,_w=0.3,_c=8)
%.5f  gauss(o=1,_w=0.7,_c=8)
%.5f  gauss(o=2,_w=0.5,_c=8)
%.5f  gauss(o=2,_w=0.7,_c=8)
%.5f  gauss(o=3,_w=0.9,_c=8)
%.5f  repulsion(o=0,_c=8)	o is offset of squared distance repulsion
%.5f  hydrophobic(g=0.5,_b=1.5,_c=8)		g is a good distance, b the bad distance
%.5f  hydrophobic(g=0.5,_b=1,_c=8)		g is a good distance, b the bad distance
%.5f  hydrophobic(g=0.5,_b=2,_c=8)		g is a good distance, b the bad distance
%.5f  hydrophobic(g=0.5,_b=3,_c=8)		g is a good distance, b the bad distance
%.5f  non_hydrophobic(g=0.5,_b=1.5,_c=8)	value is linearly interpolated between g and b
%.5f  vdw(i=4,_j=8,_s=0,_^=100,_c=8)	i and j are LJ exponents
%.5f  vdw(i=6,_j=12,_s=1,_^=100,_c=8) s is the smoothing, ^ is the cap
%.5f  non_dir_h_bond(g=-0.7,_b=0,_c=8)	good and bad
%.5f  non_dir_h_bond(g=-0.7,_b=0.2,_c=8)	good and bad
%.5f  non_dir_h_bond(g=-0.7,_b=0.5,_c=8)	good and bad
%.5f  non_dir_h_bond(g=-1,_b=0,_c=8)	good and bad
%.5f  non_dir_h_bond(g=-1,_b=0.2,_c=8)	good and bad
%.5f  non_dir_h_bond(g=-1,_b=0.5,_c=8)	good and bad
%.5f  non_dir_h_bond(g=-1.3,_b=0,_c=8)	good and bad
%.5f  non_dir_h_bond(g=-1.3,_b=0.2,_c=8)	good and bad
%.5f  non_dir_h_bond(g=-1.3,_b=0.5,_c=8)	good and bad
%.5f  non_dir_anti_h_bond_quadratic(o=0.0,_c=8) 
%.5f  non_dir_anti_h_bond_quadratic(o=0.5,_c=8) 
%.5f  non_dir_anti_h_bond_quadratic(o=1.0,_c=8) 	
%.5f  non_dir_h_bond_lj(o=-0.7,_^=100,_c=8)	LJ 10-12 potential, capped at ^
%.5f  non_dir_h_bond_lj(o=-1,_^=100,_c=8)	LJ 10-12 potential, capped at ^
%.5f  non_dir_h_bond_lj(o=-1.3,_^=100,_c=8)	LJ 10-12 potential, capped at ^
%.5f  num_tors_div	div constant terms are not linearly independent
%.5f  num_heavy_atoms_div	
%.5f  num_heavy_atoms	these terms are just added
%.5f  num_tors_add
%.5f  num_tors_sqr
%.5f  num_tors_sqrt
%.5f  num_hydrophobic_atoms
%.5f  ligand_length
""" % (param_1, param_2, param_3, param_4, param_5, param_6, param_7, param_8, param_9, param_10, param_11, param_12, param_13, param_14, param_15, param_16, param_17, param_18, param_19, param_20, param_21, param_22, param_23, param_24, param_25, param_26, param_27, param_28, param_29, param_30, param_31, param_32, param_33, param_34, param_35, param_36, param_37, param_38, param_39, param_40, param_41, param_42, param_43, param_44, param_45, param_46)

    #print(custom_score)
    file_write("custom-sf.score", custom_score)

    # run the docking
    bashCommand="./smina-do.sh %s" % (trial_id)
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]

    # value of RMSD (best in top 3 scored poses)
    with open(outDir + "bestRMSD3.txt") as f:
        score = f.readlines()
    score1 = float(score[0].strip())

    # number of generated poses
    with open(outDir + "howManyPosesGenerated.txt") as f:
        score = f.readlines()
    score2 = float(score[0].strip())


    # the sign of the lowest affinity
    with open(outDir + "lowestAffinity.txt") as f:
        score = f.readlines()
    score3temp = float(score[0].strip())
    # sign of the affinity. We want to have it negative
    score3 = math.copysign(1, score3temp)



    print("****** Best RMSD: ", score1, "--------- Poses", score2, "++++++++++++ Lowest affinity:", score3)
    return score1, score2, score3


study = optuna.create_study(study_name=study_name, directions=["minimize", "maximize", "minimize"], storage=storage, load_if_exists=True)

study.optimize(objective, n_trials=n_trials, timeout=time_budget)  # Invoke optimization of the objective function.


print("\n\nBest trial:")

print(f"Number of trials on the Pareto front: {len(study.best_trials)}")


studyDf = study.trials_dataframe()
print(studyDf)


print(studyDf.columns)

print(study.trials_dataframe())
