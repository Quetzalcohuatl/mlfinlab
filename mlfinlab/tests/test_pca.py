"""
Test PCA for Statistical Arbitrage module.
"""

import unittest
import os
import pandas as pd
import numpy as np

from mlfinlab.statistical_arbitrage import calc_pca


class TestPCA(unittest.TestCase):
    """
    Test PCA.
    """

    def setUp(self):
        """
        Sets the file path for the tick data csv.
        """
        # Set project path to current directory.
        project_path = os.path.dirname(__file__)
        # Add new data path to match stock_prices.csv data.
        data_path = project_path + '/test_data/stock_prices.csv'
        # Read csv, parse dates, and drop NaN.
        self.data = pd.read_csv(data_path, parse_dates=True, index_col="Date").dropna(axis=1)

    def test_calc_pca(self):
        """
        Test PCA calculation.
        """
        # Calculate PCA for given data with 1 principal component.
        res = calc_pca(np.log(self.data), 1)

        # There are two items in the tuple.
        self.assertEqual(len(res), 2)

        # Length of projection is the same as data.
        self.assertEqual(len(res[0]), 2141)

        # Check some values for projection.
        self.assertAlmostEqual(res[0][5][0], -3.719554, delta=1e-3)
        self.assertAlmostEqual(res[0][100][0], -3.56338343, delta=1e-3)
        self.assertAlmostEqual(res[0][1000][0], 2.6786415, delta=1e-3)

        # Check the length of the second output.
        self.assertEqual(len(res[1]), 23)

        # Check some values for the first principal component.
        self.assertAlmostEqual(res[1][4][0], -0.24159355, delta=1e-3)
        self.assertAlmostEqual(res[1][9][0], -0.233308519, delta=1e-3)
        self.assertAlmostEqual(res[1][22][0], -0.2389528258, delta=1e-3)
