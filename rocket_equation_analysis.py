# --------------------------------------------------
# Rocket Equation Numerical Analysis
# Simone Muscolino
# --------------------------------------------------

# This project explores the Tsiolkovsky Rocket Equation
# and compares different propulsion systems using Python.

# --------------------------------------------------
# Import Libraries
# --------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------
# Rocket Parameters
# --------------------------------------------------

# Initial mass of the rocket (kg)
m_initial = 500

# Propellant mass flow rate (kg/s)
mass_flow_rate = 5

# Time range for simulation
t_max = 60
t = np.linspace(0, t_max, 1000)

# --------------------------------------------------
# Propulsion Systems (Effective Exhaust Velocity)
# --------------------------------------------------

# Different propulsion technologies
propulsion_systems = {
    "Chemical Rocket": 2500,
    "Advanced Chemical Rocket": 3000,
    "Nuclear Thermal Rocket": 4500
}

# --------------------------------------------------
# Rocket Equation Function
# --------------------------------------------------

def rocket_velocity(v_e, m0, m_dot, t):

    """
    Computes rocket velocity using the Tsiolkovsky rocket equation
    """

    m = m0 - m_dot * t

    # avoid negative mass
    m[m <= 0] = np.nan

    delta_v = v_e * np.log(m0 / m)

    return delta_v


# --------------------------------------------------
# Velocity Plot
# --------------------------------------------------

plt.figure(figsize=(10,6))

for system, v_e in propulsion_systems.items():

    v = rocket_velocity(v_e, m_initial, mass_flow_rate, t)

    plt.plot(t, v, label=system)

plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.title("Rocket Velocity Evolution for Different Propulsion Systems")

plt.grid(True)
plt.legend()

plt.savefig("rocket_velocity_plot.png", dpi=300)

plt.show()

# --------------------------------------------------
# Mass Evolution Plot
# --------------------------------------------------

mass = m_initial - mass_flow_rate * t

plt.figure(figsize=(10,6))

plt.plot(t, mass)

plt.xlabel("Time (s)")
plt.ylabel("Rocket Mass (kg)")
plt.title("Rocket Mass Evolution During Propellant Burn")

plt.grid(True)

plt.savefig("rocket_mass_plot.png", dpi=300)

plt.show()
