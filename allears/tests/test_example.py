import pytest
from django.test import Client


@pytest.mark.django_db
def test_index_view():
    client = Client()
    response = client.get("/allears/")
    assert response.status_code == 200
    assert b"Welcome to AllEars! <3" in response.content

@pytest.mark.django_db
def test_index_view_error():
    client = Client()
    response = client.get("/allears/")
    assert response.status_code == 200
    assert b"Welcome to AllEars!" in response.content

