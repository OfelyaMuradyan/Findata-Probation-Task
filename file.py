import pandas as pd

def reading_files():
    text1 = open("/home/ofelya/CompanyA_Quarter1.txt", "r")
    print(text1.read())

    text2 = open("/home/ofelya/CompanyA_Quarter2.txt", "r")
    print(text2.read())

    text3 = open("/home/ofelya/CompanyB_Quarter1.txt", "r")
    print(text3.read())

    text4 = open("/home/ofelya/CompanyB_Quarter2.txt", "r")
    print(text4.read())

def CompanyA(result):
    result1 = result.loc[result.index[1:8], result.columns[0:1]]
    result1 = result1.applymap(lambda x: int(x.replace(',', '').replace('$', '').replace('.','')))
    result1['Difference'] = result1.apply(lambda row: row[1] - row[0], axis=1)
    print(result1)

def CompanyB(result):
    result2 = result.loc[result.index[1:8], result.columns[2:3]]
    result2 = result2.applymap(lambda x: int(x.replace(',', '').replace('$', '').replace('.','')))
    result2['Difference'] = result2.apply(lambda row: row[1] - row[0], axis=1)
    print(result2)

def creating_df():
    dfA1 = pd.read_csv('/home/ofelya/CompanyA_Quarter1.txt', sep = ":")

    dfA2 = pd.read_csv('/home/ofelya/CompanyA_Quarter2.txt', sep = ":")
    dfA2 = dfA2.drop('Company', axis=1)

    dfB1 = pd.read_csv('/home/ofelya/CompanyB_Quarter1.txt', sep = ":")
    dfB1 = dfB1.drop('Company', axis=1)

    dfB2 = pd.read_csv('/home/ofelya/CompanyB_Quarter2.txt', sep = ":")
    dfB2 = dfB2.drop('Company', axis=1)

    frames = [dfA1,dfA2,dfB1,dfB2]
    result = pd.concat(frames, axis = 1)
    result.set_index('Company', inplace=True)
    print(result)

    user = input('Which company\'s difference do you want?: ')
    if user == 'A':
        CompanyA(result)
    elif user == 'B':
        CompanyB(result)

reading_files()
creating_df()