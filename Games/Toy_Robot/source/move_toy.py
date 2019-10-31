class Move(object):

    # This function will move the toy robot by one step in current direction,
    # till robot is not falling from table.
    def move_robot(self):
        cx, cy = self.curr_pos
        if self.curr_dir == "NORTH" and -1 < cy + 1 < self.table_height:
            self.curr_pos = cx, cy + 1
        elif self.curr_dir == "SOUTH" and -1 < cy - 1 < self.table_height:
            self.curr_pos = cx, cy - 1
        elif self.curr_dir == "EAST" and -1 < cx + 1 < self.table_width:
            self.curr_pos = cx + 1, cy
        elif self.curr_dir == "WEST" and -1 < cx - 1 < self.table_width:
            self.curr_pos = cx - 1, cy