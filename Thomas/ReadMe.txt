Read Me

Copy data and examples into $CAFFE_ROOT

yearbook is the entire dataset

yearbook-reduced only contains photos from 1935 and 2009. This two class problem will be much easier to debug and train. Once we find hyperparameters that provide meaningful results, we can proceed to the larger dataset. 

create_yearbook.sh is based off of create_imagenet.sh from caffe/examples/imagenet

lenet_solver.prototxt and lenet_train_test.prototxt are based off of the files of similar name in caffe/examples/mnist 

I reduced the batch sizes because my gpu's memory was maxing out

Github is not allowing me to upload yearbook_train_lmdb and yearbook_val_lmdb for the full yearbook dataset because the files are too large.


