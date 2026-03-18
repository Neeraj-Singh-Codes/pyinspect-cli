# Practical 3 - 1:

def cal_metrics(retrieved_set, relevant_set):
    tp = len(retrieved_set.intersection(relevant_set))
    fp = len(retrieved_set.difference(relevant_set))
    fn = len(relevant_set.difference(retrieved_set))
    print(f"True Positive: {tp}\nFalse Positive: {fp}\nFalse Negative: {fn}")

    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    f_measure = (2*precision * recall) / (precision + recall)

    return precision, recall, f_measure

retrieved_set = set(["doc1","doc2","doc3"])
relevent_set = set(["doc1","doc4"])
p, r, f = cal_metrics(retrieved_set, relevent_set)
print(f"Precision: {p}")
print(f"Recall: {r}")
print(f"F1 Score: {f}")








# Practical 3 - 2:
from sklearn.metrics import average_precision_score

y_true = [0,1,1,0,1,1]
y_scores = [0.1,0.4,0.35,0.8,0.65,0.9]
average_precision = average_precision_score(y_true, y_scores)
print(f"Average Precision-Recall Score: {average_precision}")