# Clarity
Clarity is a library for quickly and intuitively exploring complex data.  Driven by state-of-the-art machine learning and statistics, Clarity provides simple commands for the following:
  - **Extracting key features from input data** - *e.g.* natural language processing to identify important words in a set of documents
  - **Discovering models of key features** - *e.g.* learning a low-dimensional representation of document characteristics
  - **Visualizing knowledge inside models** - *e.g.* 3D exploration of knowledge in documents

Clarity is built on a philosophy of minimalism, including internal application of heuristics to help speed up the process of scientific discovery for everyone.  This library has been developed with special interest in supporting intelligence visualization in virtual and augmented reality, including a forthcoming application to a 3D Wikipedia.

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
  'A document about epistemology...', 
  'A document about particle physics...', 
  'A document about quantum physics...', 
  'A document about cats...', 
  'A document about dogs...'
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
Intuitively, we can see that Clarity got rid of all the extra words (*'A document about'* and *'...'*) in the data set it was originally provided.

Let's see how.  At the top we make a list of ```observations```, which may be of any data type, and pass it to ```clarity.sense()```.  From this, Clarity will construct an object called ```truth```.  With ```truth``` we can ```focus()``` to automatically extract features in each observation that may best explain it.

Under the hood, when Clarity runs ```focus()```, it constructs a sparse normalized *N* x *F* matrix, where *N* is number of observations and *F* is number of features.  Such a matrix is often useful for machine learning in general, and one can extract it by calling ```truth.matrix```.

Readers satisfied so far with this idea of feature extraction may wish to skip to [*Discovering Models*](#discovering-models), to see how these features are applied.  They can learn more about [*Non-Parametric Heuristics*](#heuristics) and [*Parameterization*](#parameterization) for feature extraction in the following sections.

##### Non-Parametric Heuristics
Remarkably, ```focus()``` can function non-parametrically, without any guidance from humans.  This is because Clarity's englightenment engineers have developed A.I. that can automatically infer how best to consider and concentrate on any type of data, following clues like data structures and distributions.  For the example above, Clarity will recognize that all data observations are natural language, and it will extract key words from the language with a fast algorithm like [TF-IDF](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) to extract from each string the words that best characterize it.

Depending on the complexity of the data, ```focus()``` without user-specified parameters could indeed take more than a few moments - possibly minutes to hours.  Further, to avoid undermining its purpose, Clarity will not attempt to execute any algorithm for feature extraction if it does not identify one that is appropriate.

##### Parameterization
Finally, enlightment engineers can easily specify the feature extraction algorithms and parameters that are known to be best for their case, following documentation for "advanced users".  We encourage anyone with strong domain and/or computational expertise to pursue this approach, since this intuition is still likely to be better than that of our general artificial intelligence.

### Discovering Models
...

### Visualizing Knowledge
...

### License
[MIT](http://opensource.org/licenses/MIT)
