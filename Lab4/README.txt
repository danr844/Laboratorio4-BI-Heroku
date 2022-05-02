Instrucciones de instalación, despliegue y funcionamiento del API.
1. Clonar el repositorio https://github.com/danr844/Laboratorio4-BI-Heroku.git de Github
2. Instalar las siguientes librerías, en la terminal del dispositivo: 
	pip install fastapi
	pip install "uvicorn[standard]" 
3. Ejecutar el archivo main.py con el siguiente comando: python -m uvicorn main:app --reload (Preferiblemente en VSCODE con python instalado)
4. Abrir cualquier aplicación que permita la subida de archivos mediante el método POST (Se utiliza preferiblemente Postman)
5. Se ingresan las direcciones dependiendo de los servicios a los que se quiera acceder:
	http://127.0.0.1:8000/predict -Para obtener la predicción que realiza el modelo propuesto
	http://127.0.0.1:8000/R2 -Para calcular el R cuadrado de los datos subidos y de las prediciones para la variable Life Expectancy
6. Posteriormente se ingresa en JSON los datos de la siguiente forma para los respectivos servicios (Para que el programa los pueda representar como un dataframe):
a. Para realizar el predict, el formato debe ser de la siguiente forma
{
    "adult_mortality": 71.0,
    "infant_deaths": 1.0,
    "alcohol": 9.97,
    "percentage_expenditure": 3829.550928,
    "hepatitis_B": 95.0,
    "measles": 91.0,
    "bmi": 6.3,
    "under_five_deaths": 1.0,
    "polio": 92.0,
    "total_expenditure": 8.32,
    "diphtheria": 93.0,
    "hiv_aids": 0.1,
    "gdp": 23465.38559,
    "population": 198954.0,
    "thinness_10_19_years": 0.7,
    "thinness_5_9_years": 0.7,
    "income_composition_of_resources": 0.905,
    "schooling": 20.6
}
b. Para calcular el R2 el formato debe ser de la siguiente forma:
{
    "dataL": [
        {
            "life_expectancy": 59.9,
            "adult_mortality": 271.0,
            "infant_deaths": 64.0,
            "alcohol": 0.01,
            "percentage_expenditure": 73.52358168,
            "hepatitis_B": 62.0,
            "measles": 492.0,
            "bmi": 18.6,
            "under_five_deaths": 86.0,
            "polio": 58.0,
            "total_expenditure": 8.18,
            "diphtheria": 62.0,
            "hiv_aids": 0.1,
            "gdp": 612.696514,
            "population": 327582.0,
            "thinness_10_19_years": 17.5,
            "thinness_5_9_years": 17.5,
            "income_composition_of_resources": 0.476,
            "schooling": 10.0
        },
        {
            "life_expectancy": 59.9,
            "adult_mortality": 268.0,
            "infant_deaths": 66.0,
            "alcohol": 0.01,
            "percentage_expenditure": 73.21924272,
            "hepatitis_B": 64.0,
            "measles": 430.0,
            "bmi": 18.1,
            "under_five_deaths": 89.0,
            "polio": 62.0,
            "total_expenditure": 8.13,
            "diphtheria": 64.0,
            "hiv_aids": 0.1,
            "gdp": 631.744976,
            "population": 31731688.0,
            "thinness_10_19_years": 17.7,
            "thinness_5_9_years": 17.7,
            "income_composition_of_resources": 0.47,
            "schooling": 9.9
        }]}
7. Después de esto, el programa por si solo realiza una estandarización de los datos, se asegura que sean numéricos y llena los espacios vacíos de cada columna con
   la media respectiva. Finalmente, el pipeline ejecuta un modelo de regresión lineal ya realizado anteriormente por nosotros para poder obtener los valores deseados y 
   los arroja como respuesta hacia la aplicación que se usó.
8. Posteriormente se pueden hacer todas las solicitudes que se deseen. (Teniendo en cuenta factores como que no se ingresen números que no puedan ser almacenados en
   float y que en el caso del R2 no poner menos de 2 registros ya que este no podrá calcular la regresión)