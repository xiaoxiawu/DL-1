# This is an ugly hack to use util.py in the src folder. DO NOT COPY THIS, BUT
# RATHER PUT ALL YOUR CODE IN src FOLDER!!
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'src'))
# END OF UGLY HACK

from util import *
import classification
from classification import evaluate

THIS_DIRECTORY = path.dirname(path.abspath(__file__))

class Predictor:
  DATASET_TYPE = 'yearbook'
  def predict(self, image_path):
  	year = evaluate(image_path)
    	return year

