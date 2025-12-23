import plotly.express as px
df = px.data.tips()

#use of hover
fig = px.scatter( df, x="total_bill", y="tip", color="day", size="size",
    hover_name="time",            # bold name shown first
    hover_data={"sex":True,       # show these fields
                "size":True,
                "tip":":.2f"},    # format tip to 2 decimal places
    title="Bill vs Tip with Clean Hover"
)
fig.show()

#animation
import plotly.express as px
gap = px.data.gapminder().query("continent == 'Asia'")

fig = px.scatter( gap, x="gdpPercap", y="lifeExp", size="pop", color="country", animation_frame="year",    # creates slider + play button
    animation_group="country", log_x=True, size_max=60, title="GDP vs Life Expectancy (Asia) — Animation")
fig.show()



#dropdowns & button--let the user change views
#create a dataframe
df=px.data.gapminder().query("country == ['Bangladesh', 'Pakistan', 'India']")
print(df.head())

#create the base figure
fig=px.line(df, x='year', y='gdpPercap', color='country', title=" YEAR vs POPULATION LINE GRAPH")


#add dropdown
fig.update_layout(
    updatemenus=[
        dict(
            buttons=list([
                dict(label="All",
                     method="update",
                     args=[{"visible": [True, True, True]},
                           {"title": "All Countries"}]),
                dict(label="India",
                     method="update",
                     args=[{"visible": [True, False, False]},
                           {"title": "India"}]),
                dict(label="China",
                     method="update",
                     args=[{"visible": [False, True, False]},
                           {"title": "China"}]),
                dict(label="United States",
                     method="update",
                     args=[{"visible": [False, False, True]},
                           {"title": "United States"}]),
            ]),
            direction="down",
            showactive=True,
        )
    ]
)
fig.show()





