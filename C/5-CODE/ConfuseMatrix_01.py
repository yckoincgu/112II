import numpy as np
from sklearn.metrics import confusion_matrix, fbeta_score, classification_report, cohen_kappa_score,recall_score,precision_score

y_true = [2, 0, 2, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2]
c=confusion_matrix(y_true, y_pred)

print('Confuse Matrix = \n%s\n' % c)