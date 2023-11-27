from django.shortcuts import render
from . import models
from . import forms

# Create your views here.
def home(request):

    banners = models.Banners.objects.all()
    services = models.Service.objects.all()[:3]
    gimgs = models.GalleryImage.objects.all().order_by('-id')[:9]
    return render(request,'home.html',{'banners':banners,'services':services,'gimgs':gimgs})

def page_detail(request,id):
    page = models.Page.objects.get(id=id)
    return render(request,'page.html',{'page':page})

#FAQS
def faq_list(request):
    faq = models.Faq.objects.all()
    return render(request,'faq.html',{'faqs':faq})

#Enquiry
def enquiry(request):
    msg=''
    if request.method=='POST':
        form = forms.EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            msg = "Data has been saved!"
    form = forms.EnquiryForm
    return render(request,'enquiry.html',{'form':form,'msg':msg})

#Gallery
def gallery(request):
    gallery=models.Gallery.objects.all().order_by('-id')
    return render(request,'gallery.html',{'gallerys':gallery})

#Show the Gallery Photos
def gallery_detail(request,id):
    gallery = models.Gallery.objects.get(id=id)
    gallery_imgs=models.GalleryImage.objects.filter(gallery=gallery).order_by('-id')
    return render(request,'gallery_imgs.html',{'gallery_imgs':gallery_imgs,'gallery':gallery})

# Pricing
def pricing(request):
    pricing = models.SubPlan.objects.all()
    allfeatures = models.SubPlanFeatures.objects.all();
    return render(request,'pricing.html',{'plans':pricing,'allfeatures':allfeatures})