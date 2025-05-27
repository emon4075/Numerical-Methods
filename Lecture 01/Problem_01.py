import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

def segment_area(radius, height):
    """Calculate the area of a circular segment with given radius and height."""
    if height <= 0:
        return 0
    if height >= 2 * radius:
        return np.pi * radius**2
    
    # Formula for segment area
    return radius**2 * np.arccos((radius - height) / radius) - (radius - height) * np.sqrt(2 * radius * height - height**2)

def calculate_water_height_for_volume_ratio(radius, volume_ratio):
    """Calculate the water height in a horizontal cylinder for a given volume ratio."""
    def func(height):
        segment = segment_area(radius, height)
        circle = np.pi * radius**2
        return segment / circle - volume_ratio
    
    # Use root-finding algorithm to find height
    result = root_scalar(func, bracket=[0, 2*radius], method='brentq')
    height = result.root
    
    return height

def visualize_cylinder_fill(radius, height):
    """Visualize the cylinder cross-section with water."""
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Draw circle
    circle = plt.Circle((0, 0), radius, fill=False, color='black', linewidth=2)
    ax.add_patch(circle)
    
    # Draw water level
    water_level = height - radius
    x = np.linspace(-radius, radius, 1000)
    water_top = np.ones_like(x) * water_level
    
    # Calculate bottom of circle at each x
    circle_bottom = -np.sqrt(radius**2 - x**2)
    
    # Fill water area
    ax.fill_between(x, circle_bottom, np.minimum(water_top, np.sqrt(radius**2 - x**2)), 
                    color='blue', alpha=0.5)
    
    # Draw axes and labels
    ax.axhline(y=0, color='gray', linestyle='--', alpha=0.7)
    ax.axvline(x=0, color='gray', linestyle='--', alpha=0.7)
    ax.set_aspect('equal')
    ax.set_xlim(-1.5*radius, 1.5*radius)
    ax.set_ylim(-1.5*radius, 1.5*radius)
    ax.set_title(f'Horizontal Cylinder Cross-Section\nWater Height = {height:.4f} (= {height/(2*radius):.4f} × diameter)')
    ax.set_xlabel('Width')
    ax.set_ylabel('Height')
    ax.text(1.1*radius, water_level, f'Water level: {height:.4f}', verticalalignment='center')
    
    plt.grid(True, alpha=0.3)
    plt.show()

# Execute the calculation
radius = 1.0  # Example radius
diameter = 2 * radius
volume_ratio = 0.25  # 1/4 of total volume

height = calculate_water_height_for_volume_ratio(radius, volume_ratio)

print("\nHorizontal Cylinder Partial Fill Calculator")
print("--------------------------------------------")
print(f"Cylinder radius: {radius:.4f} units")
print(f"Cylinder diameter: {diameter:.4f} units")
print(f"Desired volume ratio: {volume_ratio:.4f} ({volume_ratio*100:.1f}%)")
print(f"Required water height: {height:.6f} units")
print(f"Height as fraction of diameter: {height/diameter:.6f}")
print(f"Height as fraction of radius: {height/radius:.6f}")

# Verify the solution
segment = segment_area(radius, height)
circle = np.pi * radius**2
actual_ratio = segment / circle
print("\nVerification:")
print(f"Target volume ratio: {volume_ratio:.10f}")
print(f"Actual volume ratio: {actual_ratio:.10f}")
print(f"Error: {abs(actual_ratio - volume_ratio):.10e}")

# Visualize the solution
visualize_cylinder_fill(radius, height)