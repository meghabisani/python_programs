Toy_Robot
----------------------------------------------------------------
A simulator of a Toy_Robot, moving around a tabletop


Introduction
----------------------------------------------------------------
This software simulates a movement of toy robot on and around a square tabletop of dimensions 5 units x 5 units. The robot can be placed, moved, turn and made to report it's location. It will never move or fall off the table to destruction, and must be placed before it will respond to additional commands.
For problem statement refer PROBLEM.md

Design
----------------------------------------------------------------
Refer to 'Toy_Robot/development/00_Approach_Design_Development.txt' for the Design and Development Approach

Installation
----------------------------------------------------------------
Ensure you have Python 3.x is installed.

Execution
----------------------------------------------------------------
To run the simulator, change directory to 
'Toy_Robot/source/'
python toy_robot.py file_name.txt

Instructions must be provided via file_name.txt. List of steps intended for robot must be listed in file_name.txt,
one command per line.


Test Approach and Design 
----------------------------------------------------------------
Refer to detailed testing guide '00_Guide_Test_Case_Design_and_Considerations.txt' for Automated
and non Automated Functional Test cases.


Testing
----------------------------------------------------------------
For Automation Tests;
change directory to 
'Toy_Robot/testing'

Execute;
python automated_test.py

This will execute all the test case files present in 
'Toy_Robot/testing/Test_Cases/'

Output will be reported in 
'Toy_Robot/testing/monitor.log' and
as well as command prompt.
