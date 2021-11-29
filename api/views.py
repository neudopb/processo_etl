from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import *

# ************************* LOAD *************************

class NumbersView(APIView):

    def get(self, request, *args, **kw):

        numbersClass = NumbersClass(*args, **kw)
        result = numbersClass.do_work()
        response = Response(result, status=status.HTTP_200_OK)
        return response