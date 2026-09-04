import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df=pd.read_csv("C:/Users/nidum/Downloads/USA_Housing.csv")
df.head()
print("Dataset Shape:", df.shape)
print(df.describe())
print(df.columns)
df.drop(["Address"], inplace=True, axis=1)
x=df.drop(["Price"], axis=1) #Separating x (independent variables- All features except Price)
print(x)
y=df["Price"] #Dependent variable-Price
print(y)

#Splitting the dataset into 80% training and 20% testing
X_train, X_test, y_train, y_test= train_test_split(x,y, test_size=0.2, random_state=42)
print("Training Data Shape:", X_train.shape, y_train.shape)
print("testing Data Shape:", X_test.shape, y_train.shape)
X_train.head()
y_train.head()

model=LinearRegression()
model.fit(X_train, y_train)

y_pred=model.predict(X_test)
y_pred[0:5]
comparison_df=pd.DataFrame({"Actual Price":y_test, "Predicted Price":y_pred.astype(float).round(3)})
print(comparison_df.head(10)) #Display first 10 comparisons

