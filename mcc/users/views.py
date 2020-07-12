from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["POST"])
def login_view(request):
    # TODO: Refactor to use OAuth 2.0
    user = authenticate(email=request.data["email"], password=request.data["password"])
    if user is not None:
        # A backend authenticated the credentials
        login(request, user)
        return Response("Succesful login attempt", status=status.HTTP_200_OK)

    else:
        # No backend authenticated the credentials
        return Response(
            "Unsuccessful login attempt", status=status.HTTP_401_UNAUTHORIZED
        )
