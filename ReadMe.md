# Goal-Driven Fully Autonomous Exploration through DRL

## Table of Contents
- [Project Description](#project-description)
- [Project Contents](#project-contents)
- [Contact](#contact)
- [Disclaimer](#disclaimer)

## Project Description
This repository consist of an implementation of a DRL-based robot exploration approache. The local navigation stack of the robot is trained using a TD3 neural network to get to the local goals in an optimal and safe manner. These points are generatede following a heuristics that takes into consideration the characteristics of the surronding area as well as the original mission: mapping an unknown environment.


## Project Contents
The project includes the following components:

- **Source Code:** that is a ROS Noetic put-together package containing the (trained) local planner as well as the global planner and mapping plugin of the robot.

- **TD3 Package:** that contains the necessary and put-together files for training the local navigation stack of the robot using the TD3 network.

- **Report File:** that explains in full details the whole process of way points generation, selection, navigation, and mapping.

## Disclaimer
This project is based on the work of [Reinis Cimurs](https://github.com/reiniscimurs), with more built in and completed files that you can directly execute. Proper citation is made in the Report file as well.

## Contact
Feel free to explore and use the project files. If you have any technical questions or feedback please don't hesitate to reach out.

- [Linkedin Profile](https://www.linkedin.com/in/yhadj/)
- [Email](mailto:yasser.hadj@g.enp.edu.dz)