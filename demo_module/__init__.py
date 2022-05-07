import pathlib
import sys

# append an additional location where to look for Python modules
sys.path.append(f"{pathlib.Path(__file__).parent.resolve()}/dependencies")

from loader import register

from . import main

register(sys.modules[__name__], {"id": __name__, "name": "demo", "actions": {"get_public_ip": main.get_public_ip}})
