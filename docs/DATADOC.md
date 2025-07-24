# Validación de Esquemas

Cada ejecución de pipeline genera la documentación y esta debe ser actualizada acá si cambia.
La fuente es recolectada por encuestas individuales e independientes desde la coordinación.

## Egresados
Fuente Coordinación: ReunionEgresados.xlsx
Renombramiento: 20240717_Encuestas_InformacionReunionEgresados.xlsx 
Destino: 20240717_Transformado_InformacionReunionEgresados

| Columna                                  | Tipo       |
|------------------------------------------|------------|
| ID                                       | int64      |
| Hora de inicio                           | datetime64[ns] |
| Hora de finalización                     | datetime64[ns] |
| Correo electrónico                       | object     |
| Nombre Completo                          | object     |
| Correo electrónico2                      | object     |
| Código                                   | float64    |
| LinkedIn                                 | object     |
| ¿Para qué empresa trabajas actualmente?  | object     |
| ¿A qué sector/industria pertenece la empresa? | object     |
| ¿Cuál es tu cargo actual?                | object     |
| ¿Está relacionado tu cargo con la formación que recibiste en MINE? | object     |
| ¿Qué habilidades relacionadas con MINE aportan al desempeño en tu cargo actual? | object     |
| De acuerdo a tu criterio, ¿Cómo calificarías tu experiencia al haber cursado la maestría MINE? | int64      |
| ¿Qué tan probable es que recomiendes MINE a otros? | int64      |
| ¿Tienes alguna sugerencia o comentario que te gustaría compartir con nosotros para mejorar MINE? | object     |
| ¿Cómo evaluarías el apoyo brindado por nosotros como Universidad de los Andes para tu inserción laboral después de la graduación? | float64    |
| ¿Cuál es tu cargo actual?_Limpio         | object     |
| ¿Para qué empresa trabajas actualmente?_Limpio | object     |
| ¿A qué sector/industria pertenece la empresa?_Limpio | object     |
| ¿Qué habilidades relacionadas con MINE aportan al desempeño en tu cargo actual?_Limpio | object     |
| ¿Tienes alguna sugerencia o comentario que te gustaría compartir con nosotros para mejorar MINE?_Limpio | object     |
| Año                                      | int32      |


## Empleadores
Fuente Coordinación: ReunionEmpleadores.xlsx
Renombramiento: 20241127_Encuestas_InformacionReunionEmpleadores.xlsx 
Destino: 20241127_Transformado_InformacionReunionEmpleadores.xlsx

| Columna                                  | Tipo       |
|------------------------------------------|------------|
| ID                                       | int64      |
| Nombre de contacto                       | object     |
| Cargo                                    | object     |
| Empresa                                  | object     |
| Sector de Industria                      | object     |
| Correo electrónico                       | object     |
| Cercano al contacto                      | object     |
| Canal de comunicación                    | object     |
| Asistencia                               | int64      |
| Fecha de Comunicación                    | datetime64[ns] |
| Empresa_Limpia                           | object     |
| Cargo_Limpio                             | object     |
| Sector_Limpio                            | object     |
| Sector                                   | object     |


## Estudiantes
Fuente Coordinación: ReunionEstudiantes.xlsx
Renombramiento: 20240401_Encuestas_InformacionReunionEstudiantes.xlsx
Destino: 20240401_Transformado_InformacionReunionEstudiantes.xlsx

| Columna                                  | Tipo       |
|------------------------------------------|------------|
| ID                                       | int64      |
| Hora de inicio                           | datetime64[ns] |
| Hora de finalización                     | datetime64[ns] |
| Correo electrónico                       | object     |
| Nombre                                   | object     |
| Nombre Completo                          | object     |
| Correo electrónico2                      | object     |
| Código                                   | float64    |
| LinkedIn                                 | object     |
| ¿Cuál es tu cargo actual?                | object     |
| ¿Para qué empresa trabajas actualmente?  | object     |
| ¿A qué sector/industria pertenece la empresa? | object     |
| ¿Tienes experiencia laboral relevante en el campo relacionado con MINE? | object     |
| ¿En qué semestre de la maestría te encuentras? | object     |
| ¿Planeas inscribir el proyecto de grado para el próximo semestre? | object     |
| De acuerdo a tu criterio, ¿Cómo calificarías tu experiencia hasta el momento cursando la maestría? | int64      |
| ¿Qué tan probable es que recomiendes nuestro programa a otros? | int64      |
| En términos generales, ¿consideras que la maestría ha cumplido con tus expectativas? | object     |
| ¿Tienes alguna sugerencia o comentario que te gustaría compartir con nosotros para mejorar el programa? | object     |
| ¿Cuál es tu cargo actual?_Limpio         | object     |
| ¿Para qué empresa trabajas actualmente?_Limpio | object     |
| ¿A qué sector/industria pertenece la empresa?_Limpio | object     |
| ¿Tienes alguna sugerencia o comentario que te gustaría compartir con nosotros para mejorar el programa?_Resumido | object     |

## Eventos
Fuente Coordinación: ReunionEventos.xlsx
Renombramiento: 20250507_Encuestas_InformacionEventoCharlemosdelfuturo.xlsx
Destino: 20250507_Transformado_InformacionEventoCharlemosdelfuturo.xlsx

| Columna                                  | Tipo       |
|------------------------------------------|------------|
| Id                                       | int64      |
| Hora de inicio                           | datetime64[ns] |
| Hora de finalización                     | datetime64[ns] |
| Correo electrónico                       | object     |
| Nombre Completo                          | object     |
| Correo institucional                     | object     |
| ¿Qué semestre de la maestría se encuentra cursando? | object     |
| Nombre de la empresa y/o organización donde actualmente trabaja | object     |
| ¿Qué cargo ocupa actualmente?            | object     |
| ¿Qué cargo aspira al terminar la Maestría? | object     |
| LinkedIn                                 | object     |
| Nombre de la empresa y/o organización donde actualmente trabaja_Limpio | object     |
| ¿Qué cargo ocupa actualmente?_Limpio     | object     |
| ¿Qué cargo aspira al terminar la Maestría?_Limpio | object     |
| Año                                      | int32      |


## Profesores
Fuente Coordinación: ReunionEventos.xlsx
Renombramiento: 20250417_Encuestas_InformacionReunionProfesores.xlsx
Destino: 20250417_Transformado_InformacionReunionProfesores.xlsx

| Columna                                  | Tipo       |
|------------------------------------------|------------|
| ID                                       | int64      |
| Nombre                                   | object     |
| Cargo                                    | object     |
| Empresa                                  | object     |
| Correo electrónico                       | object     |
| Curso                                    | object     |
| Estado                                   | object     |
| Empresa_Limpia                           | object     |
| Cargo_Limpio                             | object     |


## ProyectoFinal
Fuente Coordinación: InformaciónProyectoFinal.xlsx 
Renombramiento: 20231110_Encuestas_InformacionCandidatosProyectoFinal.xlsx
Destino: 20231110_Transformado_InformacionCandidatosProyectoFinal.xlsx

| Columna                                  | Tipo       |
|------------------------------------------|------------|
| ID                                       | int64      |
| Hora de inicio                           | datetime64[ns] |
| Hora de finalización                     | datetime64[ns] |
| Correo electrónico                       | object     |
| Nombre                                   | object     |
| Hora de la última modificación           | float64    |
| Nombre completo                          | object     |
| Código                                   | int64      |
| correo electrónico2                      | object     |
| ¿Ya tiene grupo de trabajo? Recuerde que el número esperado es entre 3 y 4 integrantes. | object     |
| ¿Ya tiene empresa donde va a realizar el proyecto? | object     |
| Nombre de la empresa                     | object     |
| ¿Requiere de apoyo para encontrar empresa y proyecto? | object     |
| Nombre de la empresa_Limpio              | object     |
| Año                                      | int32      |
| Semestre                                 | int64      |
