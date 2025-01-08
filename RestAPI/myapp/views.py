from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from myapp.models import Students
from rest_framework.response import Response
from myapp.serializers import StudentsSerializer

# Create your views here.
class StudentsView(APIView):
    def get(self,request,sid=None):
        if sid:
            result=Students.objects.filter(id=sid)
            serializers=StudentsSerializer(result,many=True    )
            return Response({'status':'Success','students':serializers.data})
        else:
            result=Students.objects.all()
            serializers=StudentsSerializer(result, many=True)
            return Response({'status':'Success','students':serializers.data}) 

    def post(self,request):
        serializers=StudentsSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'status':'Success','data':serializers.data})
        else:
            return Response({'status':'Error','data':serializers.errors})

    def patch(self,request,sid):
        result=Students.objects.get(id=sid)
        serializers=StudentsSerializer(result,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'status':'Success','data':serializers.data})
            # return Response({'status':'Success','data':serializers.data})
        else:
            return Response({'status':'Updated','data':serializers.data})
        
    def delete(self,request,sid=None):
        # result=Students.objects.get(id=sid)
        result=get_object_or_404(Students,id=sid)

        result.delete()
        return Response({'status':'Success','data':'Record Deleted'})