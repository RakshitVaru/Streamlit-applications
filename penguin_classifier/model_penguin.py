import pandas as pd

dataset= pd.read_csv("https://raw.githubusercontent.com/dataprofessor/code/master/streamlit/part3/penguins_cleaned.csv")


df= dataset.copy()
target='species'
encode=['sex', 'island']

for i in encode:
    dummy= pd.get_dummies(df[i], prefix=i)
    df=pd.concat([df,dummy], axis=1)
    del df[i]

target_mapper= {'Adelie':0, 'Chinstrap':1, 'Gentoo':2}
def taget_encode(val):
    return target_mapper[val]

df['species']= df['species'].apply(taget_encode)

X=df.drop('species',axis=1)
Y=df['species']

from sklearn.ensemble import RandomForestClassifier

clf= RandomForestClassifier()

clf.fit(X,Y)

import pickle
pickle.dump(clf, open('penguins_clf.pkl','wb'))