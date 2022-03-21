# %% [markdown]
'''
### Quiz
1. 写一个函数，一个球自由落体，输入时间t和时间间隔dt，计算t每间隔dt时间的位移。


2. 写代码生成下面这个些数据，同样颜色的为一个nparray，注意维度和方向：
   ![](..\code\2021-03-26-23-59-29.png)



3. 求下面这个积分  
 $\int_0^1\int_0^1\int_0^1(x^y-z)dxdydz$

### Assignment

4. 在一个 3 维空间内，物质的密度分布为$\rho=x^2y^2z^2$,求一个圆锥体，底面为 xy 平面，圆心在原点，
半径为 1，高为 1 的圆锥体的质量
'''

# %% 
# practice 1
# 1 自由落体
import numpy as np
def freeFall(t, dt):
    time = np.arange(0, t, dt)
    return 0.5*9.8*time**2

res = freeFall(10,1)
res
# %%
# 3 求积分
xn = np.linspace(0, 1, 100)
grid = np.meshgrid(xn, xn, xn)

def f(x,y,z):
    return x**y-z
allPoint = f(*grid)
I = np.average(allPoint)
I
# %%
# practice 2
# 求圆锥体的质量
from scipy import integrate
def f(x,y,z):
    return x**2*y**2*z**2

I = integrate.tplquad(f,-1,1, lambda x: -(1-x**2)**0.5,
                        lambda x:(1-x**2)**0.5,
                        lambda x,y: 0,
                        lambda x,y: 1-(x**2+y**2)**0.5)
I