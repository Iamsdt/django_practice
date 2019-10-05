from rest_framework import serializers
from quotes_app.models import Quote, QuoteCategory


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote

        fields = ['quote', 'author']



class QuoteCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteCategory

        fields = ('__all__')