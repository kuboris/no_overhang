# Automatically remove overhangs in any 3d print
Magic/Automatic removal of overhangs in any object.

- Do you hate overhangs with passion, 
- Do you despise removing support structures,
- Do you crave for smooth 3d texture?

If you do, then this tool is for you. 

## What is it?
Blender scripting code that rotates all object faces to be at least X amount of degrees (45 by default) from horizontal plane.
In default configuration it just colors all the overhangs with red color.

## How?
1) Open object in Blender in edit mode.
2) Select all the faces.(Preferably deselect faces on the bottom to avoid rotating them)
3) Paste script into the scripting window.
4) Alter OVERHANG_ANGLE and MIN_Z variables according to your needs.
5) Run it, wait....(will be pretty slow on detailed geometries)
6) Magically all the faces should be facing at least X degrees from the horizontal plane.

## Wait... Does that work?
YES!*

*Meaning it does what it's supposed to do.. that is rotating faces. However it can do pretty
unexpecting things as it has a "few" known edgecases/bugs.
There are few "small" issues you can encounter(and hopefully fix with a pull request)
1) It doesn't work when the opened object is rotated in blender before running the script.(Requires fix)
2) Rotation of the face alters faces around it little and script needs to be run multiple times.(Requires smart fix)
3) Because rotation alters faces around it bottom faces(base) can be warped even if not selected.(Requires fix)
4) Even if the face is 45degrees angle it doesn't mean it's printable as the bottom edge could still be under an angle bigger than 45 degrees.
5) "Fixed" objects can have "spikes" pointing down that would still require supports - but only in 1 point.
6) Ignores bridging.
7) It's very slow in big geometries. (However works very well for low poly 3d prints :) )

## Example
![Screenshot from 2021-11-29 21-48-41](https://user-images.githubusercontent.com/5594182/143940879-6f5114d7-e20a-40d8-be8e-17e00133b81a.png)
On the left is the original Stanford bunny. On the right is a fixed one.
Blue faces are overhangs that were taken care of by the script.

## Why
This approach with much better implementation has actually pretty strong applications for decorative prints.
Please, anyone knowing blender/3d printing could add a pull request and fix any of the bugs.
