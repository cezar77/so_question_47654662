from collections import OrderedDict

from rest_framework import serializers

from .models import Species


class SpeciesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Species
        fields = (
            'url', 'id', 'canonical_name', 'slug',  'species', 'genus',
            'subfamily', 'family', 'order', 'class_name', 'phylum',
            'ncbi_id', 'ncbi_taxonomy',
        )
        read_only_fields = ('slug',)
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

    def to_representation(self, obj):
        # call the parent method and get an OrderedDict
        data = super(SpeciesSerializer, self).to_representation(obj)
        # generate a list of the keys and replace the key 'class_name'
        keys = list(data.keys())
        keys.insert(keys.index('class_name'), 'class')
        keys.remove('class_name')
        # remove 'class_name' and assign its value to a new key 'class'
        class_name = data.pop('class_name')
        data.update({'class': class_name})
        # create new OrderedDict with the order given by the keys
        response = OrderedDict((k, data[k]) for k in keys)
        return response

    #def to_internal_value(self, data):
    #    class_value = data.get('class')
    #    data.update({'class_name': class_value})
    #    return super(SpeciesSerializer, self).to_internal_value(data)
