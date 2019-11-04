# xviz.py
Python implementation of XVIZ protocol. Note that this repository only comply with the protocol standard, the some of the implemented structure and modules definition are not the same. 

# Requirements
`websockets` module requires Python 3
[`gltflib`](https://github.com/sergkr/gltflib)

# Reference
- [glTF](https://github.com/KhronosGroup/glTF/blob/master/specification/2.0/README.md)
    - C++ header glTF library: https://github.com/syoyo/tinygltf
    - XViz implementation: https://github.com/uber-web/loaders.gl/blob/master/modules/gltf/scripts/glbdump.js
    - pygltflib: https://gitlab.com/dodgyville/pygltflib
    - gltflib: https://github.com/sergkr/gltflib
- Websocket
    - websocket on Python3: https://websockets.readthedocs.io/en/2.7/index.html
    - single websocket on Python2/3: https://github.com/Pithikos/python-websocket-server