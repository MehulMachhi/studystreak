from rest_framework.views import APIView


class PublicAPI(APIView):
    authentication_classes = []
    permission_classes = []