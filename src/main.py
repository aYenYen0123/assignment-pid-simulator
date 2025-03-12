import run_simulation
from run_simulation import run_pid_controlled_simulation
from run_simulation import run_uncontrolled_simulation

# Run the uncontrolled simulation
print("Running uncontrolled simulation...")
sim_uncontrolled = run_uncontrolled_simulation(v_init=10, duration_s=100
                                                , filename="unontrolled_v_t_plot.png")

# Run the PID controlled simulation
print("\nRunning PID controlled simulation...")
sim_controlled = run_pid_controlled_simulation(v_init=10, kp=0.08, ki=0.1, kd=0.02
                                                , setpoint=5.0, duration_s=100
                                                , filename = "pid_controlled_v_t_plot.png")