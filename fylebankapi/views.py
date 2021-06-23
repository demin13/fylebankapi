from django.shortcuts import render
from fylebankapi.serialization import Serializationbanks,Serializationbranches
from fylebankapi.models import bankmodel,branchmodel
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from .pagination import pageForBranches

@csrf_exempt
def bankList1(request):
    if request.method=='GET':
        queryset = bankmodel.objects.all()
        bank_serializer = Serializationbanks(queryset,many=True)
        return JsonResponse(bank_serializer.data,safe=False)

@csrf_exempt
def branchLists(request):
    if request.method=='GET':
        queryset = branchmodel.objects.all()
        branch_serializer = Serializationbranches(queryset,many=True)
        return JsonResponse(branch_serializer.data,safe=False)

class bankList(ListAPIView):
    queryset = bankmodel.objects.all()
    serializer_class = Serializationbanks
    #filter_backends = [django_filters.rest_framework.DjangoFilterBackend,SearchFilter]
    filter_backends = [SearchFilter]
    search_fields = ['^name']

class branchList(ListAPIView):
    queryset = branchmodel.objects.all()
    serializer_class = Serializationbranches
    pagination_class = pageForBranches
    filter_backends = [SearchFilter]#[django_filters.rest_framework.DjangoFilterBackend]
    #filterset_fields = ['branch']
    search_fields = ['^branch']
    ordering = ['ifsc']


class branchList1(ListAPIView):
    queryset = branchmodel.objects.all()
    serializer_class = Serializationbranches
    pagination_class = pageForBranches
    filter_backends = [SearchFilter]
    #filterset_fields = ['city']
    search_fields = ['ifsc','bank_id','branch','city','district','state']
    ordering = ['ifsc']



@api_view(['GET'])
def showbank(request):
    if request.method=='GET':
        results=bankmodel.objects.all()
        serialize=Serializationbanks(results,many=True)
        return Response(serialize.data)

@api_view(['GET'])
def showbranches(request):
    if request.method=='GET':
        results=branchmodel.objects.all()
        serialize=Serializationbranches(results,many=True)
        return Response(serialize.data)
