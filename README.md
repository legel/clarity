# Clarity
Clarity is a [machine learning](https://en.wikipedia.org/wiki/Machine_learning) library for fast discovery and exploration of high dimensional data, including simple commands for the following:
  - [Extracting features from data](#extracting-key-features) - *e.g.* identifying key words in documents with [tf-idf](https://en.wikipedia.org/wiki/Tf%E2%80%93idf)
  - [Discovering models of features](#discovering-models) - *e.g.* learning deep representations with [word2vec](http://code.google.com/p/word2vec/)
  - [Visualizing models](#visualizing-models) - *e.g.* 3D embedding of high dimensional knowledge with [t-SNE](http://lvdmaaten.github.io/tsne/)

Clarity can help speed up the process of scientific discovery, and visualize artificial intelligence harvested from data, including for virtual and augmented reality.

##### Installation
```sh
$ pip install clarity
```
### Extracting Key Features
Consider the following example code from ```extract_features.py```:
```python
import clarity
# structure input data as a list called 'observations'
observations = [
  'A document about epistemology ...', 
  'A document about particle physics ...', 
  'A document about quantum physics ...', 
  'A document about cats ...', 
  'A document about dogs ...'
  ]
# load input data into a clarity object
truth = clarity.sense(observations)
# parse input data to extract key features
truth.focus()
print truth
```
Running this example produces the following output:
```sh
$ python extract_features.py
['epistemology', 'particle physics', 'quantum physics', 'cats', 'dogs']
```
Intuitively, we can see that Clarity got rid of useless information (```A document about``` and ```...```) in the data it was provided.

Let's see how.  At the top of ```extract_features.py``` we make a list of ```observations```, pass it to ```clarity.sense()``` to construct an object called ```truth```, through which we ```focus()```.  This function attempts to automatically identify the features that best distinguish each observation.

Under the hood, when Clarity runs ```focus()```, it constructs a sparse normalized *N* x *F* matrix, where *N* is number of observations and *F* is number of features.  Such a matrix is often useful for machine learning in general, and one can extract it by calling ```truth.matrix```.

##### Non-Parametric Heuristics
Remarkably, ```focus()``` can function non-parametrically, with no human input.  This is because Clarity probabilistically infers how best to consider and concentrate on any type of data.  For the example above, Clarity will recognize that all data observations are natural language, and then it will extract words from the language, and process them with [tf-idf](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) so it can filter out words that are too frequent.

Depending on the size and entropy of the data, ```focus()``` without user-specified parameters could indeed take more than a few moments.  If Clarity does not identify an algorithm likely to correctly extract features, then it will politely suggest that you try to do so.

##### Parameterization
We can manually define feature extraction algorithms and parameters that are known to be best for any of our particular cases, either by separately pre-processing the data before inserting into ```clarity.sense()```, or by providing arguments to ```focus()```.  ...

### Discovering Models
...

### Visualizing Models
...

### License
[MIT](http://opensource.org/licenses/MIT)
