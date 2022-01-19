from tensorflow.keras.optimizers import Adam

def train_model(model, X_train, Y_train, **params):
	lr = params.get("lr")
	train_epochs = params.get("train_epochs")
	batch_size = params.get("batch_size")
	val_split = params.get("val_split")
	model_verbose = params.get("model_verbose")

	print("training neural network...")

	opt = Adam(learning_rate = lr)

	model.compile(optimizer = opt, loss = 'binary_crossentropy',
             metrics = ['accuracy'])

	model.fit(X_train, Y_train, epochs = train_epochs,
                batch_size = batch_size, validation_split = val_split,
                verbose = model_verbose)