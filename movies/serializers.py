from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie
from datetime import date
from actors.serializers import ActorSerializer
from genres.serializers import GenreSerializer


class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'

    
    def validate_release_date(self, value):
        current_year = date.today().year
        if value < 1900:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1900.')
        elif value > date.today().year:
            raise serializers.ValidationError(f'A data de lançamento não pode ser posterior a {current_year}.')
        
        return value
    
    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('O resumo não deve ser maior que 500 caracteres.')
        return value
    

class MovieListDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genre = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'name', 'genre', 'actors', 'release_date', 'rate', 'resume']

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        if rate:
            return round(rate, 1)
        return None



