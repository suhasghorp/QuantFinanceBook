#%%
"""
Created on Thu Nov 28 2018
Bivariate normal PDF
@author: Lech A. Grzelak
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.mlab import bivariate_normal

def BivariateNormalPDFPlot():

    # Number of points in each direction

    n    = 40;
    
    # Parameters

    mu_1    = 0;
    mu_2    = 0;
    sigma_1 = 1;
    sigma_2 = 0.5;
    rho1    = 0.0
    rho2    = -0.8
    rho3    = 0.8  
        
    # Create a grid and a multivariate normal

    x = np.linspace(-3.0,3.0,n)
    y = np.linspace(-3.0,3.0,n)
    X, Y = np.meshgrid(x,y)
    Z = lambda rho: bivariate_normal(X,Y,sigma_1,sigma_2,mu_1,mu_2,rho*sigma_1*sigma_2)
    
    # Make a 3D plot- rho = 0.0

    fig= plt.figure(1)
    ax = fig.gca(projection='3d')
    ax.plot_surface(X, Y, Z(rho1),cmap='viridis',linewidth=0)
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    plt.show()
    
    # Make a 3D plot- rho = -0.8

    fig= plt.figure(2)
    ax = fig.gca(projection='3d')
    ax.plot_surface(X, Y, Z(rho2),cmap='viridis',linewidth=0)
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    plt.show()
    
    # Make a 3D plot- rho = 0.8

    fig= plt.figure(3)
    ax = fig.gca(projection='3d')
    ax.plot_surface(X, Y, Z(rho3),cmap='viridis',linewidth=0)
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    plt.show()
                          
BivariateNormalPDFPlot()
