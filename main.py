import sys
from ruamel.yaml import YAML

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


if __name__ == "__main__":
    print(
        f"::debug :: Editing file {str(sys.argv[1])}, with the key {str(sys.argv[2])} to the value {str(sys.argv[3])}"
    )
    vers = edit_yaml(str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]))
    print(f"::debug :: File {str(sys.argv[1])} edited")
