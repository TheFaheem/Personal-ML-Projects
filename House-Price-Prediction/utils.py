import numpy as np
def load_data( ):
	data = np.loadtxt("house_price_data.txt", delimiter=',')
	X = data[:,0]
	y = data[:,1]
	return X, y
	

x_train, y_train = load_data() 