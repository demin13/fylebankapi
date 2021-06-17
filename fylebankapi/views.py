from fylebankapi.serialization import Serializationbanks,Serializationbranches
from fylebankapi.models import bankmodel,branchmodel
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
import django_filters

class bankList(ListAPIView):
    queryset = bankmodel.objects.all()
    serializer_class = Serializationbanks
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend,SearchFilter]
    filterset_fields = ['id']

class branchList(ListAPIView):
    queryset = branchmodel.objects.all()
    serializer_class = Serializationbranches
    filter_backends = [SearchFilter]#[django_filters.rest_framework.DjangoFilterBackend]
    #filterset_fields = ['branch']
    search_fields = ['^branch']
    ordering = ['ifsc']


class branchList1(ListAPIView):
    queryset = branchmodel.objects.all()
    serializer_class = Serializationbranches
    filter_backends = [SearchFilter]
    #filterset_fields = ['city']
    search_fields = ['^ifsc','^bank_id','^branch','^address','^city','district','state']
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
