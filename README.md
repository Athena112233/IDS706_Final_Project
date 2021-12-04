# Airplane Ticket Price Prediction Tool
## Remaining Tasks
1. Deploy model (Tianyun)
2. Connect lambda to model endpoint and output solution (Athena)
3. Build website using APP Runner or S3 (Ying)
4. Send solution back to user via lambda or API gateway (Minjung)
5. Readme writing 
6. Demo


## Introduction
This Airplane Ticket Price Prediction Tool aims to provide users with price predictions based on a pre-trained machine learning model through an interactive website.  
The tool primarily consists of two parts:
* **Machine learning model (Amazon SageMaker)**

The data we used for building the model contains information for domestic flights in the United States from 2018. (Source: https://www.kaggle.com/zernach/2018-airplane-flights).

Data is stored in the AWS S3 bucket. Feature engineering, model building, and model validation will be implemented on Amazon SageMaker as the main platform. 
(add model later)
* **Interactive website for the final deliverable (AWS S3 Website)**

The website can be accessed at https://athena112233.github.io/airplane_ticket_price/.
Users will interact with this website to utilize this tool to get multiple  ticket price predictions based on their custom inputs.  The website will allow users to input variables (e.g.  origin, destination) and return multiple predictions generated from the pre-trained ML model for users to compare and optimize their travel plan.
 
## Methods
![IDS7061](https://user-images.githubusercontent.com/90014065/144720495-b60e9359-225b-4149-8365-f9d40549d3ec.png)
### Data Cleaning Pipeline
* Dropped Columns: 'Unnamed: 0', 'ItinID', 'MktID', 'MktCoupons', 'OriginWac', 'DestWac', 'ContiguousUSA', 'Miles'
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
