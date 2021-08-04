#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas             as pd
import datetime
from   bokeh.plotting     import show, figure, output_file, save
from   bokeh.io           import show, output_notebook, curdoc, export_png
from   bokeh.models       import ColumnDataSource,LinearAxis, Range1d, NumeralTickFormatter, LabelSet, Label, BoxAnnotation, DatetimeTickFormatter
from   bokeh.models.tools import HoverTool


# In[13]:


"|IMPORT DATA|"
path = r'https://github.com/ncachanosky/research/blob/master/Economic%20Series/'
file = r'Resumen%20Estadistico%20-%20Internacional.xlsx?raw=true'
IO   = path + file
sheet = 'DATA'

data = pd.read_excel(IO, sheet_name = sheet, usecols="A:C, S", skiprows=2, nrows=12318, engine='openpyxl') # Be patient...

data = data.dropna()

data = data.rename(columns={"TFP (CONSTANT 2007)":"TFP"})


# In[15]:


"|CHECK DATA|"
data.tail()


# In[20]:


data_arg = data.loc[data["COUNTRY"]=="Argentina",:]


# In[21]:


data_arg


# In[22]:


cds = ColumnDataSource(data_arg)

#BUILD FIGURE
p = figure(title = "EL HUB ECONÓMICO | PRODUCTIVIDAD TOTAL DE LOS FACTORES EN ARGENTINA",
           x_axis_label = "Año", 
           plot_height  = 400,
           plot_width   = 700)

p.toolbar_location = "right"
p.toolbar.autohide = True
p1 = p.line("YEAR", "TFP", color="blue", line_alpha=0.50, width=4, legend_label="TFP"    ,
            muted_alpha=0.20, source=cds)

p.add_tools(HoverTool(renderers=[p1], tooltips = [("TFP"    , "@TFP")], mode="vline"))

p.legend.location     = "top_left"
p.legend.orientation  = "horizontal"
p.legend.click_policy = "mute"
show(p)


# In[ ]:




