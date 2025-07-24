# Encuesta Cleaner

**Script para limpiar texto y clasificar sectores de encuestas empresariales.**
Este proyecto permite procesar datos de encuestas de forma reproducible usando **Docker**.

# Historia Académica ETL

Proyecto ETL modular con Python, Docker, Makefile y CI/CD.

## Requisitos

- Python 3.11+
- Docker instalado
- make instalado

## Validar ruta PowerShell

Get-Location | Select-Object -ExpandProperty Path

## Estructura del proyecto

```
├── app/              # Código fuente principal
├── dashboards/       # Proyecto de PowerBI
├── scripts/run.sh    # Script con menú interactivo de ejecución
├── data/             # Archivos Excel originales (entrada)
├── output/           # Archivos procesados (salida)
├── scripts/          # Comandos de ejecución
├── docs/             # Documentación del proyecto
├── Dockerfile
├── Makefile
├── requirements.txt
├── docker-compose.yml
```

### Construir la imagen Docker

```bash
docker build -t encuestas .
```

### Ejecutar un flujo específico (modo directo)

```bash
docker run -it \
  -v "${PWD}/data:/app/data" \
  -v "${PWD}/output:/app/output" \
  encuestas --empleadores

# Otros flujos disponibles:
# --estudiantes
# --eventos
```

### 3Entrar a un contenedor interactivo (modo bash)

```bash
docker run -it \
  -v "${PWD}/data:/app/data" \
  -v "${PWD}/output:/app/output" \
  encuestas bash
```

Dentro del contenedor:

```bash
# Ejecutar desde el menú interactivo:
bash scripts/run.sh

# O correr módulos directamente:
python3 -m app.main --empleadores
python3 -m app.main --estudiantes
python3 -m app.main --eventos
```

### Usar Docker Compose (opcional)

```bash
docker-compose build
docker-compose run encuestas
```

Para abrir bash dentro del contenedor usando Compose:

```bash
docker-compose run encuestas bash
```

## Verificar estructura

```bash
docker run -it \
  -v "${PWD}/data:/app/data" \
  -v "${PWD}/output:/app/output" \
  encuestas bash

ls /app
```

## Notas

- Asegúrate de que los archivos **Excel de entrada** estén dentro de la carpeta `data/`.
- Los resultados procesados se guardarán en `output/`.
- Manténer actualizado tu contenedor ejecutando `docker build` cada vez que se modifiquen dependencias o el código fuente.