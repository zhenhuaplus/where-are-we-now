import chart_studio
import chart_studio.plotly as py
import aggregate_results


def push_to_plotly():
    fig = aggregate_results.obtain_results()

    username = 'jamesjplus'  # your username
    api_key = '5mb9BzjI0ffrT6kaCotT'  # your api key - go to profile > settings > regenerate key
    chart_studio.tools.set_credentials_file(username=username, api_key=api_key)

    py.plot(fig, filename='2020summer', auto_open=False)

    print('Successfully pushed to Plotly')

if __name__ == '__main__':

    push_to_plotly()

