from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from deshawnapi.models import Appointment, Walker


class AppointmentView(ViewSet):

    def retrieve(self, request, pk=None):
        """Retrieve a single appointment"""
        appointment = Appointment.objects.get(pk=pk)
        serialized = AppointmentSerializer(appointment)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def list(self, request):
        """List all appointments"""
        appointments = Appointment.objects.all()
        serialized = AppointmentSerializer(appointments, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Create an Appointment"""
        # Create a new appointment instance using the `create` ORM method
        appointment = Appointment.objects.create(
            # Get the related walker from the database using the request body value
            walker=Walker.objects.get(pk=request.data["walkerId"])
            # Assign the appointment date using the request body value
            date=request.data["appointmentDate"]
        )

        # Serialization will be covered in the next chapter
        serialized = AppointmentSerializer(appointment)

        # Respond with the newly created appointment in JSON format with a 201 status code
        return Response(serialized.data, status=status.HTTP_201_CREATED)


# The serializer will be covered in the next chapter
class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = ('id', 'walker', 'date')
