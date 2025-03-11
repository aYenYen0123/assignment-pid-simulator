"""
Module for simulation of vehicle dynamics with or without control.
"""
import numpy as np
import matplotlib.pyplot as plt
from vehicle_dynamics import Vehicle
from pid_controller import PIDController


class Simulation:
    """
    Class for simulating vehicle dynamics with or without control.
    """
    
    def __init__(self, vehicle=None, controller=None, dt_s=1.0):
        """
        Initialize the simulation with given parameters.
        
        Args:
            vehicle: Vehicle instance to simulate
            controller: Optional controller instance
            dt_s: Time step in seconds
        """
        self.vehicle = vehicle if vehicle else Vehicle()
        self.controller = controller
        self.dt_s = dt_s
        
        # Data storage for plotting
        self.time_points = []
        self.velocity_points = []
        self.control_inputs = []
    
    def run(self, duration_s=100, setpoint=None):
        """
        Run the simulation for the specified duration.
        
        Args:
            duration_s: Duration in seconds
            setpoint: Optional setpoint for the controller
            
        Returns:
            tuple: (time_points, velocity_points, control_inputs)
        """
        # Reset data storage
        self.time_points = []
        self.velocity_points = []
        self.control_inputs = []
        
        # Set controller setpoint if provided
        if setpoint is not None and self.controller:
            self.controller.setpoint = setpoint
            self.controller.reset()
        
        # Initialize vehicle to its initial state
        t = 0.0
        
        # Run simulation loop
        while t <= duration_s:
            # Record current state
            self.time_points.append(t)
            self.velocity_points.append(self.vehicle.velocity_mps)
            
            # Calculate control input if controller exists
            control_input = 0.0
            if self.controller:
                control_input = self.controller.compute(self.vehicle.velocity_mps, self.dt_s)
            self.control_inputs.append(control_input)
            
            # Update vehicle state
            self.vehicle.update_state(control_input, self.dt_s)
            
            # Increment time
            t += self.dt_s
        
        return self.time_points, self.velocity_points, self.control_inputs
    
    def plot_results(self, filename=None):
        """
        Plot the simulation results.
        
        Args:
            filename: Optional filename to save the plot
        """
        plt.figure(figsize=(12, 8))
        
        # Plot velocity
        plt.subplot(2, 1, 1)
        plt.plot(self.time_points, self.velocity_points, 'b-', label='Velocity (m/s)')
        
        # If controller exists, plot setpoint
        if self.controller:
            plt.axhline(y=self.controller.setpoint, color='r', linestyle='--', 
                        label=f'Setpoint ({self.controller.setpoint} m/s)')
            
            # Plot error threshold regions if we have a setpoint
            error_threshold = self.controller.setpoint * 0.01  # 1% error
            plt.axhline(y=self.controller.setpoint + error_threshold, color='g', linestyle=':',
                        label=f'1% Error Threshold')
            plt.axhline(y=self.controller.setpoint - error_threshold, color='g', linestyle=':')
        
        plt.grid(True)
        plt.xlabel('Time (s)')
        plt.ylabel('Velocity (m/s)')
        plt.legend()
        plt.title('Vehicle Velocity over Time')
        
        # Plot control input if controller exists
        if self.controller:
            plt.subplot(2, 1, 2)
            plt.plot(self.time_points, self.control_inputs, 'g-', label='Control Force (N)')
            plt.grid(True)
            plt.xlabel('Time (s)')
            plt.ylabel('Control Force (N)')
            plt.legend()
            plt.title('Control Input over Time')
        
        plt.tight_layout()
        
        # Save plot if filename is provided
        if filename:
            plt.savefig(filename)
            
        plt.show()
        
    def find_settling_time(self, setpoint, error_threshold_percent=1.0):
        """
        Find the time it takes for the velocity to settle within the error threshold.
        
        Args:
            setpoint: Target setpoint
            error_threshold_percent: Error threshold as a percentage of setpoint
            
        Returns:
            float or None: Settling time in seconds, None if never settles
        """
        if not self.velocity_points:
            return None
        
        error_threshold = setpoint * error_threshold_percent / 100.0
        
        # Find the first time point where the velocity stays within the error threshold
        for i in range(len(self.time_points)):
            if abs(self.velocity_points[i] - setpoint) <= error_threshold:
                # Check if it stays within the threshold for all subsequent points
                if all(abs(v - setpoint) <= error_threshold for v in self.velocity_points[i:]):
                    return self.time_points[i]
        
        # If no settling point found
        return None
