from django.shortcuts import render

# Create your views here.


import os
from django.http import JsonResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from PIL import Image
import numpy as np

def upload_and_process_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)

        with Image.open(fs.path(filename)) as img:
            img_array = np.array(img)
            average_pixel_value = np.mean(img_array)

        os.remove(fs.path(filename))

        result = average_pixel_value > 150
        return JsonResponse({'average_pixel_value': average_pixel_value, 'is_greater_than_150': result})

    return render(request, 'index.html')












