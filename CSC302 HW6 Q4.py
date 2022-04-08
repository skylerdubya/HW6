import pandas as pd
import seaborn as sns

#Your code goes here.
world_cup = pd.read_csv('/content/drive/MyDrive/DATA/WorldCupMatches.csv')
world_cup.head()

#4a total number of matches between teams?
team_pairs1 = world_cup.groupby(['Home Team Initials', 'Away Team Initials']).count().reset_index()
team_pairs1.rename(columns={'Year':'weight'}, inplace=True)
test = team_pairs1[{'Home Team Initials', 'Away Team Initials', 'weight'}]
#print(team_pairs1.shape)
test.head(50)

#4b
team_pairs2 = world_cup.groupby(['Home Team Initials', 'Away Team Initials'])['Home Team Goals'].sum().reset_index()
team_pairs2.head(50)

#4c
team_pairs = pd.merge(test,team_pairs2, on=['Home Team Initials', 'Away Team Initials'], how='inner')
team_pairs.head(50)

#4d
team_pairs.to_csv("/content/drive/My Drive/HW6.csv")
