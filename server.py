from SimpleXMLRPCServer import SimpleXMLRPCServer

server = SimpleXMLRPCServer(("127.0.0.1", 8000), allow_none=True)

print "Server started on port 8000"

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

server.register_function(add, "add")
server.register_function(subtract, "subtract")

server.serve_forever()