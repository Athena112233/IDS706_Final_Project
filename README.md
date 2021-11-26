# Airplane Ticket Price Prediction Tool
## Introduction
## Methods
### Data Cleaning Pipeline
* Dropped Columns: 'Unnamed: 0', 'ItinID', 'MktID', 'MktCoupons', 'OriginWac', 'DestWac', 'ContiguousUSA'
### Model Building
### Model Validation
### Model Deployment
## Conclusion
## How to run this repo?
### How to run on SageMaker (for team members only)
* Follow this tutorial to set up a SageMaker Instance https://aws.amazon.com/getting-started/hands-on/build-train-deploy-machine-learning-model-sagemaker/
* After instance is ready, click on Jupyter Lab
* upload the file models/modeling.ipynb to Jupyter Lab
* In the 4th cell, modify bucket and file name to the S3 bucket that stores your dataset
* Run the file and do the following:
  * Set up feature tranformation pipeline
  * Set up model pipeline
  * Test model 
