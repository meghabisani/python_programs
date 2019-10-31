from place_toy import Place
from report_toy import Report
from move_toy import Move
from change_direction_toy import ChangeDirection
import sys


# This is the driver class which will control and manage the flow of toy robot
# against any number of valid or invalid arguments
class RobotSimulator(Place, Report, Move, ChangeDirection):
    start = [0, 0]

    def __init__(self):
        self.flag = True
        self.exit = "REPORT"
        self.curr_pos = self.start[:]
        self.curr_dir = "SOUTH EAST"
        self.directions = ["EAST", "SOUTH", "WEST", "NORTH"]
        self.table_width = 5
        self.table_height = 5

    def choose_option(self, step):
        if step.partition(' ')[0] == "PLACE":
            self.place_robot(step)
        elif step == "MOVE":
            self.move_robot()
        elif step == "LEFT" or step == "RIGHT":
            self.change_dir_robot(step)
        elif step == self.exit:  # when REPORT input is given, print the current toy's position and exit.
            self.report_robot()

    def main(self):
        place_check = False
        if len(sys.argv) == 2:
            with open(sys.argv[1], 'r') as f:
                commands = list(filter(None, [name.rstrip() for name in f]))
            for cmd in commands:
                if self.flag:
                    if self.place_robot(cmd) and not place_check:
                        place_check = True
                    elif place_check:
                        self.choose_option(cmd)
                    else:
                        continue
                else:
                    break
        else:
            print("Please give valid file based input")


obj = RobotSimulator()
obj.main()
