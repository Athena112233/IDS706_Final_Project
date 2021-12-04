#!/usr/bin/env python
# coding: utf-8

# In[2]:


from __future__ import print_function

import argparse
import os
import pandas as pd
import numpy as np

from sklearn.externals import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # Sagemaker specific arguments. Defaults are set in the environment variables.

    # Saves Checkpoints and graphs
    parser.add_argument(
        "--output-data-dir", type=str, default=os.environ["SM_OUTPUT_DATA_DIR"]
    )

    # Save model artifacts
    parser.add_argument("--model-dir", type=str, default=os.environ["SM_MODEL_DIR"])

    # Train data
    parser.add_argument("--train", type=str, default=os.environ["SM_CHANNEL_TRAIN"])

    args = parser.parse_args()

    file = os.path.join(args.train, "Cleaned_2018_Flights.csv")
    data = pd.read_csv(file, engine="python")

    data = data.dropna()
    data = data.drop(
        columns=[
            "Unnamed: 0",
            "ItinID",
            "MktID",
            "MktCoupons",
            "OriginWac",
            "DestWac",
            "ContiguousUSA",
            "Miles",
        ]
    )

    # Y: PricePerTicket; X: all other variables
    X = data.drop(columns=["PricePerTicket"])
    Y = data[["PricePerTicket"]]

    # Split training and testing dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X, Y, test_size=0.33, random_state=42
    )

    numerical_cols = ["NumTicketsOrdered"]
    categorical_cols = ["Quarter", "Origin", "Dest", "AirlineCompany"]

    categorical_transformer = Pipeline(
        steps=[("onehot", OneHotEncoder(handle_unknown="ignore"))]
    )
    preprocessor = ColumnTransformer(
        transformers=[("cat", categorical_transformer, categorical_cols)],
        remainder="passthrough",
    )
    
    LR_pipe = Pipeline([("preprocessor", preprocessor), ("LinearRegressor", LinearRegression())])
    LR_pipe.fit(X_train, y_train)

    joblib.dump(LR_pipe, os.path.join(args.model_dir, "model.joblib"))
    
def model_fn(model_dir):
    """Deserialized and return fitted model

    Note that this should have the same name as the serialized model in the main method
    """
    regressor = joblib.load(os.path.join(model_dir, "model.joblib"))
    return regressor

