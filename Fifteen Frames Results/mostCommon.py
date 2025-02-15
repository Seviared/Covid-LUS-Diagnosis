import itertools
import operator
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
def most_common(L):
  # get an iterable of (item, iterable) pairs
    SL = sorted((x, i) for i, x in enumerate(L))
  # print 'SL:', SL
    groups = itertools.groupby(SL, key=operator.itemgetter(0))
  # auxiliary function to get "quality" for an item
    def _auxfun(g):
        item, iterable = g
        count = 0
        min_index = len(L)
        for _, where in iterable:
            count += 1
            min_index = min(min_index, where)
    # print 'item %r, count %r, minind %r' % (item, count, min_index)
        return count, -min_index
  # pick the highest-count/earliest item
    return max(groups, key=_auxfun)[0]

def patient_score(y_test,y_pred):
    patient_pred=[]
    patient_test=[]
    i=0
    #making patient test values
    while i<len(y_test):
        patient_test.append(y_test[i])
        i=i+15
    #making patient predict values
    i=0
    counter=0
    frames=[]
    while i<len(y_pred):
        frames.append(y_pred[i])
        counter=counter+1
        if(counter==15):
            prediction=most_common(frames)
            patient_pred.append(prediction)
            frames=[]
            counter=0
        i=i+1
    print(confusion_matrix(patient_test,patient_pred))
    print(classification_report(patient_test,patient_pred, digits=3))
