import run_simulation
from run_simulation import run_pid_controlled_simulation
from run_simulation import run_uncontrolled_simulation

if __name__ == "__main__":
    # Run the uncontrolled simulation
    print("Running uncontrolled simulation...")
    sim_uncontrolled = run_uncontrolled_simulation(v_init=6, duration_s=100)
    
    # Run the PID controlled simulation
    print("\nRunning PID controlled simulation...")
    sim_controlled = run_pid_controlled_simulation(v_init=6, kp=1, ki=0.6, kd=0, setpoint=5.0, duration_s=100)