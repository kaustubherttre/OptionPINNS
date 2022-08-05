#Add tests here
#import module
import sys
sys.path.insert(0, '../src/')
from  BSNumerical import BSNumerical
from BSAnalytical import BSAnalytical
import matplotlib.pyplot as plt

if __name__ == '__main__':
    model_Numerical = BSNumerical(0,20,10,1,0.2,0.25, 160, 1000)
    model_Analytical = BSAnalytical(0,20,10,0.2,1, 0.25, 160)
    plt.plot(model_Numerical.matrix[:,1], label = 't = T at BSNumerical')
    plt.plot(model_Analytical.prices, label = 't = T at BSAnalytical')
    plt.show()