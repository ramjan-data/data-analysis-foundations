import plotly.express as px
# print(px.data.__all__)

df = px.data.iris()

#scatter graph
fig = px.scatter(df,x="sepal_width", y="sepal_length", color="species", title="Iris Sepal Dimensions")

# Common layout tweaks
fig.update_layout(title_font_size=22, xaxis_title="Sepal Width (cm)", yaxis_title="Sepal Length (cm)", legend_title="Species")
fig.show()

#color customization
fig = px.scatter( df, x='sepal_width', y='sepal_length', color='species',color_discrete_sequence=['green','red','blue'])
fig.show()

#color customization for continues data
tips = px.data.tips()
fig = px.scatter( tips, x='total_bill', y='tip', color='size', color_continuous_scale='Viridis')
fig.show()

#axes and background
fig.update_layout( plot_bgcolor='white',        # inside chart 
    paper_bgcolor='white',       # outside background  
    font=dict(size=14),  width=700,
    height=450)

fig.update_xaxes(title_text='nothing', showgrid=True, gridcolor='lightgrey')
fig.update_yaxes(showgrid=True, gridcolor='lightgrey')
fig.show()


#adding simple annonation
fig.add_annotation( text="Max point", x=4.4, y=7.8, showarrow=True, arrowhead=2)
fig.show()


#subplots for comparison
from plotly.subplots import make_subplots
import plotly.graph_objects as go

fig = make_subplots(rows=1, cols=2, subplot_titles=("Sepal", "Petal"))

fig.add_trace(go.Scatter(x=df["sepal_width"], y=df["sepal_length"], mode='markers', name='Sepal'),  row=1, col=1)
fig.add_trace(go.Scatter(x=df["petal_width"], y=df["petal_length"], mode='markers', name='Petal'),row=1, col=2)

fig.update_layout(title_text="Sepal vs Petal Comparison")
fig.show()


