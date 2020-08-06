

import pandas as pd
df = pd.read_json (r'D:\data\dhairya.____20200804_part_1\comments.json')
export_csv = df.to_csv (r'D:\data\dhairya.____20200804_part_1\comments.csv', index = None, header=True)