# Clarity
Clarity is a library for quickly and intuitively exploring complex data.  Driven by [machine learning](https://en.wikipedia.org/wiki/Machine_learning) it provides simple commands for the following:
  - **Extracting features from data** - *e.g.* identifying key words in documents
  - **Discovering models of features** - *e.g.* learning deep representations from [word2vec](http://code.google.com/p/word2vec/)
  - **Visualizing knowledge in models** - *e.g.* exploring connectivity across documents in 3D

Clarity can help speed up the process of scientific discovery, and support visualization of intelligence harvested from data, especially for virtual and augmented reality.

### Installation
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

Let's see how.  At the top of ```extract_features.py``` we make a list of ```observations```, which may be of any data type. We pass it to ```clarity.sense()``` to construct an object called ```truth```, from which we can ```focus()```.  This function will attempt to automatically identify and focus on the features that best distinguish each observation.

Readers satisfied so far with this idea of feature extraction may wish to skip to [*Discovering Models*](#discovering-models), to see how these features are applied.  They can learn more about [*Non-Parametric Heuristics*](#heuristics) and [*Parameterization*](#parameterization) for feature extraction in the following sections.

Under the hood, when Clarity runs ```focus()```, it constructs a sparse normalized *N* x *F* matrix, where *N* is number of observations and *F* is number of features.  Such a matrix is often useful for machine learning in general, and one can extract it by calling ```truth.matrix```.

##### Non-Parametric Heuristics
Remarkably, ```focus()``` can function non-parametrically, and thus with minimal input.  This is because Clarity's englightenment engineers have developed A.I. that can automatically infer how best to consider and concentrate on any type of data.  For the example above, Clarity will recognize that all data observations are natural language, and it will extract key words from the language with a fast algorithm like [TF-IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf), and then filter words with a low weight returned by that algorithm.

Depending on the complexity of the data, ```focus()``` without user-specified parameters could indeed take more than a few moments - possibly minutes to hours.  Further, to avoid undermining its purpose, Clarity will not attempt to execute any algorithm for feature extraction if it does not identify one that is appropriate.

##### Parameterization
Finally, enlightment engineers can easily specify the feature extraction algorithms and parameters that are known to be best for their case, following documentation for "advanced users".  We encourage anyone with strong domain and/or computational expertise to pursue this approach, since this intuition is still likely to be better than that of our general artificial intelligence.

### Discovering Models
...

### Visualizing Knowledge
...

### License
[MIT](http://opensource.org/licenses/MIT)
