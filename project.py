import pandas as pd 
import geopandas as gpd
import plotly.express as px
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go


data = pd.read_csv('cost-of-living_v2.csv')
points = pd.read_csv('points.csv', sep=";")
codes = pd.read_csv('codici.csv', sep=";")
Init = data.merge(points, on=['city','country'], how='left')
df = Init.merge(codes, on='country', how='left')
df['lat'] = df['lat'].str.replace(",", ".")
df['lng'] = df['lng'].str.replace(",", ".")


# tot
# df['sum']= df.iloc[:,2:54].sum(axis=1)
# filt
df['sum']= df['x2'] + df['x8'] + df['x9'] + df['x12'] + df['x11'] + df['x28'] + df['x36'] + df['x33']*30 + df['x43'] + df['x38'] + df['x39'] + df['x44'] + df['x45'] + df['x50'] +df['x34']/12

stip = df.groupby("country")['x54'].mean()
stipj = stip.to_frame().merge(codes, on=['country'], how='left')
#defstip=stipj.where(filter).dropna()

tot = df.groupby("country")['sum'].mean()
totj = tot.to_frame().merge(codes, on=['country'], how='left')
#deftot = totj.where(filter).dropna()

rapp = stipj.merge(totj, on='country', how='left')
def fil(stato, data, col):
    filter=data['country']==stato
    tt = data.where(filter).dropna()
    return tt[col].values[0]

def fil_city(citta, data, col):
    filter=data['city']==citta
    tt = data.where(filter).dropna()
    return tt[col].values[0]



# totj.to_csv("ah.csv");

# fig = go.Figure(data=go.Choropleth(
#     locations = totj['Alpha3'],
#     z = stipj['x54'] - totj['sum']/12,
#     text = totj['country'],
#     colorscale = 'Oranges',
#     autocolorscale=False,
#     reversescale=False,
#     marker_line_color='darkgray',
#     marker_line_width=1,
#     colorbar_tickprefix = '$',
#     colorbar_title = 'Stipendio - Costo vita (USD)',
#     zmax=2000,
#     zmid=500,
#     zmin=1
# ))

# fig.update_layout(
#     title_text='..',
#     geo=dict(
#         showframe=True,
#         showcoastlines=True,
#         projection_type='equirectangular',
#         scope = 'europe',
        
#     ),
#     annotations = [dict(
#         x=0.2,
#         y=0.55,
#         xref='paper',
#         yref='paper',
#         text='',
#         showarrow = False
#     )]
# )
# fig.show();

# stati = ['Italia', 'Francia', 'Svizzera', 'Germany', 'Austria', 'Greece', 'Portugal', 'Spain', 'United Kingdom', 'Hungary', 'Slovenia', 'Croatia', 'Serbia', 'Albania', 'Bulgaria', 'Romania', 'Ukraine', 'Russia', 'Poland', 'Netherlands', 'Sweden']

# fig = go.Figure(data=[
#     go.Bar(name='Stipendio medio', x=stati, y=[fil("Italy", stipj, "x54"), fil("France", stipj, "x54"), fil("Switzerland", stipj, "x54"),  fil("Germany", stipj, "x54"), fil("Austria", stipj, "x54"), fil("Greece", stipj, "x54"), fil("Portugal", stipj, "x54"), fil("Spain", stipj, "x54"), fil("United Kingdom", stipj, "x54"), fil("Hungary", stipj, "x54"), fil("Slovenia", stipj, "x54"), fil("Croatia", stipj, "x54"), fil("Serbia", stipj, "x54"), fil("Albania", stipj, "x54"),fil("Bulgaria", stipj, "x54"),fil("Romania", stipj, "x54"),fil("Ukraine", stipj, "x54"), fil("Russia", stipj, "x54"), fil("Poland", stipj, "x54"), fil("Netherlands", stipj, "x54"), fil("Sweden", stipj, "x54")]),
#     go.Bar(name='Costo della vita', x=stati, y=[fil("Italy", totj, "sum")/12, fil("France", totj, "sum")/12, fil("Switzerland", totj, "sum")/12, fil("Germany", totj, "sum")/12, fil("Austria", totj, "sum")/12, fil("Greece", totj, "sum")/12, fil("Portugal", totj, "sum")/12, fil("Spain", totj, "sum")/12, fil("United Kingdom", totj, "sum")/12,fil("Hungary", totj, "sum")/12,fil("Slovenia", totj, "sum")/12,fil("Croatia", totj, "sum")/12,fil("Serbia", totj, "sum")/12,fil("Albania", totj, "sum")/12,fil("Bulgaria", totj, "sum")/12,fil("Romania", totj, "sum")/12,fil("Ukraine", totj, "sum")/12,fil("Russia", totj, "sum")/12 ,fil("Poland", totj, "sum")/12, fil("Netherlands", totj, "sum")/12, fil("Sweden", totj, "sum")/12 ])
# ])
# Change the bar mode
# fig.update_layout(barmode='group',
#                 );
# fig.update_traces(marker_color="green", selector={"name": "Stipendio medio"});
# fig.update_traces(marker_color="blue", selector={"name": "Costo della vita"});

# fig.show()

# fig = px.scatter(rapp, x="x54", y=rapp['sum']/12, color="country", symbol="country",
#                 labels={
#                         "x54": "Stipendio mensile",
#                         "y": "Costo della vita",
        
#                 })
# fig.show()


cities=['Rome', 'Milan', 'Naples', 'Turin', 'Bologna', 'Palermo', 'Florence', 'Venice', 'Catania', 'Trieste', 'Brescia', 'Cagliari']

fig = go.Figure(data=[
    go.Bar(name='Monolocale', x=cities, y=[fil_city("Rome", df, "x48"),fil_city("Milan", df, "x48"),fil_city("Naples", df, "x48"),fil_city("Turin", df, "x48"),fil_city("Bologna", df, "x48"),fil_city("Palermo", df, "x48"),fil_city("Florence", df, "x48"),fil_city("Venice", df, "x48"),fil_city("Catania", df, "x48"),fil_city("Trieste", df, "x48"),fil_city("Brescia", df, "x48"),fil_city("Cagliari", df, "x48")]),
    go.Bar(name='Trilocale', x=cities, y=[fil_city("Rome", df, "x50"),fil_city("Milan", df, "x50"),fil_city("Naples", df, "x50"),fil_city("Turin", df, "x50"),fil_city("Bologna", df, "x50"),fil_city("Palermo", df, "x50"),fil_city("Florence", df, "x50"),fil_city("Venice", df, "x50"),fil_city("Catania", df, "x50"),fil_city("Trieste", df, "x50"),fil_city("Brescia", df, "x50"),fil_city("Cagliari", df, "x50")])
])
# Change the bar mode
fig.update_layout(barmode='stack')
fig.update_traces(marker_color="orange", selector={"name": "Monolocale"});
fig.update_traces(marker_color="brown", selector={"name": "Trilocale"});
fig.show()




