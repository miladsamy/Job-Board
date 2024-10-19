import django_filters
from .models import Job

class JobFilter(django_filters.FilterSet):
    title= django_filters.CharFilter(lookup_expr='icontains') # to search for any word in title
    description= django_filters.CharFilter(lookup_expr='icontains')# to search for any word in description
    class Meta:
        model= Job
        fields='__all__'
        exclude=['owner','published_at','image','salary','vacancy','slug']