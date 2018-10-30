#!/usr/bin/env python3

import numpy as np

class Perceptron(object):
    """Perceptron classifier.

    Parameters
    ------------
    eta : float
        Learning rate (between 0.0 and 1.0)
    n_iter : int
        Passes over the training dataset.

    Attributes
    -----------
    w_ : 1d-array
        Weights after fitting.
    errors_ : list
        Number of misclassifications (updates) in each epoch.

    """
    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, X, y):
        """Fit training data.

        Parameters
        ----------
        X : {array-like}, shape = [n_samples, n_features]
            Training vectors, where n_samples is the number of samples and
            n_features is the number of features.
        y : array-like, shape = [n_samples]
            Target values.

        Returns
        -------
        self : object

        """
        
        # TODO: Fit the perceptron classifier
        # BEGIN YOUR CODE
        
        
        
        # END YOUR CODE
        return self

    def net_input(self, X):
        """Calculate net input"""
                
        # TODO: Calculate the net input at this neuron
        # YOUR CODE HERE
        net_input = None
        # END YOUR CODE
        
        return net_input

    def predict(self, X):
        """Return class label after unit step"""
        # TODO: Predict the class label after activation
        # YOUR CODE HERE
        predictions = None
        # END YOUR CODE
        return predictions