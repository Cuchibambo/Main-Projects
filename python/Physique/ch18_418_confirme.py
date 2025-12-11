1#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ====================================================================
# Chapitre 18 Activité 3                                    correction
# ====================================================================
from matplotlib import pyplot as plt
from math import pi
import numpy as np

T=1    # Période en ms
t=np.linspace(0,4,400) # Définition du tableau des dates en ms

A1=float(input('Amplitude du signal 1 en V : A1 ='))
A2=float(input('Amplitude du signal 2 en V : A2 ='))
phi=eval(input('Phase à l\'origine de la source 2 : phi = '))
s1=A1*np.cos((2*pi*t)/T)
s2=A2*np.cos(((2*pi*t)/T)+phi)
s3=s1+s2

# Affichage des courbe
plt.plot(t,s1,label='$A_{1}\cos(\dfrac{2\pi}{T}t)$')
plt.plot(t,s2,label=r'$A_{2}\cos(\dfrac{2\pi}{T}t+\varphi)$')
plt.plot(t,s3,label=r'$A_{1}\cos(\dfrac{2\pi}{T}t)+A_{2}\cos(\dfrac{2\pi}{T}t+\varphi)$')
plt.xlabel('t (en ms)')
plt.ylabel('s1,s2 et s3')
plt.xlim((0,4))
plt.ylim(-max(A1,A2)+2,max(A1,A2)+2)
plt.grid()
plt.legend(loc = 9, ncol=3)
plt.show()

