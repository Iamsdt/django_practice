from rest_framework import generics
from quotes_app.models import QuoteCategory, Quote
from .serializers import QuoteCategorySerializer, QuoteSerializer


# Create your views here.
class QuoteAPIView(generics.ListAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class QuoteCategoryAPIView(generics.ListAPIView):
    queryset = QuoteCategory.objects.all()
    serializer_class = QuoteCategorySerializer
