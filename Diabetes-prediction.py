import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv("diabetes.csv")

X = df.drop("Outcome",axis=1)
y = df["Outcome"]

X_train,X_test,y_train,y_test=train_test_split(
X,y,test_size=0.2,random_state=42)

model = LogisticRegression(max_iter=1000)

model.fit(X_train,y_train)

prediction = model.predict(X_test)

print("Accuracy : ",accuracy_score(y_test,prediction))

patient = pd.DataFrame({
    "Pregnancies": [2], "Glucose": [120],
    "BloodPressure": [70], "SkinThickness": [20],
    "Insulin": [80], "BMI": [25.5],
    "DiabetesPedigreeFunction": [0.4], "Age": [35]
})

prediction = model.predict(patient)

if prediction[0] == 1:
    print("Prediction: Diabetic")
else:
    print("Prediction: Not Diabetic")