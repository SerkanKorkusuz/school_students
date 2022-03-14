from django.http import Http404, HttpRequest, HttpResponse
from rest_framework import status, viewsets, filters
from rest_framework.response import Response
from .models import School, Student
from .serializers import SchoolSerializer, StudentSerializer


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    search_fields = ['name', 'location']
    filter_backends = (filters.SearchFilter,)
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    search_fields = ['first_name', 'last_name']
    filter_backends = (filters.SearchFilter,)
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def list(self, request: HttpRequest, school_pk=None, **kwargs) -> HttpResponse:
        # If it is a request from a DRF nested routing, then school_pk is conditioned.
        queryset = self.queryset.filter(school=school_pk) if school_pk else self.queryset
        serializer = self.serializer_class(queryset, many=True)
        if serializer.data:
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)

        raise Http404

    def retrieve(self, request: HttpRequest, pk=None, school_pk=None, **kwargs) -> HttpResponse:
        # If it is a request from a DRF nested routing, then school_pk is conditioned.
        queryset = self.queryset.filter(pk=pk, school=school_pk) if school_pk else self.queryset.filter(pk=pk)
        serializer = self.serializer_class(queryset, many=True)
        if serializer.data:
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)

        raise Http404

    def create(self, request, **kwargs) -> HttpResponse:
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            school = serializer.validated_data.get('school')
            # If it is a request from a DRF nested routing, then the student instance belongs to kwargs['school_pk']
            school_rel = School.objects.get(id=kwargs.get('school_pk', school.id))

            # Check and raise an exception if the maximum school capacity is already reached.
            if not school.max_student_capacity > len(school.students.all()):
                error_data = serializer.errors
                error_data['msg'] = f'The maximum capacity of {school} is already reached. ' \
                                    f'No more students can be enrolled.'
                return Response({"status": "error", "data": error_data}, status=status.HTTP_400_BAD_REQUEST)

            serializer.validated_data['school'] = school_rel
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
