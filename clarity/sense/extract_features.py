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
