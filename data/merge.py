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

# Write to CSV
baseball.to_csv('baseball.csv', index = False)