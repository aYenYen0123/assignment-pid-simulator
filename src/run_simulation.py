"""
Module for simulation of vehicle dynamics with or without control.
"""
from vehicle_dynamics import Vehicle
from pid_controller import PIDController
from simulation import Simulation

def run_uncontrolled_simulation(v_init=10, duration_s=100, filename="uncontrolled_velocity.png"):
    """
    Run and plot a simulation without a controller.
    """
    vehicle = Vehicle(mass_kg=1.0, initial_velocity_mps=v_init, drag_coefficient_kgpm=0.05)
    sim = Simulation(vehicle=vehicle)
    sim.run(duration_s=100)
    sim.plot_results(filename=filename)
    return sim


def run_pid_controlled_simulation(v_init=10, kp=2.0, ki=0.1, kd=1.0, setpoint=5.0, duration_s=100, filename="pid_controlled_velocity.png"):
    """
    Run and plot a simulation with a PID controller.
    
    Args:
        v_init: initial_velocity_mps
        kp: Proportional gain
        ki: Integral gain
        kd: Derivative gain
        setpoint: Target velocity
        duration_s: Simulation duration
    
    Returns:
        Simulation: The completed simulation object
    """
    vehicle = Vehicle(mass_kg=1.0, initial_velocity_mps=v_init, drag_coefficient_kgpm=0.05)
    controller = PIDController(kp=kp, ki=ki, kd=kd, setpoint=setpoint)
    sim = Simulation(vehicle=vehicle, controller=controller)
    sim.run(duration_s=duration_s)
    sim.plot_results(filename=filename)
    
    # Report settling time
    settling_time = sim.find_settling_time(setpoint, error_threshold_percent=1.0)
    if settling_time is not None and settling_time <= 30:
        print(f"System settled within 1% of setpoint ({setpoint} m/s) in {settling_time:.2f} seconds")
    else:
        print(f"System did not settle within 1% of setpoint in under 30 seconds")
    
    return sim

def run_gain_scheduled_pid_simulation(v_init=10
                                      , kp=(2.0, 1.0), ki=(0.1, 0.05), kd=(0.0, 0.0)
                                      , setpoint=5.0, duration_s=100
                                      , filename="gain_scheduled_pid_velocity.png"):
    """
    Run and plot a simulation with a gain scheduled PID controller.
    Defined veclocity region:
        For v > 1 (m/s), use gain1
        For v <= 1 (m/s), use gain2

    Args:
        v_init: initial_velocity_mps
        kp: Proportional gain1, Proportional gain2
        ki: Integral gain1, Integral gain2 
        kd: Derivative gain1, Derivative gain2
        setpoint: Target velocity
        duration_s: Simulation duration
    
    Returns:
        Simulation: The completed simulation object
    """
    vehicle = Vehicle(mass_kg=1.0, initial_velocity_mps=v_init, drag_coefficient_kgpm=0.05)

    controller = PIDController(kp=kp[0], ki=ki[0], kd=kd[0], setpoint=setpoint)
    sim = Simulation(vehicle=vehicle, controller=controller)
    sim.run(duration_s=duration_s)
    sim.plot_results(filename=filename)
    
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
    sim_uncontrolled = run_uncontrolled_simulation(v_init=6, duration_s=100)
    
    # Run the PID controlled simulation
    print("\nRunning PID controlled simulation...")
    sim_controlled = run_pid_controlled_simulation(v_init=6, kp=1, ki=0.6, kd=0, setpoint=5.0, duration_s=100)
