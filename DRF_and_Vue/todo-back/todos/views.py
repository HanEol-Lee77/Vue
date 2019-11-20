from django.shortcuts import render, get_object_or_404
from .serializers import TodoSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view 
from django.contrib.auth import get_user_model
# Create your views here.

#언제 불리게끔 만들려면.. 데코레이터 : @ 사용! @api_view , import!
@api_view(['POST'])
def todo_create(request):
    serializer = TodoSerializer(data=request.POST)
    print(serializer)
    print(serializer.is_valid())
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(status=400) # valid하지 않은 경우 이 에러 띄우기!

# /users/2/
@api_view(['GET'])
def user_detail(request, pk):
    User = get_user_model()
    # User.object.get(pk=pk)
    user = get_object_or_404(User, pk=pk)

    # 요청이 들어온 JWT의 user정보와 pk로 검색하여 나온 user 객체의 정보가 같을 경우
    if request.user != user: # request로 들어온 정보를 가지고 알아서 판단할 것
        return Response(status=404)

    serializer = UserSerializer(user)
    return Response(serializer.data)