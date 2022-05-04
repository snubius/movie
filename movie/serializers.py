from rest_framework import serializers
from movie.models import Movie, Janr


# class MovieSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100)
#     desc = serializers.CharField(max_length=250)
#     year = serializers.DateField()
#     created_date = serializers.DateTimeField()
#     update_at_date = serializers.DateTimeField()
#     author =serializers.CharField()
#     janr = serializers.CharField()

class MovieModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        #fields ='__all__'
        exclude =('created_date',
                  'update_at_date')


class JanrModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Janr
        fields = 'all'