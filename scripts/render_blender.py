import subprocess
import sys


def render(path: str):
    cmd = [
        "blender",
        "-b",
        path,
        "-o",
        "/data/output/frame_####",
        "-F",
        "PNG",
        "-x",
        "1",
        "-a",
    ]
    subprocess.check_call(cmd)


if __name__ == "__main__":
    render(sys.argv[-1])
