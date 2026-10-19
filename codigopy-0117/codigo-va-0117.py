
# Matias Lopez NC 0117
# Practica: Canales RGB con una plancha

import cv2
import matplotlib.pyplot as plt
from pathlib import Path

# Definir las carpetas
carpeta = Path(__file__).resolve().parent.parent
ruta_imagen = carpeta / "img-original-0117"/"plancha.jpg"
ruta_resultados = carpeta / "resultado-img-0117"

ruta_resultados.mkdir(parents=True, exist_ok=True)

# Cargar imagen
imagen = cv2.imread(str(ruta_imagen))

if imagen is None:
    print("Error: no se encontro plancha.jpg")
    print("Revisa la carpeta imagenes")
    exit()

# Mostrar metadatos
print("Nombre: plancha.jpg")
print("Ancho y alto:", imagen.shape[1], "x", imagen.shape[0])
print("Canales:", imagen.shape[2])
print("Tipo de dato:", imagen.dtype)

# Convertir de BGR a RGB
rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

# Separar canales
rojo = rgb[:, :, 0]
verde = rgb[:, :, 1]
azul = rgb[:, :, 2]

# Mostrar las imagenes
plt.figure(figsize=(10, 7))

plt.subplot(2, 2, 1)
plt.imshow(rgb)
plt.title("Imagen original")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(rojo, cmap="gray")
plt.title("Canal rojo")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(verde, cmap="gray")
plt.title("Canal verde")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(azul, cmap="gray")
plt.title("Canal azul")
plt.axis("off")

plt.tight_layout()
plt.savefig(str(ruta_resultados / "canales_rgb.png"))
plt.show()

print("Practica terminada correctamente.")
print("Resultado guardado en resultados/canales_rgb.png")

# Matias Lopez NC 0117
import cv2
import matplotlib.pyplot as plt

imagen = cv2.imread("img-original-0117/plancha.jpg")

if imagen is None:
    print("Error al cargar la imagen")
    exit()

# Convertir de BGR a RGB
imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

plt.imshow(imagen_rgb)
plt.title("Imagen convertida de BGR a RGB")
plt.axis("off")
plt.show()