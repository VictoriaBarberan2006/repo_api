import requests
url = 'https://midas.minsal.cl/farmacia_v2/WS/getLocalesTurnos.php'

try:
    respuesta = requests.get(url, timeout=10)
    respuesta.raise_for_status()
    datos = respuesta.json
    print("datos recibidos correctamente: ")
    print(datos)

except requests.exceptions.Timeout:
    print("La consulta demoró demasiado. Intente nuevamente más tarde.")
except requests.exceptions.HTTPError:
    print("La API devolvió un error HTTP. Revise el código o las credeciales.")
except requests.exceptions.RequestException:
    print("No fue posible conectarse con el servicio externo.")
