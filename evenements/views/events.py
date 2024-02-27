from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status, generics
from evenements.models import Evenement
from evenements.serializers.serializer_out import EvenementSerializerGet
from evenements.serializers.serializer_input import EvenementSerializerPost
from rest_framework.permissions import IsAuthenticated



@api_view(['GET'])
def allEvenement(request):
    event = Evenement.objects.all().order_by("-id")
    serializer = EvenementSerializerGet(event,many=True).data
    return Response(serializer, status= status.HTTP_200_OK)


@api_view(['GET'])
def detailEvenement(request, pk):
    if pk is not None:
        event = Evenement.objects.get(id=pk)
        serializer = EvenementSerializerGet(event).data
        return Response(serializer, status= status.HTTP_200_OK)
    data ={"msg":"L'identifiant ne peux pas etre saans valeur "}
    return Response(data, status=status.HTTP_400_BAD_REQUEST)


#  modifier les information 
class EvenementUpdateView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializerPost


#add event
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ajouterEvent(request):
    serializer = EvenementSerializerPost(data = request.data)
    if serializer.is_valid():
        serializer.save()
        data = {"msg": "Evénement est bien ajouté "}
        return Response (data, status=status.HTTP_200_OK)
    data = {"msg": "Echec d'enregistrement"}
    return Response(data, status=status.HTTP_400_BAD_REQUEST)

#suprimer event 
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def suprimerEvent(request, pk):
    event = Evenement.objects.get(id=pk)
    event.delete()
    data = {"msg": "Evénement suprimé "}
    return Response (data, status=status.HTTP_200_OK)
    
    
    