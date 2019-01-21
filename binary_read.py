
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import argparse

# ---- Parser - list of arguments passed when the script is launch

parser = argparse.ArgumentParser(prog='PROG',
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 description='This code can be used to read a binary and translate it in pandas dataframe structure')

parser.add_argument('--path_file', metavar='p',
                    help='Path of the binary file')
parser.add_argument('--file_name', metavar='f',
                    help='Name of the binary file')
parser.add_argument('--header_file_name', metavar='hf',
                    help='Name of the header of the binary file')
parser.add_argument('--file_end', metavar='hf',
                    help='Name of the final file export in csv')

args = parser.parse_args()

# ---- List of Functions ----------------------------------
def plot_figure(data, id1, id2):
    '''
       Function to plot signal
       input :
            data : dataframe
            id1 : column's number for the x axis
            id2 : column's number for the y axis
       output :
            figure
    '''
    
    # ---- Make a figure
    plt.figure(figsize=(15,7))
    plt.plot(data.iloc[:,id1], data.iloc[:,id2], label=data.columns[id2])
    plt.grid(True)
    plt.xlabel(TS_CMP_25Hz.columns[id1]+' (s)')
    plt.ylabel(TS_CMP_25Hz.columns[id2]+' (m)')
    plt.legend()

# ---- main ----------------------------------

if __name__ == '__main__':
    # ---- Path of the file
    path = args.path_file

    # ---- Extract binary value with numpy
    data = np.fromfile(path+args.file_name)

    # ---- Extract colum's name for the matrix
    header = pd.read_csv(path+args.header_file_name)

    # ---- Reshape the vector in matrix
    data = data.reshape(header.shape[1], int(data.shape[0]/header.shape[1]))

    # ---- Create a dataframe from the data
    TS_CMP_25Hz = pd.DataFrame(data=data.T, columns=header.columns)

    # ---- Export 10 first lines in csv file
    TS_CMP_25Hz.iloc[:10, :].to_csv(args.file_end+'.csv')
