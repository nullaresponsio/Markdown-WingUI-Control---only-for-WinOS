import os
import inspect
import graphviz

# Directory of the graphviz Python package
print(os.path.dirname(graphviz.__file__))

# File in which Digraph is implemented
print(inspect.getsourcefile(graphviz.Digraph))

# Current working directory (where retrieval_attention.png is generated)
print(os.getcwd())
