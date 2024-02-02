class Operation:

    def __init__(self, id, date, state, opAm, dscr, fr, to):
        self.id = id
        self.date = date
        self.state = state
        self.opAm = opAm
        self.dscr = dscr
        self.fr = fr
        self.to = to

    def state_operation(self):
        if self.state == "EXECUTED":
            return True
        else:
            return False

    def right_date(self):
        self.rightdate = self.date.strip()


