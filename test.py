import pandas as pd

df = pd.read_excel('Опросники.xlsx', sheet_name='Тест 2')
#name = df.iloc[:,4:8]
#df[6].mask(df[6] == 'Да', 1, inplace=True)
#df[5].mask(df[5] == 'Нет', 1, inplace=True)
#df.loc[df[] == 'Да'] = 1 
#f[1,2,3,4,5].mask(df[1,2,3,4,5] == 'Нет', 1, inplace=True)
#df[df.columns[1:10] == 'Нет'] = 3
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
list2 = [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38]
list3 = [39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58]
list4 = [59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79]

for x in range(1,80):
   if x in list1:
    df[x].mask(df[x] == 'Да', 1, inplace=True) or  df[x].mask(df[x] == 'Нет', 0, inplace=True)
   elif x in list2:
    df[x].mask(df[x] == 'Да', 1, inplace=True) or df[x].mask(df[x] == 'Нет', 0, inplace=True) 
   elif x in list3:
    df[x].mask(df[x] == 'Да', 1, inplace=True) or df[x].mask(df[x] == 'Нет', 0, inplace=True)
   elif x in list4:
    df[x].mask(df[x] == 'Да', 1, inplace=True) or  df[x].mask(df[x] == 'Нет', 0, inplace=True)


   
   

#

df.to_excel('test2.xlsx', sheet_name="Лист 1")