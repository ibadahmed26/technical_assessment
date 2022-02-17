from rest_framework import viewsets
from .models import ResumeModel
from .serializer import ResumeSerializer
from rest_framework.response import Response
from django.db.models import Q


class ResumeData(viewsets.ModelViewSet):
    serializer_class = ResumeSerializer

    def get_queryset(self):
        resumes = ResumeModel.objects.all()
        return resumes

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        param_list = params["pk"].split("-")
        resume = ResumeModel.objects.filter(
            Q(skill__contains=param_list[0]) | Q(experience__contains=param_list[1])
        )
        serialized = ResumeSerializer(resume, many=True)
        return Response({"status": True, "data": serialized.data})
