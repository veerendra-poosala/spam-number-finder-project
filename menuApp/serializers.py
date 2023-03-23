from rest_framework import serializers 

from .models import ContactsModel 


class ContactsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactsModel
        fields = '__all__'