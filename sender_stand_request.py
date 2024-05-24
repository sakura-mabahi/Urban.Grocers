import configuration
import requests
import data


# Función que realiza una solicitud HTTP POST para crear un nuevo usuario.
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, json=body, headers=data.header)

# Solicitud POST para crear un nuevo usuario y devuelve el token de autenticación del usuario.
def get_new_user_token():
    response = post_new_user(data.user_body)
    dataN = response.json()
    return dataN['authToken']

# Función que copia el header existente, obtiene un token de autenticación de usuario y lo agrega al header copiado.
def get_header_with_token():
    header = data.header.copy()
    authToken = get_new_user_token()
    header["Authorization"] = f"Bearer {authToken}"
    return header

# Esta función copia el cuerpo de la solicitud, obtiene un header que incluye el token de autenticación de usuario y realiza una solicitud POST con el cuerpo y el header.
def post_new_kit(body):
    headers = get_header_with_token()
    return requests.post(configuration.URL_SERVICE+configuration.KITS_PATH, json=body, headers=headers)

