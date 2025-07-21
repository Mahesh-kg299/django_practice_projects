from rest_framework import serializers
from .models import Member, Book

class BookSerializer(serializers.ModelSerializer):
    book_id = serializers.CharField(max_length=25, write_only=True)

    class Meta:
        model = Book
        fields = ["book_id", 'title', 'author', 'isbn', 'is_borrowed', 'borrowed_by']

class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn']

class MemberSerializer(serializers.ModelSerializer):
    member_id = serializers.CharField(max_length=10, write_only=True)
    class Meta:
        model = Member
        fields = ['member_id', 'name', 'dob']


class BookBasicSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    author = serializers.CharField(max_length=25)
    isbn = serializers.IntegerField(required=False)
    is_borrowed = serializers.BooleanField(required=False)
    borrowed_by = serializers.PrimaryKeyRelatedField(queryset=Book.objects.all(), allow_null=True, required=False)
    
    def create(self, validated_data):
        return Book.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.author = validated_data.get("author", instance.author)
        instance.isbn = validated_data.get("isbn", instance.isbn)
        instance.is_borrowed = validated_data.get("is_borrowed", instance.is_borrowed)
        instance.save()
        return instance