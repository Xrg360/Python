import pandas
data = [[1, 'Liquid', 24, 12],
[2, 'Virtus.pro', 19, 14],
[3, 'PSG.LGD', 15, 19],
[4,'Team Secret', 10, 20]] 
headers=["Pos", "Team", "Win", "Lose"] 
print(pandas.DataFrame(data, headers))
# print('                                         ')
# print('-----------------------------------------')
# print('                                         ')
# print(pandas.DataFrame(data, headers))