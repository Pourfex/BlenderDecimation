#! /bin/bash
for var in "$@"
do
    gltf-pipeline -i input_LOD${var}.glb -o input_LOD${var}_draco.glb -d --draco.compressionLevel 10 --draco.quantizePositionBits 16
done