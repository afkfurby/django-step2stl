import Mesh
import Part

shape = Part.Shape()
shape.read('file_path')
doc = FreeCAD.newDocument('Doc')
pf = doc.addObject("Part::Feature","x")
pf.Shape = shape
Mesh.export([pf], 'file_out')
