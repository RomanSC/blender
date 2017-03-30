#!/usr/bin/python3
# Get working directory and append to path
import os, sys
cwd = os.getcwd()
sys.path.append(cwd)

# from importlib import reload

# Blender imports
import bpy, bgl, blf

from math import *
from mathutils import *
import random

from mycolors import gimme_color

def rainbow_render(savedir, rainbow):
    for x in range(len(rainbow)):
        change_color(rainbow[x])

        # TODO:
        # Move to render mode
        # Render
        # Then save to savedir

        cool_save(savedir, str(x))

def cool_save(savedir, filename):
    os.chdir(savedir)

    # You'll wanna check out this source for saving and rendering
    # shots around an object
    # https://stackoverflow.com/questions/14982836/rendering-and-saving-images-through-blender-python
    scene = bpy.data.scenes['Scene']

    scene.render.filepath = filename
    bpy.ops.render.render(write_still=True)

    os.chdir("..")

def make_savedir(savedir):
    if not os.path.exists(savedir):
        os.makedirs(savedir)

def change_color(color):
    spot = bpy.data.objects["Spot"]
    spot.data.color = color

def default_color():
    spot = bpy.data.objects["Spot"]
    spot.data.falloff_type = "LINEAR_QUADRATIC_WEIGHTED"
    #spot.data.use_diffuse = False
    spot.data.use_diffuse = True
    spot.data.distance = 600
    spot.data.color = (0.7, 0.7, 0.7)

def cool_lamp():
    bpy.ops.object.mode_set(mode="OBJECT")

    bpy.ops.object.lamp_add(type="SPOT",
                            radius=3,
                            location=(0, 0, 38)
                            )

    bpy.context.object.data.energy = 1.3333333333333333333333

    # Set default colors
    default_color()

def make_coolplane(plane, random=False):
    # Subdivide and make shape
    plane.select = True
    bpy.ops.object.mode_set(mode="EDIT")

    # Default is to not use a random seed
    if not random:
        bpy.ops.mesh.subdivide(number_cuts=20,
                               fractal=0.333,
                               fractal_along_normal=0.111)
    else:
        mynums = [i for i in range(30)]
        myrand_num = random.choice(mynums)


        bpy.ops.mesh.subdivide(number_cuts=20,
                               fractal=0.333,
                               fractal_along_normal=0.111,
                               seed=myrand_num)

        bpy.ops.uv.unwrap(method="ANGLE_BASED",
                          margin=0.001)

def create_plane():
    bpy.ops.mesh.primitive_plane_add()

    xyz = {"x": "10", "y": "10", "z": "10"}
    for key, val in xyz.items():
        # hack
        exec("bpy.data.objects[\"Plane\"].scale." + key + " = " + val)

    ob = bpy.context.object
    ob.name = 'Coolplane'

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

def cursor_and_cam(res=[1920, 1080]):
    # Camera
    scene = bpy.data.scenes["Scene"]

    # Set camera location
    xyz = {"x": "0", "y": "0", "z": "18"}
    for key, val in xyz.items():
        # hack
        exec("scene.camera.location." + key + " = " + val)

    # Set camera rotation
    xyz = {"x": "0", "y": "0", "z": "0"}
    for key, val in xyz.items():
        exec("scene.camera.rotation_euler." + key + " = " + val)

    # Set cursor to center
    bpy.context.scene.cursor_location = (0.0, 0.0, 0.0)
    scene.render.resolution_x = res[0]
    scene.render.resolution_y = res[1]
    scene.render.resolution_percentage = 100

def main():
    res = [1920, 1200]
    cursor_and_cam(res)

    savedir = "fractals/"

    make_savedir(savedir)

    # if not savedir.endswith("/"):
    #     savedir = "/"
    #     print(savedir)

    # Remove default cube and lamp objects
    delete_cube_and_lamp()

    # Create a plane for late modding
    create_plane()

    plane = bpy.data.objects["Coolplane"]

    # Subdivide and apply fractal
    make_coolplane(plane)

    # Create lamp used for coloring
    cool_lamp()

    # Change lamp color
    # color = (0.0253, 0, 1)
    color = (0.11, 0, -0.78)
    change_color(color)

    # How to use:
    # https://krazydad.com/tutorials/makecolors.php
    # center = 128
    # width = 127
    # frequency = 2.4
    # rainbow = gimme_color(frequency,frequency,frequency,0,2,4,center,width,50);

    # center = 128
    # width = 127
    # frequency = 0.10
    # rainbow = gimme_color(frequency,frequency,frequency,0,2,4,center,width,50);

    rainbow = gimme_color(1,1,1,0,2,4);

    rainbow_render(savedir, rainbow)

    # cool_save(savedir, "test")

if __name__ == "__main__":
    main()

