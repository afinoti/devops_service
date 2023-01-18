import json


class my_example_service:
    def __init__(self):
        print("init")

    def echo(self, path, args, load):
        """Reverse and return the provided URI"""
        output = {"path": path, "arg": args, "load": load}
        return json.dumps(output, indent=2, sort_keys=True)

    def process(self, path, arg, load):
        print(f"arg:{arg}")
        return "".join(reversed(arg))
