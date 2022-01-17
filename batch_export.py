import bpy
import os
from math import radians

##Cleans all decimate modifiers
def cleanAllDecimateModifiers(obj):
    for m in obj.modifiers:
        if(m.type=="DECIMATE"):
#           print("Removing modifier ")
            obj.modifiers.remove(modifier=m)

modifierName='DecimateMod'
planarAngles = [0, 1, 5, 10, 30]

bpy.ops.import_scene.gltf(filepath='/Users/a.delforges/Documents/BlenderDecimation/input.glb')

objectList=bpy.data.objects

for planarAngle in planarAngles:
    for obj in objectList:
        if(obj.type=="MESH"):

            cleanAllDecimateModifiers(obj)

            modifier=obj.modifiers.new(modifierName,'DECIMATE')
            modifier.decimate_type = "DISSOLVE"
            modifier.angle_limit = radians(planarAngle)

    basedir = os.path.dirname(bpy.data.filepath)
    fn = os.path.join(basedir, "input_LOD" + str(planarAngle))
    bpy.ops.export_scene.gltf(filepath=fn + ".glb", export_apply=True)
