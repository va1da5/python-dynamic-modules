import sys

from loader import register

from . import main

register(sys.modules[__name__], {"id": __name__, "name": "hello_world", "actions": {"handle": main.handle}})
