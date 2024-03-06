from numpy import savez
import pandas as pd
import sys

# barf whenever there are not exactly two arguments
infile, outfile = sys.argv[1:]

# read the pickle
df = pd.read_pickle(infile)
# we need to rename the 'file' key for compatibility with savez()
# we also recode the filenames to match the new format, and
# convert to UTF8 strings
df['files'] = [f'{f[:-7].decode()}.npz' for f in df.pop('file')]
# write Numpy's stable/simple npz format
savez(outfile, **df)
