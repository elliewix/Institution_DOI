import pandas as pd

# read in the main GRID file

grid_csv = pd.read_csv("grid.csv")

# read in the GRID types file
gridtypes = pd.read_csv("types.csv")

# left merge on ID and grid_id

grid_merge = pd.merge(grid_csv, gridtypes, how='left', left_on = ['ID'], right_on = ['grid_id'])

# write out the new merged file

grid_merge.to_csv('grid_merge.csv')