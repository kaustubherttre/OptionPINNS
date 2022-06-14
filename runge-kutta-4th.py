import math
def function(x,y):
    return ((x-y)/2)

#Do rungekutta here
def rungeKutta(x0, y0, x, h ):

    #number of iterations
    n = (int)((x-x0)/h)
    y = y0
    for i in range(1, n+1):
        k1 = h * function(x0, y)
        k2 = h * function(x0 + 0.5*h, y + 0.5*k1)
        k3 = h * function(x0 + 0.5*h, y + 0.5*k2)
        k4 = h * function(x0 + h, y + k3)
        y = y + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4)
        x0 = x0+h
    return y



if __name__ == "__main__":
    print("Function result", rungeKutta(0,1,2,0.2))
    for i in range(10):
        print(f"Functional Result at {i}", rungeKutta(0,1,2,0.2))

