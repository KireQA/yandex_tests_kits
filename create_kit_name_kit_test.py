import sender_stand_request # импортируем сюда наши функции 
import data # импоритруем сюда инфо из дата

def get_kit_body(name): # создаем вспомогательную ф-ию
    current_body = data.kit_body.copy() #п росим сделать копию шаблона
    current_body["name"] = name # подменяем название на то которое передадим
    return current_body # возвращаем результат

def positive_assert(kit_body): # создаем правила для позиитивных проверок
    auth_token = sender_stand_request.get_new_user_token() # просим добыть токен
    response = sender_stand_request.post_new_kit(kit_body, auth_token) # отправляем запрос на создание набора передавая туда наш токен

    assert response.status_code == 201 # проверяем чтобы сервер сказал что он создал
    assert response.json()["name"] == kit_body["name"] # проверяем что имя в ответе совпадает с тем что мы отправили

    print(f"Код ответа: {response.status_code}") # а тут я просто хочу чтобы мне высвечивалась информация, так как не люблю когда в целом ответ без информации (молчание это не информация для меня)
    print(f"json: {response.json()}")
    print("Тест пройден успешно")

def negative_assert(kit_body): # создаю правила для негативных сценариев
    auth_token = sender_stand_request.get_new_user_token() # создает нового пользователя, создает новый токен
    response = sender_stand_request.post_new_kit(kit_body, auth_token) # создает набор

    assert response.status_code == 400

    print(f"Код ответа: {response.status_code}")
    print(f"JSON: {response.json()}")
    print("Негативный тест пройден успешно")

# Начинаю писать автотесты по порядку

def test_create_kit_1_letter_in_name_get_success_response(): # допустимое кол-во символов 1
    kit_body = get_kit_body("a") #сюда пишем количество букв
    positive_assert(kit_body) #отдаем на проверку

def test_create_kit_511_letter_in_name_get_success_response(): # допустимое ко-во 511
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert(kit_body)

def test_create_kit_0_letter_in_name_get_error_response(): # недопустимое количество, 0 символов
    kit_body = get_kit_body("")
    negative_assert(kit_body)

def test_create_kit_512_letter_in_name_get_error_response(): # недопустимое количество, 512 символов
    kit_body = get_kit_body ("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert(kit_body)

def test_create_kit_english_letter_in_name_get_success_response():
    kit_body = get_kit_body("Tester")
    positive_assert(kit_body)

def test_create_kit_russian_letter_in_name_get_success_response():
    kit_body = get_kit_body("Тестировщик")
    positive_assert(kit_body)

def test_create_kit_specsymbol_in_name_get_success_response():
    kit_body = get_kit_body("@#$%^&*()")
    positive_assert(kit_body)

def test_create_kit_space_symbol_in_name_get_success_response():
    kit_body = get_kit_body(" тестер молодец ")
    positive_assert(kit_body)

def test_create_kit_number_in_name_get_success_response():
    kit_body = get_kit_body("123")
    positive_assert(kit_body)

def test_create_kit_none_in_name_get_error_response(): # в прошлых сценариях программа сама копировала себя
    kit_body = data.kit_body.copy() # в этом мне надо создать копию самому
    kit_body.pop("name") # потому что я удаляю конкретно строку имя из системы, это не пустое поле имя, это отсутствие поля имя
    negative_assert(kit_body)

def test_create_kit_number_type_in_name_get_error_response(): # тут нам нужно изменить тип строки на число
    kit_body = get_kit_body(123) # строка всегда ("такая") а число всегда (такое)
    negative_assert(kit_body)

# Отсюда я пишу запуск автотестов по порядку

# test_create_kit_1_letter_in_name_get_success_response() # 1 тест
# test_create_kit_511_letter_in_name_get_success_response() # 2 тест
# test_create_kit_0_letter_in_name_get_error_response() # 3 тест
# test_create_kit_512_letter_in_name_get_error_response() # 4 тест
# test_create_kit_english_letter_in_name_get_success_response() # 5 тест
# test_create_kit_russian_letter_in_name_get_success_response() # 6 тест
# test_create_kit_specsymbol_in_name_get_success_response() # 7 тест
# test_create_kit_space_symbol_in_name_get_success_response() # 8 тест
# test_create_kit_number_in_name_get_success_response() # 9 тест
# test_create_kit_none_in_name_get_error_response() # 10 тест
# test_create_kit_number_type_in_name_get_error_response() # 11 тест