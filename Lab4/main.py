from typing import Optional
from joblib import load
from fastapi import FastAPI
from typing import List
import json

#import DataModel

import pandas as pd
from pydantic import BaseModel
# Para determinar el rendimiento del modelo con las métricas MSE, MAE y R2
from sklearn.metrics import r2_score

class DataModel(BaseModel):

# Estas varibles permiten que la librería pydantic haga el parseo entre el Json recibido y el modelo declarado.
    adult_mortality: float
    infant_deaths: float
    alcohol: float
    percentage_expenditure: float
    hepatitis_B: float
    measles: float
    bmi: float
    under_five_deaths: float
    polio: float
    total_expenditure: float
    diphtheria: float
    hiv_aids: float
    gdp: float
    population: float
    thinness_10_19_years: float
    thinness_5_9_years: float
    income_composition_of_resources	: float
    schooling: float
    #class Config:
      #orm_mode = True

#Esta función retorna los nombres de las columnas correspondientes con el modelo esxportado en joblib.
    def columns(self):
        return ["Adult Mortality", "infant deaths", "Alcohol","percentage expenditure","Hepatitis B", "Measles", "BMI",
                "under-five deaths", "Polio", "Total expenditure", "Diphtheria", "HIV/AIDS", "DGP", "Population",
                "thinness 10-19 years", "thinness 5-9 years", "Income composition of resources", "Schooling"]

class DataModelWithY(BaseModel):

# Estas varibles permiten que la librería pydantic haga el parseo entre el Json recibido y el modelo declarado.
    life_expectancy:float
    adult_mortality: float
    infant_deaths: float
    alcohol: float
    percentage_expenditure: float
    hepatitis_B: float
    measles: float
    bmi: float
    under_five_deaths: float
    polio: float
    total_expenditure: float
    diphtheria: float
    hiv_aids: float
    gdp: float
    population: float
    thinness_10_19_years: float
    thinness_5_9_years: float
    income_composition_of_resources	: float
    schooling: float
    #class Config:
      #orm_mode = True

#Esta función retorna los nombres de las columnas correspondientes con el modelo esxportado en joblib.
    def columns(self):
        return ["Life expectancy","Adult Mortality", "infant deaths", "Alcohol","percentage expenditure","Hepatitis B", "Measles", "BMI",
                "under-five deaths", "Polio", "Total expenditure", "Diphtheria", "HIV/AIDS", "DGP", "Population",
                "thinness 10-19 years", "thinness 5-9 years", "Income composition of resources", "Schooling"]              

class DataLista(BaseModel):
   dataL: List[DataModelWithY]
app = FastAPI()


@app.get("/")
def read_root():
   return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
   return {"item_id": item_id, "q": q}

@app.post("/predict")
def make_predictions(dataModel: DataModel):
    df = pd.DataFrame(dataModel.dict(), index=[0])
    df.columns = dataModel.columns()
    model = load("assets/modelo.joblib")
    result = model.predict(df)
    return result[0]

@app.post("/R2")
def compare_data(dataModel: DataLista):
    #df = pd.DataFrame(dataModel.dataL, index=[0])
    df=pd.DataFrame.from_records([s.dict() for s in dataModel.dataL])
    df.columns = ["Life expectancy","Adult Mortality", "infant deaths", "Alcohol","percentage expenditure","Hepatitis B", "Measles", "BMI",
                "under-five deaths", "Polio", "Total expenditure", "Diphtheria", "HIV/AIDS", "DGP", "Population",
                "thinness 10-19 years", "thinness 5-9 years", "Income composition of resources", "Schooling"] 
    print(df)
    model = load("assets/modelo.joblib")
    # Se selecciona la variable objetivo, en este caso "Life expectancy". 
    Y_Dado = df['Life expectancy']
    df=df.drop(['Life expectancy'], axis=1)
    result = model.predict(df)
    R2=r2_score(Y_Dado, result)
    return R2
    