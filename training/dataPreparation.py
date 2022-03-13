import pandas as pd
import numpy as np

class DataPrep:
    def __init__(self, train):
        self.train = train
        self.titles = set([i for i in self.train['Name'].str.split().apply(lambda x: x[1]).unique() if "." in i])
        self.Pclass = ("Pclass_" + self.train.Pclass.astype(str)).unique().tolist()
        self.Sex = self.train.Sex.unique().tolist()
        self.req_cols = "Not set"
        self.target = "Not set"


    def fit(self,df):
        df.index = df["PassengerId"]
        df = df[[i for i in list(df) if i != "PassengerId"]]
        df['Title'] = df["Name"].apply(lambda x: set(x.split()).intersection(self.titles))
        df['Title'] = df['Title'].apply(lambda x: list(x)[0] if len(list(x))>0 else "NoTitle")
        df['Pclass'] = df['Pclass'].astype(str)
        df['Pclass'] = np.where(df['Pclass'] == "1","Pclass_1",
                                np.where(df['Pclass'] == "2","Pclass_2",
                                        np.where(df['Pclass'] == "3","Pclass_3",np.nan)))
        df = pd.concat([df,pd.get_dummies(df.Title,dummy_na=False, drop_first=False)], axis=1)
        df = pd.concat([df,pd.get_dummies(df.Pclass,dummy_na=False, drop_first=False)], axis=1)
        df['Sex'] = np.where(df['Sex'] == "male",0,1)
        df["Age"] = df["Age"].fillna(df["Age"].mean())
        training_data = df.sample(frac=0.8, random_state=25)
        testing_data = df.drop(training_data.index)

        if self.req_cols == "Not set":
            self.req_cols = ['Sex', 'Age', 'SibSp',
                            'Parch','Fare','Capt.',
                            'Col.', 'Don.', 'Dr.', 'Jonkheer.', 'Major.', 'Master.', 'Miss.',
                            'Mlle.', 'Mme.', 'Mr.', 'Mrs.', 'Ms.', 'NoTitle', 'Rev.', 'Pclass_1',
                            'Pclass_2', 'Pclass_3']
            self.target = ['Survived']

        return training_data[self.req_cols], training_data[self.target], testing_data[self.req_cols], testing_data[self.target]

if __name__ == "__main__":
    train = pd.read_csv("data/train.csv")

    data = DataPrep(train)

    train_X, train_Y, test_X, test_Y  = data.fit(train)

    print(train_X.head())
    print(train_Y.Survived.value_counts())

    print(test_X.head())
    print(test_Y.Survived.value_counts())