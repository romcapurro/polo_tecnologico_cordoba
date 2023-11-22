
import matplotlib
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt

font = {'size': 14}
matplotlib.rc('font', **font)
st.title('Polo Tecnológico Córdoba')

# Mostrar una imagen
st.image('https://images.unsplash.com/photo-1523961131990-5ea7c61b2107?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', use_column_width=True)


def new_line():
    st.markdown("<br>", unsafe_allow_html=True)


# Contenido de la pestaña 'Análisis general'
tab_titles = ['💡 Objetivo del proyecto 󠀠 󠀠 󠀠 ', '🧭 Analizando Córdoba   ',
              "‍🧬‍ Benchmarking 󠀠󠀠 󠀠  ", "🗺️ Áreas con baja conectividad   ", "🧠 KPIs     󠀠 󠀠 󠀠 "]
tabs = st.tabs(tab_titles)

# Objetivo del proyecto
with tabs[0]:
    new_line()
    st.markdown("<h2 style='text-align: center; '>💡 Objetivo del proyecto</h2>    ",
                unsafe_allow_html=True)
    new_line()

    st.markdown("""
        El objetivo principal de este proyecto es contribuir a la transformación de la Provincia de Córdoba en un Polo Tecnológico. 
        Para lograrlo, se llevarán a cabo diversas actividades relacionadas con la infraestructura de tecnologías de la información y la comunicación (TIC).
        Este proyecto presenta el código en Python utilizado para analizar y visualizar datos relacionados con la conectividad en la provincia.
        """, unsafe_allow_html=True)
    new_line()

# Analizando Córdoba
with tabs[1]:
    new_line()
    st.markdown("<h2 style='text-align: center; 'id='análisis'>🧭 Analizando Córdoba (EDA)</h2> ",
                unsafe_allow_html=True)

    new_line()

    st.markdown("""
        Para cumplir con el objetivo propuesto fueron consideradas las siguientes situaciones en la provincia de Córdoba: Correlaciones entre Variables,
        Comparación con la Velocidad de Conexión, Análisis de Penetración de Fibra Óptica, Análisis de Datos de Conectividad, Análisis Estadístico. """, unsafe_allow_html=True)

    new_line()

    # conn_type = st.selectbox('Tipo de conexión:', [
    #     'TODAS', 'ADSL', 'CABLEMODEM', 'DIAL UP', 'FIBRA OPTICA', 'OTROS', 'SATELITAL', 'WIMAX', 'WIRELESS'])

    df_cordoba = pd.read_csv(
        'https://opcionerp.com/wp-content/uploads/DF_cordoba.csv')
    columns_to_convert = ['ADSL', 'CABLEMODEM', 'DIAL UP',
                          'FIBRA OPTICA', 'OTROS', 'SATELITAL', 'WIMAX', 'WIRELESS']

    # if conn_type != 'TODAS':
    #     columns_to_convert.remove(conn_type)
    #     df_cordoba.drop(columns=columns_to_convert, inplace=True)
    #     df_cordoba = df_cordoba[df_cordoba[conn_type] > 0]
    #     columns_to_convert = [conn_type]

    # Calcular la cobertura total para cada tipo de conexión
    total_coverage = df_cordoba[columns_to_convert].sum()

    # Graficar la cobertura total
    plt.figure(figsize=(10, 6))
    total_coverage.sort_values().plot(kind='barh', color="#6d4b61")

    # Ajustar la transparencia del fondo del gráfico
    plt.title('Cobertura total de conexiones en la provincia de Córdoba')
    plt.xlabel('Cantidad de conexiones')
    plt.ylabel('Tipo de conexión')
    st.pyplot(plt)

    # Visualizar la distribución de conexiones en cada tipo mediante boxplot
    plt.figure(figsize=(12, 8))
    df_cordoba[columns_to_convert].boxplot()

    plt.title(
        'Distribución de conexiones en diferentes localidades (Provincia de Córdoba)')

    plt.ylabel('Cantidad de conexiones')
    st.pyplot(plt)

    st.markdown("""
        **Basándome en las estadísticas descriptivas, aquí algunas conclusiones:**

1. **Conexiones dominantes:**
   - Las conexiones ADSL y de cablemódem tienen un recuento significativo, con medias de 243.93 y 206.42, respectivamente. Esto sugiere que estas dos tecnologías son las más comunes en las localidades de la provincia de Córdoba.

2. **Variedad en las conexiones:**
   - Existe una variedad significativa en los tipos de conexiones, como se refleja en las altas desviaciones estándar para ADSL, cablemódem, fibra óptica, y otros. Esto indica que algunas localidades tienen una mayor diversidad de opciones de conexión a Internet que otras.

3. **Fibra óptica:**
   - Aunque la media de conexiones de fibra óptica es relativamente alta (139.94), la desviación estándar también es considerable (238.29). Esto indica que mientras algunas localidades tienen una cantidad considerable de conexiones de fibra óptica, otras pueden tener muy pocas.

4. **Conexiones inalámbricas:**
   - Las conexiones inalámbricas tienen un recuento alto (299 registros) con una media de 127.13. Sin embargo, la alta desviación estándar (176.80) sugiere variabilidad en la cantidad de conexiones inalámbricas en diferentes localidades.

5. **Limitaciones:**
   - Las conexiones de marcado (DIAL UP) tienen un recuento muy bajo (5 registros), lo que puede no ser representativo de la realidad en todas las localidades. Se debe tener precaución al interpretar estos resultados debido a la baja cantidad de datos.

6. **Datos faltantes:**
   - Algunas categorías, como WiMAX, tienen un recuento muy bajo o nulo, lo que limita la capacidad de realizar conclusiones significativas sobre estas categorías.

En general, estos resultados sugieren que hay una diversidad significativa en la infraestructura de conexión a Internet en las localidades de la provincia de Córdoba. La elección de un tipo de conexión puede depender en gran medida de la ubicación geográfica, la disponibilidad de servicios y las preferencias de los usuarios en cada área. """, unsafe_allow_html=True)
    new_line()

# Benchmarking
with tabs[2]:
    new_line()
    st.markdown("<h2 style='text-align: center; '>‍🧬‍ Benchmarking</h2>",
                unsafe_allow_html=True)
    new_line()

    st.markdown("""
        Para el análisis de benchmarking se consideraron los siguientes provincias: Córboba, Buenos Aires, CABA, Chubut,
        Neuquen, Rio Negro, San Luis, Santa Cruz, Santa Fe,Tierra del Fuego.
        """, unsafe_allow_html=True)
    new_line()

    DF_provincias = pd.read_csv(
        'https://opcionerp.com/wp-content/uploads/DF_provincias.csv')

    # Colores en formato RGB con diferentes tonalidades
    violeta = [(0.4, 0.1, 0.4), (0.6, 0.3, 0.6)]
    aqua = [(0.1, 0.5, 0.6), (0.3, 0.7, 0.8)]
    gris = [(0.3, 0.3, 0.3), (0.5, 0.5, 0.5)]
    verde = [(0.1, 0.5, 0.2), (0.3, 0.7, 0.4)]

    colors = violeta + aqua + gris + verde

    provincias = DF_provincias['Provincia'].unique()
    provincias = np.insert(provincias, 0, 'TODAS')

    option = st.selectbox('Provincias', provincias)

    if 'TODAS' != option:
        DF_provincias = DF_provincias[DF_provincias['Provincia'] == option]

    # Realizar un gráfico de barras apiladas con los nuevos colores
    plt.figure(figsize=(12, 6))
    sns.countplot(x='Provincia', hue='Tipo de Tecnología',
                  data=DF_provincias, palette=colors)
    plt.xticks(rotation=45, ha='right')
    plt.title('Distribución de Tipos de Tecnologías por Provincia')
    plt.xlabel('Provincia')
    plt.ylabel('Cantidad de Conexiones')
    plt.legend(title='Tipo de Tecnología')

    # Mostrar el gráfico en Streamlit
    st.pyplot(plt)

    st.markdown("""
        Conclusiones:

1.  Distribución de Tecnologías por Provincia:
   - Buenos Aires: Presenta una diversidad de tecnologías, siendo ADSL la más común. También se observa la presencia de cablemódem, dial-up y fibra óptica en algunas localidades.
    - Córdoba: La distribución de tecnologías varía en diferentes localidades, con una presencia significativa de ADSL, fibra óptica y wireless. Algunas localidades muestran una falta de ciertos tipos de tecnologías.
    - CABA: Se destaca por tener una alta cantidad de conexiones wireless y cablemódem, con presencia de otras tecnologías en menor medida.
    - Chubut, Neuquén, Río Negro, San Luis, Santa Cruz, Santa Fe, Tierra del Fuego: Estas provincias muestran diferentes patrones de distribución de tecnologías. Algunas tienen una fuerte presencia de ADSL y otras de cablemódem, fibra óptica o wireless.

3.  Áreas de Mejora:
    - Identificar áreas donde ciertos tipos de tecnologías son limitadas o no están disponibles podría señalar oportunidades de mejora en la infraestructura de conectividad en esas localidades.

 4.  Enfoque en Fibra Óptica y Wireless:
    - La presencia de fibra óptica y conexiones inalámbricas (wireless) es notable en varias provincias. Estos podrían ser aspectos clave para mejorar la conectividad.
                
También es crucial considerar factores adicionales como densidad poblacional, características geográficas y políticas gubernamentales que podrían influir en la conectividad. """,
                unsafe_allow_html=True)

    new_line()

# Áreas con baja conectividad
with tabs[3]:
    new_line()
    st.markdown("<h2 style='text-align: center; '>‍🗺️‍ Áreas con baja conectividad</h2>    ",
                unsafe_allow_html=True)
    new_line()
    st.markdown("""
        Se identificaron áreas con baja conectividad en la provincia de Córdoba, considerando la cantidad de conexiones por cada 100 hogares como indicador.
        Se generó un listado de localidades con baja conectividad, lo que proporciona información valiosa para enfocar esfuerzos 
        y recursos en mejorar la infraestructura en estas áreas.
""", unsafe_allow_html=True)
    new_line()

    areas_baja_conectividad_cordoba = pd.read_csv(
        'https://opcionerp.com/wp-content/uploads/DF_areas_baja_conectividad.csv')

    primeras_10_localidades = areas_baja_conectividad_cordoba.head(10)

    # localidades = areas_baja_conectividad_cordoba['Localidad'].unique()
    # localidades = np.insert(localidades, 0, 'TODAS')

    # option = st.selectbox('Localidades', localidades)

    # if 'TODAS' != option:
    #     areas_baja_conectividad_cordoba = areas_baja_conectividad_cordoba[
    #         areas_baja_conectividad_cordoba['Localidad'] == option]
    #     primeras_10_localidades = areas_baja_conectividad_cordoba.head(10)

    # Graficar las conexiones por 100 hogares en las primeras 10 localidades
    plt.figure(figsize=(12, 6))
    plt.barh(primeras_10_localidades['Localidad'],
             primeras_10_localidades['Total Conexiones por 100 Hogares'], color="#6d4b61")
    plt.xlabel('Total Conexiones por 100 Hogares')
    plt.ylabel('Localidad')
    plt.title(
        'Conexiones por 100 Hogares en las Primeras 10 Localidades con Baja Conectividad en Córdoba')
    st.pyplot(plt)
    st.markdown("""
        Las conclusiones de los resultados indican que hay varias localidades en la provincia de Córdoba con baja conectividad, medida en términos de conexiones por cada 100 hogares. A continuación, se presentan algunas observaciones basadas en los datos analizados:

1. **Diversidad en la Magnitud de Baja Conectividad:** La magnitud de baja conectividad varía entre las diferentes localidades, yendo desde 1.0 hasta 15.0 conexiones por cada 100 hogares. Esto sugiere que algunas áreas tienen una situación más crítica que otras en términos de infraestructura de conexión.

2. **Dispersión Geográfica:** Las localidades con baja conectividad no están concentradas en una región específica de la provincia. Están distribuidas en varios partidos y áreas geográficas, lo que indica que la falta de conectividad no es un problema limitado a una sola zona.

3. **Enfoque Prioritario:** Dada la diversidad en la magnitud de baja conectividad, podría ser beneficioso para las autoridades y proveedores de servicios priorizar las áreas con las peores condiciones. Esto podría llevarse a cabo mediante inversiones adicionales en infraestructura o programas específicos para mejorar la conectividad en esas localidades.

4. **Análisis Continuo:** Es importante realizar un análisis continuo y monitoreo de la conectividad en la provincia para identificar cambios en el tiempo y evaluar la efectividad de las intervenciones realizadas.

5. **Colaboración con Comunidades:** Para abordar el problema de baja conectividad de manera efectiva, puede ser útil colaborar con las comunidades locales para comprender mejor sus necesidades y desafíos específicos.

Estas observaciones son puntos iniciales y se recomienda un analizar, factores adicionales como la densidad de población, la infraestructura existente y las condiciones socioeconómicas locales. Además, se debe tener en cuenta que la conectividad puede ser afectada por factores externos, como eventos climáticos o cambios en la demanda de servicios.
""", unsafe_allow_html=True)
    new_line()

# KPIs
with tabs[4]:
    new_line()
    st.markdown("<h2 style='text-align: center; '>‍🧠‍ KPIs</h2>    ",
                unsafe_allow_html=True)
    new_line()
    st.markdown("""
		Consigna:
        Debes graficar y medir el KPI propuesto a continuación, representándolo adecuadamente en el dashboard. A su vez, tambíen tienes que proponer, 
        medir y graficar un segundo KPI que consideres relevante para la temática. El KPI propuesto es:
        Aumentar en un 2% el acceso al servicio de internet para el próximo trimestre, cada 100 hogares, por provincia.
        """, unsafe_allow_html=True)
    new_line()

    df_kpi = pd.read_csv('https://opcionerp.com/wp-content/uploads/KPI.csv')

    # Selector de trimestre
    trimestres = df_kpi['Trimestre'].unique().astype('str')
    trimestres = np.insert(trimestres, 0, 'TODOS')
    trimestre = st.selectbox('Trimestres', trimestres, key="df_kpi")

    if trimestre != 'TODOS':
        df_kpi = df_kpi[df_kpi['Trimestre'] == trimestre.astype('int')]

    # Grafico el KPI
    # Configuración de estilo para seaborn
    sns.set(style="whitegrid")

    # Crear una figura y ejes
    plt.figure(figsize=(12, 6))

    # Graficar el KPI por provincia y trimestre
    sns.lineplot(x='Provincia', y='KPI', hue='Trimestre', data=df_kpi)

    # Ajustes adicionales para mejorar la visualización
    plt.title('KPI de Aumento en Acceso a Internet por Provincia')
    plt.xlabel('Provincia')
    plt.ylabel('KPI (%)')
    plt.xticks(rotation=45)

    # Ajustar la leyenda para que no se superponga con el gráfico
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

    # Eliminar las líneas punteadas en el gráfico
    sns.despine()
    st.pyplot(plt)

    st.markdown("""
		Propuesta de KPI
        Para establecer un KPI con un objetivo de mejora para el futuro, podríamos considerar un objetivo específico de incremento en la velocidad de bajada. Supongamos que deseamos aumentar la velocidad de bajada en un 5% para el próximo trimestre en comparación con el trimestre actual. El KPI podría calcularse de la siguiente manera:
                
        $Objetivo_KPI = ((Vel_media_futuro - Vel_media_actual)/Vel_media_actual)$ * 100
        """, unsafe_allow_html=True)
    new_line()

    # Grafico mi propuesta de KPI de aumento de velocidad del 5%
    df_velocidad = pd.read_csv(
        'https://opcionerp.com/wp-content/uploads/KPI2.csv')

    # Selector de trimestre
    trimestre = st.selectbox('Trimestres', trimestres, key="df_velocidad")

    if trimestre != 'TODOS':
        df_velocidad = df_velocidad[df_velocidad['Trimestre']
                                    == trimestre.astype('int')]

    # Configuración de estilo para seaborn
    sns.set(style="whitegrid")

    # Crear una figura y ejes
    plt.figure(figsize=(12, 6))

    # Graficar el KPI por provincia y año-trimestre
    sns.lineplot(x='Provincia', y='Objetivo_KPI',  hue='Trimestre',
                 data=df_velocidad)  # hue='Año-Trimestre', )

    # Ajustes adicionales para mejorar la visualización
    plt.title('KPI de Aumento en Acceso al 5 % por trimestre')
    plt.xlabel('Velocidad')
    plt.ylabel('KPI (%)')
    plt.xticks(rotation=83)
    st.pyplot(plt)
    st.markdown("""
		Conclusiones

1. Análisis de Velocidad Media de Internet:
   - Analisis de la velocidad media de Internet en diferentes provincias durante varios años y trimestres.
   - Se identificaron variaciones significativas en la velocidad media entre provincias y trimestres.


2. Objetivo de Mejora y KPI:
   - Propuesta de un objetivo de mejora del 5% en la velocidad media de Internet.
   - Nuevo KPI (Objetivo_KPI) para evaluar el progreso hacia ese objetivo.

3. Análisis de Objetivo_KPI:
   - Comparación la velocidad media actual con el objetivo del 5% para evaluar el rendimiento de cada provincia en cada trimestre.
   - Se identificaron provincias y trimestres que superaron o no alcanzaron el objetivo del 5%.

4. Ajustes y Consideraciones Adicionales:
   - Se realizaron ajustes en la presentación de datos y se consideró la conversión de variables a categóricas para facilitar el análisis y la visualización.

5. Conclusiones Específicas:
   - Se proporcionaron observaciones específicas sobre provincias con buen rendimiento, aquellas que necesitan mejoras y patrones identificados en el análisis gráfico.


        """, unsafe_allow_html=True)
    new_line()
