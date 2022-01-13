import gensim
from vncorenlp import VnCoreNLP
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential, load_model

"""Initialize

"""

model_name = "baomoi.vn.model.bin"
w2v = gensim.models.KeyedVectors.load_word2vec_format(model_name, binary= True)
# w2v_weights = w2v.vectors
# vocab_size, embedding_size = w2v_weights.shape
rdrsegmenter = VnCoreNLP("vncorenlp/VnCoreNLP-1.1.1.jar", annotators="wseg", max_heap_size='-Xmx500m')

LSTM_model = load_model("models/LSTM_model.save")

MAX_LENGTH = 500
number_topic = 12

def seq2tokens(seq):
    tokens = []
    for word in seq:
        if (word in w2v.wv.vocab):
            tokens.append(w2v.wv.vocab[word].index)
    return tokens

def process(sample):     
    sample = rdrsegmenter.tokenize(sample)  
    sample = ' '.join([' '.join(sent) for sent in sample])
    sample = gensim.utils.simple_preprocess(sample)
    sample = seq2tokens(sample)
    sample = pad_sequences([sample],maxlen=MAX_LENGTH).tolist()
    return sample[0]

def classify(text):
    vector = process(text)
    topic = LSTM_model.predict([vector])
    return topic[0].argmax(-1)


