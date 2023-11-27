from django.urls import path

from GymManageSys.settings import MEDIA_ROOT
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name='home'),
    path('pagedetail/<int:id>',views.page_detail,name='pagedetail'),
    path('faq',views.faq_list,name='faq'),
    path('enquiry',views.enquiry,name='enquiry'),
    path('gallery',views.gallery,name='gallery'),
    path('gallerydetail/<int:id>', views.gallery_detail, name='gallery_detail'),
    path('pricing',views.pricing,name='pricing'),
#     name = 'whatever' -> whatever is passed in the url
] + static(settings.MEDIA_URL,document_root=MEDIA_ROOT)

