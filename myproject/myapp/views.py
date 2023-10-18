from django.views.generic import ListView
from .models import Item

class ItemListView(ListView):
    model = Item
    template_name = 'myapp/item_list.html'
    context_object_name = 'items'
