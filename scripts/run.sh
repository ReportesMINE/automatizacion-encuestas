#!/bin/bash

echo "=== Selecciona una opción ==="
select opcion in "Procesar Empleadores" "Procesar Profesores" "Procesar Estudiantes" "Procesar Egresados" "Procesar Eventos" "Procesar Proyecto Final" "Procesar Todos" "Salir"; do
  case $REPLY in
    1)
      echo "🔵 Procesando Encuesta Empleadores..."
      python3 -m app.main --empleadores
      break
      ;;
    2)
      echo "🟢 Procesando Encuesta Profesores..."
      python3 -m app.main --profesores
      break
      ;;
    3)
      echo "🟢 Procesando Encuesta Estudiantes..."
      python3 -m app.main --estudiantes
      break
      ;;
    4)
      echo "🟢 Procesando Encuesta Egresados..."
      python3 -m app.main --estudiantes
      break
      ;;
    5)
      echo "🟢 Procesando Encuesta Eventos..."
      python3 -m app.main --eventos
      break
      ;;
    6)
      echo "🟢 Procesando Encuesta Proyectofinal..."
      python3 -m app.main --proyectofinal
      break
      ;;
    7)
      echo "🟣 Procesando Todos..."
      python3 -m app.main --empleadores --profesores --estudiantes --egresados --eventos --proyectofinal
      break
      ;;
    8)
      echo "Saliendo..."
      break
      ;;
    *)
      echo "⚠️  Opción inválida"
      ;;
  esac
done