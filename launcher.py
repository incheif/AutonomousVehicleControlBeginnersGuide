"""
Interactive Launcher for Autonomous Vehicle Control Beginner's Guide Simulations.
"""

import os
import sys
import subprocess
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
SIM_DIR = PROJECT_ROOT / "src" / "simulations"

SIMULATIONS = [
    # Localization
    ("Localization", "Extended Kalman Filter (EKF)", "src/simulations/localization/extended_kalman_filter_localization/extended_kalman_filter_localization.py"),
    ("Localization", "Unscented Kalman Filter (UKF)", "src/simulations/localization/unscented_kalman_filter_localization/unscented_kalman_filter_localization.py"),
    ("Localization", "Particle Filter (PF)", "src/simulations/localization/particle_filter_localization/particle_filter_localization.py"),
    ("Localization", "EKF vs UKF Comparison", "src/simulations/localization/ekf_vs_ukf_comparison/ekf_vs_ukf_comparison.py"),
    ("Localization", "EKF vs UKF vs PF Comparison", "src/simulations/localization/ekf_ukf_pf_comparison/ekf_ukf_pf_comparison.py"),

    # Mapping
    ("Mapping", "Binary Occupancy Grid Map", "src/simulations/mapping/binary_grid_map_construction/binary_grid_map_construction.py"),
    ("Mapping", "Cost Map Construction", "src/simulations/mapping/cost_grid_map_construction/cost_grid_map_construction.py"),
    ("Mapping", "NDT Map Construction", "src/simulations/mapping/ndt_map_construction/ndt_map_construction.py"),
    ("Mapping", "Potential Field Map Construction", "src/simulations/mapping/potential_field_map_construction/potential_field_map_construction.py"),
    ("Mapping", "VFH Polar Histogram Construction", "src/simulations/mapping/vfh_polar_histogram_construction/vfh_polar_histogram_construction.py"),

    # Path Planning
    ("Path Planning", "A* Algorithm", "src/simulations/path_planning/astar_path_planning/astar_path_planning.py"),
    ("Path Planning", "Bidirectional A*", "src/simulations/path_planning/astar_bidirectional_path_planning/astar_bidirectional_path_planning.py"),
    ("Path Planning", "Hybrid A*", "src/simulations/path_planning/astar_hybrid_path_planning/astar_hybrid_path_planning.py"),
    ("Path Planning", "Dijkstra Algorithm", "src/simulations/path_planning/dijkstra_path_planning/dijkstra_path_planning.py"),
    ("Path Planning", "D* Algorithm", "src/simulations/path_planning/dstar_path_planning/dstar_path_planning.py"),
    ("Path Planning", "RRT Algorithm", "src/simulations/path_planning/rrt_path_planning/rrt_path_planning.py"),
    ("Path Planning", "RRT* Algorithm", "src/simulations/path_planning/rrt_star_path_planning/rrt_star_path_planning.py"),
    ("Path Planning", "Bidirectional RRT*", "src/simulations/path_planning/rrt_star_bidirectional_path_planning/rrt_star_bidirectional_path_planning.py"),
    ("Path Planning", "Informed RRT*", "src/simulations/path_planning/informed_rrt_star_path_planning/informed_rrt_star_path_planning.py"),
    ("Path Planning", "Probabilistic Road Map (PRM)", "src/simulations/path_planning/prm_path_planning/prm_path_planning.py"),
    ("Path Planning", "Ant Colony Optimization (ACO)", "src/simulations/path_planning/aco_path_planning/aco_path_planning.py"),
    ("Path Planning", "Particle Swarm Optimization (PSO)", "src/simulations/path_planning/pso_path_planning/pso_path_planning.py"),
    ("Path Planning", "Genetic Algorithm (GA)", "src/simulations/path_planning/ga_path_planning/ga_path_planning.py"),
    ("Path Planning", "Q-Learning Path Planning", "src/simulations/path_planning/q_learning_path_planning/q_learning_path_planning.py"),
    ("Path Planning", "Elastic Bands Path Planning", "src/simulations/path_planning/elastic_bands_path_planning/elastic_bands_path_planning.py"),
    ("Path Planning", "Gradient Path Planning", "src/simulations/path_planning/gradient_path_planning/gradient_path_planning.py"),

    # Path Tracking
    ("Path Tracking", "Pure Pursuit Path Tracking", "src/simulations/path_tracking/pure_pursuit_path_tracking/pure_pursuit_path_tracking.py"),
    ("Path Tracking", "Adaptive Pure Pursuit Path Tracking", "src/simulations/path_tracking/adaptive_pure_pursuit_path_tracking/adaptive_pure_pursuit_path_tracking.py"),
    ("Path Tracking", "Stanley Path Tracking", "src/simulations/path_tracking/stanley_path_tracking/stanley_path_tracking.py"),
    ("Path Tracking", "Rear Wheel Feedback Tracking", "src/simulations/path_tracking/rear_wheel_feedback_tracking/rear_wheel_feedback_tracking.py"),
    ("Path Tracking", "Linear Quadratic Regulator (LQR)", "src/simulations/path_tracking/lqr_path_tracking/lqr_path_tracking.py"),
    ("Path Tracking", "Model Predictive Control (MPC)", "src/simulations/path_tracking/mpc_path_tracking/mpc_path_tracking.py"),
    ("Path Tracking", "Model Predictive Path Integral (MPPI)", "src/simulations/path_tracking/mppi_path_tracking/mppi_path_tracking.py"),

    # Perception
    ("Perception", "LiDAR Obstacle Sensing", "src/simulations/perception/lidar_obstacle_sensing/lidar_obstacle_sensing.py"),
    ("Perception", "Point Cloud Rectangle Fitting", "src/simulations/perception/point_cloud_rectangle_fitting/point_cloud_rectangle_fitting.py"),
    ("Perception", "Point Cloud Robust LS Rectangle Fitting", "src/simulations/perception/point_cloud_rectangle_fitting/point_cloud_robustLS_rectangle_fitting.py"),
    ("Perception", "KD-Tree Nearest Neighbor Search", "src/simulations/perception/point_cloud_search/search_nearest_neighbor_kd_tree.py"),
    ("Perception", "KD-Tree Neighbor Points Search", "src/simulations/perception/point_cloud_search/search_neighbor_points_kd_tree.py"),
    ("Perception", "Sensor Auto Calibration", "src/simulations/perception/sensor_auto_calibration/sensor_auto_calibration.py"),

    # Course
    ("Course", "Cubic Spline Course 2D Plot", "src/simulations/course/cubic_spline/cubic_spline_2d_plot.py"),
    ("Course", "Cubic Spline Course Plot", "src/simulations/course/cubic_spline/cubic_spline_plot.py"),
]


def run_sim(relative_path: str):
    script_path = PROJECT_ROOT / relative_path
    if not script_path.exists():
        print(f"Error: Script not found: {script_path}")
        return
    print(f"\n>>> Running: {relative_path}")
    print("Press Ctrl+C or close the plot window to exit.\n")
    try:
        subprocess.run([sys.executable, str(script_path)], cwd=str(PROJECT_ROOT), check=True)
    except KeyboardInterrupt:
        print("\nSimulation stopped.")
    except Exception as e:
        print(f"Error running simulation: {e}")


def main():
    if len(sys.argv) > 1:
        query = sys.argv[1].lower()
        if query.isdigit():
            idx = int(query) - 1
            if 0 <= idx < len(SIMULATIONS):
                run_sim(SIMULATIONS[idx][2])
                return
            else:
                print(f"Invalid index {query}. Choose between 1 and {len(SIMULATIONS)}.")
                return
        matches = [s for s in SIMULATIONS if query in s[1].lower() or query in s[2].lower()]
        if len(matches) == 1:
            run_sim(matches[0][2])
            return
        elif len(matches) > 1:
            print(f"Multiple matches found for '{query}':")
            for idx, (cat, name, path) in enumerate(matches, 1):
                print(f"  [{idx}] [{cat}] {name}")
            try:
                choice = int(input("\nSelect a number to run: "))
                if 1 <= choice <= len(matches):
                    run_sim(matches[choice - 1][2])
            except (ValueError, KeyboardInterrupt):
                return
            return
        else:
            print(f"No simulations matching '{query}'.")

    # Interactive menu
    print("=" * 70)
    print(" Autonomous Vehicle Control Beginner's Guide - Simulation Launcher")
    print("=" * 70)
    current_cat = ""
    for idx, (cat, name, _) in enumerate(SIMULATIONS, 1):
        if cat != current_cat:
            current_cat = cat
            print(f"\n--- {cat} ---")
        print(f"  [{idx:2d}] {name}")
    print("\n  [ 0] Exit")
    print("=" * 70)

    try:
        choice = input("\nEnter simulation number to run (or name snippet): ").strip()
        if not choice or choice == "0":
            return
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(SIMULATIONS):
                run_sim(SIMULATIONS[idx][2])
            else:
                print("Invalid number.")
        else:
            matches = [s for s in SIMULATIONS if choice.lower() in s[1].lower() or choice.lower() in s[2].lower()]
            if matches:
                run_sim(matches[0][2])
            else:
                print(f"No simulation found matching '{choice}'.")
    except KeyboardInterrupt:
        print("\nExiting.")


if __name__ == "__main__":
    main()

