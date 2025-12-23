#faceting(compare group side by side)
import plotly.express as px
df = px.data.tips()

fig = px.scatter(df, x="total_bill", y="tip", color="sex", facet_col="day",      # columns for each day
                  title="Tip vs Total Bill per Day")            #facet_col-horizontal layout, facet_row--verticle_layout
fig.show()


#scatter matrix
df = px.data.iris()
fig = px.scatter_matrix( df, dimensions=["sepal_length", "sepal_width", "petal_length", "petal_width"], color="species", title="Iris Pair Relationships")
fig.show()

#3D scatter plot
fig = px.scatter_3d( df, x='sepal_length', y='sepal_width', z='petal_length', color='species', title='Iris 3D Plot')
fig.show()


#map plot
#scatter mapbox(map with points)
df = px.data.carshare()
fig = px.scatter_mapbox( df, lat="centroid_lat", lon="centroid_lon", size="car_hours", color="peak_hour", zoom=10, mapbox_style="carto-positron", title="Car Share Locations")
fig.show()

#Choropleth (Map by region values)
gap = px.data.gapminder().query("year==2007")
fig = px.choropleth( gap, locations="iso_alpha", color="gdpPercap", hover_name="country", color_continuous_scale="Viridis", title="GDP per Capita (2007)")
fig.show()




#part-4
#line
df = px.data.gapminder().query("country == 'Bangladesh'")
fig = px.line( df, x="year", y="gdpPercap", title="GDP per Capita of Bangladesh (1952–2007)")
fig.show()

#multiple line
df = px.data.gapminder().query("year >= 1990 and continent == 'Asia'")
fig = px.line( df, x="year", y="gdpPercap", color="country", title="GDP per Capita in Asia (1990+)")
fig.show()

#box plot
df = px.data.tips()
fig = px.box( df, x="day", y="total_bill", color="day", title="Total Bill Distribution per Day")
fig.show()

#violine
fig = px.violin( df, x="day", y="total_bill", color="sex", box=True, points="all", title="Distribution of Total Bills (Violin + Box)")
fig.show()

#histogram and density
fig = px.histogram( df, x="total_bill", nbins=20, color="sex", title="Histogram of Total Bills")
fig.show()

fig = px.density_contour(df, x="total_bill", y="tip", title="Bill vs Tip Density")
fig.show()


#use in stock market
import plotly.graph_objects as go
import pandas as pd
df = pd.DataFrame({
    "Date": pd.date_range("2024-01-01", periods=10, freq="D"),
    "Open": [100,102,104,106,105,108,110,107,111,115],
    "High": [102,105,107,108,107,111,112,110,113,117],
    "Low":  [99,100,103,104,102,106,108,105,109,113],
    "Close":[101,104,106,107,106,109,111,108,112,116]
})

fig = go.Figure( data=[go.Candlestick(x=df["Date"], open=df["Open"], high=df["High"],  low=df["Low"],  close=df["Close"] )])
fig.update_layout(title="Stock Price Candlestick Chart")
fig.show()



