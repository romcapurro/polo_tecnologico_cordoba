# Proyecto: Transformación de la Provincia de Córdoba en Polo Tecnológico

## Objetivos del Proyecto
El objetivo principal de este proyecto es contribuir a la transformación de la Provincia de Córdoba en un Polo Tecnológico. Para lograrlo, se llevarán a cabo diversas actividades relacionadas con la infraestructura de tecnologías de la información y la comunicación (TIC). Este README presenta el código en Python utilizado para analizar y visualizar datos relacionados con la conectividad en la provincia.

## Descripción del Código
El código se centra en el análisis de datos de accesos a Internet en diferentes localidades de la Provincia de Córdoba. Utiliza la biblioteca pandas para manipular los datos y matplotlib y seaborn para la visualización. A continuación, se detalla el contenido del código:

1. **Carga de Datos:**
   - Se carga el conjunto de datos desde el archivo CSV '15-AccesosaInternetfijoportecnologiaylocalidad_2791751699377796593.csv' en un DataFrame llamado `DF_accesos_localidad`.

2. **Limpieza de Datos:**
   - Se elimina la columna 'Unnamed: 13', ya que no contiene información relevante.

3. **Filtrado por Provincia:**
   - Se filtran las filas para incluir solo aquellas donde la provincia es 'CORDOBA', creando un nuevo DataFrame llamado `DF_cordoba`.

4. **Conversión de Tipos de Datos:**
   - Se convierten las columnas relevantes a tipos numéricos para facilitar el análisis.

5. **Análisis Estadístico:**
   - Se realizan cálculos estadísticos descriptivos y se visualizan mediante gráficos de barras y boxplot para comprender la distribución de conexiones en la provincia.

6. **Identificación de Áreas con Baja Conectividad:**
   - Se integra otro conjunto de datos sobre la penetración de Internet en cada 100 hogares.
   - Se identifican y presentan las áreas con baja conectividad en la provincia de Córdoba.

7. **Visualización de Áreas con Baja Conectividad:**
   - Se grafican las conexiones por cada 100 hogares en las primeras 10 localidades con baja conectividad en Córdoba.

8. **Benchmarking con Otras Provincias:**
   - Se realiza un análisis comparativo de la distribución de tecnologías en Córdoba y otras provincias seleccionadas.

## Instrucciones de Ejecución:
1. Asegúrate de tener Python instalado en tu entorno.
2. Ejecuta el código en un entorno que admita la ejecución de scripts de Python.
3. Asegúrate de tener todas las bibliotecas necesarias instaladas (`pandas`, `matplotlib`, `seaborn`).

## Proyecto: Convertir a la Provincia de Córdoba en Polo Tecnológico

### Objetivos del Proyecto:
El objetivo principal de este proyecto es transformar a la Provincia de Córdoba en un Polo Tecnológico, promoviendo el acceso a Internet y fomentando el desarrollo de infraestructuras tecnológicas. Para lograrlo, se llevarán a cabo las siguientes acciones:

#### 1. Análisis de Conectividad:
   - Se realizará un análisis detallado de la conectividad en la provincia, identificando áreas con baja conectividad.
   - Se buscará mejorar la infraestructura en las localidades con deficiencias en el acceso a Internet.

#### 2. Promoción de Tecnologías de Conexión:
   - Se buscará aumentar la adopción de tecnologías avanzadas, como la fibra óptica, para mejorar la calidad de la conexión.

#### 3. Benchmarking con Otras Provincias:
   - Se comparará el estado de la conectividad en Córdoba con otras provincias para identificar oportunidades de mejora y adoptar mejores prácticas.

### Conclusiones y Acciones Propuestas:
- Se identificaron periodos con mejores y peores ingresos.
- Se analizó la penetración de Internet fijo y por cada 100 habitantes.
- Se compararon las tecnologías de Banda Ancha Fija y Dial up.
- Se visualizó la distribución de velocidades de Internet por provincia y trimestre.
- Se analizó la distribución de tipos de conexiones en la provincia de Córdoba, calculando la velocidad promedio y la cobertura por tipo de conexión.

Con estos insights, se proponen acciones para impulsar el desarrollo tecnológico en Córdoba, incluyendo mejoras en la infraestructura de Internet, promoción de tecnologías de banda ancha y estrategias para aumentar la cobertura de conexiones de alta velocidad.

