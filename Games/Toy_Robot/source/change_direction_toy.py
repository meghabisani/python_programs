class ChangeDirection(object):

    # This function will turn the direction of toy robot
    def change_dir_robot(self, dir_cmd):
        ind = self.directions.index(self.curr_dir)
        if dir_cmd == "LEFT":
            if ind > 0:
                self.curr_dir = self.directions[ind - 1]
            else:
                self.curr_dir = self.directions[3]
        elif dir_cmd == "RIGHT":
            if ind < 3:
                self.curr_dir = self.directions[ind + 1]
            else:
                self.curr_dir = self.directions[0]