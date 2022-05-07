# Demo Module

This module is meant for a demonstrational purpose to show how a module can be created and dynamically mounted to a running service.

The module could come with additional dependencies that are not present in the hosting server.

## Building

The command below with generate a `demo_module.zip` file which includes source code and dependencies.

```bash
make build
```

## Development

module self registers to a central registry. Because of that, there are some rules to adhere. The [`__init__.py`](./__init__.py) file needs to import register function and provide details about itself.

```python
from loader import register

register(sys.modules[__name__], {"id": __name__, "name": "demo", "actions": {"get_public_ip": main.get_public_ip}})
```
`id`, `name` and `actions` parameters are *required*.
