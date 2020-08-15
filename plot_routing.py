import plotly.graph_objects as go

def plotRouting(coord, color, name, legendgroup, showlegend):
    trace = go.Scattermapbox(lat=coord['lat'],
                             lon=coord['lon'],
                             mode='lines',
                             marker=go.scattermapbox.Marker(size=8,
                                                            color=color,
                                                            opacity=0.5
                                                            ),
                             hoverinfo='skip',
                             name=name,
                             legendgroup=legendgroup,
                             showlegend=showlegend,
                            )
    return trace