from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from followers.models import Followers
from followers.serializers import FollowersSerializer


class FollowerList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FollowersSerializer
    queryset = Followers.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FollowersSerializer
    queryset = Followers.objects.all()