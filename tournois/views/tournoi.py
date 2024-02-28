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
    
    def update(self, request, *args, **kwargs):
        tournoi_send_id = kwargs['pk']
        tournoi = Tournois.objects.get(id = tournoi_send_id)
        user = self.request.user
        if tournoi.user != None:
            if user.id != tournoi.user.id:
                return Response({"msg":"Vous n'êtes pas autorisé à effectuer cette modification."}, status=status.HTTP_403_FORBIDDEN)
            return super().update(request, *args, **kwargs)
        return Response({"msg":"Une Erreur c'est produite"}, status=status.HTTP_403_FORBIDDEN)


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
    tournoi = Tournois.objects.get(id=pk)
    user = request.user
    if tournoi.user != None:
        if tournoi.user.id == user.id:
            tournoi.delete()
            return Response ({"msg": "Evénement suprimé "}, status=status.HTTP_200_OK)
        return Response ({"msg":"Vous n'êtes pas autorisé à effectuer cette supression."}, status=status.HTTP_200_OK)
    return Response({"msg":"Une Erreur c'est produite"}, status=status.HTTP_403_FORBIDDEN)