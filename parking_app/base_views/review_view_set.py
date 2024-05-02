from rest_framework import viewsets
from rest_framework.response import Response
from parking_app.models import Review
from parking_app.serializers import ReviewSerializer
from drf_yasg.utils import swagger_auto_schema


class BaseReviewViewSet(viewsets.ViewSet):
    def list(self, request): # /api/review/
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=ReviewSerializer)
    def create(self, request): # /api/review/
        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def retrieve(self, request, pk=None): # /api/review/<pk>/
        review =  Review.objects.get(id=pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)