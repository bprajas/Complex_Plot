import numpy as np
import matplotlib.pyplot as plt

def complex_plot():
  imags = []
  reals = []
  x_store = []
  y_store = []
  funcstr = input("Enter lambda followed by function (x):")
  func = eval(funcstr)

  for y in np.linspace(-5,5,5):
    for x in np.linspace(-5,5,5):
      z = complex(x,y)
      x_store.append(x)
      y_store.append(y)

      if z == 0 and (funcstr == 'lambda x: 1/x' or funcstr == 'lambda x: 1/x**2' or funcstr == 'lambda x: 1/x**3'):
        z = complex(0,0)
      else:
        z = func(z)
      imags.append(z.imag)
      reals.append(z.real)
  return reals, imags, x_store, y_store

x,y,X,Y=complex_plot()
plt.ion()
plt.figure(figsize=(24,20))
plt.scatter(x,y,s=30,alpha=0.5, color = 'blue')
plt.scatter(X,Y, s=30, alpha=0.5, color = 'red')
a = max(max(max(X),max(x)),max(max(Y),max(y)))
b = min(min(min(X),min(x)),min(min(Y),min(y)))
plt.xlim(1.1*b,1.1*a)
plt.ylim(1.1*b,1.1*a)
for i in range(0, len(x)):
    plt.arrow(X[i], Y[i],x[i] - X[i],y[i] - Y[i],color='green', head_width=min(0.5*(1/(1+((((x[i] - X[i])**2 + (y[i] - Y[i])**2)**0.5)/5))),0.05), head_length=min(0.6*(1/(1+((((x[i] - X[i])**2 + (y[i] - Y[i])**2)**0.5)/5))),0.05), alpha=0.8)
plt.show()
