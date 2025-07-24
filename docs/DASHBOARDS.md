# Nombramiento y relaciones de tableros Power BI

Cuando se desee crear una nueva **vista** basada en el nombramiento de un tablero ya existente, y su nombre de **fuente de datos** ya esté en uso, 
se recomienda usar un **guion (-)** para especificar que se trata de un **detalle o variante** adicional de esa vista.  

---

# Rutas Online
Repositorio Ruta Fuente : https://uniandes.sharepoint.com/sites/MINE779/Documentos%20compartidos/General/Anal%C3%ADtica/Datos/Raw/

Repositorio Ruta Destino : https://uniandes.sharepoint.com/sites/MINE779/Documentos%20compartidos/General/Anal%C3%ADtica/Datos/Processed/

---

## Estructura

| Proyecto `.pbix`            | Tablero                     | Fuente de datos (`Power Query Editor`)            |
|-----------------------------|-----------------------------|---------------------------------------------------|
| **EncuestasGenerales.pbix** | CandidatosProyectoFinal     | `InformacionCandidatosProyectoFinal`              |
|                             | EventoCharlemosdelfuturo    | `InformacionEventoCharlemosdelfuturo`             |
|                             | ReuniónEgresados            | `InformacionReunionEgresados`                     |
|                             | ReuniónEgresadosDetallada   | `InformacionReunionEgresados`                     |
|                             | ReuniónEstudiantes          | `InformacionReunionEstudiantes`                   |
|                             | ReuniónProfesores           | `InformacionReunionProfesores`                    |
|                             | ReuniónEmpleadores          | `InformacionReunionEmpleadores`                   |

---

## Buenas prácticas

- Usar nombres **claros y descriptivos** para los tableros.
- Mantener la **coherencia** entre nombre de tablero y archivo transformado.
- Agregar un **sufijo** con guion para distinguir variantes o detalles (`-Cursos`, `-General`, `-Periodos`, etc.).

---