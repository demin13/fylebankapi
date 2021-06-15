from fylebankapi.serialization import Serializationbanks
from fylebankapi.serialization import Serializationbranches
from fylebankapi.models import bankmodel
from fylebankapi.models import branchmodel
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
import django_filters

class bankList(ListAPIView):
    queryset = bankmodel.objects.all()
    serializer_class = Serializationbanks
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id']

class branchList(ListAPIView):
    queryset = branchmodel.objects.all()
    serializer_class = Serializationbranches
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['branch']
    ordering = ['ifsc']


class branchList1(ListAPIView):
    queryset = branchmodel.objects.all()
    serializer_class = Serializationbranches
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['city']
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