import plotly.graph_objects as go
import numpy as np
import plotly.express as px
import pandas as pd

def shade_plot(data,x_col,y_col,mean_col,n_splits,range_color=[0.99,1.01],filter_count=50):
    xs = np.linspace(data[x_col].min(),data[x_col].max(),n_splits)
    ys = np.linspace(data[y_col].min(),data[y_col].max(),n_splits)
    
    mean = {}
    count = {}
    median = {}
    x_dist = xs[1]-xs[0]
    y_dist = ys[1]-ys[0]
    for y in ys:
        mean[y] = []
        median[y] = []
        count[y] = []
        for x in xs:
            if data[(data[x_col] >= x) & \
                (data[x_col] < x+x_dist) & \
                (data[y_col] >= y) & \
                (data[y_col] < y+y_dist)][mean_col].count() > filter_count:
                
                mean[y].append(data[(data[x_col] >= x) & \
                                        (data[x_col] < x+x_dist) & \
                                        (data[y_col] >= y) & \
                                        (data[y_col] < y+y_dist)][mean_col].mean())
                
                median[y].append(data[(data[x_col] >= x) & \
                                        (data[x_col] < x+x_dist) & \
                                        (data[y_col] >= y) & \
                                        (data[y_col] < y+y_dist)][mean_col].mean())
                
            else:
                mean[y].append(1)
                median[y].append(1)
                
            count[y].append(data[(data[x_col] >= x) & \
                                    (data[x_col] < x+x_dist) & \
                                    (data[y_col] >= y) & \
                                    (data[y_col] < y+y_dist)][mean_col].count())
    
    
    fig = px.imshow(pd.DataFrame(mean,index=xs).swapaxes("index", "columns"),
                      color_continuous_scale='RdBu',
                      range_color=range_color,
                      color_continuous_midpoint=1,
                      template="plotly_dark",
                      title='Means')
    
    fig1 = px.imshow(pd.DataFrame(median,index=xs).swapaxes("index", "columns"),
                      color_continuous_scale='RdBu',
                      range_color=range_color,
                      color_continuous_midpoint=1,
                      template="plotly_dark",
                      title='Medians')
    
    fig2 = px.imshow(pd.DataFrame(count,index=xs).swapaxes("index", "columns"),template="plotly_dark",title='Count')
    
    fig.show()
    fig1.show()
    fig2.show()
    