#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

# Make sure that caffe is on the python path:
caffe_root = '/Users/Bob/caffe/'  # this file is expected to be in {caffe_root}/examples
import sys
sys.path.insert(0, caffe_root + 'python')

import caffe

plt.rcParams['figure.figsize'] = (10, 10)
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'gray'

#import os
# if not os.path.isfile(caffe_root + 'examples/yearbook models/yearbook_alexnet_train_iter_2567.caffemodel'):
#     print("Downloading pre-trained CaffeNet model...")
#     !../Users/Bob/caffe/scripts/download_model_binary.py /Users/Bob/caffe/models/bvlc_reference_caffenet

caffe.set_mode_cpu()

model_def = caffe_root + 'examples/yearbook/deploy.prototxt'
model_weights = caffe_root + 'examples/yearbook/yearbook_alexnet_train_iter_2567.caffemodel'
binary_proto_mean = caffe_root + 'data/yearbook/yearbook_mean.binaryproto'

blob = caffe.proto.caffe_pb2.BlobProto()
data = open( binary_proto_mean  , 'rb' ).read()
blob.ParseFromString(data)
mean_arr = np.array( caffe.io.blobproto_to_array(blob) )[0]

net = caffe.Net(model_def,      # defines the structure of the model
                model_weights,  # contains the trained weights
                caffe.TEST)     # use test mode (e.g., don't perform dropout)

# # load the mean ImageNet image (as distributed with Caffe) for subtraction
# mu = np.load(caffe_root + 'python/caffe/imagenet/ilsvrc_2012_mean.npy')
mu = mean_arr.mean(1).mean(1)  # average over pixels to obtain the mean (BGR) pixel values
# print 'mean-subtracted values:', zip('BGR', mu)

# # create transformer for the input called 'data'
transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})

transformer.set_transpose('data', (2,1,0))  # move image channels to outermost dimension
transformer.set_mean('data', mu)            # subtract the dataset-mean value in each channel
transformer.set_raw_scale('data', 255)      # rescale from [0, 1] to [0, 255]
#transformer.set_channel_swap('data', (2,1,0))  # swap channels from RGB to BGR

# set the size of the input (we can skip this if we're happy
#  with the default; we can also change it later, e.g., for different batch sizes)
net.blobs['data'].reshape(1,        # batch size
                          3,         # 3-channel (BGR) images
                          227, 227)  # image size is 227x227

def evaluate(im_dir):
	image = caffe.io.load_image(im_dir)
                                #caffe_root + 'data/yearbook/' + im_dir
	transformed_image = transformer.preprocess('data', image)
	plt.imshow(image)

	# copy the image data into the memory allocated for the net
	net.blobs['data'].data[...] = transformed_image

	### perform classification
	output = net.forward()

	output_prob = output['prob'][0]  # the output probability vector for the first image in the batch

	year = output_prob.argmax()+ 1905
	return year

def main():
	im_dir = '/Users/Bob/caffe/CS395T/CS395T/data/yearbook/M/1983_Massachusetts_Plymouth_Plymouth-Carver_37-4.png'
	year = evaluate(im_dir)
	print 'predicted class is:', year
if __name__ == "__main__":main()













