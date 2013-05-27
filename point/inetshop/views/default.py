__author__ = 'dl'

from django.shortcuts import render_to_response
from django.http import HttpResponse
from inetshop.utils.loadxml import loadxml,enablelog

def main(request):
    return render_to_response("main.html")

def nofound(request):
    return render_to_response("nofound.html")

def report_load_xml(request):
    (categories,products)=loadxml(r"http://localhost:8000/static/xml/xml1.html")
    return render_to_response('report_load_xml.html',{'categories':categories,'products':products})

