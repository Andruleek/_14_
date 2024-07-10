import pytest
from fastapi.testclient import TestClient
from main import app
from faker import Faker
from src.repository.contacts import ContactsRepository
from src.database.models import Contact

fake = Faker()

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def contacts_repo():
    return ContactsRepository()

def test_get_contacts(client, contacts_repo):
    for _ in range(5):
        contact = Contact(
            name=fake.name(),
            email=fake.email(),
            phone=fake.phone_number()
        )
        contacts_repo.create(contact)

    response = client.get("/contacts")

    assert response.status_code == 200

    data = response.json()
    assert len(data) == 5
    for contact in data:
        assert "id" in contact
        assert "name" in contact
        assert "email" in contact
        assert "phone" in contact

def test_get_contacts_empty(client, contacts_repo):
    contacts_repo.delete_all()

    response = client.get("/contacts")

    assert response.status_code == 200

    data = response.json()
    assert len(data) == 0