from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from app.models import StreamingPlatform, WatchList, Review
from app.api import serializers


class StreamPlatformTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="rootroot")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream = StreamingPlatform.objects.create(name='netflix', about="Streaming platform", website_link="https://www.google.com.bd/?hl=bn")

    def test_streamplatform_create(self):
        data = {
            "name": "netflix",
            "about": "Streaming platform",
            "website_link": "https://www.google.com.bd/?hl=bn"
        }
        response = self.client.post(reverse('stream'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_streamplatform_list(self):
        response = self.client.get(reverse('stream'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_streamplatform_detail(self):
        response = self.client.get(reverse('stream_details', args=(self.stream.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class WatchListTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="rootroot")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream = StreamingPlatform.objects.create(name='netflix', about="Streaming platform", website_link="https://www.google.com.bd/?hl=bn")

        self.watchlist = WatchList.objects.create(platform=self.stream, title="3 idiots", story_line="Streaming platform", active=True)

    def test_streamplatform_create(self):
        data = {
            "paltform": self.stream,
            "title": "3 idiots",
            "story_line": "Streaming platform",
            "active": True
        }
        response = self.client.post(reverse('list'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_streamplatform_list(self):
        response = self.client.get(reverse('list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_streamplatform_detail(self):
        response = self.client.get(reverse('details', args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(WatchList.objects.count(), 1)
        self.assertEqual(WatchList.objects.get().title, '3 idiots')


class ReviewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="example", password="rootroot")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream = StreamingPlatform.objects.create(name='netflix', about="Streaming platform", website_link="https://www.google.com.bd/?hl=bn")

        self.watchlist = WatchList.objects.create(platform=self.stream, title="3 idiots", story_line="Streaming platform", active=True)
        self.watchlist2 = WatchList.objects.create(platform=self.stream, title="3 idiots", story_line="Streaming platform", active=True)
        self.review = Review.objects.create(review_user=self.user, rating=4, description="great movie", watchlist=self.watchlist2, active=True)

    def test_Review_create(self):
        data = {
            "review_user": self.user,
            "rating": 5,
            "description": "great movie",
            "watchlist": self.watchlist,
            "active": True
        }
        response = self.client.post(reverse('review_create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(reverse('review_create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Review.objects.count(), 2)
        # self.assertEqual(Review.objects.get().rating, 5)

    def test_review_create_unauthenticated(self):
        data = {
            "review_user": self.user,
            "rating": 5,
            "description": "gret movie",
            "watchlist": self.watchlist,
            "active": True
        }
        self.client.force_authenticate(user=None)
        response = self.client.post(reverse('review_create', args=(self.watchlist2.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_review_update(self):
        data = {
            "review_user": self.user,
            "rating": 4,
            "description": "great movie",
            "watchlist": self.watchlist2,
            "active": False
        }
        response = self.client.put(reverse('review_details', args=(self.review.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_list(self):
        response = self.client.get(reverse('review', args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_list_ind(self):
        response = self.client.get(reverse('review_details', args=(self.review.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_user(self):
        response = self.client.get("/watch/review/?username" + self.user.username)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
