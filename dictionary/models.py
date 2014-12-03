#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.

# Table 1: Word
class Dictionary(models.Model):
    '''Main Word'''
    word = models.ForeignKey('Word', verbose_name=u'单词')
    characteristics = models.ForeignKey('Characteristics',
                                       verbose_name=u'词性')
    meanings = models.ForeignKey('Meanings', verbose_name=u'词义')
    associatal_words = models.OneToOneField('Associatal_words',
                                         verbose_name=u'联想词')
    associatal_detach = models.OneToOneField('Associatal_detach',
                                          verbose_name=u'拆分词')
    collocations = models.ForeignKey('Collocations', 
                                     verbose_name=u'搭配/词组')
    sample_sentences = models.ForeignKey('Sample_sentences',
                                         verbose_name=u'例句')
    english_translation = models.ForeignKey('English_translation',
                                            verbose_name=u'英译')
    associatal_pictures = models.ForeignKey('Associatal_pictures',
                                            verbose_name=u'联想图片')

    class Meta:
        ordering = ['word']

    def __unicode__(self):
        return str(self.word)

class Word(models.Model):
    '''Only Words'''
    word = models.CharField(max_length=255, verbose_name=u'单词')

    def __unicode__(self):
        return self.word

class Characteristics(models.Model):
    '''store Word's Characteristics'''
    characteristics = models.CharField(max_length=10, verbose_name=u'词性')

    def __unicode__(self):
        return self.characteristics
    
class Meanings(models.Model):
    '''store word's meanings'''
    meanings = models.CharField(max_length=500, verbose_name=u'词义')

    def __unicode__(self):
        return self.meanings

class Associatal_words(models.Model):
    '''Store word's Associatal words'''
    words = models.ForeignKey('Word', verbose_name=u'联想词')

    def __unicode__(self):
        return self.words

class Associatal_detach(models.Model):
    '''Detach word to many parts'''
    detach = models.ForeignKey('Detach_word', verbose_name=u'拆分词')

    def __unicode__(self):
        return self.detach

class Detach_word(models.Model):
    part = models.CharField(max_length=20, verbose_name=u'单词的部分')
    meanings = models.CharField(max_length=255, 
                                verbose_name=u'拆分部分的意思')

    def __unicode__(self):
        return str(self.part + ':' + self.meanings)

class Collocations(models.Model):
    '''Word Collocations'''
    collocations = models.CharField(max_length=255, verbose_name=u'搭配')

    def __unicode__(self):
        return self.collocations

class Sample_sentences(models.Model):
    '''Sample Sentences'''
    sample_sentences = models.CharField(max_length=500, 
                                        verbose_name=u'例句')

    def __unicode__(self):
        return self.sample_sentences

class English_translation(models.Model):
    '''English_translation'''
    english_translation = models.CharField(max_length=500,
                                          verbose_name='英译')

class Associatal_pictures(models.Model):
    '''Associatal pictures'''
    associatal_pictures = models.ImageField(upload_to='static/pictures',
                                           default='',
                                           height_field=100,
                                           width_field=100,
                                           max_length=255)
