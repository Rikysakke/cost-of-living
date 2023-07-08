import pandas as pd 
import geopandas as gpd
import plotly.express as px
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go

#### LEGGIAMO I CSV ED INIZIALIZIAMO LE VARIABILI

data = pd.read_csv('cost-of-living_v2.csv')
points = pd.read_csv('points.csv', sep=";")
codes = pd.read_csv('codici.csv', sep=";")
Init = data.merge(points, on=['city','country'], how='left')
df = Init.merge(codes, on='country', how='left')
df['lat'] = df['lat'].str.replace(",", ".")
df['lng'] = df['lng'].str.replace(",", ".")
df['sum']= df['x2'] + df['x8'] + df['x9'] + df['x12'] + df['x11'] + df['x28'] + df['x36'] + df['x33']*30 + df['x43'] + df['x38'] + df['x39'] + df['x44'] + df['x45'] + df['x50'] +df['x34']/12
df['cibo']= df['x2'] + df['x8'] + df['x9'] + df['x11'] + df['x12']
df['trasporto']= df['x29'] + df['x33']*30 
df['casa']=df['x50']
stip = df.groupby("country")['x54'].mean()
stipj = stip.to_frame().merge(codes, on=['country'], how='left')
tot = df.groupby("country")['sum'].mean()
totj = tot.to_frame().merge(codes, on=['country'], how='left')
dfitaly=df.where(df['country']=="Italy")
rapp = stipj.merge(totj, on='country', how='left')
bollette = df.groupby("country")['x36'].mean()
bollettej = bollette.to_frame().merge(codes, on=['country'], how='left')
istruzione = df.groupby("country")['x43'].mean()
istruzionej = istruzione.to_frame().merge(codes, on=['country'], how='left')


###### DEFINIAMO LE FUNZIONI PER FILTRARE ALCUNE OPERAZIONI DI RICERCA
def fil(stato, data, col):
    filter=data['country']==stato
    tt = data.where(filter).dropna()
    return tt[col].values[0]

def fil_city(citta, data, col):
    filter=data['city']==citta
    tt = data.where(filter).dropna()
    return tt[col].values[0]





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

########################################################

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

########################################################


# fig = px.scatter(rapp, x="x54", y=rapp['sum']/12, color="country", symbol="country",
#                 labels={
#                         "x54": "Stipendio mensile",
#                         "y": "Costo della vita",
        
#                 })
# fig.show()

########################################################

# cities=['Rome', 'Milan', 'Naples', 'Turin', 'Bologna', 'Palermo', 'Florence', 'Venice', 'Catania', 'Trieste', 'Brescia', 'Cagliari']

# fig = go.Figure(data=[
#     go.Bar(name='Monolocale', x=cities, y=[fil_city("Rome", df, "x48"),fil_city("Milan", df, "x48"),fil_city("Naples", df, "x48"),fil_city("Turin", df, "x48"),fil_city("Bologna", df, "x48"),fil_city("Palermo", df, "x48"),fil_city("Florence", df, "x48"),fil_city("Venice", df, "x48"),fil_city("Catania", df, "x48"),fil_city("Trieste", df, "x48"),fil_city("Brescia", df, "x48"),fil_city("Cagliari", df, "x48")]),
#     go.Bar(name='Trilocale', x=cities, y=[fil_city("Rome", df, "x50"),fil_city("Milan", df, "x50"),fil_city("Naples", df, "x50"),fil_city("Turin", df, "x50"),fil_city("Bologna", df, "x50"),fil_city("Palermo", df, "x50"),fil_city("Florence", df, "x50"),fil_city("Venice", df, "x50"),fil_city("Catania", df, "x50"),fil_city("Trieste", df, "x50"),fil_city("Brescia", df, "x50"),fil_city("Cagliari", df, "x50")])
# ])
# # Change the bar mode
# fig.update_layout(barmode='stack')
# fig.update_traces(marker_color="orange", selector={"name": "Monolocale"});
# fig.update_traces(marker_color="brown", selector={"name": "Trilocale"});
# fig.show()

########################################################

# cities = ['Rome', 'Paris', 'Berna', 'Berlin', 'Vienna', 'Athens', 'Lisbon', 'Madrid', 'London', 'Budapest', 'Ljubljana', 'Zagreb', 'Belgrade', 'Tirana', 'Sofia', 'Bucharest', 'Kiev', 'Moscow', 'Warsaw', 'Amsterdam', 'Stockholm']

# fig = go.Figure(data=[
#     go.Bar(name='Stipendio medio', x=cities,  y=[fil_city("Rome", df, "x54"), fil_city("Paris", df, "x54"), fil_city("Bern", df, "x54"),  fil_city("Berlin", df, "x54"), fil_city("Vienna", df, "x54"), fil_city("Athens", df, "x54"), fil_city("Lisbon", df, "x54"), fil_city("Madrid", df, "x54"), fil_city("London", df, "x54"), fil_city("Budapest", df, "x54"), fil_city("Ljubljana", df, "x54"), fil_city("Zagreb", df, "x54"), fil_city("Belgrade", df, "x54"), fil_city("Tirana", df, "x54"),fil_city("Sofia", df, "x54"),fil_city("Bucharest", df, "x54"),fil_city("Kyiv", df, "x54"), fil_city("Moscow", df, "x54"), fil_city("Warsaw", df, "x54"), fil_city("Amsterdam", df, "x54"), fil_city("Stockholm", df, "x54")]),
#     go.Bar(name='Costo della vita',  x=cities, y=[fil_city("Rome", df, "sum")/12, fil_city("Paris", df, "sum")/12, fil_city("Bern", df, "sum")/12, fil_city("Berlin", df, "sum")/12, fil_city("Vienna", df, "sum")/12, fil_city("Athens", df, "sum")/12, fil_city("Lisbon", df, "sum")/12, fil_city("Madrid", df, "sum")/12, fil_city("London", df, "sum")/12, fil_city("Budapest", df, "sum")/12,fil_city("Ljubljana", df, "sum")/12,fil_city("Zagreb", df, "sum")/12,fil_city("Belgrade", df, "sum")/12,fil_city("Tirana", df, "sum")/12,fil_city("Sofia", df, "sum")/12,fil_city("Bucharest", df, "sum")/12,fil_city("Kyiv", df, "sum")/12,fil_city("Moscow", df, "sum")/12 ,fil_city("Warsaw", df, "sum")/12, fil_city("Amsterdam", df, "sum")/12, fil_city("Stockholm", df, "sum")/12])
# ])

# fig.update_layout(barmode='group',
#                 );
# fig.update_traces(marker_color="green", selector={"name": "Stipendio medio"});
# fig.update_traces(marker_color="blue", selector={"name": "Costo della vita"});

# fig.show()

########################################################

# cities=['Rome', 'Milan', 'Naples', 'Turin', 'Bologna', 'Palermo', 'Florence', 'Venice', 'Catania', 'Trieste', 'Brescia', 'Cagliari']

# filx = df.where((df['city']==cities[0]) | (df['city']==cities[1]) | (df['city']==cities[2]) | (df['city']==cities[3]) | (df['city']==cities[4]) | (df['city']==cities[5]) | (df['city']==cities[6]) | (df['city']==cities[7]) | (df['city']==cities[8]) | (df['city']==cities[9]) | (df['city']==cities[10]) | (df['city']==cities[11]))

# fig = px.scatter(filx, x="x54", y=df['sum']/12, color="city", text="city", symbol=None,
#                 labels={
#                         "x54": "Stipendio mensile",
#                         "y": "Costo della vita",
        
#                 })

# fig.update_traces(textposition='top center')
# fig.show()
# categorie = ['Cibo','Trasporti','Servizi',
#               'Casa'];
# stati = ['Italia', 'Russia', 'United States', 'China', 'Australia', 'United Arab Emirates', 'Morocco', 'India'];
# df_cibo=df.groupby("country")['cibo'].mean()
# df_ciboj = df_cibo.to_frame().merge(codes, on=['country'], how='left')
# df_trasporto=df.groupby("country")['trasporto'].mean()
# df_trasportoj = df_trasporto.to_frame().merge(codes, on=['country'], how='left')
# df_casa=df.groupby("country")['casa'].mean()
# df_casaj = df_casa.to_frame().merge(codes, on=['country'], how='left')

########################################################

# fig = go.Figure()

# fig.add_trace(go.Scatterpolar(
#       r=[fil("Italy", df_trasportoj, "trasporto"), fil("Russia", df_trasportoj, "trasporto"), fil("United States", df_trasportoj, "trasporto"), fil("China", df_trasportoj, "trasporto"),fil("Australia", df_trasportoj, "trasporto"),fil("United Arab Emirates", df_trasportoj, "trasporto"), fil("Morocco", df_trasportoj, "trasporto"), fil("India", df_trasportoj, "trasporto")],
#       theta=stati,
#       fill='toself',
#       name='Trasporto',
#       marker_color='red'
     
# ))

# fig.add_trace(go.Scatterpolar(
#       r=[fil("Italy", df_casaj, "casa"), fil("Russia", df_casaj, "casa"), fil("United States", df_casaj, "casa"), fil("China", df_casaj, "casa"),fil("Australia", df_casaj, "casa"),fil("United Arab Emirates", df_casaj, "casa"), fil("Morocco", df_casaj, "casa"), fil("India", df_casaj, "casa")],
#       theta=stati,
#       fill='toself',
#       name='Abitazione',
#       marker_color='green'
     
# ))

# fig.update_layout(
#   polar=dict(
#     radialaxis=dict(
#       visible=True,
#       range=[0, 2000],
      
#     ),
    
#     ),
  
#   showlegend=True
# )

# fig.show()

########################################################

# fig = go.Figure()
# fig.add_trace(go.Box(
#     y=dfitaly['sum']/12,
#     name='Costo vita',
#     marker_color='blue',

# ))
# fig.add_trace(go.Box(
#     y=dfitaly['x54'],
#     name='Stipendio medio',
#     marker_color='green',

# ))

# fig.show()

########################################################

# filtrastati = (bollettej['country'] == "Italy") | (bollettej['country'] == "Switzerland") | (bollettej['country'] == "France") | (bollettej['country'] == "Turkey") | (bollettej['country'] == "Monaco") | (bollettej['country'] == "Liechtenstein") |(bollettej['country'] == "United States") |  (bollettej['country'] == "United Kingdom") | (bollettej['country'] == "Hungary") | (bollettej['country'] == "Norway") 

# fig = px.pie(bollettej.where(filtrastati), values='x36', names='country')
# fig.update_traces(textposition='inside', textinfo='label')
# fig.show()

fig = go.Figure()

countries = ['Italy', 'Switzerland', 'France', 'Turkey', 'Spain', 'Netherlands', 'China', 'United Kingdom', 'Hungary', 'Norway']

for country in countries:
    fig.add_trace(go.Violin(x=df['country'][df['country'] == country],
                            y=df['x43'][df['country'] == country].where(df['x43']>0),
                            name=country,
                            box_visible=True,
                            meanline_visible=True))

fig.show()