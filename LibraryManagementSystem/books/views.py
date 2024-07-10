from rest_framework import viewsets 
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import action


class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=True, methods=['get'] , url_path='borrow',url_name='borrow')
    def borrow(self, request, pk=None):
        try:
            book = self.get_object()
            if book.availability_status:
                book.availability_status = False
                book.save()
                return Response(BookSerializer(book).data)
            else:
                return Response({'Error':'Book not available'})
        except Exception as e:
            return Response({'error':e})    

    @action(detail=True, methods=['get'] , url_path='submit_back',url_name='submit_back')
    def submit_back(self, request, pk=None):
        try:    
            book = self.get_object()
            if not book.availability_status:
                book.availability_status = True
                book.save()
                return Response(BookSerializer(book).data)
            else:
                return Response({'Error':"Book wasn't issued" })
        except Exception as e:
            return Response({'error':e})  


