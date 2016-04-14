import pickle
from sklearn.metrics import precision_score, recall_score
from sklearn import svm, linear_model
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import cross_validation

with open('classlabels_train.pickle', 'rb') as handle:
	classlabels_train = pickle.load(handle)
with open('feature_matrix_train.pickle', 'rb') as handle:
	feature_matrix_train = pickle.load(handle)
with open('classlabels_test.pickle', 'rb') as handle:
	classlabels_test = pickle.load(handle)
with open('feature_matrix_test.pickle', 'rb') as handle:
	feature_matrix_test = pickle.load(handle)

#print len(classlabels_test), len(classlabels_train),len(feature_matrix_test),len(feature_matrix_train)
k = 8000   # 9900 out of 10000 as the training set, 10000-9900 as the tuning set
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


####Random Forest,
## The number of trees in the forest, n_estimators 
rf = RandomForestClassifier(n_estimators = 100, min_samples_split=1)
print rf.fit(X,Y)
y_pred_rf = rf.predict_proba(x).tolist()
print "random forest"

y_pred = []
for item in y_pred_rf:
	if item[0] >= 0.3:
		y_pred.append(0)
	else:
		y_pred.append(1)

print "P; %f" % precision_score(y_true, y_pred)
print "R; %f" % recall_score(y_true, y_pred)


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
clf = svm.SVC(C=1000, class_weight =  {0: 5, 1: 1})
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

print

#test_set cv
# rf = RandomForestClassifier(n_estimators = 100, min_samples_split=1)
# precision = cross_validation.cross_val_score(rf, feature_matrix_test, classlabels_test, cv=5, scoring='precision')
# recall = cross_validation.cross_val_score(rf, feature_matrix_test, classlabels_test, cv=5, scoring='recall')
# print "test set random forest"
# print "Precision:", precision.mean()
# print "Recall:", recall.mean()
#
# clf = svm.SVC(C=1000, class_weight =  {0: 5, 1: 1})
# precision = cross_validation.cross_val_score(clf, feature_matrix_test, classlabels_test, cv=5, scoring='precision')
# recall = cross_validation.cross_val_score(clf, feature_matrix_test, classlabels_test, cv=5, scoring='recall')
# print "test set svm"
# print "Precision:", precision.mean()
# print "Recall:", recall.mean()

rf = RandomForestClassifier(n_estimators = 100, min_samples_split=1)

fold_size = 2000
test_data_1 = feature_matrix_test[:fold_size]
train_data_1 = feature_matrix_test[fold_size:fold_size*2]
test_class_1 = classlabels_test[:fold_size]
train_class_1 = classlabels_test[fold_size:fold_size*2]

rf.fit(train_data_1, train_class_1)
y_pred_rf = rf.predict_proba(test_data_1).tolist()

y_pred = []
for item in y_pred_rf:
	if item[0] >= 0.3:
		y_pred.append(0)
	else:
		y_pred.append(1)

print "P; %f" % precision_score(y_true, y_pred)
print "R; %f" % recall_score(y_true, y_pred)



