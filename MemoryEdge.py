class MemoryEdge:
    #source is planned to be the starting memory node
    #target is planned to be the ending memory node
    #weight is planned to be a value representing the strength of the connection

    #constructor
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight

    #getters and setters
    def set_source(self, source):
        self.source = source

    def set_target(self, target):
        self.target = target

    def set_weight(self, weight):
        self.weight = weight

    def get_source(self):
        return self.source

    def get_target(self):
        return self.target

    def get_weight(self):
        return self.weight
