"""
Module for PID controller implementation.
"""


class PIDController:
    """
    PID Controller implementation for controlling vehicle velocity.
    """
    
    def __init__(self, kp=1.0, ki=0.0, kd=0.0, setpoint=0.0):
        """
        Initialize the PID controller with given parameters.
        
        Args:
            kp: Proportional gain
            ki: Integral gain
            kd: Derivative gain
            setpoint: Target value to maintain
        """
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.setpoint = setpoint
        
        # Initialize error tracking
        self.previous_error = 0.0
        self.integral = 0.0
    
    def compute(self, process_variable, dt_s=1.0):
        """
        Compute the control output based on the current process variable.
        
        Args:
            process_variable: Current value of the variable being controlled
            dt_s: Time step in seconds
            
        Returns:
            float: Control output
        """
        # Calculate error
        error = self.setpoint - process_variable
        
        # Calculate P, I, and D terms
        p_term = self.kp * error
        
        self.integral += error * dt_s
        i_term = self.ki * self.integral
        
        derivative = (error - self.previous_error) / dt_s
        d_term = self.kd * derivative
        
        # Update previous error
        self.previous_error = error
        
        # Calculate total output
        output = p_term + i_term + d_term
        
        return output
    
    def reset(self):
        """
        Reset the controller's internal state.
        """
        self.previous_error = 0.0
        self.integral = 0.0
