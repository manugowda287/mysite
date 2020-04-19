#!/usr/local/bin/python
# coding: latin-1
from django.core.serializers import json
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import pandas as pd

import sys
import numpy


def index(request):
   template = loader.get_template('index.html')
   return HttpResponse(template.render())


def dataset(request):
   template = loader.get_template('FirstPage.html')
   return HttpResponse(template.render())


def statastic(request):
   template = loader.get_template('SecondPage.html')
   return HttpResponse(template.render())


def HistoHeat(request):
   template = loader.get_template('ThirdPage.html')
   return HttpResponse(template.render())

def prediction(request):
   template = loader.get_template('LastPage.html')
   return HttpResponse(template.render())