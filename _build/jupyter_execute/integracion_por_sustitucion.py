#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import display, Latex, Math, HTML, IFrame
from IPython.display import Markdown as md
from sympy import *


# # Integracion por sustitución
# 
# ## Regla de la sustitución o cambio de variable
# 
# Existen integrales que no pueden ser resueltas mediante integración directa:
# 
# $$\int{2x\sqrt{1+x^2}}dx$$
# 
# En casos como los anteriores lo que se realiza es un cambio de variable para transformar la expresión original en una expresión que pueda ser resuelta empleando el método de integración directa.
# 
# ## Método de sustitución o cambio de variable
# 
# ```{note}
# **Teorema - Regla de la sustitución**
# 
# Si $u=g(x)$ es una función derivable cuyo rango es un intervalo $I$ y $f$ es continua sobre $I$, entonces:
# 
# $$\int{f(g(x))g'(x)}dx = \int{f(u)}du$$
# ```
# 
# ### Estrategia de solución empleando el método de sustitución
# 
# 1. Observe cuidadosamente el integrando y seleccione una expresión dentro del integrando $g(x)$ haciendola igual a $u$. Cuando seleccione $g(x)$ busque que $g'(x)$ sea también parte del integrando.
# 2. Sustituya $u=g(x)$ y $du=g'(x)dx$ de tal manera que la integral quede en términos de $u$.
# 3. Una vez hecho lo anterior, proceda a evaluar la integral con respecto a $u$. Si la integral no puede ser evaluada es necesario devolverse y seleccionar una expresión diferente para $u$.
# 4. Evalué la integral en términos de $u$.
# 5. Recupere la variable de modo que escriba el resultado en términos de $x$ (variable original).
# 
# #### Ejemplos
# 
# ---
# 1. Obtenga la integral indefinida de la siguiente expresión: $\int{6x(3x^2+4)^4}dx$
# ---
# **Solución**: Se elige como sustitución $u=3x^2+4$ de modo que $du=6xdx$

# In[64]:


# Integración respecto a u
x = symbols('x')
u = symbols('u')
fu = u**4
r = integrate(fu,u)
display(r)


# Luego, retornando a la variable original se tiene que:

# In[65]:


# Recuperación de la variable original
display(r.subs(u,3*x**2 + 4))


# **Solución**:
# 
# $$\int{6x(3x^2+4)^4}dx = \frac{(3x^2+5)^5}{5} + C$$

# ---
# 2. Obtenga la integral indefinida de la siguiente expresión: $\int{\sqrt{2x+1}}dx$
# ---
# **Solución**: Se elige como sustitución $u=2x+1$ de modo que $du=2dx$

# In[105]:


x = symbols('x')
u = symbols('u')
fu = Rational(1,2)*sqrt(u)
ru = integrate(fu,u)
display(ru)


# Luego, retornando a la variable original se tiene que:

# In[106]:


# Recuperación de la variable original
display(ru.subs(u,2*x+1))


# **Solución**:
# 
# $$\int{\sqrt{2x+1}}dx = \frac{1}{3}(2x+1)^{3/2} + C$$
# 
# ---
# 3. Obtenga la integral indefinida de la siguiente expresión:  $\int{\frac{x}{1-4x^2}}dx$
# ---
# 
# **Solución**: Se elige como sustitución $u=1-4x^2$ de modo que $du=-8xdx$
# 

# In[74]:


x = symbols('x')
u = symbols('u')
fu = -Rational(1,8)/sqrt(u)
ru = integrate(fu,u)
display(ru)


# Luego, retornando a la variable original se tiene que:

# In[75]:


# Recuperación de la variable original
display(ru.subs(u,1-4*x**2))


# 
# **Solución**:
# 
# $$\int{\frac{x}{1-4x^2}}dx = -\frac{1}{4}\sqrt{1-4x^2} + C$$

# ---
# 4. Obtenga la integral indefinida de la siguiente expresión:  $\int{e^{5x}}dx$
# ---
# 
# **Solución**: Se elige como sustitución $u=5x$ de modo que $du=5dx$

# In[76]:


x = symbols('x')
u = symbols('u')
fu = Rational(1,5)*exp(u)
ru = integrate(fu,u)
display(ru)


# Luego, retornando a la variable original se tiene que:

# In[77]:


# Recuperación de la variable original
display(ru.subs(u,5*x))


# **Solución**:
# 
# $$\int{e^{5x}}dx = \frac{1}{5}e^{5x} + C$$
# 
# ---
# 5. Obtenga la integral indefinida de la siguiente expresión:  $\int{\frac{\sin{t}}{\cos^3{t}}}dt$
# ---
# 
# **Solución**: Se elige como sustitución $u=\cos{t}$ de modo que $du=-\sin{t}dt$

# In[78]:


t = symbols('t')
u = symbols('u')
fu = -1/u**3
ru = integrate(fu,u)
display(ru)


# Luego, retornando a la variable original se tiene que:

# In[79]:


# Recuperación de la variable original
display(ru.subs(u,cos(t)))


# **Solución**:
# 
# $$\int{\frac{\sin{t}}{\cos^3{t}}}dt = \frac{1}{2\cos^2{t}} + C$$
# 
# ---
# 6. Obtenga la integral indefinida de la siguiente expresión:  $\int{\sqrt{1+x^2}x^5}dx$
# ---
# 
# **Solución**: Se elige como sustitución $u=1+x^2$ de modo que $du=2xdx$

# In[ ]:


x = symbols('x')
u = symbols('u')
fu = Rational(1,2)*sqrt(u)*(u-1)**2
ru = integrate(fu,u)
ru = simplify(ru).expand()
display(ru)


# Luego, retornando a la variable original se tiene que:

# In[ ]:


# Recuperación de la variable original
display(ru.subs(u,1+x**2))


# **Solución**:
# 
# $$\int{\sqrt{1+x^2}x^5}dx = \frac{1}{7}(1+x^2)^{7/2} -\frac{2}{5}(1+x^2)^{5/2} + \frac{1}{3}(1+x^2)^{3/2} + C$$
# 
# ---
# 7. Obtenga la integral indefinida de la siguiente expresión:  $\int{\tan{x}}dx$
# ---
# 
# **Solución**: Teniendo en cuenta que $\tan{x} = \frac{\sin{x}}{\cos{x}}$
# 
# Se elige como sustitución $u = \cos{x}$ de modo que $du = -\sin{x}dx$

# In[ ]:


x = symbols('x')
u = symbols('u')
fu = -1/u
ru = integrate(fu,u)
display(ru)


# Luego, retornando a la variable original se tiene que:

# In[ ]:


# Recuperación de la variable original
display(ru.subs(u,cos(x)))


# **Solución**:
# 
# $$\int{\tan{x}}dx = -\ln{|\cos{x}|} + C = \ln{|\sec{x}|} + C $$
# 
# ---
# 8. Obtenga la integral indefinida de la siguiente expresión:  $\int{x^2\sqrt{2x+1}}dx$
# ---
# 
# **Solución**: Se elige como sustitución $u = 2x + 1$ de modo que $du = 2dx$

# In[99]:


x = symbols('x')
u = symbols('u')
fu = (((1-u)/2)**2)*(sqrt(u))/2
ru = simplify(integrate(fu,u)).expand()
display(ru)


# Luego, retornando a la variable original se tiene que:

# In[101]:


# Recuperación de la variable original
display(ru.subs(u,2*x+1))


# **Solución**:
# 
# $$\int{x^2\sqrt{2x+1}}dx = \frac{(2x+1)^{7/2}}{28} - \frac{(2x+1)^{5/2}}{10} + \frac{(2x+1)^{3/2}}{12} + C $$
# 
# 
# ---
# 9. Obtenga la integral indefinida de la siguiente expresión:  $\int{\frac{{(\tan^{-1}{x})}^2}{1+x^2}}dx$
# ---
# 
# **Solución**: Se elige como sustitución $u = \tan^{-1}{x}$ de modo que $du = \frac{1}{1+x^2}dx$

# In[102]:


x = symbols('x')
u = symbols('u')
fu = u**2
ru = integrate(fu,u)
display(ru)


# Luego, retornando a la variable original se tiene que:

# In[107]:


# Recuperación de la variable original
display(ru.subs(u,atan(x)))


# **Solución**: $\int{\frac{{(\tan^{-1}{x})}^2}{1+x^2}}dx = \frac{1}{3}(\tan^{-1}{x})^3 + C $
# 
# ## Enlaces
# * https://www.yu.edu/sites/default/files/inline-files/Lec14_sympy.pdf
# * https://scipy-lectures.org/packages/sympy.html
# * https://dynamics-and-control.readthedocs.io/en/latest/0_Getting_Started/Notebook%20introduction.html
# * https://vknight.org/pfm/tools-for-mathematics/03-calculus/how/main.html
# * http://prob140.org/sp17/textbook/ch17/Calculus_in_SymPy.html
# * http://prob140.org/textbook/content/README.html
# * https://www.math.purdue.edu/~bradfor3/ProgrammingFundamentals/Sympy/
# * https://scipy-lectures.org/packages/sympy.html
# * https://dynamics-and-control.readthedocs.io/en/latest/0_Getting_Started/Notebook%20introduction.html
# * https://towardsdatascience.com/simplify-calculus-for-machine-learning-with-sympy-8a84e57b30bb
# * https://zetcode.com/python/sympy/
# * https://colab.research.google.com/github/drvinceknight/Python-Mathematics-Handbook/blob/master/01-Symbolic-mathematics-with-Sympy.ipynb
# * https://github.com/drvinceknight/Python-Mathematics-Handbook
