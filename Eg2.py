class Gate ( object ):
    def __init__(self):
        self.value = None

    def logic(self, *args):
        self.input = args
        raise NotImplementedError

    def output(self):
        return self.value


class AndGate (Gate):
    def __init__(self):
        super(AndGate, self).__init__()

    def logic(self, *args):
        self.value = args[0] and args[1]
        return self.value

    def output(self):
        return self.value


class OrGate (Gate):
    def __init__(self):
        super(OrGate, self).__init__()

    def logic(self, *args):
        self.value = args[0] or args[1]
        return self.value

    def output(self):
        return self.value


class NotGate (Gate):
    def __init__(self):
        super(NotGate, self).__init__()

    def logic(self, *args):
        self.value = not args[0]
        return self.value

    def output(self):
        return self.value


class NandGate (AndGate, NotGate):
    def __init__(self):
        super(NandGate, self).__init__()

    def logic(self, *args):
        self.value = NotGate.logic(self, AndGate.logic(self, *args))
        return self.value

    def output(self):
        return self.value


class NorGate (OrGate, NotGate):
    def __init__(self):
        super(NorGate, self).__init__()

    def logic(self, *args):
        self.value = NotGate.logic(self, OrGate.logic(self, *args))
        return self.value

    def output(self):
        return self.value


# Nand Gate Example
nandGate = NandGate()
nandGate.logic(1, 1)
print(nandGate.output())
nandGate.logic(0, 1)
print(nandGate.output())

# Nor Gate Example
norGate = NorGate()
norGate.logic(1, 0)
print(norGate.output())
norGate.logic(0, 0)
print(norGate.output())
