import os
import argparse
import numpy as np
import matplotlib.pyplot as plt

#Function for calculating means and plotting
def calc_mean(p, result):
    num_list = []
    for root, dirs, files in os.walk(p):
        for file in files:
            if file == result and os.path.getsize(os.path.join(root, file)) != 0: # This should prevent null values from going into the results
                    num_list.append(float(open(os.path.join(root, file)).readline()))

    #creates a box plot
    plt.figure(figsize = (10,7))
    plt.boxplot(num_list)
    name = result.split(".")[0]
    plt.title(name)
    plt.savefig(args['p']+name+".png")

    #calculates mean
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
