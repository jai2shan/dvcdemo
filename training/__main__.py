from training.dataPreparation import *
from training.modelling import *
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import yaml
import json
import numpy as np


def load_config(config_name):
    with open(config_name) as file:
        config = yaml.safe_load(file)
    print(config)
    return config

def np_encoder(object):
    if isinstance(object, np.generic):
        return object.item()

if __name__ == "__main__":
    config = load_config("config.yaml")

    train = pd.read_csv(config["data_directory"])

    data = DataPrep(train)

    train_X, train_Y, test_X, test_Y  = data.fit(train)

    model = ourModel(config["model_name"],
                     eval(config["model"]),
                     train_X, train_Y)
    result = model.fitModel()
    print(result)
    
    with open('result.json', 'w') as fp:
        json.dump(result, fp, default=np_encoder)

