
import pandas as pd #Cargar el dataset
import dash #Crear el dashboard
import plotly.express as px #Crear las graficas
from dash import Dash, html, dcc 
from dash.dependencies import Input, Output # Crear el GUI

# Carga el archivo CSV
dataset = pd.read_csv("C:/Users/PC/Downloads/programacion/Tablafinal.csv", sep=';', encoding='latin1')# Cargar el dataset

# Renombra las columnas
df = dataset.rename(columns={
    'Consideras que la cantidad que se da de comida al estudiante es proporcional al pago que se hace':'comida al pago',
    'Cuantos almuerzos pagas a la semana  en promedio': 'Pago almuerzos semanal',
    'Edad del estudiante': 'Edad_estudiante',
    'Cuanto pagas por almuerzos al mes': 'Pago_almuerzo',
    'Grado que se encuentra cursando el estudiante Ingrese solo el grado sin ningun caracter especial de 1 a 9': 'Grado',
    'En promedio Cuantas veces por semana su hijo no termina su comida en la cafeteria y la deja desperdiciada': 'cantidaddesperdicio',
    'Como calificaria la variedad de alimentos ofrecidos en la cafetera escolar En una escala del 1 al 10': 'Variedad_alimentos',
    'Con que frecuencia utiliza su hijo los servicios de la cafeteria escolar': 'Frecuencia_cafeteria',
    'Cree que el desperdicio se puede deber a que no consumen los alimentos por motivos culturales religiosos o personales':'Motivo',
    'Su hijo esta a gusto con el menu de la cafeteria':'Gusto menu',
    'Si selecciono no por que no le gusta el menu':'razon de falta de gusto en el menu',
    'Como calificara la atencion del personal de la cafeteria y docentes ':'C.Atencion',
    'Si tu respuesta es menor a 5 en una sola palabra di el comportamiento en especifico que te disgusta':'Aspecto',
    'Consideras que la porcion de alimento que se le da a tu hijo es la adecuada para su edad':'Adecuada_edad'

})

app = dash.Dash(__name__)#crear una instancia de la aplicación Dash
   #definir el layout de la aplicacion web
app.layout = html.Div([
    dcc.Graph(id='Alimentacion-segun-el-grado'),
    dcc.Graph(id='Grafica-2'),
    dcc.Graph(id='Grafica-3'),
    dcc.Graph(id='Grafica-4'),
    dcc.Graph(id='Grafica-5'),
    dcc.Graph(id='Grafica-6'),
    dcc.Graph(id='Grafica-7'),
    dcc.Graph(id='Grafica-8'),
    dcc.Graph(id='Grafica-9'),
    dcc.Graph(id='Grafica-10'),
    dcc.Graph(id='Grafica-11'),
    dcc.Graph(id='Grafica-12'),
    dcc.Graph(id='Grafica-14'),
    dcc.Graph(id='Grafica-15'),
    dcc.Graph(id='Grafica-13'),
    dcc.Graph(id='Grafica-16'),
    dcc.Graph(id='Grafica-17'),
    dcc.Graph(id='Grafica-18'),
    dcc.Graph(id='Grafica-19'),
    
])

@app.callback( # Hace componentes de la interfaz de usuario reaccione a las interacciones del usuario y se actualicen.
    [Output('Alimentacion-segun-el-grado', 'figure'),
     Output('Grafica-2', 'figure'),
     Output('Grafica-3', 'figure'),
     Output('Grafica-4', 'figure'),
     Output('Grafica-5', 'figure'),
     Output('Grafica-6', 'figure'),
     Output('Grafica-7', 'figure'),
     Output('Grafica-8', 'figure'),
     Output('Grafica-9', 'figure'),
     Output('Grafica-10', 'figure'),
     Output('Grafica-11', 'figure'),
     Output('Grafica-12', 'figure'),
     Output('Grafica-14', 'figure'),
     Output('Grafica-15', 'figure'),
     Output('Grafica-13', 'figure'),
     Output('Grafica-16', 'figure'),
     Output('Grafica-17', 'figure'),
     Output('Grafica-18', 'figure'),
     Output('Grafica-19', 'figure')],

    [Input('Alimentacion-segun-el-grado', 'id')]
)

def Grafica(n):
    df_sum = df.groupby('Edad_estudiante')['Pago almuerzos semanal'].sum().reset_index()
    filtro = (df["Frecuencia_cafeteria"].isin(["De 1 a 2 veces por semana", "De 3 a 5 veces por semana", "Ocasionalmente", "Nunca"]))
    df_filtrado = df[filtro]
    #Calcular y filtrar el dataset en la columna de edad estudiante
    
    
    df_filtrado = df_filtrado[df_filtrado['Grado'] != 0]
    df_filtrado['Grado'] = pd.Categorical(df_filtrado['Grado'], categories=sorted(df_filtrado['Grado'].unique()))  # cambia la variable grado a una categorica y permite que aparezca en orden
    df_filtrado = df_filtrado.sort_values('Grado')#ordena las filas segun el grado
    df_filtrado12 = df_filtrado.sort_values('Variedad_alimentos')
    #filtrar el dataset en la columna de grado
    
    df_filtrado1 = df[df['razon de falta de gusto en el menu'] != 'no tengo respuesta']
    df_filtrado2 = df[df['Aspecto']!='no tengo respuesta']
    df_filtrado3 = df[df['C.Atencion']!=0 ]
    df_filtrado4 = df[df['Motivo']!=' ' ]
    df_filtrado5 = df[df['Grado']!=0]
    #Filtrar cada palabra del dataframe para que no se seleccione
    figure1 = px.bar(df_sum, x='Edad_estudiante', y='Pago almuerzos semanal', title='Alimentacion por edades')
    figure2 = px.scatter(df, x='Edad_estudiante', y='Pago almuerzos semanal', title='Alimentacion por edades')
    figure3 = px.scatter_3d(df, x='Edad_estudiante', y='Pago almuerzos semanal', z='Pago_almuerzo',title='Relacion del pago semanal por edades')
    figure4 = px.box(df, y='Edad_estudiante',title=' Edades de los estudiante encuestados')
    figure5 = px.bar(df_filtrado, x='Grado', y="Frecuencia_cafeteria", color='Frecuencia_cafeteria',title='Alimentacion por edades')
    figure6 = px.pie(df, names='Frecuencia_cafeteria', title='Frecuencia de Uso de la Cafetería Escolar')
    figure7 = px.pie(df_filtrado4,names='Motivo',title='Cree que el desperdicio puede deberse a motivos culturales,religiosos o personales')
    figure8 = px.scatter_3d(df, x='Gusto menu', y='Variedad_alimentos', z='Pago_almuerzo', color='Variedad_alimentos',title='Relación entre la Variedad del Menú, Satisfacción de los estudiantes y Pago de Almuerzos Mensuales')
    figure9 = px.violin(df, y='Pago almuerzos semanal', box=True, title='Distribución del Pago de Almuerzos Semanal')
    figure10= px.pie(df,names='Gusto menu',title='Su hijo esta a gusto con el menu de la cafeteria')
    figure11= px.bar(df_filtrado1, x='razon de falta de gusto en el menu',title='Si selecciono no cual cree que sea la razon')
    figure12= px.pie(df_filtrado3, names='C.Atencion',title='Como calificara la atencion del personal de la cafeteria y docentes ')
    figure14= px.pie(df, names='Adecuada_edad',title='Consideras que la porcion de alimento que se le da a tu hijo es la adecuada para su edad')
    figure15= px.pie(df, names='Variedad_alimentos',title='Del 1 al 10 califique la variedad de los alimentos')
    figure13= px.bar(df_filtrado2, x='Aspecto',title='Si tu respuesta es menor a 5 en una sola palabra di el comportamiento en especifico que te disgusta')
    figure15 = px.histogram(df, x='Edad_estudiante', nbins=20, title='Distribución de Edades')
    figure16 = px.pie(df_filtrado5, names='Pago almuerzos semanal', facet_col='Grado',title='Pago de Almuerzos por Grado')
    figure17 = px.bar(df_filtrado12, x='Grado', y='Pago almuerzos semanal', color='Variedad_alimentos',title='Pago de Almuerzos por Grado y Variedad', barmode='stack')
    figure18 = px.bar(df, x='Edad_estudiante', y='Pago almuerzos semanal', title='Pago de Almuerzos por Edad')
    figure19 = px.box(df, x='Grado', y='Pago almuerzos semanal', title='Distribución del Pago de Almuerzos por Grado')
    return figure1, figure2, figure3, figure4, figure5,figure6,figure7,figure8,figure9,figure10,figure11,figure12,figure14,figure15,figure13,figure16, figure17, figure18, figure19


if __name__ == '__main__':
    app.run_server(debug=True)