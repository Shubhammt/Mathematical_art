def rk4(fx,t,step,dfx):
    k1 = step*dfx(t,fx)
    k2 = step*dfx(t+0.5*step, fx+0.5*k1)
    k3 = step*dfx(t+0.5*step, fx+0.5*k2)
    k4 = step*dfx(t+step, fx+k3)
    
    return fx+ k1/6. + k2/3. + k3/3. + k4/6.