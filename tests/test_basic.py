from django.urls import reverse
from rest_framework import status


def test_frontpage(client):
    response = client.get(reverse('index'))
    assert response.status_code == 302
    assert response.url == reverse('schema-swagger-ui')


def test_ping_pong(client):
    """ Ping-pong monitoring check. """
    response = client.get(reverse('ping'))
    assert response.status_code == status.HTTP_200_OK
    assert response.content == b'pong'
