import sys
from ruamel.yaml import YAML
import toml
import json

yaml = YAML()


def edit_yaml(file: str, key: str, value: str):
    keypart_lst = key.split(".")
    with open(file, "r") as fp:
        data = yaml.load(fp)
    elem = data
    for keypart in keypart_lst[:-1]:
        elem = elem[keypart]
    elem[keypart_lst[-1]] = value
    with open(file, "w") as fp:
        yaml.dump(data, fp)
    return True


def edit_toml(file: str, key: str, value: str):
    keypart_lst = key.split(".")
    with open(file, "r") as fp:
        data = toml.load(fp)
    elem = data
    for keypart in keypart_lst[:-1]:
        elem = elem[keypart]
    elem[keypart_lst[-1]] = value
    with open(file, "w") as fp:
        toml.dump(data, fp)
    return True


def edit_json(file: str, key: str, value: str):
    keypart_lst = key.split(".")
    with open(file, "r") as fp:
        data = yaml.load(fp)
    elem = data
    for keypart in keypart_lst[:-1]:
        elem = elem[keypart]
    elem[keypart_lst[-1]] = value
    with open(file, "w") as fp:
        json.dump(data, fp)
    return True


if __name__ == "__main__":
    file = str(sys.argv[1])
    key = str(sys.argv[2])
    value = str(sys.argv[3])
    ext = file.split(".")[-1]
    print(f"::debug :: Editing file {file}, with the key {key} to the value {value}")

    if ext in ["yaml", "yml"]:
        edit_yaml(file, key, value)
    elif ext in ["toml"]:
        edit_toml(file, key, value)
    elif ext in ["json"]:
        edit_json(file, key, value)
    else:
        raise NotImplemented(f"The extension {ext} is not implemented")
    print(f"::debug :: File {str(sys.argv[1])} edited")
