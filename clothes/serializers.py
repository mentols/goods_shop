from rest_framework import serializers

from clothes.models import Good, Category

class AdminTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = '__all__'
        # read_only_fields = ('tittle', 'author')
