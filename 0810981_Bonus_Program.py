import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(-1.4, 1.4, 100)
iv = np.linspace(-500/1000, 500/1000, 100)
y = np.linspace(0.0, 1.0, 11)
Vov = 0.3
I = 0.4/1000
id_1 = id_2 = I/2
kn = (I/2)/((1/2)*(Vov**2))
  
def find_id_1(Vid):
    return (I/2)+(I/Vov)*(Vid/2)*math.sqrt(1 - ((Vid/2)/Vov)**2)

def find_id_2(Vid):
    return (I/2)-(I/Vov)*(Vid/2)*math.sqrt(1 - ((Vid/2)/Vov)**2)

def find_Vid(i):
    return Vov * i

id_1_I = []
id_2_I = []
Vid = []

for i in x:
    id_1_I.append(find_id_1(find_Vid(i)) / I)
    id_2_I.append(find_id_2(find_Vid(i)) / I)
plt.plot(x, id_1_I, label = 'id1/I')
plt.plot(x, id_2_I, label = 'id2/I')
plt.ylabel('id/I | range: [0.0 : 1.0]')
plt.xlabel('Vid/Vov | range: [-1.4 : 1.4]')
plt.legend()