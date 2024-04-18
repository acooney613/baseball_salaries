import pandas as pd


field = pd.read_csv('field/field.csv')
salary = pd.read_csv('salary/salary.csv')
batter = pd.read_csv('batter/batter.csv')

# function to assign handedness based on information provided from baseball reference documentation
def batter_direction(name):
    if '*' in name:
        return 'L'
    elif '#' in name:
        return 'S'
    else:
        return 'R'
    
# Clean columns
field = field.drop(['G', 'GS', 'CG'], axis = 1)
field = field.rename(columns = {'Inn' : 'Def-Inn'})

# Select certain columns
salary = salary.drop(['Name', 'Age', 'Tm'], axis = 1)

# Clean columns
batter['Age'] = batter['Age'].astype(int)
batter['Bat'] = batter['Name'].apply(batter_direction)
stats = batter.drop(['Name', 'Age', 'Tm', 'Lg', 'G', 'Pos Summary'], axis = 1)

# Merge each dataset
baseball = field.merge(salary, on = ['Name-additional', 'Season'])
baseball = baseball.merge(stats, on = ['Name-additional', 'Season'])

# feature engineering for data
baseball = baseball.drop(['Name', 'Age', 'Name-additional'], axis = 1)
baseball['Salary'] = baseball['Salary'].str.replace('$', '').astype(float)

baseball['Pos_C'] = baseball['Position'].apply(lambda x: 1 if 'C' in x else 0)
baseball['Pos_1B'] = baseball['Position'].apply(lambda x: 1 if '1B' in x else 0)
baseball['Pos_2B'] = baseball['Position'].apply(lambda x: 1 if '2B' in x else 0)
baseball['Pos_3B'] = baseball['Position'].apply(lambda x: 1 if '3B' in x else 0)
baseball['Pos_SS'] = baseball['Position'].apply(lambda x: 1 if 'SS' in x else 0)
baseball['Pos_OF'] = baseball['Position'].apply(lambda x: 1 if 'OF' in x else 0)

baseball['Num_Pos'] = baseball[['Pos_C', 'Pos_1B', 'Pos_2B', 'Pos_3B', 'Pos_SS', 'Pos_OF']].sum(axis = 1)
baseball['R/AB'] = baseball['R'] / baseball['AB']
baseball['2B/AB'] = baseball['2B'] / baseball['AB']
baseball['3B/AB'] = baseball['3B'] / baseball['AB']
baseball['HR/AB'] = baseball['HR'] / baseball['AB']
baseball['RBI/AB'] = baseball['RBI'] / baseball['AB']
baseball['BB/PA'] = baseball['BB'] / baseball['PA']
baseball['SB - CS'] = baseball['SB'] - baseball['CS']
baseball['BB - SO'] = baseball['BB'] - baseball['SO'] # measures a batters eye
baseball['E/Def-Inn'] = baseball['E'] / baseball['Def-Inn']
baseball['DP/Def-Inn'] = baseball['DP'] / baseball['Def-Inn']

baseball = baseball.drop(['Position', 'Def-Inn', 'PO', 'A', 'E', 'DP', 'PA', 'AB', 'R', 'H', 
                          '2B', '3B', 'HR', 'RBI', 'SB', 'CS', 'BB', 'SO', 'TB', 'GDP', 'HBP', 'SH', 'SF', 'IBB'], axis = 1)

# Write to CSV
baseball.to_csv('baseball.csv', index = False)