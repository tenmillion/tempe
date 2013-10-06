#Traub's model
# alphan = 0.016*(35.1-x)/(exp((35.1-x)/5)-1)
# betan = 0.25*exp((20.0-x)/40)
# alpham = 0.32*(13.1-x)/(exp((13.1-x)/4)-1)
# betam = 0.28*(x-40.1)/(exp((x-40.1)/5)-1)
# alphah = 0.128*exp(17.0-x)/18)
# betah = 4/(exp((40.0-x)/5)+1)

from __future__ import division
from numpy import *
from pylab import *

## Functions
# K channel
alpha_n = vectorize(lambda v: 0.016*(35.1-(v+60))/(exp((35.1-(v+60))/5)-1) if v != 35.1-60 else 0.08)
beta_n  = lambda v: 0.25*exp((20-(v+60))/40)
n_inf   = lambda v: alpha_n(v)/(alpha_n(v) + beta_n(v))

# Na channel (activating)
alpha_m = vectorize(lambda v: 0.32*(13.1-(v+60))/(exp((13.1-(v+60))/4)-1) if v != 13.1-60 else 1.28)
beta_m  = vectorize(lambda v: 0.28*((v+60)-40.1)/(exp(((v+60)-40.1)/5)-1) if v != 40.1-60 else 1.4)
m_inf   = lambda v: alpha_m(v)/(alpha_m(v) + beta_m(v))

# Na channel (inactivating)
alpha_h = lambda v: 0.128*exp((17-(v+60))/18)
beta_h  = lambda v: 4/(1 + exp((40-(v+60))/5))
h_inf   = lambda v: alpha_h(v)/(alpha_h(v) + beta_h(v))

### channel activity ###
v = arange(-100,51) # mV
figure()
plot(v, m_inf(v), v, h_inf(v), v, n_inf(v))
legend(('m','h','n'))
title('Steady state values of ion channel gating variables')
ylabel('Magnitude')
xlabel('Voltage (mV)')

## setup parameters and state variables
T     = 55    # ms
dt    = 0.025 # ms
time  = arange(0,T+dt,dt)

## HH Parameters
V_rest  = -65      # mV
Cm      = 1      # uF/cm2
gbar_Na = 30    # mS/cm2
gbar_K  = 15     # mS/cm2
g_l  = 0.3    # mS/cm2
E_Na    = 50    # mV
E_K     = -90    # mV
E_l     = -65 # mV

Vm      = zeros(len(time)) # mV
Vm[0]   = V_rest
m       = m_inf(V_rest)      
h       = h_inf(V_rest)
n       = n_inf(V_rest)

## Stimulus
I = zeros(len(time))
for i, t in enumerate(time):
  if 5 <= t <= 6: I[i] = 19 # uA/cm2

## Simulate Model
for i in range(1,len(time)):
  g_Na = gbar_Na*(m**3)*h
  g_K  = gbar_K*(n**4)

  m += dt*(alpha_m(Vm[i-1])*(1 - m) - beta_m(Vm[i-1])*m)
  h += dt*(alpha_h(Vm[i-1])*(1 - h) - beta_h(Vm[i-1])*h)
  n += dt*(alpha_n(Vm[i-1])*(1 - n) - beta_n(Vm[i-1])*n)

  Vm[i] = Vm[i-1] + (I[i-1] - g_Na*(Vm[i-1] - E_Na) - g_K*(Vm[i-1] - E_K) - g_l*(Vm[i-1] - E_l)) / Cm * dt 

## plot membrane potential trace
figure()
plot(time, Vm, time, I)
title('Traub et al. Example')
ylabel('Membrane Potential (mV)')
xlabel('Time (msec)')

show()
