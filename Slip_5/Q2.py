import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import seaborn as sns

pima =  pd.read_csv(r"C:\Users\Vishwanath\Practicals---\DM_Slips\Slip_5\diabetes.csv")
feature_cols=['Pregnancies','Insulin','BMI','Age','Glucose','BloodPressure',
 'DiabetesPedigreeFunction']
x=pima[feature_cols]
y=pima.Outcome
X_train,X_test,Y_train,Y_test =train_test_split(x,y,test_size=0.3,random_state=1)
classifier=DecisionTreeClassifier()
classifier=classifier.fit(X_train,Y_train)
y_pred=classifier.predict(X_test)
print(y_pred)
from sklearn.metrics import confusion_matrix
confusion_matrix(Y_test,y_pred)
print(confusion_matrix(Y_test,y_pred))
#accuracy
print("accuracy:",metrics.accuracy_score(Y_test,y_pred))
from six import StringIO
from IPython.display import Image
from sklearn.tree import export_graphviz
import pydotplus
dot_data=StringIO()
export_graphviz(classifier,out_file=dot_data,filled=True, rounded=True,special_characters=True,feature_names=feature_cols,class_names=['0','1'])
graph=pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('diabetes.png')
Image(graph.create_png())