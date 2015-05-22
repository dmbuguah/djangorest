# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
# from django.http import Http404
# from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics

class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

  """
  List all snippets,or create a new snippet.
  """
  queryset = Snippet.objects.all()
  serializer_class = SnippetSerializer


  # def get(self, request, format=None):
  #   snippets = Snippet.objects.all()
  #   serializer = SnippetSerializer(snippets, many=True)
  #   return Response(serializer.data)

  # def post(self, request, format=None):
  #   serializer = SnippetSerializer(data=request.data)
  #   if serializer.is_valid():
  #     serializer.save()
  #     return Response(serializer.data, status=status.HTTP_201_CREATED)
  #   return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  def get(self,request, *args,**kwargs):
    return self.list(request, *args,**kwargs)

  def post(self, request, *args,**kwargs):
    return self.create(request, *args, **kwargs)


# class JSONResponse(HttpResponse):
#   """
#   An HttpResponse that renders its content into JSON.
#   """
#   def __init__(self, data, **kwargs):
#     content = JSONRenderer().render(data)
#     kwargs['content_type'] = 'application/json'
#     super(JSONResponse,self).__init__(content, **kwargs)

# @csrf_exempt
# @api_view(['GET','POST'])
# def snippet_list(request, format=None):
#   """
#   List all code snippets, or create a new snippet.
#   """
#   if request.method == 'GET':
#     snippets = Snippet.objects.all()
#     serializer = SnippetSerializer(snippets, many=True)
#     return Response(serializer.data)

#     # return JSONResponse(serializer.data)

#   elif request.method == 'POST':
#     data = JSONParser().parse(request)
#     serializer = SnippetSerializer(data=data)
#     if serializer.is_valid():
#       serializer.save()
#       return JSONResponse(serializer.data,status.status.HTTP_201_CREATED)
#     return JSONResponse(serializer.errors,staus.status.HTTP_400_BAD_REQUEST)

# @csrf_exempt
class SnippetDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
  """
  Retrieve,update or delete a snippet instance.
  """
  # def get_object(self, pk):
  #   try:
  #     return Snippet.objects.get(pk=pk)
  #   except Snippet.DoesNotExist:
  #     raise Http404

  # def get(self, request,pk, format=None):
  #   snippet = self.get_object(pk)
  #   serializer = SnippetSerializer(snippet)
  #   return Response(serializer.data)

  # def put(self, request,pk, format=None):
  #   snippet = self.get_object(pk)
  #   serializer = SnippetSerializer(snippet,data = request.data)
  #   if serializer.is_valid():
  #     serializer.save()
  #     return Response(serializer.data)
  #   return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

  def delete(self,request,pk, format=None):
    snippet = self.get_object(pk)
    snippet.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

  def get(self,request, *args,**kwargs):
    return self.retrieve(request, *args, **kwargs)

  def put(self,request, *args,**kwargs):
    return self.update(request, *args, **kwargs)

  def delete(self,request, *args, **kwargs):
    return self.destroy(request, *args, **kwargs)



# @api_view(['GET','PUT','DELETE'])
# def snippet_detail(request,pk,format=None):
#   """
#   Retrieve,update and delete a code snippet.
#   """
#   try:
#     snippet = Snippet.objects.get(pk=pk)
#   except Snippet.DoesNotExist:
#     return HttpResponse(status=status.HTTP_404_BOT_FOUND)

#   if request.method == 'GET':
#     serializer = SnippetSerializer(snippet)
#     return Response(serializer.data)

#   elif request.method == 'PUT':
#     data = JSONParser().parse(request)
#     serializer = SnippetSerializer(snippet, data=data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#   elif request.method == 'DELETE':
#     snippet.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)



