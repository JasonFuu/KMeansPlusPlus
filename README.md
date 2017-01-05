# KMeansPlusPlus
Python K-means++ implementation
## About
This implementation is more for my own purposes and to get a better idea of how K-Means++/K-Means work
## Requirements
* Python 3.x
* Numpy
* Matplotlib (optional, to run Testing.py and graph results)

## Usage
The constructor takes in two arguments, ```points_list``` and ```k```:
* ```points_list```: 2d list containing n-dimensional points

  points_list = [[Point1], [Point2], etc.]; n-dimensional point x = [X1, X2, ..., Xn]
* ```k```: Number of desired clusters/centroids

Calling ```final_centroids``` after creating the object returns the final centroids in the same format as ```points_list```

## Example

Seeds from randomly generated data, x∈[0, 100], y∈[0, 50], n = 50, k = 7:
![alt text](https://github.com/JasonFuu/KMeansPlusPlus/blob/master/Screenshots/figure_1-1.png)

## Notes
Testing.py is used to create the screenshots, but is not necessary to run K-Means++
