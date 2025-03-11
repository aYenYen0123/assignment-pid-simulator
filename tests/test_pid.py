"""
Test cases for the PID controller module.
"""
import pytest
from pid_controller import PIDController


def test_pid_initialization():
    """Test PID controller initializes with correct parameters."""
    controller = PIDController(kp=1.0, ki=0.5, kd=0.25, setpoint=10.0)
    
    assert controller.kp == 1.0
    assert controller.ki == 0.5
    assert controller.kd == 0.25
    assert controller.setpoint == 10.0
    assert controller.previous_error == 0.0
    assert controller.integral == 0.0


def test_proportional_only_control():
    """Test PID control with only proportional gain."""
    controller = PIDController(kp=2.0, ki=0.0, kd=0.0, setpoint=10.0)
    
    # For process_variable = 5.0:
    # Error = 10.0 - 5.0 = 5.0
    # Output = 2.0 * 5.0 = 10.0
    output = controller.compute(process_variable=5.0)
    
    assert output == pytest.approx(10.0)
    assert controller.previous_error == 5.0
    assert controller.integral == 5.0  # Integral is updated even if ki is 0


def test_integral_accumulation():
    """Test integral term accumulation over time."""
    controller = PIDController(kp=0.0, ki=1.0, kd=0.0, setpoint=10.0)
    
    # First call: Error = 10.0 - 5.0 = 5.0, Integral = 5.0, Output = 1.0 * 5.0 = 5.0
    output1 = controller.compute(process_variable=5.0, dt_s=1.0)
    assert output1 == pytest.approx(5.0)
    assert controller.integral == 5.0
    
    # Second call: Error = 10.0 - 5.0 = 5.0, Integral = 5.0 + 5.0 = 10.0, Output = 1.0 * 10.0 = 10.0
    output2 = controller.compute(process_variable=5.0, dt_s=1.0)
    assert output2 == pytest.approx(10.0)
    assert controller.integral == 10.0


def test_derivative_term():
    """Test derivative term calculation."""
    controller = PIDController(kp=0.0, ki=0.0, kd=1.0, setpoint=10.0)
    
    # First call: Error = 10.0 - 5.0 = 5.0, previous_error = 0.0
    # Derivative = (5.0 - 0.0) / 1.0 = 5.0, Output = 1.0 * 5.0 = 5.0