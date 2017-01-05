"""K-Means++ class made for multiple parameters. Returns k initial seeds to be used in Equal_Cluster_K_Means"""
import numpy as np
import random
import math

class K_Means_Plus_Plus:

    """Input is a 2D list of n-dimensional points"""
    def __init__(self, points_list, k):
        self.centroid_count = 0
        self.point_count = len(points_list)
        self.cluster_count = k
        self.points_list = list(points_list)
        self.initialize_random_centroid()
        self.initialize_other_centroids()

    """Picks a random point to serve as the first centroid"""
    def initialize_random_centroid(self):
        self.centroid_list = []
        index = random.randint(0, len(self.points_list)-1)

        self.centroid_list.append(self.remove_point(index))
        self.centroid_count = 1

    """Removes point associated with given index so it cannot be picked as a future centroid.
    Returns list containing coordinates of newly removed centroid"""
    def remove_point(self, index):
        new_centroid = self.points_list[index]
        del self.points_list[index]

        return new_centroid

    """Finds the other k-1 centroids from the remaining lists of points"""
    def initialize_other_centroids(self):
        while not self.is_finished():
            distances = self.find_smallest_distances()
            chosen_index = self.choose_weighted(distances)
            self.centroid_list.append(self.remove_point(chosen_index))
            self.centroid_count += 1


    """Calculates distance from each point to its nearest cluster center. Then chooses new
    center based on the weighted probability of these distances"""
    def find_smallest_distances(self):
        distance_list = []

        for point in self.points_list:
            distance_list.append(self.find_nearest_centroid(point))

        return distance_list

    """Finds centroid nearest to the given point, and returns its distance"""
    def find_nearest_centroid(self, point):
        min_distance = math.inf

        for values in self.centroid_list:
            distance = self.euclidean_distance(values, point)
            if distance < min_distance:
                min_distance = distance

        return min_distance

    """Chooses an index based on weighted probability"""
    def choose_weighted(self, distance_list):
        distance_list = [x**2 for x in distance_list]
        weighted_list = self.weight_values(distance_list)
        indices = [i for i in range(len(distance_list))]
        return np.random.choice(indices, p = weighted_list)

    """Weights values from [0,1]"""
    def weight_values(self, list):
        sum = np.sum(list)
        return [x/sum for x in list]

    """computes N-d euclidean distance between two points represented as lists:
     (x1, x2, ..., xn) and (y1, y2, ..., yn)"""
    def euclidean_distance(self, point1, point2):
        point1 = np.asarray(point1)
        point2 = np.asarray(point2)

        return np.linalg.norm(point2-point1)

    """Checks to see if final condition has been satisfied (when K centroids have been created)"""
    def is_finished(self):
        outcome = False
        if self.centroid_count == self.cluster_count:
            outcome = True

        return outcome

    """Returns final centroid values"""
    def final_centroids(self):
        return self.centroid_list

