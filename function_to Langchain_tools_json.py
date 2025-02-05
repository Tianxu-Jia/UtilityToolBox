import inspect
import json
from typing import get_type_hints


def function_to_tool_json(func):
    if inspect.isfunction(func):
        obj_type = "function"
    elif inspect.isclass(func):
        obj_type = "class"
    else:
        return -1
    # Get function name and docstring
    tool_name = func.__name__
    description = inspect.getdoc(func) or "No description provided."

    # Use type hints to build the parameter schema
    sig = inspect.signature(func)
    type_hints = get_type_hints(func)

    properties = {}
    required = []
    for name, param in sig.parameters.items():
        # If a parameter doesn't have a default, consider it required
        if param.default is inspect.Parameter.empty:
            required.append(name)
        # Use type hints if available, otherwise default to string
        param_type = type_hints.get(name, str).__name__
        properties[name] = {"type": param_type, "description": f"Parameter {name}"}

    tool_json = {
        "type": obj_type,
        obj_type: {
            "name": tool_name,
            "description": description,
            "parameters": {
                "type": "object",
                "properties": properties,
                "required": required,
            },
        },
    }
    return json.dumps(tool_json, indent=2)


# Example usage:
def my_tool(x: int, y: float = 3.14):
    """
    This tool does something interesting with x and y.
    """
    return x * y


print(function_to_tool_json(my_tool))
debug = 1
