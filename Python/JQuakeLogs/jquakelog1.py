import pandas as pd

jquake_df = pd.read_csv('/home/mightygboole1815/Python/JQuakeLogs/CSVs/jquakelog4.csv', index_col='Intensity')
                                  
print(jquake_df)