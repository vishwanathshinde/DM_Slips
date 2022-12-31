import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

df = pd.read_csv(r"C:\Users\Vishwanath\Practicals---\DM_Slips\Slip_16\diabetes.csv")
feature_cols = ['Pregnancies', 'Glucose', 'BloodPressure','Insulin','BMI','DiabetesPedigreeFunction','Age']


x = df[feature_cols]
y = df.Outcome
X_train, X_test, Y_train, Y_test = train_test_split(x,y,test_size=0.3,random_state=1)
classifier = DecisionTreeClassifier()
classifier = classifier.fit(X_train,Y_train)
y_pred = classifier.predict(X_test)
print(y_pred)

from sklearn.metrics import confusion_matrix
confusion_matrix(Y_test,y_pred)
print(confusion_matrix(Y_test,y_pred))

print(metrics.accuracy_score(Y_test,y_pred))

from six import StringIO
from sklearn.tree import export_graphviz
import pydotplus

dot_data = StringIO()
export_graphviz(classifier, out_file=dot_data)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('Diabetes.png')