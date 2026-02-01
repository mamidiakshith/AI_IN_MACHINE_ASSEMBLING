from sklearn.metrics import precision_score, recall_score, f1_score, roc_auc_score

for fold, (train_index, test_index) in enumerate(kf.split(X)):
    print(f"\n--- Fold {fold+1}/{kf.n_splits} ---")

    # Split data for the current fold
    X_train_fold, X_test_fold = X[train_index], X[test_index]
    y_train_fold, y_test_fold = y.iloc[train_index], y.iloc[test_index]

    # Train KNN model
    knn_fold = KNeighborsClassifier(n_neighbors=5)
    knn_fold.fit(X_train_fold, y_train_fold)

    # Make predictions and get probabilities
    y_pred_fold = knn_fold.predict(X_test_fold)
    y_probs_fold = knn_fold.predict_proba(X_test_fold)[:, 1]

    # Calculate metrics
    fold_accuracy = accuracy_score(y_test_fold, y_pred_fold)
    # For precision, recall, f1-score, we are interested in the minority class (1)
    fold_precision = precision_score(y_test_fold, y_pred_fold, pos_label=1, zero_division=0)
    fold_recall = recall_score(y_test_fold, y_pred_fold, pos_label=1, zero_division=0)
    fold_f1 = f1_score(y_test_fold, y_pred_fold, pos_label=1, zero_division=0)
    fold_auc_roc = roc_auc_score(y_test_fold, y_probs_fold)

    # Calculate Specificity
    cm_fold = confusion_matrix(y_test_fold, y_pred_fold)
    TN_fold, FP_fold, FN_fold, TP_fold = cm_fold.ravel()
    fold_specificity = TN_fold / (TN_fold + FP_fold)

    # Store metrics
    accuracy_scores.append(fold_accuracy)
    precision_scores.append(fold_precision)
    recall_scores.append(fold_recall)
    f1_scores.append(fold_f1)
    auc_roc_scores.append(fold_auc_roc)
    specificity_scores.append(fold_specificity)

    print(f"Accuracy: {fold_accuracy:.4f}")
    print(f"Precision (Class 1): {fold_precision:.4f}")
    print(f"Recall (Class 1): {fold_recall:.4f}")
    print(f"F1-score (Class 1): {fold_f1:.4f}")
    print(f"AUC-ROC: {fold_auc_roc:.4f}")
    print(f"Specificity: {fold_specificity:.4f}")

print("\nCross-validation complete. Metrics for each fold have been calculated and stored.")