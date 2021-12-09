import tensorflow as tf
from tensorflow import keras
from datetime import datetime
from packaging import version

# based on code from https://towardsdatascience.com/how-to-split-a-tensorflow-dataset-into-train-validation-and-test-sets-526c8dd29438 "get_dataset_partitions_tf"

logdir = "logs/new_logs/" + datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = keras.callbacks.TensorBoard(log_dir=logdir)


class TFModel:
    def __init__(self):
        self.model = keras.Sequential([
            keras.layers.Reshape(target_shape=(768,), input_shape=(768,)),
            keras.layers.Dense(units=500, activation='tanh'), #tanh
            keras.layers.Dense(units=400, activation='tanh'), #With this layer added ending with training and test accuracy of 51%
            keras.layers.Dense(units=200, activation='tanh'),
            #keras.layers.Dense(units=200, activation='tanh'),
            #keras.layers.Dense(units=10, activation='tanh'),
            keras.layers.Dense(units=2, activation='softmax')
        ])

        #Adam or SGD Optimizer?
        #Maybe change the learnign rate?
        #Loss type, either categoricalCrossentropy or Binary binary_crossentropy
        #optim = keras.optimizers.SGD(learning_rate=0.1, momentum=0.9) #0.001
        #optim = tf.train.AdamOptimizer(learning_rate=0.01)
        #Creating some callbacks here to improve learning
        #'adam'
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy']) #tf.losses.CategoricalCrossentropy(from_logits=True 'binary_crossentropy',

    def train(self, train_data, eval_data):
        r_lr = tf.keras.callbacks.ReduceLROnPlateau(monitor='val_loss', factor=0.3, patience=5, min_lr=0.001)
        s_b_model = tf.keras.callbacks.ModelCheckpoint(filepath='tensorflow_model/checkpoints/', save_weights_only=False,
                                                       monitor='val_accuracy', mode='max', save_best_only=True)

        self.history = self.model.fit(
                train_data.repeat(),
                epochs=60, #120 is getting about 52% #200 get 50% #50 get 53-54%
                steps_per_epoch=100,
                validation_data=eval_data.repeat(),
                validation_steps=3,
                callbacks=[tensorboard_callback, s_b_model] #r_lr
        )

    def evaluate(self, x_data, y_labels):
        self.model = tf.keras.models.load_model('tensorflow_model/checkpoints/')
        return self.model.evaluate(x_data, y_labels)

        #self.model.load_weights('tensorflow_model/checkpoints/')
        #return self.model.evaluate(x_data, y_labels)

    def predict(self, data):
        self.model = tf.keras.models.load_model('../tensorflow_model/checkpoints/')
        #self.model.load_weights('tensorflow_model/checkpoints/')
        return self.model.predict(data)

    def preprocess(self, x, y):
        return tf.data.Dataset.from_tensor_slices((x, y)).shuffle(len(y)).batch(967) #500 batch for max

    def preprocess_unlabeled(self, x):
        return tf.data.Dataset.from_tensor_slices((x))

    def save(self):
        ## TODO: Write this function to save the model in tensorflow_model/tfmodel_checkpoint
        pass


#Borrowed from https://www.machinecurve.com/index.php/2020/11/03/how-to-evaluate-a-keras-model-with-model-evaluate/
def get_dataset_partitions(ds, ds_size, train_split=0.8, val_split=0.1, test_split=0.1, shuffle=True,
                                  shuffle_size=10000):
    assert (train_split + test_split + val_split) == 1

    if shuffle:
        # Specify seed to always have the same split distribution between runs
        ds = ds.shuffle(shuffle_size, seed=12)

    train_size = int(train_split * ds_size)
    val_size = int(val_split * ds_size)

    #print("SIZE:", len(list(ds)[0][1]))
    train_ds = [[],[]]
    val_ds = [[],[]]
    test_ds = [[],[]]


    for x,y in ds:
        print("ITER:", y, x)

        train_ds[0] = x[0:train_size]
        train_ds[1] = y[0:train_size]
        val_ds[0] = x[train_size:train_size+val_size]
        val_ds[1] = y[train_size:train_size+val_size]
        test_ds[0] = x[val_size:]
        test_ds[1] = y[val_size:]

        print("SIZEUUUU",len(train_ds[1]))

    return tf.data.Dataset.from_tensor_slices((train_ds[0], train_ds[1])).shuffle(len(train_ds[1])).batch(train_size), \
        tf.data.Dataset.from_tensor_slices((val_ds[0], val_ds[1])).shuffle(len(val_ds[1])).batch(val_size), \
        tf.data.Dataset.from_tensor_slices((test_ds[0], test_ds[1])).shuffle(len(test_ds[1])).batch(ds_size - (train_size + val_size))

    #train_ds = ds.take(train_size)
    #print([y for x, y in train_ds])
    #val_ds = ds.skip(train_size).take(val_size)
    #print([y for x, y in val_ds])
    #test_ds = ds.skip(train_size).skip(val_size)
    #print([y for x, y in test_ds])

    #return train_ds, val_ds, test_ds
