import numpy as np
from sklearn.metrics import confusion_matrix, fbeta_score, classification_report, cohen_kappa_score,recall_score,precision_score

y_true = [2, 0, 2, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2]
c=confusion_matrix(y_true, y_pred)

print('Confuse Matrix = \n%s\n' % c)

n = len(y_true)
class_n = c.shape[0]
print(class_n)

npv_numerator = np.zeros(class_n) 
print(npv_numerator)

true = c.sum(axis=1)
print(true)



pos_label=1
result = c[1-pos_label, 1-pos_label]
print(result)

pred = c.sum(axis=0)
print(pred)

print(pred[1-pos_label])