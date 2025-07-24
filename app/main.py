import argparse
from pathlib import Path
from app.services.processor import procesar_excel
from app.pipelines.flujo_empleadores import reglas_empleadores
from app.pipelines.flujo_profesores import reglas_profesores
from app.pipelines.flujo_estudiantes import reglas_estudiantes
from app.pipelines.flujo_egresados import reglas_egresados
from app.pipelines.flujo_eventos import reglas_eventos
from app.pipelines.flujo_proyectofinal import reglas_proyectofinal

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--empleadores", action="store_true", help="Procesar encuesta empleadores")
    parser.add_argument("--profesores", action="store_true", help="Procesar encuesta profesores")
    parser.add_argument("--estudiantes", action="store_true", help="Procesar encuesta estudiantes")
    parser.add_argument("--egresados", action="store_true", help="Procesar encuesta egresados")
    parser.add_argument("--eventos", action="store_true", help="Procesar encuesta eventos")
    parser.add_argument("--proyectofinal", action="store_true", help="Procesar encuesta proyecto final")
    args = parser.parse_args()

    base_dir = Path(__file__).resolve().parent.parent

    if args.empleadores:
        print("⚙⚙ Ejecutando flujo: Empleadores")
        ruta_entrada_empleadores = base_dir / "data" / "20241127_Encuestas_InformacionReunionEmpleadores.xlsx"
        ruta_salida_empleadores = base_dir / "output" / "20241127_Transformado_InformacionReunionEmpleadores.xlsx"
        print(f"✅ Ruta entrada empleadores: {ruta_entrada_empleadores}")
        reglas = reglas_empleadores()
        procesar_excel(ruta_entrada_empleadores, ruta_salida_empleadores, reglas)

    if args.profesores:
        print("⚙⚙ Ejecutando flujo: Profesores")
        ruta_entrada_profesores = base_dir / "data" / "20250417_Encuestas_InformacionReunionProfesores.xlsx"
        ruta_salida_profesores = base_dir / "output" / "20250417_Transformado_InformacionReunionProfesores.xlsx"
        print(f"✅ Ruta entrada profesores: {ruta_entrada_profesores}")
        reglas = reglas_profesores()
        procesar_excel(ruta_entrada_profesores, ruta_salida_profesores, reglas)

    if args.estudiantes:
        print("⚙⚙ Ejecutando flujo: Estudiantes")
        ruta_entrada_estudiantes = base_dir / "data" / "20240401_Encuestas_InformacionReunionEstudiantes.xlsx"
        ruta_salida_estudiantes = base_dir / "output" / "20240401_Transformado_InformacionReunionEstudiantes.xlsx"
        print(f"✅ Ruta entrada estudiantes: {ruta_entrada_estudiantes}")
        reglas, columnas_a_eliminar = reglas_estudiantes()
        procesar_excel(ruta_entrada_estudiantes, ruta_salida_estudiantes, reglas, columnas_a_eliminar)

    if args.egresados:
        print("⚙⚙ Ejecutando flujo: Egresados")
        ruta_entrada_egresados = base_dir / "data" / "20240717_Encuestas_InformacionReunionEgresados.xlsx"
        ruta_salida_egresados = base_dir / "output" / "20240717_Transformado_InformacionReunionEgresados.xlsx"
        print(f"✅ Ruta entrada egresados: {ruta_entrada_egresados}")
        reglas, columnas_a_eliminar = reglas_egresados()
        procesar_excel(ruta_entrada_egresados, ruta_salida_egresados, reglas, columnas_a_eliminar)

    if args.eventos:
        print("⚙⚙ Ejecutando flujo: Evento-charla")
        ruta_entrada_evento = base_dir / "data" / "20250507_Encuestas_InformacionEventoCharlemosdelfuturo.xlsx"
        ruta_salida_evento = base_dir / "output" / "20250507_Transformado_InformacionEventoCharlemosdelfuturo.xlsx"
        print(f"✅ Ruta entrada egresados: {ruta_entrada_evento}")
        reglas, columnas_a_eliminar = reglas_eventos()
        procesar_excel(ruta_entrada_evento, ruta_salida_evento, reglas, columnas_a_eliminar)

    if args.proyectofinal:
        print("⚙⚙ Ejecutando flujo: Proyecto-Final")
        ruta_entrada_proyectofinal = base_dir / "data" / "20231110_Encuestas_InformacionCandidatosProyectoFinal.xlsx"
        ruta_salida_proyectofinal = base_dir / "output" / "20231110_Transformado_InformacionCandidatosProyectoFinal.xlsx"
        print(f"✅ Ruta entrada empleadores: {ruta_entrada_proyectofinal}")
        reglas = reglas_proyectofinal()
        procesar_excel(ruta_entrada_proyectofinal, ruta_salida_proyectofinal, reglas)