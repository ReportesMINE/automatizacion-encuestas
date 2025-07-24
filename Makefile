# ====================================================
# Makefile para Encuestas ETL
# ====================================================
IMAGE_NAME = automatizacion_encuestas

.PHONY: egresados empleadores estudiantes eventos profesores proyectofinal build run-egresados run-empleadores run-estudiantes run-eventos run-profesores run-proyectofinal run-menu clean

HOST_PWD = $(shell powershell -Command "Get-Location | Select-Object -ExpandProperty Path")

# ====================================================
# Makefile para Flujos en Python
# ====================================================
egresados:
	py -m app.main --egresados

empleadores:
	py -m app.main --empleadores

estudiantes:
	py -m app.main --estudiantes

eventos:
	py -m app.main --eventos

profesores:
	py -m app.main --profesores

proyectofinal:
	py -m app.main --proyectofinal

# ====================================================
# Makefile para Flujos en Docker
# ====================================================
build:
	docker build -t $(IMAGE_NAME) .

run-egresados:
	docker run --rm -v "$(HOST_PWD)/data:/app/data" -v "$(HOST_PWD)/output:/app/output" $(IMAGE_NAME) --egresados

run-empleadores:
	docker run --rm -v "$(HOST_PWD)/data:/app/data" -v "$(HOST_PWD)/output:/app/output" $(IMAGE_NAME) --empleadores

run-estudiantes:
	docker run --rm -v "$(HOST_PWD)/data:/app/data" -v "$(HOST_PWD)/output:/app/output" $(IMAGE_NAME) --estudiantes

run-eventos:
	docker run --rm -v "$(HOST_PWD)/data:/app/data" -v "$(HOST_PWD)/output:/app/output" $(IMAGE_NAME) --eventos

run-profesores:
	docker run --rm -v "$(HOST_PWD)/data:/app/data" -v "$(HOST_PWD)/output:/app/output" $(IMAGE_NAME) --profesores

run-proyectofinal:
	docker run --rm -v "$(HOST_PWD)/data:/app/data" -v "$(HOST_PWD)/output:/app/output" $(IMAGE_NAME) --proyectofinal

run-menu:
	docker run -it --rm -v "$(HOST_PWD)/data:/app/data" -v "$(HOST_PWD)/output:/app/output" $(IMAGE_NAME)

# ====================================================
# Makefile para Limpiar
# ====================================================
clean:
	rm -rf __pycache__ .venv output/*.xlsx
	echo "🧹 Carpeta limpia!"
