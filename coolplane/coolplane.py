#!/usr/bin/python3
import sys, os

# Working Directory
cwd = os.getcwd()
sys.path.append(cwd)

# Blender imports
import bpy, bgl, blf

from math import *
from mathutils import *

def create_plane():
    bpy.ops.mech.primitive_plane_add()

def coolplane():
    # Camera
    scene = bpy.data.scenes["Scene"]

    # Set camera location
    coords = {"x": "0", "y": "0", "z": "15"}
    for key, val in coords.items():
        print(key, val)
        exec("scene.camera.location." + key + " = " + val)

    # Set cursor to center
    bpy.context.scene.cursor_location = (0.0, 0.0, 0.0)

coolplane()
#create_plane)

