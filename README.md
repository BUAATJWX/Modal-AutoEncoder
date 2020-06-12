# Modal Autoencoder 

The project proposed a new modal autoencoder with novel regularization method. Other traditional autoencoders come from the [github](https://github.com/fdavidcl/ae-review-resources).
Autoencoders are symmetrical neural networks trained to reconstruct their inputs onto their outputs, with some restrictions that force them to find meaningful codifications of data.

## Hardware
- python3.7
- [TensorFlow 2.0](https://www.tensorflow.org/)
- [Keras](https://github.com/keras-team/keras)
## Contents
- `autoencoder.py` defines an `Autoencoder` class which describes the model that will be learned out of the data.
* * Traditional Autenoders : Basci autoencoder(BAE), [Sparse autoencoder](https://pdfs.semanticscholar.org/eb2f/e260af00818907fe82024203d8a5a1386777.pdf)(SAE), [Contractive autoencoder*](https://dl.acm.org/citation.cfm?id=3104587)(CAE),
[Denoising autoencoder](https://dl.acm.org/citation.cfm?id=1390294)(DAE) and so on.
* * Modal autoencoder: Mode decomposition method combines with BAE to generate new MAE, with DAE to generate MDAE, with CAE to generate MCAE,  with SAE to generate MSAE and so on.
- `utils.py` defines additional functionality needed the sparse, contractive, denoising and robust autoencoders, and new loss function and weight update algorithm.
- `mnist.py` includes the training process for autoencoders with MNIST data.


## License

The code in this repository is licensed under MAEv1.0, which allows you to redistribute and use it in your own work.