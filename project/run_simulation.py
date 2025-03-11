"""
Module for simulation of vehicle dynamics with or without control.
"""
from vehicle_dynamics import Vehicle
from pid_controller import PIDController
from simulation import Simulation

def run_uncontrolled_simulation():
    """
    Run and plot a simulation without a controller.
    """
    vehicle = Vehicle(mass_kg=1.0, initial_velocity_mps=10.0, drag_coefficient_kgpm=0.05)
    sim = Simulation(vehicle=vehicle)
    sim.run(duration_s=100)
    sim.plot_results(filename="uncontrolled_velocity.png")
    return sim


def run_pid_controlled_simulation(kp=2.0, ki=0.1, kd=1.0, setpoint=5.0, duration_s=100):
    """
    Run and plot a simulation with a PID controller.
    
    Args:
        kp: Proportional gain
        ki: Integral gain
        kd: Derivative gain
        setpoint: Target velocity
        duration_s: Simulation duration
    
    Returns:
        Simulation: The completed simulation object
    """
    vehicle = Vehicle(mass_kg=1.0, initial_velocity_mps=10.0, drag_coefficient_kgpm=0.05)
    controller = PIDController(kp=kp, ki=ki, kd=kd, setpoint=setpoint)
    sim = Simulation(vehicle=vehicle, controller=controller)
    sim.run(duration_s=duration_s)
    sim.plot_results(filename="pid_controlled_velocity.png")
    
    # Report settling time
    settling_time = sim.find_settling_time(setpoint, error_threshold_percent=1.0)
    if settling_time is not None and settling_time <= 30:
        print(f"System settled within 1% of setpoint ({setpoint} m/s) in {settling_time:.2f} seconds")
    else:
        print(f"System did not settle within 1% of setpoint in under 30 seconds")
    
    return sim


if __name__ == "__main__":
    # Run the uncontrolled simulation
    print("Running uncontrolled simulation...")
    sim_uncontrolled = run_uncontrolled_simulation()
    
    # Run the PID controlled simulation
    print("\nRunning PID controlled simulation...")
    sim_controlled = run_pid_controlled_simulation(kp=2.0, ki=0.1, kd=1.0, setpoint=5.0, duration_s=100)