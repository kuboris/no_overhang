# Script assuming the object is currently in Edit Mode
# with selected faces

import bpy
import bmesh
import math
import random
import mathutils
from mathutils import Vector
import logging

obj = bpy.context.edit_object
me = obj.data
bm = bmesh.from_edit_mesh(me)
# Todo this seems to not work if whole object is rotated
z_negative = Vector((0,0,-1))
OVERHANG_ANGLE = 45
# Do not rotate the face if it's center is bellow this z point.
# Should in theory work for keeping base flat
MIN_Z = 0
# What angle from horizontal plane to check
check_angle = 90 - OVERHANG_ANGLE

# Return degrees of rotation
def angle_from_vector(vec , vec2):
    print('original_vector')
    print(vec)
    angle = vec.angle(vec2)
    return math.degrees(angle)

selected_faces = [f for f in bm.faces if f.select]

for f in selected_faces:
        f.select = False;

for f in selected_faces:
    f.select = True  # Select face in edit mode.
    normal = f.normal
    # Skip if center under z 0
    z_point = f.calc_center_median()[2]
    print('Zpoint')
    print(z_point)
    # Calculate angle of normal towards -z:
    normal_angle = angle_from_vector(normal, z_negative)
    print('normal_angle')
    logging.info(normal_angle)
    # This should calculate direct vector to Z
    axis = normal.cross(z_negative)
    if axis[0] == 0:
        x_share = 0
    else:
        # Well this is extreme oversimplification rotate face
        # by ratio of rotation towards z in x and y axis. 
        # Needs to be sanitized
        x_share = abs(axis[0])/(abs(axis[0]) + abs(axis[1]))
        
    y_share = 1 - x_share
    # If its less than ~45 degrees from negative -z vector
    # try to rotate it to be at least 45 degrees from -z vector
    if normal_angle < (check_angle - 1) and z_point > MIN_Z:
        rotate_by = check_angle - normal_angle
        ro_x = math.radians(rotate_by * x_share)
        if axis[0] < 0:
            ro_x = -ro_x
        ro_y = math.radians(rotate_by * y_share)
        if axis[1] < 0:
            ro_y = -ro_y
        print('Ro_x, ro_y')
        print(ro_x)
        print(ro_y)
        print('Rotate by')
        print(rotate_by)
        print('X_share, Y_share')
        print(x_share)
        print(y_share)
        # This could be somehow streamlined but I don't know how to rotate along normal
        # All the share calculation could be then removed.
        bpy.ops.transform.rotate(value=ro_y, orient_axis='Y')
        bpy.ops.transform.rotate(value=ro_x, orient_axis='X')
        # TODO: This could contain a lot of check to see whether rotation creates a spike
        # TODO: maybe rotate in such a way that faces below are not affected
    
    f.select = False

for f in selected_faces:
        f.select = True;            ## ReSelect the original polys

bmesh.update_edit_mesh(me, True)
