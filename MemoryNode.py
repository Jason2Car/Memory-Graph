class MemoryNode:
    #name is planned to be an identifier for this memory/associated object
    #semantic is planned to be an array holding the semantic info about this memory/associated object
    #connections is planned to be an array holding the connections to other memory nodes, may need to make a edge class for specical connections

    #constructor
    def __init__(self, name, semantic, connections):
        self.name = name
        self.semantic = semantic
        self.connections = connections

    #getters and setters
    def set_name(self, name):
        self.name = name

    def set_semantic(self, semantic):
        self.semantic = semantic

    def set_connections(self, connections):
        self.connections = connections

    def get_name(self):
        return self.name

    def get_semantic(self):
        return self.semantic

    def get_connections(self):
        return self.connections
