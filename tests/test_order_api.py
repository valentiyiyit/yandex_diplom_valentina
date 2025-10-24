# Йийит Валентина, 36 когорта — Финальный проект, вторая часть

import time
import requests
from configuration import BASE_URL, CREATE_ORDERS, GET_ORDER, TIMEOUT
from sender_stand_requests import create_order, get_order
import data

def test_order_creation_and_retrieval():
    # необязательная проверка доступности swagger, не валим тест
    try:
        r = requests.get(f"{BASE_URL}/docs/", timeout=TIMEOUT, allow_redirects=True)
        print("DOCS status =", r.status_code)
    except Exception as e:
        print("DOCS check skipped:", e)

    # 1) создаём заказ
    resp = create_order(data.order_body)
    assert resp.status_code in (200, 201), f"Создание заказа вернуло {resp.status_code}: {resp.text}"

    body = resp.json()
    track = body.get("track") or body.get("trackNumber") or body.get("track_number")
    assert track, f"В ответе нет 'track': {body}"
    print("TRACK =", track)

    # 2) получаем заказ по треку
    time.sleep(0.3)
    get_resp = get_order(track)
    assert get_resp.status_code == 200, f"Получение по треку вернуло {get_resp.status_code}: {get_resp.text}"
