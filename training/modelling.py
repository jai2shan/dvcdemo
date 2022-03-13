from sklearn.metrics import *
import pandas as pd
import pickle


class ourModel:
    def __init__(self,algoName, model,x,y):
        self.accuracy = None
        self.algoName = algoName
        self.model = model()
        self.x = x
        self.y = y
        self.fit_model = None
    
    def fitModel(self):
        self.fit_model = self.model.fit(self.x, self.y)
        filename = 'model/model.sav'
        pickle.dump(self.model,  open(filename, 'wb'))

        y_pred = self.fit_model.predict(self.x)
        tn, fp, fn, tp = confusion_matrix(self.y, y_pred).ravel()

        result = {"True Negative": tn,
                  "False Positive": fp,
                  "False Negative": fn,
                  "True Positive": tp}

        print("Accuracy : ",accuracy_score(self.y, y_pred))
        print("Classification Report : ",classification_report(self.y, y_pred))
        result.update(classification_report(self.y, y_pred,output_dict=True))
        
        return result


        

