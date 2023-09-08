from xmlrpc.server import SimpleXMLRPCServer

with SimpleXMLRPCServer(('0.0.0.0', 8001)) as server:

    def add_num(x, y):
        return x + y

    server.register_function(add_num, "add_num")
    server.serve_forever()