import argparse
import requests

def get_analytics_codes(domain):
  # Hacer la request hacia la API
  response = requests.get(f"https://api.hackertarget.com/analyticslookup/?q={domain}")

  # Verificar si la request tuvo éxito
  if response.status_code != 200:
    print("Error al obtener los códigos de analytics")
    return []

  # Procesar la respuesta y obtener los códigos
  lines = response.text.strip().split("\n")
  analytics_codes = [line.split(",")[1] for line in lines]

  return analytics_codes

def get_analytics_info(codes):
  results = []

  for code in codes:
    # Hacer la request hacia la API con cada código
    response = requests.get(f"https://api.hackertarget.com/analyticslookup/?q={code}")

    # Verificar si la request tuvo éxito
    if response.status_code != 200:
      print(f"Error al obtener información de analytics para el código {code}")
      continue

    # Procesar la respuesta y agregarla a la lista de resultados
    results.append(response.text.strip())

  return results

def main():
  # Crear el parser para los argumentos
  parser = argparse.ArgumentParser()
  parser.add_argument("-d", "--domain", required=True, help="Dominio a utilizar")
  parser.add_argument("-o", "--output", help="Archivo donde guardar la salida")
  args = parser.parse_args()

  # Obtener el dominio y el archivo de salida del argumento
  domain = args.domain
  output_file = args.output

  codes = get_analytics_codes(domain)
  results = get_analytics_info(codes)

  # Guardar la salida en el archivo de salida o mostrarla en pantalla
  if output_file:
    with open(output_file, "w") as f:
      for result in results:
        f.write(result + "\n")
  else:
    for result in results:
      print(result)

if __name__ == "__main__":
  main()
