
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import Account
from account.serializers import AccountSerializer
from student.models import AccountStatistics, Protagonist, Hero
from student.serializers import StatisticsSerializer


class RegistrUserView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = AccountSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)


class CreateStatistics(CreateAPIView):
    queryset = AccountStatistics.objects.all()
    serializer_class = StatisticsSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = StatisticsSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            data['response'] = True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)


class UserByToken(APIView):
    def post(self, request):
        data = {
            'id': str(request.user.id),
            'email': str(request.user.email),
            'last_name': str(request.user.last_name),
            'first_name': str(request.user.first_name),
            'patronymic': str(request.user.patronymic),

            'location': str(request.user.location),
            'school_number': str(request.user.school_number),
            'is_teacher': str(request.user.is_teacher),
            'gender': str(request.user.gender),
        }
        print(data.values())
        return Response(data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def CreateHero(request):
    if request.method == 'POST':
        acc = AccountStatistics.objects.create(
            account=request.user,
            user_name=f'{request.user.last_name} {request.user.first_name} {request.user.patronymic}'
        )
        print(acc)
        id_hero = request.data['hero']
        prot = Protagonist.objects.create(
            account=request.user,
            hero=Hero.objects.get(pk=id_hero),
            name=request.data['hero_name']
        )
        return Response({'Студент успошно создан'})


