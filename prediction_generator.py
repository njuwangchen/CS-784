__author__ = 'ClarkWong'
from sklearn.ensemble import RandomForestClassifier
import pickle

with open('feature_matrix_train_20000.pickle', 'rb') as handle:
	feature_matrix_train = pickle.load(handle)

with open('classlabels_train_20000.pickle', 'rb') as handle:
    classlabels_train = pickle.load(handle)

with open('feature_matrix_predict.pickle', 'rb') as handle:
    feature_matrix_predict = pickle.load(handle)

# for i in feature_matrix_train[:20]:
#     print i
# print()
#
# for k in classlabels_train[:20]:
#     print k
# print()
#
# for j in feature_matrix_predict[:20]:
#     print j
# print()

rf = RandomForestClassifier(n_estimators = 100, min_samples_split=1)

threshold = 0.35

rf.fit(feature_matrix_train, classlabels_train)
y_pred_rf = rf.predict_proba(feature_matrix_predict).tolist()

y_pred = []
for item in y_pred_rf:
	if item[0] >= threshold:
		y_pred.append(0)
	else:
		y_pred.append(1)

line = 1
with open('result.txt', 'w') as output:
    for i in y_pred:
        if i == 0:
            output.write(str(line)+", MISMATCH\n")
        else:
            output.write(str(line)+", MATCH\n")
        line += 1