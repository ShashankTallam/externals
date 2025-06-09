def p8():
    from sklearn.datasets import load_breast_cancer 
    from sklearn.model_selection import train_test_split 
    from sklearn.tree import DecisionTreeClassifier, plot_tree 
    from sklearn.metrics import accuracy_score 
    import matplotlib.pyplot as plt 
    X, y = load_breast_cancer(return_X_y=True) 
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42) 
    clf = DecisionTreeClassifier(random_state=42).fit(Xtr, ytr) 
    print(f"Accuracy: {accuracy_score(yte, clf.predict(Xte))*100:.2f}%") 
    print("Class:", ["Malignant", "Benign"][clf.predict([Xte[0]])[0]]) 
    plot_tree(clf, filled=True); plt.show()