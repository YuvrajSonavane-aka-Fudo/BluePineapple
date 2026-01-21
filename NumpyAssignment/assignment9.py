import numpy as np

'''
Linear regression from scratch using normal equation for line fitting
'''

import numpy as np

# 1. Generate synthetic data
np.random.seed(42)
X = 2 * np.random.rand(200, 1)        
noise = np.random.randn(200, 1)      
y = 3 * X + 5 + noise                 

# 2. Add bias term (column of ones) to X for intercept calculation
X_b = np.c_[np.ones((200, 1)), X]

# 3. Apply Normal Equation: theta = (X^T * X)^-1 * X^T * y
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

# 4. Print estimated parameters
intercept, slope = theta_best[0][0], theta_best[1][0]
print(f"Estimated Intercept: {intercept}")
print(f"Estimated Slope: {slope}")
