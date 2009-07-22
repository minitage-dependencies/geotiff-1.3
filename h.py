
import os

def h(o, b):
    os.environ['LDFLAGS'] = os.environ['LDFLAGS'].replace('-Wl,-rpath -Wl', '-L')


