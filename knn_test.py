import numpy as np 
import pandas as pd
from font import get_font_data
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
import pickle


def main():
	# 处理缺失值
	imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
	
	# data1 = imputer.fit_transform(pd.DataFrame(get_font_data()))
	# numpy 取出特征值\目标值
	# x = data1[:,1:]
	# y = data1[:,0]
	# print(x.shape)

	data = pd.DataFrame(imputer.fit_transform(pd.DataFrame(get_font_data())))
	# print(data)
	# data.to_csv('data.csv')

	# 取出特征值\目标值
	x = data.drop([0], axis=1)
	y = data[0]
	# print(y)

	# 分割数据集
	# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2,random_state=0)
	# x_train = x.head(30)
	# y_train = y.head(30)
	
	x_train = x.iloc[30:100]
	y_train = y.iloc[30:100]
	x_test = x.iloc[0:30]
	y_test = y.iloc[0:30]
	print('训练集形状',x_train.shape)
	# 标准化
	# std = StandardScaler()
	# x_train = std.fit_transform(x_train)
	# x_test = std.transform(x_test)

	# 进行算法流程
	knn = KNeighborsClassifier(n_neighbors=1)
	# 开始训练
	knn.fit(x_train, y_train)
	# 预测结果
	y_predict = knn.predict(x_test)
	print(y_predict)

	# 得出准确率
	print(knn.score(x_test, y_test))

	# 保存模型
	# method 1 pickle
	# with open('model/knn.pickle','wb') as f:
	# 	pickle.dump(knn,f)

	# 加载模型
	with open('model/knn.pickle','rb') as f:
		knn2 = pickle.load(f)
		print(knn2.score(x_test, y_test))


if __name__ == '__main__':
	main()