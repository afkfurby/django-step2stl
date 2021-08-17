import Mesh
import Part

shape = Part.Shape()
shape.read('C:\PyCharmProjects\django_step2stl\media\Duschabdeckung_v1_uaN23aR.step')
doc = FreeCAD.newDocument('Doc')
pf = doc.addObject("Part::Feature","x")
pf.Shape = shape
Mesh.export([pf], 'C:\PyCharmProjects\django_step2stl\media\Duschabdeckung_v1_uaN23aR.stl')
