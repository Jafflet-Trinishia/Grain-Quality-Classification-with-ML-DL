

import numpy as np
import pandas as pd
import os
from PIL import Image
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from keras.utils import np_utils
from keras.preprocessing.image import  img_to_array
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
from sklearn.metrics import accuracy_score

def process(path):
	# input image dimensions
	m,n = 240,240
	classes=os.listdir(path)
	print(classes)
	x=[]
	y=[]
	count = 0
	for fol in classes:
		print (fol)
		imgfiles=os.listdir(path + '\\' + fol)
		for img in imgfiles:
			try:
				im=Image.open(path+'\\'+fol+'\\'+img)
				print(img)
				im=im.convert(mode='RGB')
				imrs=im.resize((m,n))
				imrs=img_to_array(imrs)/255
				imrs=imrs.transpose(2,0,1)
				imrs=imrs.reshape(3,m,n)
				x.append(imrs)
				y.append(count)
			except:
				pass
		count += 1

	x=np.array(x);
	y=np.array(y);
	
	print(x)
	print(y)

	x_train, x_test, y_train, y_test= train_test_split(x,y)
	

	x_train = np.reshape(x_train, (x_train.shape[0], -1))
	x_test = np.reshape(x_test, (x_test.shape[0], -1))
	
	model2=KNeighborsClassifier(n_neighbors=2, metric='euclidean')
	model2.fit(x_train, y_train)
	y_pred = model2.predict(x_test)
	
	result2=open("results/resultRF.csv","w")
	result2.write("ID,Predicted Value" + "\n")
	for j in range(len(y_pred)):
	    result2.write(str(j+1) + "," + str(y_pred[j]) + "\n")
	result2.close()
	
	mse=mean_squared_error(y_test, y_pred)
	mae=mean_absolute_error(y_test, y_pred)
	r2=r2_score(y_test, y_pred)
	
	
	print("---------------------------------------------------------")
	print("MSE VALUE FOR KNN IS %f "  % mse)
	print("MAE VALUE FOR KNN IS %f "  % mae)
	print("R-SQUARED VALUE FOR KNN IS %f "  % r2)
	rms = np.sqrt(mean_squared_error(y_test, y_pred))
	print("RMSE VALUE FOR KNN IS %f "  % rms)
	ac=accuracy_score(y_test,y_pred)
	print ("ACCURACY VALUE KNN IS %f" % ac)
	print("---------------------------------------------------------")
	

	result2=open('results/KNNMetrics.csv', 'w')
	result2.write("Parameter,Value" + "\n")
	result2.write("MSE" + "," +str(mse) + "\n")
	result2.write("MAE" + "," +str(mae) + "\n")
	result2.write("R-SQUARED" + "," +str(r2) + "\n")
	result2.write("RMSE" + "," +str(rms) + "\n")
	result2.write("ACCURACY" + "," +str(ac) + "\n")
	result2.close()
	
	
	df =  pd.read_csv('results/KNNMetrics.csv')
	acc = df["Value"]
	alc = df["Parameter"]
	colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
	explode = (0.1, 0, 0, 0, 0)  
	
	fig = plt.figure()
	plt.bar(alc, acc,color=colors)
	plt.xlabel('Parameter')
	plt.ylabel('Value')
	plt.title('KNN Metrics Value')
	fig.savefig('results/KNNMetricsValue.png') 
	plt.pause(5)
	plt.show(block=False)
	plt.close()

#process("train")
	




