from numpy import savez
import pandas as pd
import sys

# barf whenever there are not exactly two arguments
infile, outfile = sys.argv[1:]

# read the pickle
df = pd.read_pickle(infile)
# write Numpy's stable/simple npz format
savez(outfile, **df)
