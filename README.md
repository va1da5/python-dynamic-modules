# Python Dynamic Module Loader

A proof-of-concept solution for dynamically loading Python modules and extending the existing service functionality.

## Usage

```bash
# start API server
make api

# bundle demo module
cd demo_module; make build; cd ..

# upload demo module using API
curl -F 'file=@demo_module/demo_module.zip' http://127.0.0.1:8000/install

# list modules
curl http://127.0.0.1:8000/ | jq

# execute demo action
curl -sX POST http://127.0.0.1:8000/run/demo/get_public_ip | jq
```

## References

- [The Power Of The Plugin Architecture In Python](https://www.youtube.com/watch?v=iCE1bDoit9Q&ab_channel=ArjanCodes)
- [importlib — The implementation of import](https://docs.python.org/3/library/importlib.html#importlib.import_module)
- [Python import: Advanced Techniques and Tips](https://realpython.com/python-import/)
- [Plugin Architecture in Python](https://dev.to/charlesw001/plugin-architecture-in-python-jla)
- [Building a plugin architecture with Python](https://mwax911.medium.com/building-a-plugin-architecture-with-python-7b4ab39ad4fc)
- [Creating and discovering plugins](https://packaging.python.org/en/latest/guides/creating-and-discovering-plugins/)
- [Implementing a Plugin Architecture in a Python Application](https://alysivji.github.io/simple-plugin-system.html)
- [How to Design and Implement a Plugin Architecture in Python](https://mathieularose.com/plugin-architecture-in-python)
- [dorneanu/plugin_architecture.md](https://gist.github.com/dorneanu/cce1cd6711969d581873a88e0257e312)
- [pluggy - A minimalist production ready plugin system](https://github.com/pytest-dev/pluggy/)
- [🐍 Pluggable Architecture with Python](https://waylonwalker.com/python-pluggable-architecture/)
- [A Python Plugin Pattern](https://www.vinnie.work/blog/2021-02-16-python-plugin-pattern/)
- [Plugin Architecture For Your Code Using pyplugs in Python3](https://pythonhowtoprogram.com/plugin-architecture-for-your-code-using-pyplugs-in-python3/)
- [HOW TO CREATE A PYTHON PLUGIN SYSTEM WITH STEVEDORE](https://chinghwayu.com/2021/11/how-to-create-a-python-plugin-system-with-stevedore/)

