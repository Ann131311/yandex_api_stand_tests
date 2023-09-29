import sender_stend_request
# # Зайцева Анна 08- земля, диплом. Инженер по тестированию

def positive_assert(track_order):
    order_response = sender_stend_request.get_order_track(track_order)
    assert order_response.status_code == 200

# Тест 1.
def test_get_order_track_success_response():
    positive_assert(sender_stend_request.track_order)