
# Емельянова Вера Павловна 48 - когорта. Инженер по тестированию плюс
from sender_stand_request import order_request
from data.data import order_payload

 # Создание заказа и возврат трека
def test_create_order():
    response = order_request.post_create_order(order_payload.order_body)
    assert response.status_code == 201, f"Ожидался 201, получил {response.status_code}"

    data = response.json()
    assert "track" in data, "В ответе нет поля track"
    assert data["track"] is not None, "Track равен None"

 #  Получение заказа по известному треку
def test_get_order_by_track():

    known_track = 325197

    response_track = order_request.get_order_by_track(known_track)
    assert response_track.status_code == 200, f"Ожидался 200, получил {response_track.status_code}"

    data = response_track.json()
    assert "order" in data, "В ответе нет объекта order"
    assert "track" in data["order"], "В объекте order нет поля track"
    

    assert data["order"]["track"] == known_track, "Трек в ответе не совпадает с запрошенным"
