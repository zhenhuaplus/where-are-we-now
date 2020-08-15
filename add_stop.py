import plotly.graph_objects as go

def addStop(stop, color, opacity, text, name, legendgroup, showlegend):
    stop = go.Scattermapbox(lat=[stop[0]],
                            lon=[stop[1]],
                            mode='markers',
                            marker=go.scattermapbox.Marker(size=16,
                                                           color=color,
                                                           opacity=opacity,
                                                          ),
                            hoverinfo='all',
                            name=name,
                            legendgroup=legendgroup,
                            showlegend=showlegend,
                            hovertemplate =
                            '<b>%{lat:.2f}, %{lon:.2f}</b><br><br>' +
                            '<b>%{text}</b>',
                            text = [text],
                           )
    return stop