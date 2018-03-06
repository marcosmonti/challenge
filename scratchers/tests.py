# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from decimal import Decimal

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from scratchers.factories import ScratcherFactory, UserFactory
from scratchers.models import Scratcher


class ScratcherTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = UserFactory()
        self.client.force_login(self.user)

    def test_permissions(self):
        self.client.logout()
        response = self.client.get(reverse('scratcher-list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_auth_token(self):
        self.client.logout()
        token = Token.objects.create(user=self.user)

        response = self.client.get(
            reverse('scratcher-list'),
            HTTP_AUTHORIZATION='Token {}'.format(token.key)
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_incomplete_data(self):
        incomplete_data = {
            'name': 'test name',
            'description': 'description here'
        }
        response = self.client.post(reverse('scratcher-list'), incomplete_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create(self):
        data = {
            'name': 'test name',
            'description': 'description here',
            'size': Scratcher.SMALL,
            'price': 10
        }
        response = self.client.post(reverse('scratcher-list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Scratcher.objects.count(), 1)

        obj = Scratcher.objects.all()[0]
        self.assertEqual(obj.name, 'test name')
        self.assertEqual(obj.description, 'description here')
        self.assertEqual(obj.size, Scratcher.SMALL)
        self.assertEqual(obj.price, 10)

    def test_get_object(self):
        obj = ScratcherFactory()
        response = self.client.get(reverse('scratcher-detail', kwargs={'pk': obj.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        self.assertEqual(obj.name, data['name'])
        self.assertEqual(obj.description, data['description'])
        self.assertEqual(obj.size, data['size'])
        self.assertEqual(obj.price, Decimal(data['price']))

    def test_update_object(self):
        obj = ScratcherFactory()
        response = self.client.get(reverse('scratcher-detail', kwargs={'pk': obj.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        self.assertEqual(obj.name, data['name'])
        self.assertEqual(obj.description, data['description'])
        self.assertEqual(obj.size, data['size'])
        self.assertEqual(obj.price, Decimal(data['price']))

        response = self.client.patch(reverse('scratcher-detail', kwargs={'pk': obj.id}), {'price': '31.50'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['price'], '31.50')
        # reload object
        obj = Scratcher.objects.get(pk=obj.id)
        self.assertEqual(obj.price, Decimal('31.50'))

    def test_list_objects(self):
        for i in range(10):
            ScratcherFactory()

        response = self.client.get(reverse('scratcher-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 10)
