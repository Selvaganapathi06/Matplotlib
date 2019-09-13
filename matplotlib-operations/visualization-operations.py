#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Data Visualization in python
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
x =[1,2,3,4,5,6]
y =[7,8,9,10,11,12]
plt.plot(x,y)
plt.show()


# In[4]:


#Assigning values x,y axis
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
x =[1,2,3,4,5,6]
y =[7,8,9,10,11,12]
plt.title("Textile sales data")
plt.xlabel("Mens Dresses")
plt.ylabel("Womens Dress")
plt.plot(x,y)
plt.show()


# In[5]:


#comparing values x,y,z axis
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
x =[1,2,3,4,5,6]
y =[7,8,9,10,11,12]
z =[13,14,15,16,17,18]
plt.title("Textile sales data")
plt.xlabel("Mens Dresses")
plt.ylabel("Womens Dress")
plt.plot(x,y)
plt.plot(x,z)
plt.legend(['THis is x,y','This is x,z'])
plt.show()


# In[15]:


#treadin files output and perform visualization
#comparing values x,y,z axis
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
sam =pd.read_csv("sample_data.csv")
plt.title("visualization report")
plt.xlabel("persons")
plt.ylabel("scores")
plt.plot(sam.column_a,sam.column_b)
plt.plot(sam.column_a,sam.column_c)


# In[18]:


#treadin files output and perform visualization
#comparing values x,y,z axis
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
sam1 =pd.read_csv("countries.csv")
plt.plot(sam1.country,sam1.year)
plt.plot(sam1.country,sam1.population)

