# Clarity
Clarity is an open source library for intuitive visual exploration of complex data sets.  Driven by state-of-the-art algorithms from machine learning and statistics, Clarity provides a minimalist set of commands for the following use cases:
  - **Extracting key features from input data** - *e.g.* natural language processing to identify important words in a set of documents
  - **Discovering models of key features** - *e.g.* learning a 3D embedding that spatially represents clusters of similar documents
  - **Visualizing knowledge inside models** - *e.g.* dynamic rendering of a high-dimensional knowledge graph discovered from associations of important words

Together this opens up big data sets for intuitive discovery and exploration, with a particular emphasis on applications for virtual and augmented reality.

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
  'A document about astrophysics...', 
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
$ ['epistemology', 'particle physics', 'astrophysics', 'cats', 'dogs']
```
Intuitively, we can see that Clarity got rid of all the extra words in the data set it was originally provided.  We didn't have to provide it any guidance on how to do this, it figures it out on its own.  We will learn how it does this in the section on [*Non-Parametric Heuristics*](#heuristics).  If we know enough about our data and methods for parsing it, we can manually specify algorithms and parameters as arguments to ```focus()``` as seen in the section on [*Parameterization*](#parameterization).

In any case, the first step toward clarity is sensing data and focusing on its features.  The data may be of any type, so long as all instances of it are combined into a single list, and introduced as an argument to ```sense()```.  Clarity will construct an object and identify it as ```truth```.  By calling ```focus()``` on ```truth```, Clarity will seek to extract the features in each observation that may best explain it, and then it will update ```truth``` so that its core is a *N* x *F* matrix, where *N* is number of observations and *F* is number of features.

If readers are satisfied by the above discussion of feature extraction, they may wish to skip forward for now to the next section on [*Discovering Models*](#discovering-models).

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
