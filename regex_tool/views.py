import re

from rest_framework import generics, status
from rest_framework.response import Response

from .models import RegexQuery
from .serializers import RegexQuerySerializer

class RegexQueryView(generics.GenericAPIView):
    serializer_class = RegexQuerySerializer
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        pattern = serializer.validated_data['pattern']
        string = serializer.validated_data['string']
        match_type = serializer.validated_data['match_type']
        
        if match_type == RegexQuery.MatchType.FIRST:
            result = re.search(pattern, string)
            return Response({'match': result.group() if result else None})
        elif match_type == RegexQuery.MatchType.FULL:
            result = re.findall(pattern, string)
            return Response({'match': result if result else None})
