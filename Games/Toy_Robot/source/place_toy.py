import re


class Place(object):

    # This function will place the toy robot in the user-given location,
    # will keep asking user until a valid input is given.
    def place_robot(self, place_cmd):
        regex = r"^PLACE ([0-4]),([0-4]),(EAST|WEST|SOUTH|NORTH)$"
        cmd_parts = re.search(regex,place_cmd)
        if cmd_parts:
            self.curr_pos = [int(cmd_parts.group(1)), int(cmd_parts.group(2))]
            self.curr_dir = cmd_parts.group(3)
            return True
        else:
            return False
