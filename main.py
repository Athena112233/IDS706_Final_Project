import boto3, os, json
import numpy as np
import pandas as pd
import sklearn
import sagemaker
import pickle
import warnings
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

warnings.filterwarnings("ignore")

templates = Jinja2Templates(directory = "templates")

@app.get("/")
async def dashboard(request: Request):
    #return {
    #    "message": "Please enter your travel plan in the following format: Quarter,Origin,Destination,Number of ticket,Airline. For example: 1,BOS,LAX,2,AA"
    #}
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "somevar": 2
    })
    


@app.get("/PricePredict/{plan}")
async def predict(plan: str):
    
    s3 = boto3.client("s3")
    bucket = "airplane-ticket-model"
    key1 = "preprocessor.sav"
    key2 = "lr_model.sav"
    
    my_pickle = s3.get_object(Bucket=bucket, Key=key1)
    preprocessor = pickle.loads(my_pickle["Body"].read())
    my_pickle2 = s3.get_object(Bucket=bucket, Key=key2)
    model = pickle.loads(my_pickle2["Body"].read())

    # input = {"data": plan}
    types = {
        "Quarter": np.float64,
        "Origin": str,
        "Dest": str,
        "NumTicketsOrdered": np.float64,
        "AirlineCompany": str,
    }
    
    data = plan.split(",")
    df = pd.DataFrame(data).transpose()
    df.columns = list(types.keys())
    df = df.astype(types)
    df.to_numpy()

    transformed_data = preprocessor.transform(df)
    predict = "$" + str(round(model.predict(transformed_data)[0][0], 2))
    
    return {"Your predicted price will be:": predict}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
