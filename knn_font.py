import numpy as np
import pandas as pd
from font import get_font_data
from sklearn.impute import SimpleImputer
from sklearn.neighbors import KNeighborsClassifier
import pickle


class Classify:
    def __init__(self):
        self.len = None
        self.knn = self.get_knn()

    def process_data(self, data):
        imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
        return pd.DataFrame(imputer.fit_transform(pd.DataFrame(data)))

    def get_knn(self):
        # data = self.process_data(get_font_data())
        # x_train = data.drop([0], axis=1)
        # y_train = data[0]
        # knn = KNeighborsClassifier(n_neighbors=1)
        # knn.fit(x_train, y_train)
        with open('model/knn.pickle','rb') as f:
            knn2 = pickle.load(f)
            self.len = 122
        # self.len = x_train.shape[1]
        return knn2

    def knn_predict(self, data):
        df = pd.DataFrame(data)
        data = pd.concat([df, pd.DataFrame(np.zeros(
            (df.shape[0], self.len - df.shape[1])), columns=range(df.shape[1], self.len))])
        data = self.process_data(data)

        y_predict = self.knn.predict(data)
        return y_predict


if __name__ == '__main__':
    obj = Classify()
    obj.get_knn()
    obj.knn_predict()
