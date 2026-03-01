def test_get_interactions_returns_200(client) -> None:
    response = client.get("/interactions")
    assert response.status_code == 200


def test_get_interactions_response_is_a_list(client) -> None:
    response = client.get("/interactions")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
