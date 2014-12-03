#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.

# Table 1: Word
class Dictionary(models.Model):
    '''Main Word'''
    word = models.CharField(default='', max_length=255, verbose_name=u'单词')

    class Meta:
        ordering = ['word']

    def __unicode__(self):
        return '%s' % self.word

class CharMean(models.Model):
    '''store Word's Characteristics and related meanings'''
    dictionary = models.ForeignKey(Dictionary, default=-1, 
                                   related_name='charmean')
    characteristics = models.CharField(default='', max_length=10, verbose_name=u'词性')
    meanings = models.CharField(default='', max_length=500, verbose_name=u'词义')

    def __unicode__(self):
        return '(%s) %s' % (self.characteristics, self.meanings)
    
class Associatal_words(models.Model):
    '''Associatal_words'''
    dictionary = models.ForeignKey(Dictionary, default=-1, 
                                   related_name='associatal_words')
    associatal_words = models.CharField(default='', max_length=100, verbose_name=u'联想词')

    def __unicode__(self):
        return '%s' % self.associatal_words

class Associatal_detach(models.Model):
    dictionary = models.ForeignKey(Dictionary, default=-1, 
                                   related_name='associatal_detach')
    part = models.CharField(default='', max_length=20,
                            verbose_name=u'单词的部分')
    meanings = models.CharField(default='', max_length=255, 
                                verbose_name=u'拆分部分的意思')

    def __unicode__(self):
        return '%s : %s' % (self.part, self.meanings)

class Collocations(models.Model):
    '''Word Collocations'''
    dictionary = models.ForeignKey(Dictionary, default=-1, 
                                   related_name='collocations')
    collocations = models.CharField(default='', max_length=255, verbose_name=u'搭配')

    def __unicode__(self):
        return '%s' % self.collocations

class Sample_sentences(models.Model):
    '''Sample Sentences'''
    dictionary = models.ForeignKey(Dictionary, default=-1, 
                                   related_name='sample_sentences')
    sample_sentences = models.CharField(default='', max_length=500, 
                                        verbose_name=u'例句')

    def __unicode__(self):
        return '%s' % self.sample_sentences

class English_translation(models.Model):
    '''English_translation'''
    dictionary = models.ForeignKey(Dictionary, default=-1, 
                                   related_name='english_translation')
    english_translation = models.CharField(default='', max_length=500,
                                          verbose_name='英译')

    def __unicode__(self):
        return '%s' % self.english_translation

class Associatal_pictures(models.Model):
    '''Associatal pictures'''
    dictionary = models.ForeignKey(Dictionary, default=-1, 
                                   related_name='associatal_pictures')
    associatal_pictures = models.ImageField(upload_to='static/pictures',
                                           default='',
                                           height_field=100,
                                           width_field=100,
                                           max_length=255)

    def __unicode__(self):
        return '%s' % 'associatal_pictures'
