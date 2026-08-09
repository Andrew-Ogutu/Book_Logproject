from rest_framework import viewsets,permissions

from .models import Book

from .serializers import BookSerializer , EntrySerializer
from .permissions import IsOwnerOrSuperUser

class BookViewset(viewsets.ModelViewSet):
   
    queryset = Book.objects.all()

    serializer_class = BookSerializer

    permission_classes = [permissions.IsAuthenticated, IsOwnerOrSuperUser]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


