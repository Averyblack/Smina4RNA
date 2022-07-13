import os
import argparse
import numpy as np

parser = argparse.ArgumentParser(description = 'Compute mean for the docking results', epilog= '', add_help=True, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-p', help='Path to the result files', required=True, metavar='RESULT')
args = vars(parser.parse_args())



def RMSD_mean(p):
    num_list = []
    for op_folder in os.listdir(p):
        path = p+op_folder
        for file  in os.listdir(path):
            if file == "bestRMSD3.txt":
                num_list.append(float(open(path+"/"+file).readline()))

    mn = np.mean(num_list)

    mean_file = open("bestRMSD3.txt", "w")
    mean_file.write(str(mn))
    mean_file.close()

RMSD_mean(args['p'])
