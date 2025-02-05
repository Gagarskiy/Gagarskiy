import bpy

bpy.ops.mesh.primitive_cube_add(
    size=1,
    calc_uvs=True,
    enter_editmode=False,
    align='WORLD',
    location=(0, 0, 1),
    rotation=(0, 0, 0),
    scale=(1, 1, 2))

bpy.ops.mesh.primitive_cube_add(
    size=1,
    calc_uvs=True,
    enter_editmode=False,
    align='WORLD',
    location=(0, 0, 2.5),
    rotation=(0, 0, 0),
    scale=(1, 2.5, 1))
