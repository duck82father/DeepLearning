# 순차형 모델(sequential model) 예시
# 필요한 모듈 임포트 (1)
import tensorflow as tf
import matplotlib.pyplot as plt
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Flatten, Dense

# MNIST 데이터셋 가져오기 (2)
# 255.0 으로 나누는 이유는, 흑백이미지의 명도값(8bit : 0~255)을
# 모두 0~1 사이의 값으로 정규화 하기 위해
(X_train, y_train), (X_test, y_test) = mnist.load_data()
X_train, X_test = X_train / 255.0, X_test / 255.0   # 데이터 정규화

# tf.data를 사용하여 데이터 셋을 섞고 배치 만들기 (3)
ds = tf.data.Dataset.from_tensor_slices((X_train, y_train)).shuffle(10000)
train_size = int(len(X_train) * 0.7)    # 학습셋:검증셋 = 7:3
train_ds = ds.take(train_size).batch(20)
val_ds = ds.skip(train_size).batch(20)

# MNIST 분류 모델 구성 (4) - p.153
model = Sequential()
model.add(Flatten(input_shape=(28,28)))
model.add(Dense(20, activation='relu'))
model.add(Dense(20, activation='relu'))
model.add(Dense(10, activation='softmax'))

# 모델 생성
# 다중 클래스 분류 문제를 해결하는 신경망 출력층의 활성화 함수 : softmax
# 손실 함수 : sparse_categorical_crossentropy
model.compile(loss='sparse_categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

# 모델 학습
hist = model.fit(train_ds, validation_data=val_ds, epochs=10)

# 모델 평가 (evaluate)
print('모델 평가')
model.evaluate(X_test, y_test)

# 모델 정보 출력
model.summary()

# 모델 저장
model.save('mnist_model.h5')

# 학습 결과 그래프 그리기
fig, loss_ax = plt.subplots()
acc_ax = loss_ax.twinx()

loss_ax.plot(hist.history['loss'], 'y', label='train loss')
loss_ax.plot(hist.history['val_loss'], 'r', label='val loss')

acc_ax.plot(hist.history['accuracy'], 'b', label='train acc')
acc_ax.plot(hist.history['val_accuracy'], 'g', label='val acc')

loss_ax.set_xlabel('epoch : study counts')
loss_ax.set_ylabel('loss')
acc_ax.set_ylabel('accuracy')

loss_ax.legend(loc='upper left')
acc_ax.legend(loc='lower left')
plt.show()