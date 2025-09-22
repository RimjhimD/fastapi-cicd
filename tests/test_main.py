from fastapi.testclient import TestClient
from src.main import api

client = TestClient(api)

# Test home endpoint
def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Message": "Welcome to the Ticket Booking System"}

# Test POST /ticket
def test_add_ticket():
    ticket_data = {
        "id": 1,
        "flight_name": "FlightA",
        "flight_date": "2025-10-15",
        "flight_time": "14:30",
        "destination": "Paris"
    }
    response = client.post("/ticket", json=ticket_data)
    assert response.status_code == 200
    assert response.json() == ticket_data

# Test GET /ticket
def test_get_tickets():
    response = client.get("/ticket")
    assert response.status_code == 200
    tickets = response.json()
    assert isinstance(tickets, list)
    assert any(t["id"] == 1 for t in tickets)

# Test PUT /ticket/{ticket_id}
def test_update_ticket():
    updated_ticket = {
        "id": 1,
        "flight_name": "FlightB",
        "flight_date": "2025-10-20",
        "flight_time": "16:00",
        "destination": "London"
    }
    response = client.put("/ticket/1", json=updated_ticket)
    assert response.status_code == 200
    assert response.json() == updated_ticket

# Test DELETE /ticket/{ticket_id}
def test_delete_ticket():
    response = client.delete("/ticket/1")
    assert response.status_code == 200
    deleted_ticket = response.json()
    assert deleted_ticket["id"] == 1

    # Ensure ticket list is empty
    response = client.get("/ticket")
    assert response.status_code == 200
    assert response.json() == []
