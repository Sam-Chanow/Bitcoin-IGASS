import tensorflow as tf
from tensorflow import keras
from datetime import datetime
from packaging import version

logdir = "" + datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_callback = keras.callbacks.TensorBoard(log_dir=logdir)


class TFModel:
    def __init__(self):
        self.model = keras.Sequential([
            keras.layers.Reshape(target_shape=(768,), input_shape=(768,)),
            keras.layers.Dense(units=500, activation='tanh'),
            #keras.layers.Dense(units=192, activation='relu'),
            #keras.layers.Dense(units=128, activation='relu'),
            keras.layers.Dense(units=2, activation='softmax')
        ])

        self.model.compile(optimizer='adam', loss=tf.losses.CategoricalCrossentropy(from_logits=True), metrics=['accuracy'])

    def train(self, train_data, eval_data):
        self.history = self.model.fit(
                train_data.repeat(),
                epochs=200,
                steps_per_epoch=500,
                validation_data=eval_data.repeat(),
                validation_steps=3,
                callbacks=[tensorboard_callback]
        )

    def evaluate(self, data):
        return self.model.predict(data)

    def preprocess(self, x, y):
        return tf.data.Dataset.from_tensor_slices((x, y)).shuffle(len(y)).batch(500)

    def save(self):
        ## TODO: Write this function to save the model in tensorflow_model/tfmodel_checkpoint
        pass
