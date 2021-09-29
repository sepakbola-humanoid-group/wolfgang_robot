#!/usr/bin/env python3
import argparse

from wolfgang_pybullet_sim.ros_interface import ROSInterface
from wolfgang_pybullet_sim.simulation import Simulation

parser = argparse.ArgumentParser()
parser.add_argument('--robot_name', default="amy",
                    help="which robot should be started")
parser.add_argument('--robot_type', default="wolfgang",
                    help="which robot type should be started")
args, unknown = parser.parse_known_args()

if __name__ == "__main__":
    simulation = Simulation(False, robot=args.robot_type)
    ros_interface = ROSInterface(simulation, namespace=f"/{args.robot_name}/")
    ros_interface.run_simulation()
