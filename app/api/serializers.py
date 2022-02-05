from rest_framework import serializers
from app.models import WatchList, StreamingPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        # fields = "__all__"
        exclude = ['watchlist']


class WatchListSerializer(serializers.ModelSerializer):
    # reviews = ReviewSerializer(many=True, read_only=True)

    # length_name = serializers.SerializerMethodField()
    platform = serializers.CharField(source='platform.name')

    class Meta:
        model = WatchList
        fields = "__all__"


class StreamingPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)

    class Meta:
        model = StreamingPlatform
        fields = "__all__"
        # watchlist = serializers.StringRelatedField(many=True)
        # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
        # watchlist = serializers.HyperlinkedRelatedField(
        #     many=True,
        #     read_only=True,
        #     view_name='details'
        # )

        # fields=["url",'name']
# class MovieSerializer(serializers.ModelSerializer):
#     length_name = serializers.SerializerMethodField()
#
#     class Meta:
#         model = Movie
#         fields = "__all__"
#         # fields = ['id', 'name', 'description']
#         # exclude = ['name']
#
#     def get_length_name(self, object):
#         return len(object.name)
#
#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError('Name can not be less than 2')
#         else:
#             return value
#
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('Name and Description can not same')
#         else:
#             return data

# def length_name(value):
#     if len(value) < 2:
#         raise serializers.ValidationError('name can not less than 2')
#     else:
#         return value
#
#
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[length_name])
#     # name = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField()
#
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

# def validate_name(self, value):
#     if len(value) < 2:
#         raise serializers.ValidationError('Name can not be less than 2')
#     else:
#         return value
#
# def validate(self, data):
#     if data['name'] == data['description']:
#         raise serializers.ValidationError('Name and Description can not same')
#     else:
#         return data
