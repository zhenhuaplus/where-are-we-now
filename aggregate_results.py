import plotly.graph_objects as go
from add_stop import addStop
from obtain_routing import obtainRouting
from plot_routing import plotRouting

def obtain_results():

    token = 'pk.eyJ1Ijoiemhlbmh1YSIsImEiOiJjazJjZnU2d2UwZHp6M2RvMmhhOGN6cG43In0.9F-J0PB0VUlBLxLE-TE_Tw'

    # Original map, update legend
    fig = go.Figure()

    fig.update_layout(hovermode='closest',
                      mapbox_style='light',
                      mapbox_accesstoken=token,
                      mapbox_zoom=3.8,
                      mapbox=dict(center=go.layout.mapbox.Center(lat=41, lon=-115.199310),
                                  bearing=0))

    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0},
                      legend_orientation="v",
                      legend=dict(
                          x=-0.25,
                          y=0.5,
                          traceorder="normal",
                          font=dict(
                              size=16,
                              color="#003152"
                          ),
                          borderwidth=0
                      )
                      )

    # June 15
    bay = [37.427427, -122.199310]
    fig.add_trace(addStop(bay, color="#003152",
                          opacity=0.7,
                          name='Stops',
                          legendgroup='Stops',
                          showlegend=True,
                          text='June 15'))
    fig.add_trace(addStop(bay, color="#003152",
                          opacity=0,
                          name='Bay Area',
                          legendgroup='Stops',
                          showlegend=False,
                          text='June 15'))

    # June 16
    davis = [38.546340, -121.726533]
    fig.add_trace(plotRouting(obtainRouting(bay, [45.397647, -122.270569]),
                              color='#D5B5A4',
                              name='Aborted',
                              legendgroup="Aborted",
                              showlegend=True))
    fig.add_trace(plotRouting(obtainRouting(bay, [32.759912, -117.206380]),
                              color='#D5B5A4',
                              name='Aborted',
                              legendgroup="Aborted",
                              showlegend=False))
    fig.add_trace(plotRouting(obtainRouting(bay, davis),
                              color='#db4d6d',
                              name='Adopted',
                              legendgroup='Routes',
                              showlegend=True))
    fig.add_trace(addStop(davis, color="#003152",
                          opacity=0.7,
                          name='Davis, CA',
                          legendgroup='Stops',
                          showlegend=False,
                          text='June 16'))

    # June 17-26
    utah = [40.679018, -112.26300]
    fig.add_trace(plotRouting(obtainRouting(utah, [39.332114, -106.987696]),
                              color='#D5B5A4',
                              name='Aborted',
                              legendgroup='Aborted',
                              showlegend=False))
    fig.add_trace(plotRouting(obtainRouting(utah, [37.073156, -113.583815]),
                              color='#D5B5A4',
                              name='Aborted',
                              legendgroup='Aborted',
                              showlegend=False))
    fig.add_trace(plotRouting(obtainRouting(utah, [42.563728, -114.479309]),
                              color='#D5B5A4',
                              name='Aborted',
                              legendgroup='Aborted',
                              showlegend=False))
    fig.add_trace(plotRouting(obtainRouting(davis, utah),
                              color='#db4d6d',
                              name='June 16',
                              legendgroup='Routes',
                              showlegend=False))
    fig.add_trace(addStop(utah, color="#003152",
                          opacity=0.7,
                          name='Lake Point, UT',
                          legendgroup='Stops',
                          showlegend=False,
                          text='June 17-26'))

    # June 27-28
    parkCity = [40.699425, -111.566409]
    fig.add_trace(plotRouting(obtainRouting(utah, parkCity),
                              color='#003152',
                              name='With Martin',
                              legendgroup='w/Martin',
                              showlegend=True))
    fig.add_trace(addStop(parkCity, color="#003152",
                          opacity=0.7,
                          name='Park City, UT',
                          legendgroup='Stops',
                          showlegend=False,
                          text='June 27-28'))

    # June 29-30
    yellowstone = [44.532704, -110.435011]
    fig.add_trace(plotRouting(obtainRouting(parkCity, yellowstone),
                              color='#003152',
                              name='June 29',
                              legendgroup='w/Martin',
                              showlegend=False))
    fig.add_trace(addStop(yellowstone, color="#003152",
                          opacity=0.7,
                          name='Yellowstone National Park, WY',
                          legendgroup='Stops',
                          showlegend=False,
                          text='June 29-30'))

    # July 1
    grandteton = [43.753074, -110.719810]
    slc = [40.776485, -111.981147]
    fig.add_trace(plotRouting(obtainRouting(yellowstone, grandteton),
                              color='#D5B5A4',
                              name='Aborted',
                              legendgroup='Aborted',
                              showlegend=False))
    fig.add_trace(plotRouting(obtainRouting(grandteton, slc),
                              color='#D5B5A4',
                              name='Aborted',
                              legendgroup='Aborted',
                              showlegend=False))
    glacier = [48.385916, -114.072221]
    glacier_2 = [48.768817, -114.283210]
    fig.add_trace(plotRouting(obtainRouting(yellowstone, glacier),
                              color='#003152',
                              name='July 1',
                              legendgroup='w/Martin',
                              showlegend=False))
    fig.add_trace(plotRouting(obtainRouting(glacier, glacier_2),
                              color='#003152',
                              name='July 1',
                              legendgroup='w/Martin',
                              showlegend=False))
    fig.add_trace(addStop(glacier, color="#003152",
                          opacity=0.7,
                          name='Glacier National Park, MT',
                          legendgroup='Stops',
                          showlegend=False,
                          text='July 1'))

    # July 2
    greatfalls = [47.501290, -111.299398]
    fig.add_trace(plotRouting(obtainRouting(glacier, greatfalls),
                              color='#D5B5A4',
                              name='Aborted',
                              legendgroup='Aborted',
                              showlegend=False))
    kellog = [47.540682, -116.124862]
    fig.add_trace(plotRouting(obtainRouting(glacier, kellog),
                              color='#003152',
                              name='July 2',
                              legendgroup='w/Martin',
                              showlegend=False))
    fig.add_trace(addStop(kellog, color="#003152",
                          opacity=0.7,
                          name='Kellog, ID',
                          legendgroup='Stops',
                          showlegend=False,
                          text='July 2'))

    # July 3-5
    missoula = [46.864275, -113.996716]
    idahofalls = [43.496427, -112.053929]
    fig.add_trace(plotRouting(obtainRouting(idahofalls, missoula),
                              color='#D5B5A4',
                              name='Aborted',
                              legendgroup='Aborted',
                              showlegend=False))

    seattle_1 = [47.665097, -122.313306]
    seattle_2 = [47.495807, -122.313594]
    glass = [48.142749, -122.785049]
    fig.add_trace(plotRouting(obtainRouting(kellog, seattle_1),
                              color='#003152',
                              name='July 3',
                              legendgroup='w/Martin',
                              showlegend=False))
    fig.add_trace(plotRouting(obtainRouting(seattle_1, seattle_2),
                              color='#003152',
                              name='July 4',
                              legendgroup='w/Martin',
                              showlegend=False))
    fig.add_trace(plotRouting(obtainRouting(seattle_2, glass),
                              color='#003152',
                              name='July 5',
                              legendgroup='w/Martin',
                              showlegend=False))
    fig.add_trace(addStop(seattle_1, color="#003152",
                          opacity=0.7,
                          name='Seattle, WA',
                          legendgroup='Stops',
                          showlegend=False,
                          text='July 3'))
    fig.add_trace(addStop(seattle_2, color="#003152",
                          opacity=0.7,
                          name='Sea-Tac, WA',
                          legendgroup='Stops',
                          showlegend=False,
                          text='July 4-5'))

    # July 6-12
    albany = [44.616812, -123.097559]
    fig.add_trace(plotRouting(obtainRouting(seattle_2, albany),
                              color='#db4d6d',
                              name='June 6',
                              legendgroup='Routes',
                              showlegend=False))
    fig.add_trace(addStop(albany, color="#003152",
                          opacity=0.7,
                          name='Albany, OR',
                          legendgroup='Stops',
                          showlegend=False,
                          text='July 6-12'))

    # July 13-14
    crater = [42.871264, -122.169099]
    fig.add_trace(plotRouting(obtainRouting(albany, crater),
                              color='#db4d6d',
                              name='June 13',
                              legendgroup='Routes',
                              showlegend=False))
    fig.add_trace(addStop(crater, color="#003152",
                          opacity=0.7,
                          name='Crater Lake National Park, OR',
                          legendgroup='Stops',
                          showlegend=False,
                          text='July 13-14'))

    # July 15
    pa = [37.452974, -122.158954]
    fig.add_trace(plotRouting(obtainRouting(crater, pa),
                              color='#db4d6d',
                              name='June 13',
                              legendgroup='Routes',
                              showlegend=False))
    fig.add_trace(addStop(pa, color="#003152",
                          opacity=0.7,
                          name='Palo Alto, CA',
                          legendgroup='Stops',
                          showlegend=False,
                          text='Returned!'))

    return fig