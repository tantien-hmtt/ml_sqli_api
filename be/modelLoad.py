import tensorflow as tf
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence
import pickle

#######
max_words = 1000
max_len = 150
#####

model_path = './v2_lstm_model.h5'
weights_path = './v2_lstm_weights.h5'

with open('./tokenizer_config.pkl', 'rb') as config_file:
    tok = pickle.load(config_file)
try:
    loaded_model = tf.keras.models.load_model(model_path)
    loaded_model.load_weights(weights_path)
    print("Model loaded successfully.")
except Exception as e:
    print("Error loading the model:", str(e))



def predict_sqli_attack(input_val):
    
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
        return 1
    elif result <= 0.5:
        print("It seems to be a safe")
        return 0


