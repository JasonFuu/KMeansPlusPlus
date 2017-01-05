import matplotlib.pyplot as plt
import random
from KMeansPlus import K_Means_Plus_Plus

"""Tests K-means++ with 50 randomly generated 2-var data points in various ranges"""
def KMeansPlusPlus_Test():
    points = []
    xs = []
    ys = []

    for a in range(50):
        a = 100*random.random()
        b = 50*random.random()
        xs.append(a)
        ys.append(b)
        points.append([a, b])

    test = K_Means_Plus_Plus(points, 7)

    centroidx = []
    centroidy = []

    for points in test.final_centroids():
        centroidx.append(points[0])
        centroidy.append(points[1])

    plt.scatter(xs, ys, color = 'black')
    plt.scatter(centroidx, centroidy, color = 'red')

    plt.show()
    print(test.final_centroids())
