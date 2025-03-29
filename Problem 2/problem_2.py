import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parameters for the forced damped pendulum
g = 9.81  # acceleration due to gravity (m/s^2)
L = 1.0   # length of the pendulum (m)
b = 0.5   # damping coefficient (kg/s)
A = 1.0   # amplitude of the external force (N)
omega = 2.0 * np.pi / 5.0  # frequency of the external force (rad/s)

# Differential equations for the forced damped pendulum
def pendulum_ode(t, y):
    theta, omega = y
    dtheta_dt = omega
    domega_dt = - (b/m) * omega - (g/L) * np.sin(theta) + (A/m) * np.cos(omega * t)
    return [dtheta_dt, domega_dt]

# Initial conditions
theta0 = np.radians(10)  # initial angle (10 degrees)
omega0 = 0.0              # initial angular velocity

# Time settings for the simulation
t_span = (0, 30)          # time interval (seconds)
t_eval = np.linspace(t_span[0], t_span[1], 1000)  # time points to evaluate the solution

# Solve the differential equations using solve_ivp
initial_conditions = [theta0, omega0]
solution = solve_ivp(pendulum_ode, t_span, initial_conditions, t_eval=t_eval)

# Extraction of results
theta = solution.y[0]  # angle over time
omega = solution.y[1]   # angular velocity over time
t = solution.t          # time array

# Visualization of results
plt.figure(figsize=(12, 8))

# Plotting the angle over time
plt.subplot(2, 1, 1)
plt.plot(t, np.degrees(theta), label='Theta (Degrees)')
plt.title('Forced Damped Pendulum Dynamics')
plt.xlabel('Time (s)')
plt.ylabel('Angle (Degrees)')
plt.grid()
plt.legend()

# Plotting the phase space (Theta vs Omega)
plt.subplot(2, 1, 2)
plt.plot(theta, omega)
plt.title('Phase Space Plot')
plt.xlabel('Angle (radians)')
plt.ylabel('Angular Velocity (rad/s)')
plt.grid()

plt.tight_layout()
plt.show()