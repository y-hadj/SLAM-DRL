# Goal-Driven Fully Autonomous Exploration through DRL

## Table of Contents
- [Project Description](#project-description)
- [Project Contents](#project-contents)
- [Disclaimer](#disclaimer)
- [Contact](#contact)

## Project Description
This repository consists of an implementation of a DRL-based robot exploration approach. The local navigation stack of the robot is trained using a TD3 neural network to get to the local goals optimally and safely. These points are generated following heuristics that take into consideration the characteristics of the surrounding area as well as the original mission: mapping an unknown environment.


## Project Contents
The project includes the following components:

- **Source Code:** that is a ROS Noetic put-together package containing the (trained) local planner as well as the global planner and mapping plugin of the robot.

- **TD3 Package:** that contains the necessary and put-together files for training the local navigation stack of the robot using the TD3 network.

- **Report File:** that explains in full detail the whole process of waypoints generation, selection, navigation, and mapping.

## Disclaimer
This project is based on the work of [Reinis Cimurs](https://github.com/reiniscimurs), with more built-in and completed files that you can directly execute. Proper citation is made in the Report file as well.

## Contact
Feel free to explore and use the project files. If you have any technical questions or feedback please don't hesitate to reach out.

- [Linkedin Profile](https://www.linkedin.com/in/yhadj/)
- [Email](mailto:yasser.hadj@g.enp.edu.dz)
