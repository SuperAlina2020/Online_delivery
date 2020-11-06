from django_filters import FilterSet
from .models import *
from django_filters import DateFilter


class OrderFilterSet(FilterSet):
    start_date = DateFilter(field_name='date_created',lookup_expr='gte')
    end_date = DateFilter(field_name='date_created',lookup_expr='lte')
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer','data_created']


