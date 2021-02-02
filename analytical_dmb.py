import math

B = (((2**(7/2))/(3*math.sqrt(math.pi)))*((4.4e-28)*0.24)*(5.6096e35)*(1.0e-4)*
     (3.0e8)*(((8.617e-5)/((3.0e8)**2))**(1/2))) # normalized

T0 = 2.73 # K
omega_rad = 1.0e-4 # dimensionless
H0 = 67.27/(3.09e19) # 1/s, 1 Mpc = 3.09e19 km
mp = 9.3828e8 # eV/c^2 , 1.67e-27 # kg

# mx = 1.0 # GeV/c^2
mx = 1.0e9 # eV/c^2 , (1.78266191e-27) # kg
sigma0 = 1.0e-25 # cm^2

from sympy.solvers import solve
from sympy import Symbol
x = Symbol('x')
zthsol = solve((((mx/(mx+mp))*(B*sigma0*(1/(mx+mp))*(((T0*x)*((1/mp)+(1/mx)))**(0.5)))) - (H0*math.sqrt(omega_rad)*(x**2))), x)
print(zthsol)

zth = zthsol[1]
#zth = (((B**2)*(sigma0**2)*mx*T0)/((H0**2)*omega_rad*mp*(mx+mp)**3))**(1/3)
print(zth)

y = Symbol('y')
sols = solve(((H0*math.sqrt(omega_rad)*(y**2)*(mx+mp)/(B*sigma0))**2) - ((T0*y)/mp) - ((T0*(y**2))/(mx*zth)), y)
print(sols)
sols2 = solve(((B*sigma0*(1/(mx+mp))*((((T0*y)/mp)+((T0*(y**2))/(mx*zth)))**(0.5))) - (H0*math.sqrt(omega_rad)*(y**2))), y)
print(sols2)

zcrit = sols[1] #7.30823758388686e-9
kcrit = ((2*H0*(math.sqrt(omega_rad)))*(zcrit))/(3e8) # 1/m
print(kcrit)

k = 2.777e-24 # 1/m, 1 Mpc = 3.086e22 m
bool(kcrit > k)
