from informations.models import Information
from informations.serialiser.serializer_out import InformationSerialiserOut
from informations.serialiser.serializer_input import InformationSerialiserInput
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import  api_view
from rest_framework import generics

   # GET qui renvoi une liste l'element 
@api_view(['GET'])
def toutInformation(request):
    allInformation=Information.objects.all()
    serializer=InformationSerialiserOut(allInformation,many=True)
    return Response(serializer.data, status= status.HTTP_200_OK)
# GET qui renvoi un seul element 
@api_view(['GET'])
def detailInformation(request, pk=None):
    id=pk
    if id is not None:         
        information=Information.objects.get(id=id)
        serializer=InformationSerialiserOut(information)
        return  Response(serializer.data, status= status.HTTP_200_OK)

# c'est fonction doivent etre uniquement disponible pour les administrateur 
# POST  
@api_view(['POST'])
def creerInformation(request):
    serializer=InformationSerialiserOut(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'msg':'Data  created'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def suprimerInformation(request,pk):
    id=pk
    information=Information.objects.get(pk=id)
    information.delete()
    return Response({'msg':'Data Deleted'}, status= status.HTTP_200_OK)

#  modifier les information 
class InformationUpdateView(generics.UpdateAPIView):
    queryset = Information.objects.all()
    serializer_class = InformationSerialiserInput
