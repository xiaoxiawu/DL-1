Read Me

Copy data and examples into $CAFFE_ROOT

yearbook is the entire dataset

yearbook-reduced only contains photos from 1935 and 2009. This two class problem will be much easier to debug and train. Once we find hyperparameters that provide meaningful results, we can proceed to the larger dataset. 

Github is not allowing me to upload yearbook_train_lmdb and yearbook_val_lmdb for the full yearbook dataset because the files are too large.


---------- yearbook-reduced ---------- 

  caffe's loss function only works when class labels start at 0
  so I labelled photos from 1935 as 0 and photos from 2009 as 1
  
  create_yearbook.sh is based off of create_imagenet.sh from caffe/examples/imagenet
  compare these two files to see what changes were made
  
    cd $CAFFE_ROOT
    ./examples/yearbook-reduced/create_yearbook.sh

  This creates the lmdb files
  If this line does not work, you may need to set permissions for create_yearbook.sh
  
  lenet_solver.prototxt and lenet_train_test.prototxt are based off of the files of similar name in caffe/examples/mnist 
  compare these files to see what changes were made
  I reduced the batch sizes because my gpu's memory was maxing out
  
    cd $CAFFE-ROOT
    ./examples/yearbook-reduced/train_lenet.sh

  This should begin training of the network. Accuracy should be 0.5. If it is not, then there is bug in the code.
  
  
