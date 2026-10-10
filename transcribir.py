from faster_whisper import WhisperModel
from pathlib import Path
import os

# ==========================================
# CONFIGURACIÓN
# ==========================================

MODELO = "large-v3"

CARPETA_AUDIOS = Path("audios")
CARPETA_RESULTADOS = Path("resultados")

EXTENSIONES = ["*.m4a", "*.mp3", "*.wav", "*.flac"]

# ==========================================

print("Buscando audios...\n")

audios = []

for ext in EXTENSIONES:
    audios.extend(CARPETA_AUDIOS.glob(ext))

if len(audios) == 0:
    print("No se encontró ningún audio.")
    input("Presiona ENTER para salir...")
    exit()

if len(audios) == 1:
    audio = audios[0]
    print(f"Audio encontrado: {audio.name}")
else:
    print("Audios encontrados:\n")

    for i, archivo in enumerate(audios, start=1):
        print(f"{i}. {archivo.name}")

    while True:
        try:
            opcion = int(input("\nSeleccione un número: "))
            if 1 <= opcion <= len(audios):
                audio = audios[opcion-1]
                break
        except:
            pass

nombre = input(
    "\nNombre del TXT (ENTER = mismo nombre del audio): "
).strip()

if nombre == "":
    nombre = audio.stem

salida = CARPETA_RESULTADOS / f"{nombre}.txt"

print("\nCargando modelo...")

model = WhisperModel(
    MODELO,
    device="cuda",
    compute_type="float16"
)

print("Modelo cargado.")
print("Transcribiendo...\n")

segments, info = model.transcribe(
    str(audio),
    language="es",
    vad_filter=True,
    vad_parameters=dict(
        min_silence_duration_ms=500
    ),
    condition_on_previous_text=False
)

texto = ""

for segment in segments:
    print(segment.text)
    texto += segment.text + "\n"

with open(salida, "w", encoding="utf-8") as f:
    f.write(texto)

print("\n===================================")
print("TRANSCRIPCIÓN FINALIZADA")
print(f"Archivo guardado en:\n{salida}")
print("===================================")