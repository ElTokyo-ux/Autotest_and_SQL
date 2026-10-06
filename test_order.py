
# Емельянова Вера Павловна 48 - когорта. Инженер по тестированию плюс
from sender_stand_request import order_request
from data.data import order_payload


def test_get_order_by_track():
    # 1. Выполнить запрос на создание заказа
    response = order_request.post_create_order(order_payload.order_body)
    assert response.status_code == 201

    # 2. Сохранить номер трека заказа
    track = response.json()["track"]
    assert track is not None

    # 3. Выполнить запрос на получение заказа по треку заказа
    response_track = order_request.get_order_by_track(track)

    # 4. Проверить, что код ответа равен 200
    assert response_track.status_code == 200
