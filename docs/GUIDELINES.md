## 1. Estructura de Carpetas para la Documentación
📂 Documentación
├── 📄 README.md (Descripción general del proyecto y convenciones)
├── 📄 Guía de Uso (Instrucciones para usuarios y desarrollo)
├── 📄 Políticas de Nomenclatura (Estándares de nombres de archivos y carpetas)
├── 📄 Diccionario de Datos (Descripción de cada campo y origen)
├── 📄 Histórico de Cambios (Registro de modificaciones en el modelo de datos)
├── 📄 Gestión de Permisos (Roles y accesos a cada recurso)

## 2. Estructura de Carpetas para los Datos
📂 Datos
├── 📂 Raw (Datos Brutos)
│ ├──  YYYYMMDD_Fuente_Dataset.xlsx
│ ├── 📄 README.md (Definición de las fuentes)
├── 📂 Processed (Datos Procesados)
│ ├──  YYYYMMDD_Transformado_OtrosDatos.xlsx
│ ├── 📄 README.md (Reglas de transformación aplicadas)

## 3. Políticas de Nomenclatura
Archivos de datos:
    YYYYMMDD_Fuente_NombreDelDataset.ext (Ejemplo: 20250310_SharePoint_Estudiantes.xlsx)
Columnas en bases de datos:
    Para nombres (id_estudiante, fecha_nacimiento)
    Prefijos según el tipo (dim_ para dimensiones, fact_ para hechos)
Versionado:
    v1, v2, etc., en scripts o archivos importantes.
Carpetas:
    Siempre en inglés (Raw, Processed)
    Evitar espacios en nombres de carpetas (Datos_Brutos en vez de Datos Brutos)

## 4. Control de Acceso y Permisos
📂 Documentación: Solo lectura para todos, edición para administradores.
📂 Datos Brutos: Solo algunos usuarios pueden escribir, todos pueden leer.
📂 Datos Procesados: Acceso restringido según roles definidos.