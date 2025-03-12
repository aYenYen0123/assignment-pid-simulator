"""
Test cases for the vehicle dynamics module.
"""
import pytest
from vehicle_dynamics import Vehicle


def test_vehicle_initialization():
    """Test that vehicle initializes with correct parameters."""
    vehicle = Vehicle(mass_kg=2.0, initial_velocity_mps=5.0, drag_coefficient_kgpm=0.1)
    
    assert vehicle.mass_kg == 2.0
    assert vehicle.velocity_mps == 5.0
    assert vehicle.drag_coefficient_kgpm == 0.1


def test_drag_force_calculation_positive_velocity():
    """Test drag force calculation with positive velocity."""
    vehicle = Vehicle(initial_velocity_mps=10.0, drag_coefficient_kgpm=0.05)
    
    # Expected: -sign(10) * 0.05 * 10^2 = -1 * 0.05 * 100 = -5
    expected_force = -5.0
    actual_force = vehicle.calculate_drag_force()
    
    assert actual_force == pytest.approx(expected_force)


def test_drag_force_calculation_negative_velocity():
    """Test drag force calculation with negative velocity."""
    vehicle = Vehicle(initial_velocity_mps=-10.0, drag_coefficient_kgpm=0.05)
    
    # Expected: -sign(-10) * 0.05 * (-10)^2 = -(-1) * 0.05 * 100 = 5
    expected_force = 5.0
    actual_force = vehicle.calculate_drag_force()
    
    assert actual_force == pytest.approx(expected_force)


def test_drag_force_calculation_zero_velocity():
    """Test drag force calculation with zero velocity."""
    vehicle = Vehicle(initial_velocity_mps=0.0, drag_coefficient_kgpm=0.05)
    
    # Expected: -sign(0) * 0.05 * 0^2 = 0
    expected_force = 0.0
    actual_force = vehicle.calculate_drag_force()
    
    assert actual_force == pytest.approx(expected_force)


def test_update_with_no_external_force():
    """Test vehicle update with only drag force."""
    vehicle = Vehicle(mass_kg=1.0, initial_velocity_mps=10.0, drag_coefficient_kgpm=0.05)
    
    # Calculate expected velocity after 1 second
    # Drag force = -5.0 N
    # Acceleration = -5.0 / 1.0 = -5.0 m/s^2
    # New velocity = 10.0 + (-5.0 * 1.0) = 5.0 m/s
    expected_velocity = 5.0
    
    new_velocity = vehicle.update_state(external_force_n=0.0, dt_s=1.0)
    
    assert new_velocity == pytest.approx(expected_velocity)
    assert vehicle.velocity_mps == pytest.approx(expected_velocity)


def test_update_with_external_force():
    """Test vehicle update with external force."""
    vehicle = Vehicle(mass_kg=1.0, initial_velocity_mps=10.0, drag_coefficient_kgpm=0.05)
    
    # Calculate expected velocity after 1 second with external force of 10N
    # Drag force = -5.0 N
    # Total force = -5.0 + 10.0 = 5.0 N
    # Acceleration = 5.0 / 1.0 = 5.0 m/s^2
    # New velocity = 10.0 + (5.0 * 1.0) = 15.0 m/s
    expected_velocity = 15.0
    
    new_velocity = vehicle.update_state(external_force_n=10.0, dt_s=1.0)
    
    assert new_velocity == pytest.approx(expected_velocity)
    assert vehicle.velocity_mps == pytest.approx(expected_velocity)


def test_update_with_different_time_step():
    """Test vehicle update with different time step."""
    vehicle = Vehicle(mass_kg=1.0, initial_velocity_mps=10.0, drag_coefficient_kgpm=0.05)
    
    # Calculate expected velocity after 0.5 seconds
    # Drag force = -5.0 N
    # Acceleration = -5.0 / 1.0 = -5.0 m/s^2
    # New velocity = 10.0 + (-5.0 * 0.5) = 7.5 m/s
    expected_velocity = 7.5
    
    new_velocity = vehicle.update_state(external_force_n=0.0, dt_s=0.5)
    
    assert new_velocity == pytest.approx(expected_velocity)
    assert vehicle.velocity_mps == pytest.approx(expected_velocity)
