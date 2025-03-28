import numpy as np  
import matplotlib.pyplot as plt  

def projectile_range(v0, angle, g=9.81):  
    angle_rad = np.radians(angle)  
    return (v0**2 * np.sin(2 * angle_rad)) / g  

def plot_ranges(v0):  
    angles = np.linspace(0, 90, 180)  
    ranges = projectile_range(v0, angles)  

    plt.figure(figsize=(10, 6))  
    plt.plot(angles, ranges, label=f'v0 = {v0} m/s')  
    plt.title('Range of a Projectile as a Function of Angle of Projection')  
    plt.xlabel('Angle of Projection (degrees)')  
    plt.ylabel('Range (meters)')  
    plt.axhline(0, color='black', lw=0.8, ls='--')  
    plt.axvline(45, color='red', lw=0.8, ls='--', label='Max Range at 45°')  
    plt.grid()  
    plt.legend()  
    plt.savefig('projectile_range.png')  # Save the figure as an image
    plt.close()  # Close the figure window

# Example usage:  
plot_ranges(20)  # You can adjust the initial velocity here.  