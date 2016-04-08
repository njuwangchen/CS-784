import pickle
from sklearn.metrics import precision_score, recall_score
from sklearn import svm

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
y = classlabels_train[:k]
y_true_svm = classlabels_train[-(10000-k):]

####Decision Tree

####Random Forest

####Naive Bayes

####Support Vector Machines
clf = svm.SVC()
print clf.fit(X, y)
#my_list[-5:] # grab the last five elements
y_pred_svm = clf.predict(feature_matrix_train[-(10000-k):]).tolist()
#print y_true_svm
#print y_pred_svm
print "SVM"
print "P; %f" % precision_score(y_true_svm, y_pred_svm)
print "R; %f" % recall_score(y_true_svm, y_pred_svm)

####Logistic Regression

