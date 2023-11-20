import os
import tensorflow as tf
import pandas as pd
from keras.models import Model, load_model
from keras import preprocessing

# 데이터 읽어오기
cwd = os.getcwd()
train_file = os.path.join(cwd, "book_ex", "ch6", "chatbot_data.csv")
data = pd.read_csv(train_file, delimiter=',')   # delimiter : 구분자
features = data['Q'].tolist()   # 'Q' 열만 리스트로 정리?
labels = data['label'].tolist() # 'label' 열만 리스트로 정리?

# 단어 인덱스 시퀀스 벡터
corpus = [preprocessing.text.text_to_word_sequence(text) for text in features]  # corpus : 코퍼스, 말뭉치
tokenizer = preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(corpus)
sequences = tokenizer.texts_to_sequences(corpus)

MAX_SEQ_LEN = 15    # 단어 시퀀스 벡터 크기
padded_seqs = preprocessing.sequence.pad_sequences(sequences, maxlen=MAX_SEQ_LEN, padding='post')

# 테스트용 데이터셋 생성
ds = tf.data.Dataset.from_tensor_slices((padded_seqs, labels))
ds = ds.shuffle(len(features))
test_ds = ds.take(2000).batch(20)   # 테스트 데이터셋

# 감정 분류 CNN 모델 불러오기
model = load_model(os.path.join(cwd, "book_ex", "ch6", 'cnn_model.h5'))
model.summary()
model.evaluate(test_ds, verbose=2)

# 테스트용 데이터셋의 10212번째 데이터 출력
print("단어 시퀀스 : ", corpus[10212])
print("단어 인덱스 시퀀스 : ", padded_seqs[10212])
print("문장 분류(정답) : ", labels[10212])

# 테스트용 데이터셋의 10212번째 데이터 감정 예측
picks = [10212]
predict = model.predict(padded_seqs[picks])
predict_class = tf.math.argmax(predict, axis=1)
print("감정 예측 점수 : ", predict)
print("감정 예측 클래스 : ", predict_class.numpy())
