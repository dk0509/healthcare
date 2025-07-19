from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, permissions, status
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer
from django.shortcuts import get_object_or_404

# Create your views here.

class MappingListCreateView(generics.ListCreateAPIView):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

class MappingDetailView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, id):
        mappings = PatientDoctorMapping.objects.filter(patient=id)
        serializer = PatientDoctorMappingSerializer(mappings, many=True)
        return Response(serializer.data)

    def delete(self, request, id):
        mapping = get_object_or_404(PatientDoctorMapping, id=id)
        mapping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
