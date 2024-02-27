from rest_framework import status,generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from tournois.serializer.serializer_input import TournoisSerializerPost
from tournois.serializer.serializer_out import TournoisSerializerGet
from tournois.models import Tournois



@api_view(['GET'])
def allTournois(request):
    tournoi = Tournois.objects.all().order_by('-id')
    serializer = TournoisSerializerGet(tournoi, many = True).data
    return Response(serializer, status=status.HTTP_200_OK)

@api_view(['GET'])
def detailTournoi(request, pk):
    if pk is not None:
        tournoi = Tournois.objects.get(id=pk)
        serializer = TournoisSerializerGet(tournoi).data
        return Response(serializer, status= status.HTTP_200_OK)
    data ={"msg":"L'identifiant ne peux pas etre saans valeur "}
    return Response(data, status=status.HTTP_400_BAD_REQUEST)


#  modifier les emissions 
class TournoiUpdateView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Tournois.objects.all()
    serializer_class = TournoisSerializerPost


#add emissions
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ajouterTournoi(request):
    serializer = TournoisSerializerPost(data = request.data)
    if serializer.is_valid():
        serializer.save()
        data = {"msg": "Evénement est bien ajouté "}
        return Response (data, status=status.HTTP_200_OK)
    data = {"msg": "Echec d'enregistrement"}
    return Response(data, status=status.HTTP_400_BAD_REQUEST)

#suprimer emission 
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def suprimerTounoi(request, pk):
    event = Tournois.objects.get(id=pk)
    event.delete()
    data = {"msg": "Evénement suprimé "}
    return Response (data, status=status.HTTP_200_OK)