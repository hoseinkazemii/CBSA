from tensorflow.keras.optimizers import Adam

def train_model(model, X_train, X_test, Y_train, Y_test, **params):
	lr = params.get("lr")
	train_epochs = params.get("train_epochs")
	batch_size = params.get("batch_size")
	val_split = params.get("val_split")

	opt = Adam(learning_rate = lr)

	model.compile(optimizer = opt, loss = 'binary_crossentropy',
             metrics = ['accuracy'])

	model.fit(X_train, Y_train, epochs = train_epochs,
                batch_size = batch_size, validation_split = val_split)