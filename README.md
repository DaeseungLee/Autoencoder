# AutoEncoder
Autoencoder는 대표적인 Unsupervised Learning의 한 종류 입니다. AE의 기본적인 구조는 다음과 같습니다.

![image](https://user-images.githubusercontent.com/83156421/116395911-acd60a00-a85f-11eb-84ec-11c0c5a178bb.png)

위의 구조와 같이 오토인코더에서는 입력과 출력값이 같습니다. 지도 학습(Supervised Learning)에서는 입력값에 대하여 모델이 예측하기를 기대하는 정답 데이터가 존재하지만, 오토인코더는 정답이 없는 데이터 셋 만으로 학습할 수 있습니다. 예를 들어 28X28 크기의 MNIST image를 입력 값으로 넣을 때 output의 데이터 크기도 마찬가지로 28X28의 image입니다. Autoencoder 구조는 위의 그림에서 볼 수 있듯 입력된 데이터를 압축하는 Encoder와 입력값과 동일한 값을 출력하는 Decoder의 두 부분으로 나누어져 있습니다. input 데이터를 표현하는 hidden layer의 뉴런 수를 input layer보다 작게하여 데이터 압축의 효과를 얻을 수 있고, 각각의 뉴런들의 Layer의 특징들을 뽑아 낼 수 있습니다.

인코더와 디코더의 네트워크 모든 구조를 Neural network 로만 구성한다면 일반적인 DNN과 같습니다. 꼭 Neural network만 사용할 필요가 없고, CNN을 사용할 수도 있습니다. CNN에 대한 사용은 1번 예제 코드에 있습니다. 또한 Activation Function 없이 사용하는 Autoencoder는 Linear Autoencoder라고 부르고 있습니다. 이 Linear Autoencoder는 차원 압축에서 많이 사용되는 PCA와 같은 역할을 합니다. 오토인코더는 단순한 구조처럼 보이지만, 입력 데이터에 noise를 추가하고, 원본 입력이 출력되도록 하는 Denoising 효과도 가지고 있습니다. 이를 Denoising Autoencoder라고 합니다. 마찬가지로 1번 예제에서 MNIST 데이터에 Gaussian 분포의 Random noise를 더해주고 다시 원본을 출력하도록 만드는 모델을 학습시키는 코드가 있습니다. 이외에도 sparse 오토인코더, Variational Autoencoder 등이 있으며 다른 repo에서 다룰 예정입니다. 

![image](https://user-images.githubusercontent.com/83156421/116499216-99ba4d00-a8e6-11eb-91e6-068977cbb3bc.png)

위의 수식은 오토인코더의 Loss function 입니다. A와 B는 각각 오토인코더의 인코더와 디코더를 의미한다. 즉 오토인코더의 입력값으로 x값이 들어갈 때의 출력값 x_hat과 원본 x와의 차이를 가장 작게 만드는 A와 B를 찾는 것 입니다. 원본 데이터를 재구성하기 때문에 오토인코더의 Loss를 reconstruction loss라고 하며 보통 L2-norm을 사용한다고 합니다.

## Example code
### 1. Tensorflow2.0_autoencoder_tutorial_mnist
Tensorflow2.0 autoencoder를 그대로 구현하였습니다.

### 2. Stacked Autoencoders with classify fashoin MNIST data
autoencoder를 이용하여 classification model을 만들었습니다. Convolution Network나 다른 기법들(batch norm, drop out)등을 사용하지 않고도 97%의 정확도의 결과를 보일 수 있었습니다.
