from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score, recall_score

import pickle


with open('classlabels_train.pickle', 'rb') as handle:
	classlabels_train = pickle.load(handle)
with open('feature_matrix_train.pickle', 'rb') as handle:
	feature_matrix_train = pickle.load(handle)
with open('classlabels_test.pickle', 'rb') as handle:
	classlabels_test = pickle.load(handle)
with open('feature_matrix_test.pickle', 'rb') as handle:
	feature_matrix_test = pickle.load(handle)

rf = RandomForestClassifier(n_estimators = 100, min_samples_split=1)

threshold = 0.38

fold_size = 2000

precision = []
recall = []

test_data_1 = feature_matrix_test[:fold_size]
train_data_1 = feature_matrix_test[fold_size:]
test_class_1 = classlabels_test[:fold_size]
train_class_1 = classlabels_test[fold_size:]

rf.fit(train_data_1, train_class_1)
y_pred_rf = rf.predict_proba(test_data_1).tolist()

y_pred = []
for item in y_pred_rf:
	if item[0] >= threshold:
		y_pred.append(0)
	else:
		y_pred.append(1)

print "P; %f" % precision_score(test_class_1, y_pred)
print "R; %f" % recall_score(test_class_1, y_pred)

precision.append(precision_score(test_class_1, y_pred))
recall.append(recall_score(test_class_1, y_pred))

test_data_1 = feature_matrix_test[fold_size:fold_size*2]
train_data_1 = feature_matrix_test[:fold_size] + feature_matrix_test[fold_size*2:]
test_class_1 = classlabels_test[fold_size:fold_size*2]
train_class_1 = classlabels_test[:fold_size] + classlabels_test[fold_size*2:]

rf.fit(train_data_1, train_class_1)
y_pred_rf = rf.predict_proba(test_data_1).tolist()

y_pred = []
for item in y_pred_rf:
	if item[0] >= threshold:
		y_pred.append(0)
	else:
		y_pred.append(1)

print "P; %f" % precision_score(test_class_1, y_pred)
print "R; %f" % recall_score(test_class_1, y_pred)

precision.append(precision_score(test_class_1, y_pred))
recall.append(recall_score(test_class_1, y_pred))

test_data_1 = feature_matrix_test[fold_size*2:fold_size*3]
train_data_1 = feature_matrix_test[:fold_size*2] + feature_matrix_test[fold_size*3:]
test_class_1 = classlabels_test[fold_size*2:fold_size*3]
train_class_1 = classlabels_test[:fold_size*2] + classlabels_test[fold_size*3:]

rf.fit(train_data_1, train_class_1)
y_pred_rf = rf.predict_proba(test_data_1).tolist()

y_pred = []
for item in y_pred_rf:
	if item[0] >= threshold:
		y_pred.append(0)
	else:
		y_pred.append(1)

print "P; %f" % precision_score(test_class_1, y_pred)
print "R; %f" % recall_score(test_class_1, y_pred)

precision.append(precision_score(test_class_1, y_pred))
recall.append(recall_score(test_class_1, y_pred))

test_data_1 = feature_matrix_test[fold_size*3:fold_size*4]
train_data_1 = feature_matrix_test[:fold_size*3] + feature_matrix_test[fold_size*4:]
test_class_1 = classlabels_test[fold_size*3:fold_size*4]
train_class_1 = classlabels_test[:fold_size*3] + classlabels_test[fold_size*4:]

rf.fit(train_data_1, train_class_1)
y_pred_rf = rf.predict_proba(test_data_1).tolist()

y_pred = []
for item in y_pred_rf:
	if item[0] >= threshold:
		y_pred.append(0)
	else:
		y_pred.append(1)

print "P; %f" % precision_score(test_class_1, y_pred)
print "R; %f" % recall_score(test_class_1, y_pred)

precision.append(precision_score(test_class_1, y_pred))
recall.append(recall_score(test_class_1, y_pred))

test_data_1 = feature_matrix_test[fold_size*4:fold_size*5]
train_data_1 = feature_matrix_test[:fold_size*4]
test_class_1 = classlabels_test[fold_size*4:fold_size*5]
train_class_1 = classlabels_test[:fold_size*4]

rf.fit(train_data_1, train_class_1)
y_pred_rf = rf.predict_proba(test_data_1).tolist()

y_pred = []
for item in y_pred_rf:
	if item[0] >= threshold:
		y_pred.append(0)
	else:
		y_pred.append(1)

print "P; %f" % precision_score(test_class_1, y_pred)
print "R; %f" % recall_score(test_class_1, y_pred)

precision.append(precision_score(test_class_1, y_pred))
recall.append(recall_score(test_class_1, y_pred))

sum = 0
for i in precision:
    sum = sum+i
precision_avg = sum/5
print "precision", precision_avg

sum = 0
for i in recall:
    sum = sum+i
recall_avg = sum/5
print "recall", recall_avg

print "f1", precision_avg*recall_avg*2 / (precision_avg + recall_avg)

