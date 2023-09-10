import contextlib

class tag(contextlib.ContextDecorator):
    def __init__(self, name):
        self.name = name
        self.start_tag = '<{}>'.format(name)
        self.end_tag = '</{}>'.format(name)

    def __enter__(self):
        print(self.start_tag)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(self.end_tag)
        print(exc_type)
        print(exc_val)
        print(exc_tb)

with tag('tag2'):
    print('test')
    raise Exception('error')