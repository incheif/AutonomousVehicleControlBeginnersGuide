import streamlit as st
import os
from pathlib import Path

st.set_page_config(
    page_title="Autonomous Vehicle Control Explorer",
    page_icon="🚗",
    layout="wide"
)

PROJECT_ROOT = Path(__file__).resolve().parent

CATEGORIES = {
    "Path Tracking": [
        ("Pure Pursuit Path Tracking", "src/simulations/path_tracking/pure_pursuit_path_tracking/pure_pursuit_path_tracking.py", "src/simulations/path_tracking/pure_pursuit_path_tracking/pure_pursuit_path_tracking.gif",
         "Geometric path tracking that steers toward a look-ahead point on the reference path."),
        ("Adaptive Pure Pursuit Path Tracking", "src/simulations/path_tracking/adaptive_pure_pursuit_path_tracking/adaptive_pure_pursuit_path_tracking.py", "src/simulations/path_tracking/adaptive_pure_pursuit_path_tracking/adaptive_pure_pursuit_path_tracking.gif",
         "Adaptive Pure Pursuit dynamically scales the look-ahead distance according to vehicle speed."),
        ("Stanley Path Tracking", "src/simulations/path_tracking/stanley_path_tracking/stanley_path_tracking.py", "src/simulations/path_tracking/stanley_path_tracking/stanley_path_tracking.gif",
         "Stanford Stanley method combining heading error and cross-track error measured at the front axle."),
        ("Rear Wheel Feedback Tracking", "src/simulations/path_tracking/rear_wheel_feedback_tracking/rear_wheel_feedback_tracking.py", "src/simulations/path_tracking/rear_wheel_feedback_tracking/rear_wheel_feedback_tracking.gif",
         "Non-linear feedback control referenced to the rear axle center."),
        ("Linear Quadratic Regulator (LQR)", "src/simulations/path_tracking/lqr_path_tracking/lqr_path_tracking.py", "src/simulations/path_tracking/lqr_path_tracking/lqr_path_tracking.gif",
         "Optimal state-feedback controller minimizing quadratic error state costs."),
        ("Model Predictive Control (MPC)", "src/simulations/path_tracking/mpc_path_tracking/mpc_path_tracking.py", "src/simulations/path_tracking/mpc_path_tracking/mpc_path_tracking.gif",
         "Receding-horizon optimization subject to vehicle dynamics and steering constraints."),
        ("Model Predictive Path Integral (MPPI)", "src/simulations/path_tracking/mppi_path_tracking/mppi_path_tracking.py", "src/simulations/path_tracking/mppi_path_tracking/mppi_path_tracking.gif",
         "Sampling-based stochastic optimal control for complex, non-linear terrain."),
    ],
    "Localization": [
        ("Extended Kalman Filter (EKF)", "src/simulations/localization/extended_kalman_filter_localization/extended_kalman_filter_localization.py", "src/simulations/localization/extended_kalman_filter_localization/extended_kalman_filter_localization.gif",
         "Fuses odometry and noisy GNSS position data with non-linear Jacobian approximations."),
        ("Unscented Kalman Filter (UKF)", "src/simulations/localization/unscented_kalman_filter_localization/unscented_kalman_filter_localization.py", "src/simulations/localization/unscented_kalman_filter_localization/unscented_kalman_filter_localization.gif",
         "Propagates deterministic sigma points through true non-linear dynamics for accurate covariance."),
        ("Particle Filter (PF)", "src/simulations/localization/particle_filter_localization/particle_filter_localization.py", "src/simulations/localization/particle_filter_localization/particle_filter_localization.gif",
         "Monte-Carlo sequential importance sampling representing arbitrary non-Gaussian state distributions."),
        ("EKF vs UKF Comparison", "src/simulations/localization/ekf_vs_ukf_comparison/ekf_vs_ukf_comparison.py", "src/simulations/localization/ekf_vs_ukf_comparison/ekf_vs_ukf_comparison.gif",
         "Side-by-side performance comparison between EKF and UKF estimators."),
        ("EKF vs UKF vs Particle Filter", "src/simulations/localization/ekf_ukf_pf_comparison/ekf_ukf_pf_comparison.py", "src/simulations/localization/ekf_ukf_pf_comparison/ekf_ukf_pf_comparison.gif",
         "Triple comparison across non-linear dynamics and GNSS sensor noise."),
    ],
    "Path Planning": [
        ("A* Path Planning", "src/simulations/path_planning/astar_path_planning/astar_path_planning.py", "src/simulations/path_planning/astar_path_planning/astar_search.gif",
         "Heuristic grid search finding the shortest path from start to goal."),
        ("Bidirectional A*", "src/simulations/path_planning/astar_bidirectional_path_planning/astar_bidirectional_path_planning.py", "src/simulations/path_planning/astar_bidirectional_path_planning/astar_bidirectional_search.gif",
         "Searches simultaneously forward from start and backward from goal to speed up convergence."),
        ("Hybrid A*", "src/simulations/path_planning/astar_hybrid_path_planning/astar_hybrid_path_planning.py", "src/simulations/path_planning/astar_hybrid_path_planning/astar_hybrid_search.gif",
         "Kinematically feasible path planning using continuous vehicle heading and discrete grid cells."),
        ("Dijkstra Path Planning", "src/simulations/path_planning/dijkstra_path_planning/dijkstra_path_planning.py", "src/simulations/path_planning/dijkstra_path_planning/dijkstra_search.gif",
         "Classic graph search finding minimal path without heuristic guiding."),
        ("D* Path Planning", "src/simulations/path_planning/dstar_path_planning/dstar_path_planning.py", "src/simulations/path_planning/dstar_path_planning/dstar_search.gif",
         "Dynamic path re-planning in response to newly discovered obstacles."),
        ("RRT Path Planning", "src/simulations/path_planning/rrt_path_planning/rrt_path_planning.py", "src/simulations/path_planning/rrt_path_planning/rrt_search.gif",
         "Rapidly-exploring Random Tree randomly probing state space to connect start and goal."),
        ("RRT* Path Planning", "src/simulations/path_planning/rrt_star_path_planning/rrt_star_path_planning.py", "src/simulations/path_planning/rrt_star_path_planning/rrt_star_search.gif",
         "Asymptotically optimal RRT with neighborhood rewiring."),
        ("Informed RRT*", "src/simulations/path_planning/informed_rrt_star_path_planning/informed_rrt_star_path_planning.py", "src/simulations/path_planning/informed_rrt_star_path_planning/informed_rrt_star_search.gif",
         "Restricts sampling space to an ellipsoidal heuristic region once initial solution is found."),
        ("PRM Path Planning", "src/simulations/path_planning/prm_path_planning/prm_path_planning.py", "src/simulations/path_planning/prm_path_planning/prm_search.gif",
         "Probabilistic Roadmap building an obstacle-free network for multi-query routing."),
        ("Potential Field / Gradient", "src/simulations/path_planning/gradient_path_planning/gradient_path_planning.py", "src/simulations/path_planning/gradient_path_planning/gradient_descent_demo.gif",
         "Navigation using attractive force to target and repulsive field from obstacles."),
    ],
    "Mapping": [
        ("Binary Occupancy Grid Map", "src/simulations/mapping/binary_grid_map_construction/binary_grid_map_construction.py", "src/simulations/mapping/binary_grid_map_construction/binary_grid_map_construction.gif",
         "Classifies each world cell into occupied or free space from LiDAR point clouds."),
        ("Cost Grid Map", "src/simulations/mapping/cost_grid_map_construction/cost_grid_map_construction.py", "src/simulations/mapping/cost_grid_map_construction/cost_grid_map_construction.gif",
         "Assigns danger or traversal costs around detected obstacles."),
        ("NDT Map Construction", "src/simulations/mapping/ndt_map_construction/ndt_map_construction.py", "src/simulations/mapping/ndt_map_construction/ndt_map_construction.gif",
         "Normal Distributions Transform modeling local point density with Gaussian distributions."),
        ("Potential Field Map", "src/simulations/mapping/potential_field_map_construction/potential_field_map_construction.py", "src/simulations/mapping/potential_field_map_construction/potential_field_demo.gif",
         "Continuous potential gradient map around detected boundaries."),
        ("VFH Polar Histogram", "src/simulations/mapping/vfh_polar_histogram_construction/vfh_polar_histogram_construction.py", "src/simulations/mapping/vfh_polar_histogram_construction/vfh_polar_histogram_construction_demo.gif",
         "Vector Field Histogram for real-time obstacle avoidance heading selection."),
    ],
    "Perception": [
        ("LiDAR Obstacle Sensing", "src/simulations/perception/lidar_obstacle_sensing/lidar_obstacle_sensing.py", "src/simulations/perception/lidar_obstacle_sensing/lidar_obstacle_sensing.gif",
         "Simulates 2D range LiDAR scanning surrounding objects in vehicle local coordinates."),
        ("Point Cloud Rectangle Fitting", "src/simulations/perception/point_cloud_rectangle_fitting/point_cloud_rectangle_fitting.py", "src/simulations/perception/point_cloud_rectangle_fitting/point_cloud_rectangle_fitting.gif",
         "Fits bounding box rectangles to clustered obstacle scan points."),
        ("Sensor Auto Calibration", "src/simulations/perception/sensor_auto_calibration/sensor_auto_calibration.py", "src/simulations/perception/sensor_auto_calibration/sensor_auto_calibration.gif",
         "Calibrates mounting offset between vehicle center and sensor frame."),
    ]
}

# Sidebar
st.sidebar.title("🚗 AV Control Guide")
st.sidebar.markdown("**Interactive Simulation Explorer**")
category = st.sidebar.selectbox("Category", list(CATEGORIES.keys()))

algo_list = CATEGORIES[category]
algo_names = [a[0] for a in algo_list]
selected_algo_name = st.sidebar.selectbox("Algorithm", algo_names)

selected_algo = next(a for a in algo_list if a[0] == selected_algo_name)
title, py_path, gif_path, description = selected_algo

# Header
st.title(f"🚘 {title}")
st.caption(f"Category: **{category}**")
st.write(description)

col_anim, col_info = st.columns([1.2, 1])

with col_anim:
    st.subheader("Simulation Animation")
    full_gif_path = PROJECT_ROOT / gif_path
    if full_gif_path.exists():
        try:
            st.image(str(full_gif_path), caption=f"{title} (Animated Demo)", width="stretch")
        except TypeError:
            st.image(str(full_gif_path), caption=f"{title} (Animated Demo)", use_container_width=True)
    else:
        st.warning(f"Demo animation not found at: {gif_path}")

with col_info:
    st.subheader("How to Run Live")
    st.markdown("To run the live interactive Matplotlib animation window with full controls on your desktop:")
    cmd = f"python {py_path}"
    st.code(f"cd \"{PROJECT_ROOT}\"\n{cmd}", language="powershell")
    
    st.subheader("Source Code")
    full_py_path = PROJECT_ROOT / py_path
    if full_py_path.exists():
        with st.expander(f"View {Path(py_path).name}", expanded=False):
            code_text = full_py_path.read_text(encoding="utf-8")
            st.code(code_text, language="python")

st.divider()
st.subheader("📋 All Algorithms Quick Matrix")
overview_data = []
for cat, items in CATEGORIES.items():
    for name, path, _, desc in items:
        overview_data.append({"Category": cat, "Algorithm": name, "Script": Path(path).name, "Summary": desc})
try:
    st.dataframe(overview_data, width="stretch")
except TypeError:
    st.dataframe(overview_data, use_container_width=True)

