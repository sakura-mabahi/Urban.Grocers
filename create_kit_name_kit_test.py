import sender_stand_request
import data


# Función para cambiar el valor del parámetro Name en el cuerpo de la solicitud
def get_kit_body(name):
    # Copiar el diccionario con el cuerpo de la solicitud desde el archivo de datos
    kit_body = data.kit_body.copy()
    # Se cambia el valor del parámetro firstName
    kit_body["name"] = name
    # Se devuelve un nuevo diccionario con el valor Name requerido
    return kit_body

# Función de pruebas positivas
def positive_assert(name):
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = get_kit_body(name)
    # El resultado de la solicitud para crear un nuevo kit se guarda en la variable response
    kit_response = sender_stand_request.post_new_kit(kit_body)

    # Comprueba si el código de estado es 201
    assert kit_response.status_code == 201
    data = kit_response.json()
    assert name == data['name']

# Funciónes de prueba negativas
def negative_assert_code_400(name):
    response = sender_stand_request.post_new_kit(name)
    # Comprueba si el código de estado es 400
    assert response.status_code == 400
    # Comprueba que el atributo code en el cuerpo de respuesta es 400
    assert response.json()["code"] == 400

def negative_assert_no_name(name):
    # El resultado se guarda en la variable response
    response = sender_stand_request.post_new_kit(name)
    # Comprueba si el código de estado es 400
    assert response.status_code == 400
    # Comprueba que el atributo code en el cuerpo de respuesta es 400
    assert response.json()["code"] == 400
    # Comprueba el atributo message en el cuerpo de respuesta
    assert response.json()["message"] == "No se enviaron todos los parámetros requeridos"

def negative_assert_different_name(name):
    expected_name = name
    response = sender_stand_request.post_new_kit(name)
    # Comprueba si el código de estado es 400
    assert response.status_code == 400
    # Comprueba que el atributo code en el cuerpo de respuesta es 400
    assert response.json()["code"] == 400
    # Comprueba que el nombre en la respuesta es diferente del esperado
    assert response.json()["name"] != expected_name


# Prueba 1. Ki creado con éxito. El parámetro Name contiene 1 caracter
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert(data.test_1_letter_positive)

# Prueba 2. Kit creado con éxito. El parámetro Name contiene 511 caracteres
def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert(data.test_511_letter)

# Prueba 3. Error. El parámetro Name contiene 0 caracteres
def test_create_kit_0_letter_in_name_get_error_response():
    negative_assert_code_400(data.test_0_characters_negative)

# Prueba 4. Error. El parámetro Name contiene 512 caracteres, es mayor que la cantidad permitida
def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert_code_400(data.test_512_letter_negative)

# Prueba 5. Ki creado con éxito. El parámetro Name contiene caracteres especiales (permitidos)
def test_create_kit_has_special_symbol_in_name_get_success_response():
    positive_assert(data.test_character_special_positive)

# Prueba 6. Kit creado con éxito. El parámetro Name contiene espacios (permitidos)
def test_create_kit_space_in_name_get_success_response():
    positive_assert(data.test_spaces_positive)

# Prueba 7. Kit creado con éxito. El parámetro Name contiene numeros
def test_create_kit_has_number_in_name_get_success_response():
    positive_assert(data.test_numbers_positive)

# Prueba 8. Error. Falta el parámetro Name en la solicitud
def test_create_kit_no_name_get_error_response():
    # El diccionario con el cuerpo de la solicitud se copia del archivo "data" a la variable "kit_body"
    kit_body = data.kit_body.copy()
    # El parámetro "Name" se elimina de la solicitud
    kit_body.pop("name")
    # Comprueba la respuesta
    negative_assert_no_name(kit_body)

# Prueba 9. Error. El parámetro contiene un string diferente(número)
def test_create_kit_different_name_get_error_response():
    negative_assert_different_name(data.test_number_negative)
