COMMANDS_DICT = {}


def register(name: str, func: callable) -> None:
    COMMANDS_DICT[name] = func


def arguments_to_dict(args: list[str]) -> dict[str, str | bool]:
    kwarguments = {}
    for arg in args:
        if "=" not in arg:
            kwarguments[arg] = True
            continue

        key, value = arg.split("=")
        kwarguments[key.strip()] = value.strip()
    return kwarguments
