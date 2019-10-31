from __future__ import print_function


class Report(object):

    # This function will display/output the current valid position and direction of the toy robot
    def report_robot(self):
        print(self.curr_pos[0], self.curr_pos[1], self.curr_dir, sep=',')
        self.flag = False
