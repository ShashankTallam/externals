def p6():
    import numpy as np, matplotlib.pyplot as plt 
    def lwr(x, X, y, d):  # 'tau' renamed to 'd' 
        W = np.diag(np.exp(-np.sum((X - x)**2, axis=1) / (2 * d**2)))   
        return x @ np.linalg.pinv(X.T @ W @ X) @ X.T @ W @ y 
    np.random.seed(42) 
    a = np.linspace(0, 2*np.pi, 100)   
    b = np.sin(a) + 0.1*np.random.randn(100)   
    c = np.c_[np.ones(a.shape), a] 
    a_dense = np.linspace(0, 2*np.pi, 200 )   
    c_dense = np.c_[np.ones(a_dense.shape), a_dense]   
    d = 0.5   
    yp = [lwr(x, c, b, d) for x in c_dense] 
    plt.scatter(a, b, c='r', s=10) 
    plt.plot(a_dense, yp, 'b') 
    plt.show()