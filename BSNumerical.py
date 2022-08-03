from math import *
import numpy as np
import pandas as pd

# The mesh is defined as bt S and T, S is defined on the Y-axis and T is given on the x axis. 
# T

#aa=0.5*dt*(sigma*sigma*(1:N-2).*(1:N-2)-r*(1:N-2))';
#bb=1-dt*(sigma*sigma*(1:N-2).*(1:N-2)+r)';
#cc=0.5*dt*(sigma*sigma*(1:N-2).*(1:N-2)+r*(1:N-2))';
#v(2:N-1,i)=bb.*v(2:N-1,i-1)+cc.*v(3:N,i-1)+aa.*v(1:N-2,i-1)
class BSNumerical:
    def __init__(self, Smin, Smax, K, T, r, sigma, n_shares, n_time):
        self.Smin = Smin
        self.Smax = Smax
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.N = n_shares #number of shares
        self.M = n_time #time points
        self.dt = (self.T/self.M)
        self.dS = (self.Smin + self.Smax)/self.N
        self.V = np.zeros((self.N, self.M))
        
        def initial_boundry_conditions(self, Smin, K, N, M, V, dS, dt):
            for i in range(1,N):
                for j in range(1,M):
                    V[i,0] =  max(Smin+(i)*dS - K, 0)
                    V[0, j-1] = 0 
                    V[N-1,j] = (Smin + (N-1)*dS) - K*exp(-r * (j) * dt )
            return V
            
        self.mat = initial_boundry_conditions(self, Smin, K, self.N, self.M, self.V, self.dS, self.dt)
        
        def numerical_equation_helper( dt, sigma, r, N):
            t_1, t_2, t_3 = [], [], []
            for i in range(1,N-1):
                t_1.append(0.5 * dt * (pow(sigma,2)*pow(i,2)-r*(i)))
                t_2.append(1 - dt*(pow(sigma,2)*pow(i,2) + r))
                t_3.append(0.5*dt*(pow(sigma,2)*pow(i,2)+r*i))
            return np.array(t_1), np.array(t_2), np.array(t_3)
        self.t_1, self.t_2, self.t_3  = numerical_equation_helper(self.dt,self.sigma,self.r,self.N)
        def finite_difference_mat(N, M, t_1, t_2, t_3, mat):
            #v(2:N-1,i)=bb.*v(2:N-1,i-1)+cc.*v(3:N,i-1)+aa.*v(1:N-2,i-1)
            
            for i in range(1, N-1):
                for j in range(1,M):
                    mat[i+1,j-1] = np.dot(mat[1:N-1, j-1], t_2) 
            return mat
        self.matrix = finite_difference_mat(self.N, self.M, self.t_1, self.t_2, self.t_3, self.mat)
if __name__ == '__main__':
    model = BSNumerical(0,20,10,1,0.2,0.25, 5, 5)
    print(model.mat)


