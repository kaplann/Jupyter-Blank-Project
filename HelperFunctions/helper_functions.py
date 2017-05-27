import pandas as pd
from openpyxl import load_workbook
import matplotlib.pylab as plt
import matplotlib, pickle
import numpy as np

# For notebook helper Functions
from IPython.display import display, HTML, Markdown

import bokeh
from bokeh.io import output_notebook
from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models import HoverTool
from bokeh.models.widgets import Panel, Tabs

def new_section(content_id, title):
    style = "text-align:center;background:#661111;padding:40px;color:#ffffff;font-size:2.5em;"
    contentTableLink = Markdown('<a id="{}"></a>'.format(content_id))
    chapterHeader = HTML('<div style="{}">{}</div>'.format(style, title))
    back2top = Markdown('[back to top](#top)')
    return display(contentTableLink, chapterHeader, back2top)

#########################################################################################################################
######################################        Reading and Writing        ################################################
#########################################################################################################################



# Add '.pickle' if dot_pickle == False
def read_pickle(path, dot_pickle=False):
    if dot_pickle==False: 
        path = path+'.pickle'
    with open(path, 'rb') as fd: 
        obj = pickle.load(fd)
    return obj

def get_rand_cont_str(files_full_path):
    f_name = get_rand_con_name(files_full_path)
    print(f_name)
    with open(f_name, 'r', encoding='utf-8') as fd: 
        text_cont = fd.read()
    return text_cont

#************************************************************************************************************************
#*************************************        Reading and Writing        ************************************************
#************************************************************************************************************************
