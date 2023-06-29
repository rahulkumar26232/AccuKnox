from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin

from social_network.models import User
from social_network.serializers import UserModelSerializer


class SearchUserApi(ListModelMixin, viewsets.GenericViewSet):
    serializer_class = UserModelSerializer

    def get_queryset(self):
        search_keyword = self.request.query_params.get("search_keyword")

        users = User.objects.all()

        if search_keyword:
            if '@' in search_keyword:
                email_user = users.filter(email__iexact=search_keyword)

                if email_user: return email_user

            name_users = users.filter(first_name__icontains=search_keyword)
            if name_users:
                return name_users

        return users
