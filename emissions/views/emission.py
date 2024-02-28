from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, generics
from emissions.models import Emissions
from rest_framework.permissions import IsAuthenticated
from emissions.serializers.serializer_input import EmissionSerializerPost
from emissions.serializers.serializer_out import EmissionSerializerGet


@api_view(['GET'])
def allEmission(request):
    emission = Emissions.objects.all().order_by("-id")
    serializer = EmissionSerializerGet(emission,many=True).data
    return Response(serializer, status= status.HTTP_200_OK)


@api_view(['GET'])
def detailEmission(request, pk):
    if pk is not None:
        emission = Emissions.objects.get(id=pk)
        serializer = EmissionSerializerGet(emission).data
        return Response(serializer, status= status.HTTP_200_OK)
    data ={"msg":"L'identifiant ne peux pas etre saans valeur "}
    return Response(data, status=status.HTTP_400_BAD_REQUEST)


#  modifier les emissions 
class EmissionUpdateView(generics.UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Emissions.objects.all()
    serializer_class = EmissionSerializerPost

    def update(self, request, *args, **kwargs):
        emission_send_id = kwargs['pk']
        emission = Emissions.objects.get(id = emission_send_id)
        user = self.request.user
        if emission.user != None:
            if user.id != emission.user.id:
                return Response({"msg":"Vous n'êtes pas autorisé à effectuer cette modification."}, status=status.HTTP_403_FORBIDDEN)
            return super().update(request, *args, **kwargs)
        return Response({"msg":"Une Erreur c'est produite"}, status=status.HTTP_403_FORBIDDEN)


#add emissions
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def ajouterEmission(request):
    serializer = EmissionSerializerPost(data = request.data)
    if serializer.is_valid():
        serializer.save()
        data = {"msg": "Evénement est bien ajouté "}
        return Response (data, status=status.HTTP_200_OK)
    data = {"msg": "Echec d'enregistrement"}
    return Response(data, status=status.HTTP_400_BAD_REQUEST)

#suprimer emission 
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def suprimerEmission(request, pk):
    emission = Emissions.objects.get(id=pk)
    user = request.user
    if emission.user != None:
        if emission.user.id == user.id:
            emission.delete()
            return Response ({"msg": "Evénement suprimé "}, status=status.HTTP_200_OK)
        return Response ({"msg":"Vous n'êtes pas autorisé à effectuer cette supression."}, status=status.HTTP_200_OK)
    return Response({"msg":"Une Erreur c'est produite"}, status=status.HTTP_403_FORBIDDEN)