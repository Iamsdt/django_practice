from django.views.generic import ListView
from .models import QuoteCategory, Quote
# Create your views here.

class MainView(ListView):
    template_name = 'home.html'
    model = Quote

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.select_related('quoteCategory')