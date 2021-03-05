# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template

from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly.express as px

#@login_required(login_url="/login/")
def index(request):

    context = {'segment':'index', 'Titulo': "Majority Report",
               "Letras_grandes": "BIENVENIDOS"}

    frase = "hola novio, feo"
    context['parrafo'] = frase.upper()

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

def detailcharts(request):
    context = {'segment':'index', 'Titulo': "Majority Report",
               "Letras_grandes": "BIENVENIDOS"}

    frase = "hola novio, feo"
    context['parrafo'] = frase.upper()
    context['titulo'] = "Nuevo titulo"
    context['plot_div1'] = grafiquitas()

    html_template = loader.get_template( 'detailcharts.html' )
    return HttpResponse(html_template.render(context, request))





#@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        context['titulo'] = "Nuevo titulo"

        context['plot_div1'] = grafiquitas()


        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))


def grafiquitas():
    df = px.data.iris()
    plot_div = plot(px.scatter(df, x="sepal_width", y="sepal_length", color="species"), output_type='div')

    return plot_div

