# django-step2stl
Simple django stl converter.
Initally as step 2 stl converter, but it converts different formats to stl now.

### Supported Fileformats
- STEP
- 3MF

### Installation
FreeCAD needs to be installed into '/step2stl/freecad/{platform}'

### Usage
POST a single file which is named 'file' to /convert/ and it returns the url to the converted stl file