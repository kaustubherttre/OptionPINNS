#Add tests here
#import module
import sys
sys.path.insert(0, '../../src/Vanilla/')
from  BSNumerical import BSNumerical
from BSAnalytical import BSAnalyticalRange
import matplotlib.pyplot as plt

if __name__ == '__main__':
    model_Numerical = BSNumerical(0,20,10,1,0.2,0.25, 170, 1700)
    model_Analytical = BSAnalyticalRange(0,20,10,0.2,1, 0.25, 170)
    plt.plot(model_Numerical.matrix[:,1], label = 't = T at BSNumerical')
    plt.plot(model_Analytical.prices, label = 't = T at BSAnalytical')
    plt.legend()
    plt.show()
    plt.plot(model_Numerical.matrix[1:,1] - model_Analytical.prices)
    plt.legend()
    plt.show()
