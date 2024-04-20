# Activity Python 1: Task 1
# File: ACT_Python_HeaderTemplate_Team150_maarabrn.py 
# Date:    1 12 2024
# By:      Rania Maaraba
# Section: 09
# Team:    150
# 
# ELECTRONIC SIGNATURE
# Rania Maaraba
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# this program calls the program's name and compute and store the successive values of X
# using this data, it will compute the local sizes of of bins width and their quantities as well as
# store the information in a list and then print the final list.
 
import math

def HW2p1_Task1_maarabrn(a, b, n):
    
    X = [0.1]
    Y = [0.2]
   
    for i in range(n - 1):
        X_i = Y[-1]
        Y_i = -b * X[-1] + a * Y[-1] - (Y[-1]) ** 3
        
        X.append(X_i)
        Y.append(Y_i)

    num_bins = 1 + math.ceil(math.log2(n))

    bin_width = (max(X) - min(X)) / num_bins
    
    fd = [0] * num_bins
    for value in X:
        bin_index = min(int((value - min(X)) / bin_width), num_bins -1)
        fd[bin_index] += 1

    print("the frequency distribution is: ", fd)
