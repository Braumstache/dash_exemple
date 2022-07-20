import pandas as pd
#import des données
df=pd.read_csv("dash_exemple\demo\data\prix-carburants-test.csv",sep=';')
dftable=df[['dep_code','dep_name','ville','prix_nom','prix_valeur']]
dftable.rename(columns={"dep_code":"code_departement","dep_name":"departement","prix_nom":"carburant","prix_valeur":"prix"},inplace=True)
dfmap=dftable.groupby(['code_departement','departement','carburant'],group_keys = True, as_index=False)["prix"].mean()
dfmap=pd.DataFrame(dfmap)
liste_carburant=dfmap['carburant'].value_counts().keys()
liste_dep=dfmap['code_departement'].value_counts().keys()
dftable1=df[['reg_name','adresse','dep_name','ville','prix_nom','prix_valeur']]
dftable1.rename(columns={"reg_name":"region","dep_name":"departement","prix_nom":"carburant","prix_valeur":"prix"},inplace=True)
dftable1['ville'].str.lower().str.capitalize()