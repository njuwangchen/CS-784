import pickle
from sklearn.metrics import precision_score, recall_score
from sklearn import svm, linear_model
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier

with open('classlabels_train.pickle', 'rb') as handle:
	classlabels_train = pickle.load(handle)
with open('feature_matrix_train.pickle', 'rb') as handle:
	feature_matrix_train = pickle.load(handle)
with open('classlabels_test.pickle', 'rb') as handle:
	classlabels_test = pickle.load(handle)
with open('feature_matrix_test.pickle', 'rb') as handle:
	feature_matrix_test = pickle.load(handle)

#print len(classlabels_test), len(classlabels_train),len(feature_matrix_test),len(feature_matrix_train)
k = 9900   # 9900 out of 10000 as the training set, 10000-9900 as the tuning set
X = feature_matrix_train[:k]
Y = classlabels_train[:k]

#tuning
y_true = classlabels_train[-(10000-k):]
x = feature_matrix_train[-(10000-k):]

####Decision Tree
dt = DecisionTreeClassifier()
print dt.fit(X,Y)
y_pred_dt = dt.predict(x).tolist()
print "Decision Tree"
print "P; %f" % precision_score(y_true, y_pred_dt)
print "R; %f" % recall_score(y_true, y_pred_dt)


####Random Forest
nb = GaussianNB()
print nb.fit(X,Y)
y_pred_nb = nb.predict(x).tolist()
print "naive bayes"
print "P; %f" % precision_score(y_true, y_pred_nb)
print "R; %f" % recall_score(y_true, y_pred_nb)


####Naive Bayes
nb = GaussianNB()
print nb.fit(X,Y)
y_pred_nb = nb.predict(x).tolist()
print "naive bayes"
print "P; %f" % precision_score(y_true, y_pred_nb)
print "R; %f" % recall_score(y_true, y_pred_nb)
#print(metrics.classification_report(y_true, y_pred_nb))
#print(metrics.confusion_matrix(y_true, y_pred_nb))


####Support Vector Machines
clf = svm.SVC()
print clf.fit(X, Y)
#my_list[-5:] # grab the last five elements
y_pred_svm = clf.predict(x).tolist()
#print y_true_svm
#print y_pred_svm
print "SVM"
print "P; %f" % precision_score(y_true, y_pred_svm)
print "R; %f" % recall_score(y_true, y_pred_svm)

####Logistic Regression
logreg = linear_model.LogisticRegression(C=1)
print logreg.fit(X, Y)
y_pred_logreg = logreg.predict(x).tolist()
#print y_pred_logreg
print "Log Reg"
print "P; %f" % precision_score(y_true, y_pred_logreg)
print "R; %f" % recall_score(y_true, y_pred_logreg)
