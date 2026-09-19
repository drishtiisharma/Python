from scipy import stats
from scipy.stats import norm
from scipy import optimize
from scipy import integrate
from scipy import special
import numpy as np 

print("\nProbability\n")
data = np.array([10,26,58,20,55])
print("mean:",stats.tmean(data))
print("variance:",stats.tvar(data))
print("standard deviation:",stats.tstd(data))
print("standard error of mean:",stats.sem(data))

print("\nStatistics\n")

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])
res = stats.pearsonr(x,y)
print("Correlation:", res.statistic)
print("p-value:", res.pvalue)

data = np.array([28, 30, 32, 29, 31, 30, 33])
result = stats.ttest_1samp(data, 30)
print("t-statistic:", result.statistic)
print("p-value (t-test):", result.pvalue)

print("pdf:",stats.norm.pdf(0))
print("cdf:",stats.norm.cdf(1.95))

samples = stats.norm.rvs(
    loc = 50, # mean
    scale = 10, # standard deviation
    size = 5 # number of samples
)
print("samples: ",samples)

print("\nOptimization\n")

def f(x):
    return (x-3)**2
res2 = optimize.minimize_scalar(f)
print("min x:",res2.x)
print("min value at x:",res2.fun)

print("\nIntegral\n")

def f(x):
    return x**2

res3,err = integrate.quad(f,0,2)
print("integral:",res3)
print("error estimate:",err)


print("\nSpecial\n")

print("5 choose 2:",special.comb(5,2))
print("5!:",special.factorial(5))

