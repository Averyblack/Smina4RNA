import os
import argparse
import numpy as np
#from matplotlib.pyplot import plt

#Function for calculating means for every output folder
def calc_mean(p, result):
    num_list = []
    for op_folder in os.listdir(p):
        if ".txt" not in op_folder:
            path = p+op_folder
            for file  in os.listdir(path):
                if file == result:
                    print(float(open(path+"/"+file).readline()))
                    num_list.append(float(open(path+"/"+file).readline()))

    mn = np.mean(num_list)
    #Save the means as the new files 
    mean_file = open(args['p']+result, "w")
    mean_file.write(str(mn))
    mean_file.close()

#Pareser for inputing path
parser = argparse.ArgumentParser(description = 'Compute mean for the docking results', epilog= '', add_help=True, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('-p', help='Path to the result files', required=True, metavar='RESULT')
args = vars(parser.parse_args())

#Calculating mean for the return values 
calc_mean(args['p'], "return_bestRMSD1.txt")
calc_mean(args['p'], "return_bestRMSD3.txt")
calc_mean(args['p'], "return_bestRMSD5.txt")
calc_mean(args['p'], "return_howManyPosesGenerated.txt")
calc_mean(args['p'], "return_lowestAffinity.txt")
