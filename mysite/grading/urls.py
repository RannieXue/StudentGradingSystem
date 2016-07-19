from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from grading.models import Submission

urlpatterns = [ 
	url(r'^$', ListView.as_view(queryset=Submission.objects.all().order_by("-date")[:10], template_name="grading/grading.html"))]



