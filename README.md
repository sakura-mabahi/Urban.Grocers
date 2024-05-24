# Proyecto sprint 6

Este proyecto está diseñado para automatizar pruebas para la creación de un kit, específicamente para probar el campo "name".

### Lenguaje utilizado: Python

## Proceso de automatización:

El proceso de automatización se llevó a cabo en los siguientes pasos:

1. **Instalación de paquetes esenciales**: Se instaló python, pytest pycharm, git y la libreria request para facilitar las pruebas.

2. **Configuración de parámetros**: Se almacenó la URL actualizada del servidor, las APIs correspondientes y las rutas de los documentos en el archivo `configuracion.py`.

3. **Datos necesarios para las solicitudes**: Se recopilaron los datos necesarios para las solicitudes según la documentación de las APIs y se almacenaron en el archivo `data.py`.

4. **Creación de un usuario**: Se utilizó la API POST `/api/v1/users` en la carpeta `sender_stand_request` para crear un usuario. La información correspondiente al usuario estaba previamente almacenada en `data.py`.

    ```json
    {
        "firstName": "Andrea",
        "phone": "+11234567890",
        "address": "123 Elm Street, Hilltop"
    }
    ```

5. **Creación de un kit vinculado al usuario**: Se utilizó la API POST `/api/v1/kits` para crear un kit y vincularlo al usuario recién creado. Se usó un Bearer {authToken} obtenido tras la creación del usuario para esta vinculación. Ejemplo de headers:

    ```python
    headers_for_kits = {
        "Authorization": "Bearer jknnFApafP4awfAIFfafam2fma"
    }
    ```

    La información del kit proporcionada por `api/docs` es:

    ```json
    {
        "name": "Mi conjunto",
        "card": {
            "id": 1,
            "name": "Para la situación"
        },
        "productsList": null,
        "id": 7,
        "productsCount": 0
    }
    ```

    Nota: Se modificó el valor `null` por `1` en el campo `productsList` para obtener un resultado positivo en la creación del kit. Ambos valores estaban previamente almacenados en `data.py`.

## Pruebas realizadas:

El proceso de pruebas siguió los siguientes pasos:

1. Se especificó las funciones que se deseaba probar a apartir de la lista de comprobación.
2. Se solicitó la función `positive_asserts` para clasificar las respuestas positivas.
3. Se identificaron las respuestas positivas en una lista para ordenarlas y luego probarlas individualmente.
4. Se solicitó la función `negative_asserts` para clasificar las respuestas negativas.
5. Se identificaron las respuestas negativas en una lista para ordenarlas y luego probarlas individualmente.

