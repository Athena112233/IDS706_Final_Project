import boto3, os, json
import numpy as np
import pandas as pd 
import sklearn
import sagemaker
import pickle
import warnings

warnings.filterwarnings('ignore')

s3 = boto3.client("s3")

bucket = "airplane-ticket-model"
key1 = "preprocessor.sav"
key2 = "lr_model.sav"

my_pickle = s3.get_object(Bucket= bucket, Key = key1)
preprocessor = pickle.loads(my_pickle['Body'].read())
my_pickle2 = s3.get_object(Bucket= bucket, Key = key2)
model = pickle.loads(my_pickle2['Body'].read())


input = {"data": "1,BOS,LAX,2,AA"}
types = {"Quarter": np.float64, "Origin": str, "Dest": str,"NumTicketsOrdered": np.float64, "AirlineCompany": str}
data = input['data'].split(",")
df = pd.DataFrame(data).transpose()
df.columns = list(types.keys())
df = df.astype(types)
df.to_numpy()

transformed_data = preprocessor.transform(df)
predict = model.predict(transformed_data)
print(predict)