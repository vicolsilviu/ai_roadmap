# import plotly.graph_objects as go

# # Data
# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 11]

# # Create plot
# fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines+markers'))

# # Add title and labels
# fig.update_layout(title='Simple Plot',
#                   xaxis_title='X-axis Label',
#                   yaxis_title='Y-axis Label')

# # Show plot
# fig.show()

# import plotly.graph_objects as go

# # Data
# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 11]

# # Create plot with customizations
# fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines+markers',
#                                 line=dict(color='green', dash='dash'),
#                                 marker=dict(color='blue', size=10)))

# # Add title and labels
# fig.update_layout(title='Customized Plot',
#                   xaxis_title='X-axis Label',
#                   yaxis_title='Y-axis Label')

# # Show plot
# fig.show()

# import plotly.graph_objects as go

# # Create a new figure
# fig = go.Figure()

# # Add a trace to the figure
# fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6]))

# # Show plot
# fig.show()

# import plotly.subplots as sp

# # Create subplots
# fig = sp.make_subplots(rows=2, cols=2)

# # Add traces to each subplot
# fig.add_trace(go.Scatter(x=[1, 2, 3], y=[1, 4, 9]), row=1, col=1)
# fig.add_trace(go.Scatter(x=[1, 2, 3], y=[1, 2, 3]), row=1, col=2)
# fig.add_trace(go.Scatter(x=[1, 2, 3], y=[1, 0, 1]), row=2, col=1)
# fig.add_trace(go.Scatter(x=[1, 2, 3], y=[3, 2, 1]), row=2, col=2)

# # Show plot
# fig.show()

# import plotly.graph_objects as go

# # Create figure with custom size
# fig = go.Figure()

# # Add trace
# fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6]))

# # Update layout
# fig.update_layout(width=800, height=600)

# # Show plot
# fig.show()

# import plotly.graph_objects as go

# # Data
# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 11]

# # Create line plot
# fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines'))

# # Show plot
# fig.show()

# import plotly.express as px

# # Data
# df = px.data.iris()

# # Create scatter plot
# fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species')

# # Show plot
# fig.show()

# import plotly.express as px

# # Data
# df = px.data.tips()

# # Create bar plot
# fig = px.bar(df, x='day', y='total_bill', color='sex', barmode='group')

# # Show plot
# fig.show()

# import plotly.express as px

# # Data
# df = px.data.tips()

# # Create histogram
# fig = px.histogram(df, x='total_bill')

# # Show plot
# fig.show()

# import plotly.graph_objects as go
# import numpy as np

# # Data
# z = np.random.random((10, 10))

# # Create heatmap
# fig = go.Figure(data=go.Heatmap(z=z))

# # Show plot
# fig.show()


# import plotly.express as px

# # Data
# df = px.data.tips()

# # Create box plot
# fig = px.box(df, x='day', y='total_bill', color='smoker')

# # Show plot
# fig.show()

# import plotly.graph_objects as go

# # Data
# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 11]

# # Create plot
# fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines+markers'))

# # Annotate a point
# fig.add_annotation(x=5, y=11,
#                    text='Peak',
#                    showarrow=True,
#                    arrowhead=1)

# # Show plot
# fig.show()

# import plotly.graph_objects as go

# # Data
# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 11]

# # Create plot
# fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines+markers'))

# # Customize ticks
# fig.update_layout(xaxis=dict(tickmode='array', tickvals=[1, 2, 3, 4, 5], ticktext=['one', 'two', 'three', 'four', 'five']),
#                   yaxis=dict(tickmode='array', tickvals=[2, 3, 5, 7, 11], ticktext=['two', 'three', 'five', 'seven', 'eleven']))

# # Show plot
# fig.show()

# import plotly.graph_objects as go

# # Data
# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 11]

# # Create plot
# fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines+markers'))

# # Add grid
# fig.update_layout(xaxis_showgrid=True, yaxis_showgrid=True)

# # Show plot
# # fig.show()
# import plotly.graph_objects as go

# # Data
# x = [1, 10, 100, 1000, 10000]
# y = [2, 20, 200, 2000, 20000]

# # Create plot
# fig = go.Figure(data=go.Scatter(x=x, y=y, mode='lines+markers'))

# # Set logarithmic scale
# fig.update_layout(xaxis_type='log', yaxis_type='log')

# # Show plot
# fig.show()

# import plotly.subplots as sp
# import plotly.graph_objects as go

# # Create subplots with shared x-axis
# fig = sp.make_subplots(rows=2, cols=1, shared_xaxes=True)

# import plotly.subplots as sp
# import plotly.graph_objects as go

# # Create subplots with shared x-axis
# fig = sp.make_subplots(rows=2, cols=1, shared_xaxes=True)

# # Add traces to the subplots
# fig.add_trace(go.Scatter(x=[1, 2, 3], y=[1, 4, 9]), row=1, col=1)
# fig.add_trace(go.Scatter(x=[1, 2, 3], y=[2, 3, 4]), row=2, col=1)

# # Update layout
# fig.update_layout(title='Subplots with Shared X-Axis')

# # Show plot
# fig.show()

# import plotly.graph_objects as go

# # Data
# x = [1, 2, 3, 4, 5]
# y = [2, 3, 5, 7, 11]
# z = [5, 6, 2, 3, 13]

# # Create 3D scatter plot
# fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers')])

# # Update layout
# fig.update_layout(title='3D Scatter Plot')

# # Show plot
# fig.show()

# import plotly.express as px

# # Data
# df = px.data.gapminder()

# # Create animated scatter plot
# fig = px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
#                  size="pop", color="continent", hover_name="country",
#                  log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])

# # Show plot
# fig.show()

# import plotly.express as px

# # Data
# df = px.data.gapminder().query("year == 2007")

# # Create map plot
# fig = px.scatter_geo(df, locations="iso_alpha", color="continent",
#                      hover_name="country", size="pop",
#                      projection="natural earth")

# # Show plot
# fig.show()

# import plotly.graph_objects as go

# # Data
# x = [1, 2, 3, 4, 5]
# y1 = [2, 3, 5, 7, 11]
# y2 = [1, 2, 4, 8, 16]

# # Create plot
# fig = go.Figure()

# # Add traces
# fig.add_trace(go.Scatter(x=x, y=y1, mode='lines', name='Linear'))
# fig.add_trace(go.Scatter(x=x, y=y2, mode='lines', name='Exponential'))

# # Add buttons
# fig.update_layout(
#     updatemenus=[
#         dict(
#             type="buttons",
#             direction="left",
#             buttons=list([
#                 dict(
#                     args=["type", "scatter"],
#                     label="Scatter",
#                     method="restyle"
#                 ),
#                 dict(
#                     args=["type", "bar"],
#                     label="Bar",
#                     method="restyle"
#                 )
#             ])
#         )
#     ]
# )

# # Show plot
# fig.show()
