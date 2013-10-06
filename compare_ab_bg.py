#Borg-Graham model
# alpha = baserate*exp(valence*gamma*(v-vhalf)*F/RT)
# beta = baserate*exp(-valence*(1-gamma)*(v-vhalf)*F/RT)

from __future__ import division
from numpy import *
from pylab import *

F = 96.5 # kC/mol
R = 8.31 # J/molK
T1 = 273+37 # K
T2 = 273+24

## Functions
# K channel
alpha_n = lambda v: 0.015*exp(3*0.7*(v+35)*F/R/T2)
beta_n  = lambda v: 0.015*exp(-3*(1-0.7)*(v+35)*F/R/T2)
n_inf   = lambda v: alpha_n(v)/(alpha_n(v) + beta_n(v))

# Na channel (activating)
alpha_m = lambda v: 4.2*exp(4.3*0.7*(v+38)*F/R/T1)
beta_m  = lambda v: 4.2*exp(-4.3*(1-0.7)*(v+38)*F/R/T1)
m_inf   = lambda v: alpha_m(v)/(alpha_m(v) + beta_m(v))

# Na channel (inactivating)
alpha_h = lambda v: 0.2*exp(-6*0.5*(v+42)*F/R/T1)
beta_h  = lambda v: 0.2*exp(6*(1-0.5)*(v+42)*F/R/T1)
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
gbar_Na = 0.1   # mS/cm2, original in uS/cm2?
gbar_K  = 0.08     # mS/cm2
g_l  = 0.066    # mS/cm2?
E_Na    = 45    # mV
E_K     = -90    # mV
E_l     = -61 # mV

Vm      = zeros(len(time)) # mV
Vm[0]   = V_rest
m       = m_inf(V_rest)      
h       = h_inf(V_rest)
n       = n_inf(V_rest)

## Stimulus
I = zeros(len(time))
for i, t in enumerate(time):
  if 5 <= t <= 6: I[i] = 20 # uA/cm2

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
plot(time, Vm, time, -30+I)
title('Borg-Graham(from Traub?) Example')
ylabel('Membrane Potential (mV)')
xlabel('Time (msec)')

show()
