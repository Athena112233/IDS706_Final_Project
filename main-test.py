from fastapi.testclient import TestClient
from fastapi import FastAPI
from main1 import app
import pytest

client = TestClient(app)

def test_main():
    # test get recipe function
    
    response = client.get("/PricePredict/1,BOS,LAX,2,AA")
    assert response.json() ==  {'Your predicted price will be:': '$289.4'}
    assert response.status_code == 200