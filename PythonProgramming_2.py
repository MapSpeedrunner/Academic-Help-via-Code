import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
data={
    "Size":[1200,1500,900,1800,1000,1300,850,2000,1100,1600,950,2100,1050,1250,1400,1750],
    "Location":[1,1,0,1,0,1,0,1,1,1,0,1,0,1,1,1],
    "Bedrooms":[3,4,2,4,3,3,2,5,3,4,2,5,3,3,3,4],
    "Price":[75,95,45,120,55,80,40,150,70,100,50,160,60,85,90,130]
    }
df=pd.DataFrame(data)

#Features (X) and Target (y)
X=df[["Size","Location","Bedrooms"]]
y=df["Price"]

#Splitting the dataset
X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.25, random_state=42)

#Linear Regression Model
model= LinearRegression()
model.fit(X_train, y_train)

#Predictions
y_pred=model.predict(X_test)

#Calculating Mean Squared Error
mse=mean_squared_error(y_test, y_pred)
rmse=np.sqrt(mse)

#Displaying Results
print("Test Set Actual Prices:", y_test.values)
print("Predicted Prices:", y_pred)
print("Mean Squared Error (MSE):", mse)
print("Root Mean Squared Error (RMSE):", rmse)

#Plotting Predictions
plt.scatter(range(len(y_test)), y_test, color="blue", label="Actual Prices")
plt.scatter(range(len(y_pred)),y_pred, color="red", label="Predicted Prices")
plt.title("Actual v/s Predicted Housing Prices")
plt.xlabel("Test Data Points")
plt.ylabel("House Prices (in Lakhs)")
plt.legend()
plt.show()
