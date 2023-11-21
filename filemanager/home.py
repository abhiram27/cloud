from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView
from .forms import *
import json
from filemanager.models import *
from django.shortcuts import redirect
from django.contrib.auth import login
from django.core.paginator import Paginator
from django.template import RequestContext
from filemanager.models import *
from pathlib import Path
import os
from django.db import transaction
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_ROOT = os.path.join(BASE_DIR, 'filemanager\\media')

def home(request,page):
    images = File.objects.filter(filexuser__user_id=request.session['user'],deleted=False).order_by('-created')
    opt=OptionMenu.objects.all()
    page = int(page)
    paginator = Paginator(images, 10) 
    print(request.session['user'])
    imgs_pg = paginator.get_page(page)
    if request.method == "POST":
        if 'upload' in request.POST.get('buttons'):
            return redirect('/upload')
        elif 'image' in request.POST.get('buttons'):
            print(request.POST)
            post= dict(request.POST)['opt']
            print("post:", type(post))
            image_opt=json.loads("".join(post))
            if len(image_opt)!=0: 
                opt_obj=OptionMenu.objects.get(id=int(image_opt[0]))
                if opt_obj.option=='Delete':
                    img=File.objects.get(id=int(image_opt[1]))
                    img.deleted=True
                    img.save()
                elif opt_obj.option=='Visualize image':
                    return redirect(f"/visualizer/{image_opt[1]}")
                else:
                    return redirect(f"/metadata/{image_opt[1]}")
    return render(request, 'home.html', {'images': imgs_pg,'options':opt,
                                         'page':page,
                                         'next_page':((page+1) if imgs_pg.has_next() else page),
                                         'prev_page':max(1,page-1)})

def upload(request):
    if request.method == "POST":
        img=request.FILES.get('imagen')
        name = request.POST.get('nombre')
        with transaction.atomic():
            f=File.objects.create(name=name,img=img)
            Filexuser.objects.create(user_id=int(request.session['user']),
                                    file=f)
            return redirect('/home/1')
    return render(request, 'upload.html')


def visualizer(request, image_id):
    try:
        image = File.objects.get(id=image_id)
    except File.DoesNotExist:
        return render(request, 'image_not_found.html',status=404)
    return render(request, 'visualizer.html', {'image':image})

def metadata(request,image_id):
    try:
        image = File.objects.get(id=image_id)
    except File.DoesNotExist:
        return render(request, 'image_not_found.html',status=404)
    
    meta = {
            'name': image.name,
            'filename': image.img.name,
            'size': round(image.img.size/ 1024,2),
            'width': image.img.width,
            'height': image.img.height,
        }
    return render(request, "metadata.html", context={"metadata":meta})