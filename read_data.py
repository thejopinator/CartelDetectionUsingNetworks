def load_data():
    # Importing the packages necessary
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import networkx as nx
    import itertools
    import matplotlib.colors as mcolors
    from pyvis.network import Network  
    # Import dataset from .csv file for project piso
    df = pd.read_csv('Network_Dataset.csv')
    # return the dataframe
    return df