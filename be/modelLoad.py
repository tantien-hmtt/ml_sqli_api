import tensorflow as tf
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence

model_path = '../v2_lstm_model.h5'
weights_path = '../v2_lstm_weights.h5'

try:
    loaded_model = tf.keras.models.load_model(model_path)
    loaded_model.load_weights(weights_path)
    print("Model loaded successfully.")
except Exception as e:
    print("Error loading the model:", str(e))

#######
max_words = 1000
max_len = 150
tok = Tokenizer(num_words=max_words)    
#######

# def clean_data(input_val):

#     txts = tok.texts_to_sequences(input_val)
#     input_val = sequence.pad_sequences(txts, maxlen=max_len)

#     return input_val


def predict_sqli_attack():

    input_val = "example.com/api/user?admin or 1=1"
    print(input_val)
    sample_texts_list = []
    sample_texts_list.append(input_val)
    txts = tok.texts_to_sequences(sample_texts_list)
    txts = sequence.pad_sequences(txts, maxlen=max_len)
    print("texts: " + str(txts))
    result=loaded_model.predict(txts)
    print(result)
    if result > 0.5:
        print("ALERT! This can be SQL injection")
    elif result <= 0.5:
        print("It seems to be a benign")

predict_sqli_attack()
