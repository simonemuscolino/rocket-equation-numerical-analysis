# Rocket Equation Numerical Solver

This project implements a numerical analysis of the Tsiolkovsky Rocket Equation using Python.

The goal is to model the velocity evolution of a rocket as its mass decreases during propellant burn.

## Physical Model

The rocket equation is:

Δv = v_e * ln(m0 / m)

where:

v_e = effective exhaust velocity  
m0 = initial mass  
m = instantaneous mass of the rocket  

The mass decreases according to:

m(t) = m0 - ṁt

where ṁ is the propellant mass flow rate.

## Simulation

The simulation computes:

• Rocket velocity over time  
• Rocket mass evolution during propellant burn  

The results are visualized using Matplotlib.

## Parameters used

Exhaust velocity: 3000 m/s  
Initial mass: 500 kg  
Mass flow rate: 5 kg/s  
Simulation time: 60 s

## Output

The simulation generates two plots:

1. Rocket velocity vs time
2. Rocket mass vs time

## Technologies used

Python  
NumPy  
SciPy  
Matplotlib

## Educational Purpose

This project was developed as part of personal studies in aerospace engineering and numerical modeling applied to rocket propulsion.
