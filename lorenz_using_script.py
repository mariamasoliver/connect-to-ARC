import numpy as np 
from scipy.integrate import ode
 

def main(path, beta):
    T = int(1e5) #Total simulation time
    dt = 0.1 #integration time step
    nt = int(T/dt)
    
    """
    Lorentz Attractor: Definition and integration
    
    """
    def f(t, y, arg):
        sigma = arg['sigma']
        rho = arg['rho']
        beta = arg['beta']
        TC = arg['TC']
        MD = arg['MD']
        dy = np.zeros(3)
        dy[0] = sigma*(y[1]-y[0])
        dy[1] = rho*y[0]-MD*y[0]*y[2]-y[1]
        dy[2] = MD*y[0]*y[1]-beta*y[2];
        dy = dy*TC
        return dy
    
    m = 3 #Lorentz's dimension
    MD = 70
    rho = 28
    sigma = 10
    TC = 0.1
    beta = np.round(beta,2)
    arg = {'rho':rho,'sigma':sigma, 'beta':beta, 'MD':MD, 'TC': TC}
    y0 = [0.1,0.1,0.1]
    t0 = 0
    y = ode(f).set_integrator("dopri5")
    y.set_initial_value(y0, t0).set_f_params(arg)
    sup = np.zeros((m, nt))
    for i in range (nt):
        sup[:, i] = y.integrate(y.t+dt)
        
    #changing directory onto the desired folder
    os.chdir(path)
    
    """
    Saving text
    
    """    
    np.savetxt('lorenz_beta_'+str(beta)+'.txt', sup)
    
if __name__ == '__main__':
    import sys, os

    path = sys.argv[1]
    beta = int(sys.argv[2])
    if not os.path.exists(path):
        print('Directory:', path, '\ndoes not exist, creating new one.')
        os.makedirs(path) 
    else:
        print('Saving to', path)
    main(path, beta)    
    
    
    
    
    