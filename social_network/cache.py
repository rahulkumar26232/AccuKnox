import redis

from accuknox import settings

REDIS_INSTANCE = redis.from_url(url=settings.REDIS_URI, decode_responses=True)


class FriendRequestLimiterCache:
    key = 'user_id_{}_request_limit'
    second_limit = 60
    allowed_limit = 3

    @classmethod
    def get(cls, user_id: int):
        return REDIS_INSTANCE.get(cls.key.format(user_id))

    @classmethod
    def set_with_ttl(cls, user_id: int, value: int, ttl: int = None):
        if ttl is None: ttl = cls.second_limit

        REDIS_INSTANCE.setex(cls.key.format(user_id), ttl, value)

    @classmethod
    def is_sending_request_allowed(cls, user_id: int) -> bool:

        data = cls.get(user_id=user_id)

        if not data:
            cls.set_with_ttl(user_id=user_id, value=1)
            return True
        data = int(data)
        if data >= cls.allowed_limit: return False

        ttl = REDIS_INSTANCE.ttl(cls.key.format(user_id))

        cls.set_with_ttl(user_id, data + 1, ttl)

        return True
