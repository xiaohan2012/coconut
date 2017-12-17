# coconut

Construct graph from co-occurence data (like tags)

# usage

find `main.py` and modify the paths

## input data format

`,`-separated csv file:


    9713,"machine-learning,r,predictive-modeling,random-forest,accuracy"
    9715,"machine-learning,neural-network,online-learning"
    9719,"machine-learning,consumerweb"

## output data format

`networkx.Graph`