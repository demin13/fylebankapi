from rest_framework import serializers
from fylebankapi.models import bankmodel, branchmodel

class Serializationbanks(serializers.ModelSerializer):
    class Meta:
        model=bankmodel
        fields=['name','id']
        #fields='__all__'

class Serializationbranches(serializers.ModelSerializer):
    class Meta:
        model=branchmodel
        fields='__all__'
