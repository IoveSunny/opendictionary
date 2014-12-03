#!/usr/bin/env python
# coding=utf-8
#from django.forms import widgets
from rest_framework import serializers
from dictionary.models import Dictionary

class DictionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dictionary
        fields = ('id', 'word', 'characteristics', 'meanings',
                  'associatal_words', 'associatal_detach',
                  'associatal_pictures', 'collocations',
                  'english_translation', 'sample_sentences')
