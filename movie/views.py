from rest_framework.views import APIView
from rest_framework import response, status
from rest_framework.decorators import api_view
from .serializers import MovieModelSerializer, JanrModelSerializer
from .models import Movie, Janr



@api_view(['GET','POSt'])
def all_movie(request):
    if request.method == 'GET':
        queryset = Movie.objects.all()
        serializer = MovieModelSerializer(queryset, many=True)
        return response.Response(serializer.data,
                                 status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = MovieModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_200_OK)
            return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class MovieListAPIView(APIView):
#
#     def get(self, request, format=None):
#         queryset = Movie.objects.all()
#         serializer = MovieModelSerializer(queryset, many=True)
#         return response.Response(serializer.data,
#                                  status=status.HTTP_200_OK)
#
#     def post(self, request):
#         print(request.data)
#         serializer = MovieModelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return response.Response(serializer.data, status=status.HTTP_200_OK)
#         return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JanrListAPIView(APIView):
    def get(self, request, format=None):
        queryset = Janr.objects.all()
        serializer = JanrModelSerializer(queryset, many=True)
        return response.Response(serializer.data,
                                 status=status.HTTP_200_OK)


class JanrMovieListAPIView(APIView):
    def get(self, request, pk, format=None):
        queryset = Movie.objects.filter(janr=pk)
        serializer = MovieModelSerializer(queryset, many=True)
        return response.Response(serializer.data,
                                 status=status.HTTP_200_OK)


class DetailMovieAPIView(APIView):
    def get(self, request, pk, format=None, ):
        movie = Movie.objects.get(id=pk)
        serializer = MovieModelSerializer(movie)
        return response.Response(serializer.data,
                                 status=status.HTTP_200_OK)

    def put(self, request, pk, format=None, ):
        movie = Movie.objects.filter(id=pk).first()
        serializer = MovieModelSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response(status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None, ):
        movie = Movie.objects.filter(id=pk).first()
        movie.delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)



