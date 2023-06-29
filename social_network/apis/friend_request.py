from django.db import transaction, IntegrityError
from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from social_network.cache import FriendRequestLimiterCache
from social_network.models import FriendRequest
from social_network.serializers import SendFriendRequestInputSerializer, FriendRequestModelSerializer, \
    AcceptFriendRequestSerializer


class SendFriendRequestApi(APIView):

    @transaction.atomic
    def post(self, request):
        serializer = SendFriendRequestInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        to_user_id = request.data["user_id"]

        is_allowed = FriendRequestLimiterCache.is_sending_request_allowed(request.user.pk)
        if not is_allowed:
            return Response(
                dict(status='failure', message='Friend Request sending limit Reached , please try after sometime',
                     payload={}))

        if request.user.pk == to_user_id:
            return Response({
                'status': 'failure', 'message': 'can not send self request', "payload": {}})

        try:
            obj = FriendRequest(from_user_id=request.user.pk, to_user_id=to_user_id)
            obj.save()
        except IntegrityError:
            return Response({
                'status': 'failure', 'message': 'Request already sent'
                , "payload": {}
            })

        return Response({
            'status': 'success', 'message': 'Request sent successfully'
            , "payload": FriendRequestModelSerializer(obj).data
        })


class AcceptFriendRequestApi(APIView):

    @transaction.atomic
    def post(self, request):
        serializer = AcceptFriendRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        request_id = request.data['request_id']
        is_accepted = request.data['is_accepted']

        try:
            obj = FriendRequest.objects.get(to_user_id=request.user.pk, id=request_id,
                                            status=FriendRequest.StatusChoice.pending)
        except FriendRequest.DoesNotExist:
            return Response({
                'status': 'failure', 'message': 'Either invalid request id or request not in pending state'
                , "payload": {}
            })

        obj.status = FriendRequest.StatusChoice.accept if is_accepted else FriendRequest.StatusChoice.reject
        obj.save()

        return Response({
            'status': 'success', 'message': 'Request sent successfully'
            , "payload": FriendRequestModelSerializer(obj).data
        })


class FriendsListApi(ListModelMixin, viewsets.GenericViewSet):
    serializer_class = FriendRequestModelSerializer

    def get_queryset(self):
        return FriendRequest.objects.filter(from_user_id=self.request.user.pk, status=FriendRequest.StatusChoice.accept)


class PendingRequestsListApi(ListModelMixin, viewsets.GenericViewSet):
    serializer_class = FriendRequestModelSerializer

    def get_queryset(self):
        return FriendRequest.objects.filter(to_user_id=self.request.user.pk, status=FriendRequest.StatusChoice.pending)
