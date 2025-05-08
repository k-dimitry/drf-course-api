from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from api.models import User, Order


class UserOrderTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create_user(username='user1', password='1234')
        user2 = User.objects.create_user(username='user2', password='1234')
        Order.objects.create(user=user1)
        Order.objects.create(user=user1)
        Order.objects.create(user=user2)
        Order.objects.create(user=user2)

    def test_user_order_endpoint_retrieves_only_authenticated_user_orders(self):
        for username in ('user1', 'user2'):
            user = User.objects.get(username=username)
            self.client.force_login(user)
            response = self.client.get(reverse('user_orders'))

            assert response.status_code == status.HTTP_200_OK
            orders = response.json()
            self.assertTrue(all(order['user'] == user.id for order in orders))

    def test_user_order_list_unauthenticated(self):
        response = self.client.get(reverse('user_orders'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
