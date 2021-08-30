from rest_framework import serializers
from .models import Streamer, Movie


class StreamerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Streamer
        fields = ['id', 'name', 'channel']
        extra_kwargs = {
            'id': {'validators': []},
            'name': {'validators': []},
            'channel': {'validators': []},
        }

    def validate_name(self, data):
        return data


class MovieSerializer(serializers.ModelSerializer):
    streamers = StreamerSerializer(many=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def create(self, validated_data):

        streamers_data = validated_data.pop('streamers')

        movie = Movie.objects.create(**validated_data)
        movie.save()

        for streamer_data in streamers_data:
            streamer = Streamer.objects.filter(
                name=streamer_data['name']).first()
            if streamer is None:
                streamer = Streamer.objects.create(**streamer_data)
            movie.streamers.add(streamer)
        return movie

    def update(self, instance, validated_data):

        streamers_data = validated_data.pop('streamers')

        instance.title = validated_data.get('title', instance.title)
        instance.url = validated_data.get('url', instance.url)
        instance.detail = validated_data.get('detail', instance.detail)
        instance.fun = validated_data.get('fun', instance.fun)
        instance.watched_date = validated_data.get(
            'watched_date', instance.watched_date)

        instance.streamers.clear()

        for streamer_data in streamers_data:
            streamer = Streamer.objects.filter(
                name=streamer_data['name']).first()
            if streamer is None:
                streamer = Streamer.objects.create(**streamer_data)
            instance.streamers.add(streamer)

        instance.save()
        return instance
