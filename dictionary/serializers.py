#!/usr/bin/env python
# coding=utf-8
#from django.forms import widgets
from rest_framework import serializers
from dictionary.models import Dictionary
# from dictionary.models import charmean, associatal_words, associatal_detach
# from dictionary.models import associatal_pictures, collocations
# from dictionary.models import english_translation, sample_sentences

class DictionarySerializer(serializers.ModelSerializer):
    charmean = serializers.StringRelatedField(many=True)
    associatal_words = serializers.StringRelatedField(many=True)
    associatal_detach = serializers.StringRelatedField(many=True)
    associatal_pictures = serializers.StringRelatedField(many=True)
    collocations = serializers.StringRelatedField(many=True)
    english_translation = serializers.StringRelatedField(many=True)
    sample_sentences = serializers.StringRelatedField(many=True)

    class Meta:
        model = Dictionary
        fields = ('id', 'word', 'charmean',
                  'associatal_words', 'associatal_detach',
                  'associatal_pictures', 'collocations',
                  'english_translation', 'sample_sentences')
