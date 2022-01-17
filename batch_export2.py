import bpy
import os
from math import radians

ratios = [0.5]

bpy.ops.import_scene.gltf(filepath='/Users/a.delforges/Documents/BlenderDecimation/input.glb')

# switch in edit mode for cleanup - decimate option
bpy.ops.object.editmode_toggle()

# get all object in scene
objectList=bpy.data.objects

# filter by mesh
meshes = []
for obj in objectList:
  if(obj.type == "MESH"):
    meshes.append(obj)

print("{} meshes".format(len(meshes)))

# decimate all objects with a 0.5 ratio
for i, obj in enumerate(meshes):
  bpy.context.view_layer.objects.active = obj
  print("{}/{} meshes, name: {}".format(i, len(meshes), obj.name))
  print("{} has {} verts, {} edges, {} polys".format(obj.name, len(obj.data.vertices), len(obj.data.edges), len(obj.data.polygons)))
  bpy.ops.mesh.decimate(ratio=0.5)
  print("{} has {} verts, {} edges, {} polys after decimation".format(obj.name, len(obj.data.vertices), len(obj.data.edges), len(obj.data.polygons)))


basedir = os.path.dirname(bpy.data.filepath)
fn = os.path.join(basedir, "input_LOD" + str(0.5))
bpy.ops.export_scene.gltf(filepath=fn + ".glb", export_apply=True)


