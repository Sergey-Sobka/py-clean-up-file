import os


def run(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    _, src, dst = parts

    if src == dst:
        return

    if not os.path.exists(src):
        return

    with open(src, "r") as fsrc, open(dst, "w") as fdst:
        fdst.write(fsrc.read())