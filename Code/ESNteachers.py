import scipy
import scipy.integrate as integrate
import numpy as np

def Rossler(l, dt, initvals=[2.0, 0, 0], params=[0.5, 2.0, 4.0],
            abserr=1.0e-8, relerr=1.0e-6):
    """
    This function generates a sequence of data from the Rossler system, based on
    the governing equations;
        xdot = -y-z,
        ydot = x+a*y, and
        zdot = b+z*(x-c),
    where a, b, and c are arbitrary parameters.

    This function returns a nondimensionalized xtilde, ytilde, and ztilde.
    """

    def drdt(u, t, p):
        """
        This function takes in the initial state and parameter vectors and
        returns the a vector of the time derivatives of x, y, and z:
        (xdot, ydot, zdot)
        """
        x,y,z = u
        a,b,c = p

        xdot = -y-z
        ydot = x+a*y
        zdot = b+z*(x-c)

        f=[xdot, ydot, zdot]
        return f

    L = list(range(l))
    t = [dt*i for i in L]

    sols = integrate.odeint(drdt, initvals, t, args=(params,), atol=abserr, rtol=relerr)
    xsol = sols[:,0]
    ysol = sols[:,1]
    zsol = sols[:,2]
    avgx = np.average(xsol)
    avgy = np.average(ysol)
    avgz = np.average(zsol)

    xtilde = np.divide((xsol-avgx),np.sqrt(np.average((xsol-avgx)**2)))
    ytilde = np.divide((ysol-avgy),np.sqrt(np.average((ysol-avgy)**2)))
    ztilde = np.divide((zsol-avgz),np.sqrt(np.average((zsol-avgz)**2)))

    xtilde = xtilde.reshape((xtilde.shape[0],1))
    ytilde = ytilde.reshape((ytilde.shape[0],1))
    ztilde = ztilde.reshape((ztilde.shape[0],1))

    return xtilde, ytilde, ztilde

def Lorenz(l, dt, initvals=[1.0, 1.0, 1.0], params=[10, 28, 8/3], abserr=1.0e-8,
            relerr=1.0e-6):
    """
    This function generates a sequence of data from the Lorenz system, based on
    the governing equations;
        xdot = a(y-x),
        ydot = bx-y-xz, and
        zdot = xy-cz,
    where a, b, and c are arbitrary parameters.

    This function returns a nondimensionalized xtilde, ytilde, and ztilde.
    """

    def drdt(u, t, p):
        """
        This function takes in the initial state and parameter vectors and
        returns the a vector of the time derivatives of x, y, and z:
        (xdot, ydot, zdot)
        """
        x,y,z = u
        a,b,c = p

        xdot = a*y-a*x
        ydot = b*x-y-x*z
        zdot = x*y-c*z

        f=[xdot, ydot, zdot]
        return f

    L = list(range(l))
    t = [dt*i for i in L]

    sols = integrate.odeint(drdt, initvals, t, args=(params,), atol=abserr, rtol=relerr)
    xsol = sols[:,0]
    ysol = sols[:,1]
    zsol = sols[:,2]
    avgx = np.average(xsol)
    avgy = np.average(ysol)
    avgz = np.average(zsol)

    xtilde = np.divide((xsol-avgx),np.sqrt(np.average((xsol-avgx)**2)))
    ytilde = np.divide((ysol-avgy),np.sqrt(np.average((ysol-avgy)**2)))
    ztilde = np.divide((zsol-avgz),np.sqrt(np.average((zsol-avgz)**2)))

    xtilde = xtilde.reshape((xtilde.shape[0],1))
    ytilde = ytilde.reshape((ytilde.shape[0],1))
    ztilde = ztilde.reshape((ztilde.shape[0],1))

    return xtilde, ytilde, ztilde