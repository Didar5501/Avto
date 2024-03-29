from rest_framework import serializers
from .models import User, mcfcarbrand, mcfcarmodel, mcfcarcolor, country, z_avtomodel, z_avtobrand, z_avtocolor



class McfCarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = mcfcarbrand
        fields = '__all__'

class McfCarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = mcfcarmodel
        fields = '__all__'

class McfCarColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = mcfcarcolor
        fields = '__all__'


class ZAvtomodelSerializer(serializers.ModelSerializer):
    class Meta:
        model = z_avtomodel
        fields = '__all__'

class ZAvtobrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = z_avtobrand
        fields = '__all__'

class ZAvtocolorSerializer(serializers.ModelSerializer):
    class Meta:
        model = z_avtocolor
        fields = '__all__'