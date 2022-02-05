from rest_framework.throttling import UserRateThrottle


class ReviewCreateThrottling(UserRateThrottle):
    scope = 'review_create'


class ReviewListThrottling(UserRateThrottle):
    scope = 'review_list'


# class ReviewDetailThrottling(UserRateThrottle):
#     scope = 'review_detail'
