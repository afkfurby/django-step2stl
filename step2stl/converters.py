import subprocess, os
from django_step2stl import settings

# converts stp files to stl

def step2stl(filein, fileout=""):

    fileout = filein.replace(".step", "").replace(".stp", "").replace(".STEP", "").replace(".STP", "") + ".stl"

    with open(os.path.join(settings.BASE_DIR, 'step2stl/freecad/script_freecad_step2stl.py')) as Script:
        content = Script.readlines()

    with open(os.path.join(settings.BASE_DIR, 'step2stl/tmp/freecad_step2stl.py'), 'w') as Script:
        for line in content:
            new_line1 = line.replace('file_path', filein).replace('file_out', fileout)
            Script.write(new_line1)

    proc = subprocess.run([os.path.join(settings.BASE_DIR, 'step2stl/freecad/win/018/bin/FreeCADCmd.exe'), os.path.join(settings.BASE_DIR, 'step2stl/tmp/freecad_step2stl.py')], stdout=subprocess.PIPE)

    output = proc.stdout.decode(encoding='utf-8', errors='ignore')

    return fileout