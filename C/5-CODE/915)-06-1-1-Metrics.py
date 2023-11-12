import numpy as np
from sklearn.metrics import confusion_matrix, fbeta_score, classification_report, cohen_kappa_score,recall_score,precision_score
#from imblearn.metrics import geometric_mean_score


#def NPV(y_true, y_pred, labels=None, pos_label=1, ):
#pos_label 表示 binary classes 要計算哪一個 class為主, 
#          pos_label=1 表示以 class=1 為主, 如果你要計算的是以class=0 則要 pos_label=0
def NPV(y_true, y_pred, pos_label=1, average='weighted'):
    c = confusion_matrix(y_true, y_pred)
    n = len(y_true)
    class_n = c.shape[0]
    
    npv_numerator = np.zeros(class_n) 
    npv_denominator = np.zeros(class_n) 
    npv = np.zeros(class_n) 
    npv_weighted = 0 
    result = 0
    true = c.sum(axis=1)
    pred = c.sum(axis=0)
    if average=='binary':
        if pred[1-pos_label]==0:
            result = 0
        else:   
            result = c[1-pos_label, 1-pos_label]/ pred[1-pos_label]
    else: 
        for i1 in range(class_n):
            npv_numerator[i1] = n - pred[i1] - true[i1] + c[i1,i1]
            npv_denominator[i1] = n - pred[i1]
            if npv_denominator[i1]==0:
               npv[i1] = 0
            else:   
               npv[i1] = npv_numerator[i1]/npv_denominator[i1]
            npv_weighted = npv_weighted + npv[i1]*true[i1]
        if average==None:        
            result = npv
        elif average=='micro':
            result = sum(npv_numerator)/sum(npv_denominator)
        elif average=='macro':    
            result = sum(npv)/class_n
        elif average=='weighted':        
            result = npv_weighted/n 
    
    return result;


#def Specificity(y_true, y_pred, labels=None, pos_label=1, ):
#pos_label 表示 binary classes 要計算哪一個 class為主, 
#          pos_label=1 表示以 class=1 為主, 如果你要計算的是以class=0 則要 pos_label=0
def specificity(y_true, y_pred, pos_label=1, average='weighted'):
    c = confusion_matrix(y_true, y_pred)
    n = len(y_true)
    class_n = c.shape[0]
    
    spec_numerator = np.zeros(class_n) 
    spec_denominator = np.zeros(class_n) 
    spec = np.zeros(class_n) 
    spec_weighted = 0 
    result = 0
    true = c.sum(axis=1)
    pred = c.sum(axis=0)
    if average=='binary':
        if true[1-pos_label]==0:
            result = 0
        else:   
            result = c[1-pos_label, 1-pos_label]/ true[1-pos_label]
    else:
        for i1 in range(class_n):
            spec_numerator[i1] = n - pred[i1] - true[i1] + c[i1,i1]
            spec_denominator[i1] = n - true[i1]
            if spec_denominator[i1]==0:
               spec[i1] = 0
            else:   
               spec[i1] = spec_numerator[i1]/spec_denominator[i1]
            spec_weighted = spec_weighted + spec[i1]*true[i1]
        if average==None:        
            result = spec
        elif average=='micro':
            result = sum(spec_numerator)/sum(spec_denominator)
        elif average=='macro':    
            result = sum(spec)/class_n
        elif average=='weighted':        
            result = spec_weighted/n 
    
    return result;


#y_true = [0,0,1,1,1,2,2,2]
#y_pred = [0,0,0,2,1,1,1,2]


y_true = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
          0,0,0,0,0,0,0,0,0,0,
          1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
          1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
          1,1,1,1,1,1,1,1,1,1,
          2,2,2,2,2,2,2,2,2,2]
y_pred = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
          1,1,1,1,1,2,2,2,2,2,
          1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
          1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
          0,2,2,2,2,2,2,2,2,2,
          1,1,1,1,1,1,1,1,1,2]


target_names=['Class 0', 'Class 1', 'Class 2']
betaVal = 1

confus = confusion_matrix(y_true, y_pred)
print('Confuse Matrix = \n%s\n' % confus)
print('F with beta=%f -> %s\n' % (betaVal,fbeta_score(y_true, y_pred, beta=betaVal, average=None)) )
print('recall =%f -> %s\n' % (betaVal,recall_score(y_true, y_pred, average=None)) )
print('precision_score=%f -> %s\n' % (betaVal,precision_score(y_true, y_pred, average=None)) )
#print('%f'%(recall_score(y_true, y_pred, *, labels=None, pos_label=1, average='binary', sample_weight=None, zero_division='warn')))


print('NPV -> %s\n' % NPV(y_true, y_pred, average=None))
print('NPV Macro=%f Weighted=%f\n' % (NPV(y_true, y_pred, average='macro'), specificity(y_true, y_pred, average='weighted')) )
print('Specificity -> %s\n' % specificity(y_true, y_pred, average=None))
print('Specificity Macro=%f Weighted=%f\n' % (specificity(y_true, y_pred, average='macro'), specificity(y_true, y_pred, average='weighted')) )
#print('geometric_mean_score=%s\n' % geometric_mean_score(y_true, y_pred))
print('cohen_kappa_score=%s\n' % cohen_kappa_score(y_true, y_pred))

print(classification_report(y_true, y_pred, target_names=target_names, digits=5))

