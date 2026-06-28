import bpy
import sys


def convert(path: str):
    bpy.ops.wm.open_mainfile(filepath=path)
    for material in bpy.data.materials:
        if not material.use_nodes:
            continue
        nodes = material.node_tree.nodes
        principled = nodes.new("ShaderNodeBsdfPrincipled")
        nodes.clear()
        nodes.append(principled)
    bpy.ops.wm.save_mainfile(filepath=path)


if __name__ == "__main__":
    convert(sys.argv[-1])
