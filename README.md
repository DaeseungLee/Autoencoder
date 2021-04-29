# AutoEncoder
Autoencoder는 대표적인 Unsupervised Learning의 한 종류 입니다. AE의 기본적인 구조는 다음과 같습니다.

![image](https://user-images.githubusercontent.com/83156421/116395911-acd60a00-a85f-11eb-84ec-11c0c5a178bb.png)

위의 구조와 같이 오토인코더에서는 입력과 출력값이 같습니다. 지도 학습(Supervised Learning)에서는 입력값에 대하여 모델이 예측하기를 기대하는 정답 데이터가 존재하지만, 오토인코더는 정답이 없는 데이터 셋 만으로 학습할 수 있습니다. 예를 들어 28X28 크기의 MNIST image를 입력 값으로 넣을 때 output의 데이터 크기도 마찬가지로 28X28의 image입니다. Autoencoder 구조는 위의 그림에서 볼 수 있듯 입력된 데이터를 압축하는 Encoder와 입력값과 동일한 값을 출력하는 Decoder의 두 부분으로 나누어져 있습니다. input 데이터를 표현하는 hidden layer의 뉴런 수를 input layer보다 작게하여 데이터 압축의 효과를 얻을 수 있고, 각각의 뉴런들의 Layer의 특징들을 뽑아 낼 수 있습니다.


### 1. Tensorflow2.0_autoencoder_tutorial_mnist
Tensorflow2.0 autoencoder를 그대로 구현하였습니다.

### 2. Stacked Autoencoders with classify fashoin MNIST data
autoencoder를 이용하여 classification model을 만들었습니다. Convolution Network나 다른 기법들(batch norm, drop out)등을 사용하지 않고도 97%의 정확도의 결과를 보일 수 있었습니다.
