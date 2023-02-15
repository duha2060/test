import pandas as pd

df = pd.read_excel('Опросники.xlsx', sheet_name='Тест 1')
#name = df.iloc[:,4:8]
#df[6].mask(df[6] == 'Да', 1, inplace=True)
#df[5].mask(df[5] == 'Нет', 1, inplace=True)
#df.loc[df[] == 'Да'] = 1 
#f[1,2,3,4,5].mask(df[1,2,3,4,5] == 'Нет', 1, inplace=True)
#df[df.columns[1:10] == 'Нет'] = 3

list1 = [2,3,6,9,13,21,32,40,42,43,47,51,52,55,60,70]
list2 = [1,14,20,27,37,63,66,67]
list3 = [4,10,11,16,17,18,23,24,25,28,30,33,34,38,44,46,49,54,57,58,59,62,64,68]
list4 = [5,7,8,12,15,19,22,26,29,31,35,36,39,41,45,48,50,53,56,61,65,69]

for x in range(1,71):
   if x in list1:
    df[x].mask(df[x] == 'Да', 2, inplace=True) or df[x].mask(df[x] == 'Не знаю', 1, inplace=True) or df[x].mask(df[x] == 'Нет', 0, inplace=True)
    #a = df[x] + df[x]
    #print(a)
    print(df[x])
   elif x in list2:
    df[x].mask(df[x] == 'Нет', 2, inplace=True) or df[x].mask(df[x] == 'Да', 0, inplace=True) or df[x].mask(df[x] == 'Не знаю', 1, inplace=True)
   elif x in list3:
    df[x].mask(df[x] == 'Да', 2, inplace=True) or df[x].mask(df[x] == 'Не знаю', 1, inplace=True) or df[x].mask(df[x] == 'Нет', 0, inplace=True)
   elif x in list4:
    df[x].mask(df[x] == 'Да', 0, inplace=True) or df[x].mask(df[x] == 'Не знаю', 0, inplace=True) or df[x].mask(df[x] == 'Нет', 0, inplace=True)




df.to_excel('test1.xlsx', sheet_name="Тест 1",index=False)
#print(df.iloc[:,4])




