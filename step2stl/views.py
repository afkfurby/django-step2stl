from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django_step2stl import settings
from . import converters
# def convert(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
from step2stl.forms import UploadFileForm



def gui(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']

        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)

        uploaded_file_url = fs.url(filename)

        return render(request, 'gui.html', {
            'uploaded_file_url': uploaded_file_url
        })

    return render(request, 'gui.html')

def convert(request):

    ismalware = False
    if request.method == 'POST':
        my_file = request.FILES.get('file')

        # check if file is allowed:
        if my_file.name.split('.')[-1].lower() in ['stp', 'step', '3mf']: # TODO: these should be convertable ['obj', 'amf', 'stp', 'step', '3mf']

            # check file for shell if readable
            try:
                temp = my_file.read()
                decoded = temp.decode('utf-8').split('\\')
                for x in decoded:
                    if x.__contains__('sudo') or x.__contains__('echo') or x.__contains__(
                            'shell_exec') or x.__contains__('?php'):
                        ismalware = True
                        return HttpResponseRedirect('fuck you ')
            except:
                pass

            if not ismalware:
                fs = FileSystemStorage()
                filename = fs.save(fs.get_valid_name(my_file.name), my_file)

                uploaded_file_url = fs.url(filename)
                if my_file.name.split('.')[-1].lower() in ['stp', 'step']:
                    converted_file_path = converters.step2stl(fs.path(filename))
                elif my_file.name.split('.')[-1].lower() in ['3mf']:
                    converted_file_path = converters.threeMF2stl(fs.path(filename))

                converted_file_url = fs.url(converted_file_path)

                return HttpResponse(uploaded_file_url)


    return HttpResponse("nothing.")