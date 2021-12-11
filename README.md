# Airplane Ticket Price Prediction Tool
Please visit our product website: https://athena112233.github.io/airplane_ticket_price/

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
![IDS7062](https://user-images.githubusercontent.com/90014065/145660927-8133682b-68d0-43a1-b622-9f3682921bb6.png)

### Data Cleaning Pipeline
Our data cleaning pipeline consist of two components: remove unnecesscary data and transforming the data.
1. Remove Unnecessary Data: 
   dropped irrelevant data fields from the dataset which include 'Unnamed: 0', 'ItinID', 'MktID', 'MktCoupons', 'OriginWac', 'DestWac', 'ContiguousUSA', 'Miles'.
2. Transform data into sklearn readable format:
   * Categorical: Quarter, Airline Company, Origin, Destination
   * Numerical: Number Tickets Ordered 
   All the categorical variables are One-Hot-Encoded using the Scikit-Learn pre-built encoder function. The numeric variable remains the same.
The above steps finalized our input data into Ont-Hot-Encoded Quarter, Airline Company, Origin, Destination, and the numeric variable Number Tickets Ordered.

### Model Building
The model was built and deployed through Amazon SageMaker. Source codes for trianing the model are located in the model subfolder. We tested three ML algorithms -- Linear Regression, Support Vector Machine Regressor, and Random Forest Regressor. Out of the three, the Linear Regression Model has the best runtime and the best accuracy. Thus, our finalized model deployed to production is a Linear Regression model with PricePerTicket as the repsonse variable, and the transformed Origin, Destiantion, Airline Company, and Number Tickets Ordered as the response variables. 

### Model Validation
In order to assess the performance of the model, we used sklearn evaluation metrics. Mean squared error (MSE) takes the mean squared difference between the target and predicted values. This value is widely used for many regression problems and larger errors have correspondingly larger squared contributions to the mean error. 

### Model Deployment
## How to run this repo?
## User guide
Users can go to our website https://athena112233.github.io/airplane_ticket_price/ and find the 'Product' tab.
There users can see a link to our FastAPI document site.
Users can input information about their trip in a style of quarter, origin, destination, number of ticket, airline.(e.g. 1, LAX, JFK, 1, DL).
Users can click the 'Predict'.
The predicted price with users' input will be presented.
