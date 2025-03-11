"""
Module for vehicle dynamics in a one-dimensional environment.
"""
import numpy as np

class Vehicle:
    """
    Class representing a vehicle in a one-dimensional environment with drag force.
    
    f [N]: -sign(velocity_mps) * k_kgpm * (velocity_mps)^2
    """
    
    def __init__(self, mass_kg=1.0, initial_velocity_mps=10.0, drag_coefficient_kgpm=0.05):
        """
        Initialize the vehicle with given parameters.
        
        Args:
            mass_kg: Mass of the vehicle in kg
            initial_velocity_mps: Initial velocity in m/s
            drag_coefficient_kgpm: Drag coefficient in kg/m
        """
        self.mass_kg = mass_kg
        self.velocity_mps = initial_velocity_mps
        self.drag_coefficient_kgpm = drag_coefficient_kgpm
        
    def calculate_drag_force(self):
        """
        Calculate the drag force based on the current velocity.
        
        Returns:
            float: Drag force in N
        """
        sign = 1 if self.velocity_mps > 0 else -1 if self.velocity_mps < 0 else 0
        return -sign * self.drag_coefficient_kgpm * (self.velocity_mps ** 2)
    
    def update_state(self, external_force_n=0.0, dt_s=1.0):
        """
        Update the vehicle's state based on current forces.
        
        Args:
            external_force_n: External force applied to the vehicle in Newtons
            dt_s: Time step in seconds
            
        Returns:
            float: New velocity after the update
        """
        # Calculate total force (drag + external)
        drag_force = self.calculate_drag_force()
        total_force = drag_force + external_force_n
        
        # Calculate acceleration (F = ma)
        acceleration = total_force / self.mass_kg
        
        # Update velocity (v = v0 + a*t)
        self.velocity_mps += acceleration * dt_s
        
        return self.velocity_mps
