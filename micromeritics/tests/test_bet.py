import numpy as np
import unittest
from micromeritics import util
from micromeritics import bet

class TestBET(unittest.TestCase):
    def test_bet(self):

        # Carbon black reference material isotherm (N2 at 77K)
        Qads = np.array([4.39005, 4.67017, 4.79068, 4.9767, 5.14414, 5.31144,
                         5.47106, 5.63297, 5.80559, 5.96663, 6.13574, 6.31214,
                         6.49764, 6.67154, 6.85255, 7.04053, 7.22571, 7.40778,
                         7.59634, 7.7832, 7.96568, 8.1623, 8.34863, 8.54383,
                         8.74695, 8.94871, 9.16214, 9.38208, 9.61289, 9.8577,
                         10.12, 10.397, 10.6852, 11.0089, 11.3574, 11.7373,
                         12.1611, 12.6289, 13.1794, 13.819, 14.57, 15.4858,
                         16.6535, 18.2409])

        Prel = np.array([0.0433547, 0.0672921, 0.0796994, 0.0999331, 0.119912,
                         0.140374, 0.159884, 0.179697, 0.200356, 0.219646,
                         0.239691, 0.259671, 0.280475, 0.299907, 0.320048,
                         0.340746, 0.360882, 0.380708, 0.400956, 0.421168,
                         0.440603, 0.460924, 0.480902, 0.500572, 0.521144,
                         0.540715, 0.560852, 0.580887, 0.600803, 0.62089,
                         0.64084, 0.66093, 0.68071, 0.70082, 0.72096, 0.74084,
                         0.76081, 0.78045, 0.80084, 0.82107, 0.84075, 0.86069,
                         0.88041, 0.90023])

        pmin = 0.05
        pmax = 0.3
        r = bet.bet(Prel, Qads, Pmin = pmin, Pmax = pmax, csa=0.162)
        np.testing.assert_almost_equal( r.sa, 20.7049, 3 )
        np.testing.assert_almost_equal( r.sa_err, 0.0289, 4 )
        np.testing.assert_almost_equal( r.C, 149.959660, 2 )
        np.testing.assert_almost_equal( r.q_m, 4.7569, 4 )

        Pfit, Qfit = util.restrict_isotherm(Prel,Qads,pmin,pmax)
        roq = bet.Isotherm2RoquerolBET(Pfit,Qfit ) 
        np.testing.assert_almost_equal( roq[0], 4.3559, 4 )
        np.testing.assert_almost_equal( roq[6], 4.62074, 4 )

if __name__ == '__main__':
    unittest.main()
