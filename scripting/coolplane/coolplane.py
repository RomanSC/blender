#!/usr/bin/python3
# Get working directory and append to path
import os, sys; cwd = os.getcwd(); sys.path.append(cwd)

# from importlib import reload

# Blender imports
import bpy, bgl, blf

from math import *
from mathutils import *

def make_coolplane(plane):
    # Subdivide and make shape
    plane.select = True
    bpy.ops.object.mode_set(mode="EDIT")

    bpy.ops.mesh.subdivide(number_cuts=10, fractal=0.5, fractal_along_normal=0.25, seed=8)

    # TODO:
    # Use material and shaders
    # Add material
    # bpy.context.space_data.context = "MATERIAL"
    # bpy.ops.material.new()
    # bpy.ops.object.material_slot_assign()
    # bpy.context.object.active_material.use_nodes = True


def create_plane():
    bpy.ops.mesh.primitive_plane_add()

    xyz = {"x": "8", "y": "8", "z": "8"}
    for key, val in xyz.items():
        # hack
        exec("bpy.data.objects[\"Plane\"].scale." + key + " = " + val)


def delete_cube_and_lamp():
    """ Source - Stack Exchange:

        https://blender.stackexchange.com/questions/27234/python-how-to-completely-remove-an-object

    """
    # Deselect all
    bpy.ops.object.select_all(action="DESELECT")

    # Select cube and lamp
    bpy.data.objects['Cube'].select = True
    bpy.data.objects['Lamp'].select = True

    # Delete them
    bpy.ops.object.delete()

    # Deselect all again
    bpy.ops.object.select_all(action="DESELECT")

def cursor_and_cam():
    # Camera
    scene = bpy.data.scenes["Scene"]

    # Set camera location
    xyz = {"x": "0", "y": "0", "z": "15"}
    for key, val in xyz.items():
        # hack
        exec("scene.camera.location." + key + " = " + val)

    # Set camera rotation
    xyz = {"x": "0", "y": "0", "z": "0"}
    for key, val in xyz.items():
        exec("scene.camera.rotation_euler." + key + " = " + val)

    # Set cursor to center
    bpy.context.scene.cursor_location = (0.0, 0.0, 0.0)

def main():
    cursor_and_cam()
    delete_cube_and_lamp()
    create_plane()

    plane = bpy.data.objects["Plane"]

    make_coolplane(plane)

if __name__ == "__main__":
    main()

