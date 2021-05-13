# AutoEncoder  
Autoencoder에 대한 자세한 설명은 [Autoencdoer 설명글](https://ehfkswl.tistory.com/2?category=982698) 을 통해 확인하실 수 있습니다.

## Example code
### 1. Tensorflow2.0_Autoencoder_tutorial_mnist
Tensorflow2.0 autoencoder를 그대로 구현하였습니다.

- Fashion mnist 데이타를 Autoencoder에 학습 시킨 후, reconsturction한 데이터. 원본 이지미와 비슷하지만 다소 blur한 결과를 보여줍니다.  

![image](https://user-images.githubusercontent.com/83156421/116504032-6da4c900-a8f2-11eb-94ca-b3b08be93abb.png)

- Denoising Autoencoder의 noise 제거 결과입니다. noise 제거가 꽤 잘됐지만, 마찬가지로 원본이지미에 비해 blur합니다.  

![image](https://user-images.githubusercontent.com/83156421/116503964-45b56580-a8f2-11eb-95df-9da044768141.png)

### 2. Stacked Autoencoders with classify fashoin MNIST data
autoencoder를 이용하여 classification model을 만들었습니다. Convolution Network나 다른 기법들(batch norm, drop out)등을 사용하지 않고도 ***97%의 정확도***의 결과를 보일 수 있었습니다. Reconstruction한 결과는 다음과 같습니다.

![image](https://user-images.githubusercontent.com/83156421/116974487-2d31ba80-acf9-11eb-910e-b32db1539fd9.png)

기존의 이미지보다 Noise가 좀 더 있는 상태인데 classification Layer로 부터의 gradinet가 반영되서 기존 Autoencoder만 사용할 때 보다 원본 이미지의 복원 성능이 떨어졌습니다.



