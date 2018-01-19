
# coding: utf-8

# In[1]:


import requests as req
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import cenpy as cen
import pysal
import plotly
import plotly.plotly as py
import plotly.graph_objs as go


# # Business Dynamics Statistics
# The Business Dynamics Statistics (BDS) includes measures of establishment openings and closings, firm startups, job creation and destruction by firm size, age, and industrial sector, and several other statistics on business dynamics. The U.S. economy is comprised of over 6 million establishments with paid employees. The population of these businesses is constantly churning –– some businesses grow, others decline and yet others close. New businesses are constantly replenishing this pool. The BDS series provide annual statistics on gross job gains and losses for the entire economy and by industrial sector and state.
# 
# ### BDS Industrial Scope and Coverage
# #### Sectors Covered (SIC–based)	
# -  Agricultural Services, Forestry, and Fishing 
# -  Mining
# -  Construction
# -  Manufacturing
# -  Transportation and Public Utilities
# -  Wholesale Trade
# -  Retail Trade
# -  Finance, Insurance, and Real Estate
# -  Services (excluded types below)
#     -  Self–employed
#     -  Domestic service workers
#     -  Railroad employees
#     -  Agricultural production workers
#     -  Most government employees
#     -  Employees on ocean–borne vessels
#     -  Employees in foreign countries
# 
# This notebook will take a look at job creation, destruction, and employment numbers across 10 years worth of data, from 2005 to 2014.

# In[2]:


#create function to swap state codes for abbrevations
def state_abb(data):
    data['state'] = data['state'].replace('01','AL')
    data['state'] = data['state'].replace('02','AK')
    data['state'] = data['state'].replace('04','AZ')
    data['state'] = data['state'].replace('05','AR')
    data['state'] = data['state'].replace('06','CA')
    data['state'] = data['state'].replace('08','CO')
    data['state'] = data['state'].replace('09','CT')
    data['state'] = data['state'].replace('10','DE')
    data['state'] = data['state'].replace('11','DC')
    data['state'] = data['state'].replace('12','FL')
    data['state'] = data['state'].replace('13','GA')
    data['state'] = data['state'].replace('15','HI')
    data['state'] = data['state'].replace('16','ID')
    data['state'] = data['state'].replace('17','IL')
    data['state'] = data['state'].replace('18','IN')
    data['state'] = data['state'].replace('19','IA')
    data['state'] = data['state'].replace('20','KS')
    data['state'] = data['state'].replace('21','KY')
    data['state'] = data['state'].replace('22','LA')
    data['state'] = data['state'].replace('23','ME')
    data['state'] = data['state'].replace('24','MD')
    data['state'] = data['state'].replace('25','MA')
    data['state'] = data['state'].replace('26','MI')
    data['state'] = data['state'].replace('27','MN')
    data['state'] = data['state'].replace('28','MS')
    data['state'] = data['state'].replace('29','MO')
    data['state'] = data['state'].replace('30','MT')
    data['state'] = data['state'].replace('31','NE')
    data['state'] = data['state'].replace('32','NV')
    data['state'] = data['state'].replace('33','NH')
    data['state'] = data['state'].replace('34','NJ')
    data['state'] = data['state'].replace('35','NM')
    data['state'] = data['state'].replace('36','NY')
    data['state'] = data['state'].replace('37','NC')
    data['state'] = data['state'].replace('38','ND')
    data['state'] = data['state'].replace('39','OH')
    data['state'] = data['state'].replace('40','OK')
    data['state'] = data['state'].replace('41','OR')
    data['state'] = data['state'].replace('42','PA')
    data['state'] = data['state'].replace('44','RI')
    data['state'] = data['state'].replace('45','SC')
    data['state'] = data['state'].replace('46','SD')
    data['state'] = data['state'].replace('47','TN')
    data['state'] = data['state'].replace('48','TX')
    data['state'] = data['state'].replace('49','UT')
    data['state'] = data['state'].replace('50','VT')
    data['state'] = data['state'].replace('51','VA')
    data['state'] = data['state'].replace('53','WA')
    data['state'] = data['state'].replace('54','WV')
    data['state'] = data['state'].replace('55','WI')
    data['state'] = data['state'].replace('56','WY')


# In[3]:


#create function to swap business size code with explanation
def age_swap(data):
    data['fage4'] = data['fage4'].replace('m','Economy Wide - All Ages')
    data['fage4'] = data['fage4'].replace('a','0')
    data['fage4'] = data['fage4'].replace('b','1')
    data['fage4'] = data['fage4'].replace('c','2')
    data['fage4'] = data['fage4'].replace('d','3')
    data['fage4'] = data['fage4'].replace('e','4')
    data['fage4'] = data['fage4'].replace('f','5')
    data['fage4'] = data['fage4'].replace('g','6-10')
    data['fage4'] = data['fage4'].replace('h','11-15')
    data['fage4'] = data['fage4'].replace('i','16-20')
    data['fage4'] = data['fage4'].replace('j','21-25')
    data['fage4'] = data['fage4'].replace('k','26+')
    data['fage4'] = data['fage4'].replace('l','Before 1976')


# In[4]:


#create function to swap industry code with explanation
def industry_swap(data):
    data['sic1'] = data['sic1'].replace(0,'Economy Wide')
    data['sic1'] = data['sic1'].replace(7,'Agriculture, Forestry, Fishing')
    data['sic1'] = data['sic1'].replace(10,'Mining')
    data['sic1'] = data['sic1'].replace(15,'Construction')
    data['sic1'] = data['sic1'].replace(20,'Manufacturing')
    data['sic1'] = data['sic1'].replace(40,'Transportation, Communication, and Public Utilities')
    data['sic1'] = data['sic1'].replace(50,'Wholesale Trade')
    data['sic1'] = data['sic1'].replace(52,'Retail Trade')
    data['sic1'] = data['sic1'].replace(60,'Finance, Insurance, Real Estate')
    data['sic1'] = data['sic1'].replace(70,'Services')


# In[5]:


datasets = list(cen.explorer.available(verbose=True).items())
pd.DataFrame(datasets) #list of all the datasets available through the Census API


# In[6]:


dataset_1 = 'BDSFirmsTimeSeries'#name of the dataset to call

con_1 = cen.base.Connection(dataset_1)

con_1.variables


# In[7]:


#columns that will be queried
cols1 = ['d_flag','firms','fsize','job_creation','job_creation_rate','job_destruction','job_destruction_rate','net_job_creation','net_job_creation_rate','sic1','metro']
cols2 = ['emp','fage4','job_creation','job_creation_rate','net_job_creation','net_job_creation_rate','job_destruction','job_destruction_rate','sic1'] #','fsize','ifsize'


# In[8]:


#data queries varying by year
data2_2014 = con_1.query(cols2,geo_unit ='us:*', apikey ='4341d0be38fb2dd0481d00ea31d64a940ce22bd4', time = '2014', geo_filter = {})

data_2005 = con_1.query(cols1,geo_unit ='state:*', apikey ='4341d0be38fb2dd0481d00ea31d64a940ce22bd4', time = '2005', geo_filter = {})
data_2006 = con_1.query(cols1,geo_unit ='state:*', apikey ='4341d0be38fb2dd0481d00ea31d64a940ce22bd4', time = '2006', geo_filter = {})
data_2007 = con_1.query(cols1,geo_unit ='state:*', apikey ='4341d0be38fb2dd0481d00ea31d64a940ce22bd4', time = '2007', geo_filter = {})
data_2008 = con_1.query(cols1,geo_unit ='state:*', apikey ='4341d0be38fb2dd0481d00ea31d64a940ce22bd4', time = '2008', geo_filter = {})
data_2009 = con_1.query(cols1,geo_unit ='state:*', apikey ='4341d0be38fb2dd0481d00ea31d64a940ce22bd4', time = '2009', geo_filter = {})
data_2010 = con_1.query(cols1,geo_unit ='state:*', apikey ='4341d0be38fb2dd0481d00ea31d64a940ce22bd4', time = '2010', geo_filter = {})
data_2011 = con_1.query(cols1,geo_unit ='state:*', apikey ='4341d0be38fb2dd0481d00ea31d64a940ce22bd4', time = '2011', geo_filter = {})
data_2012 = con_1.query(cols1,geo_unit ='state:*', apikey ='4341d0be38fb2dd0481d00ea31d64a940ce22bd4', time = '2012', geo_filter = {})
data_2013 = con_1.query(cols1,geo_unit ='state:*', apikey ='4341d0be38fb2dd0481d00ea31d64a940ce22bd4', time = '2013', geo_filter = {})
data_2014 = con_1.query(cols1,geo_unit ='state:*', apikey ='4341d0be38fb2dd0481d00ea31d64a940ce22bd4', time = '2014', geo_filter = {})


# In[12]:


data_2009.head(100)


# In[9]:


#concatanate the data into a single dataframe
ten_year_data = pd.concat([data_2014,data_2013,data_2012,data_2011,data_2010,data_2009,data_2008,data_2007,data_2006,data_2005])

ten_year_data[ten_year_data.index== 47]

ten_year_data.groupby('state').head(20)


# In[10]:


#reorangize the dataframe to sort by years
year_sum = ten_year_data[ten_year_data['d_flag']==0].groupby('time').sum().head(20)
year_sum


# In[11]:


x_data = year_sum.index
y_data = year_sum['net_job_creation']
text_data = list(y_data)

#Bar graph of net jobs created in US from 2005 to 2014
trace0 = go.Bar(x=x_data,y=y_data)
data_bar = [trace0]
layout = go.Layout(
    title='Net Job Creation - 2006 to 2014',
    barmode='stack',
    paper_bgcolor='rgba(245, 246, 249, 1)',
    plot_bgcolor='rgba(245, 246, 249, 1)',
    showlegend=False)
annotations = [dict(
            x=xpos,
            y=ypos,
            xref='x',
            yref='y',
            text=str(ypos),
            showarrow=True,
            arrowhead=4,
            ax=0,
            ay=-40
    ) for xpos, ypos in zip(x_data, y_data)]

layout['annotations'] = annotations


# In[12]:


fig = go.Figure(data=data_bar,layout=layout)
plotly.offline.plot(fig,filename='waterfall-bar-profit',image='png',image_width = 1632,image_height=1224)


# In[13]:


us_job_create_rate = ten_year_data[ten_year_data['d_flag']==0].groupby('time').mean().head(20)


# In[14]:


jobs_2005 = ten_year_data[ten_year_data['time'] == '2005']
jobs_2014 = ten_year_data[ten_year_data['time'] == '2014']
jobs_2005[jobs_2005.index==0]['net_job_creation'].sum()


# In[15]:


net_job_create_states = pd.DataFrame(columns = ['state','2005 Job Creation','2014 Job Creation'])

net_job_create_states['2005 Job Creation'] = [jobs_2005[jobs_2005.index == i]['net_job_creation'].sum() for i in range(len(ten_year_data['state'].unique()))]
net_job_create_states['2014 Job Creation'] = [jobs_2014[jobs_2014.index == i]['net_job_creation'].sum() for i in range(len(ten_year_data['state'].unique()))]

net_job_create_states['state'] = [ten_year_data['state'].unique()[i] for i in range(len(ten_year_data['state'].unique()))]

state_abb(net_job_create_states)

net_job_create_states['Net Job Creation'] = net_job_create_states['2014 Job Creation'] - net_job_create_states['2005 Job Creation']

sorted_net_job_create = net_job_create_states.sort_values('Net Job Creation')
sorted_net_job_create = sorted_net_job_create.reset_index()
sorted_net_job_create


# In[16]:


#create bar chart of california net job rate vs US
cal_job_create_rate = ten_year_data[ten_year_data.index == 4]['net_job_creation_rate']

trace1 = go.Bar(
    x=year_sum.index,
    y= cal_job_create_rate,
    name='California',
    marker=dict(
        color='rgb(55, 83, 109)'
    )
)
trace2 = go.Bar(
    x=year_sum.index,
    y=us_job_create_rate['net_job_creation_rate'],
    name='US Average',
    marker=dict(
        color='rgb(26, 118, 255)'
    )
)
data = [trace1, trace2]
layout = go.Layout(
    title='California Job Creation Rate vs US Average',
    xaxis=dict(
        tickfont=dict(
            size=14,
            color='rgb(107, 107, 107)'
        )
    ),
    yaxis=dict(
        title='Rate',
        titlefont=dict(
            size=16,
            color='rgb(107, 107, 107)'
        ),
        tickfont=dict(
            size=14,
            color='rgb(107, 107, 107)'
        )
    ),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
    ),
    barmode='group',
    bargap=0.15,
    bargroupgap=0.1
)

fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='style-bar',image='png',image_width = 1632,image_height=1224)


# In[17]:


xytest = net_job_create_states[net_job_create_states['state'] == 'AL']['2005 Job Creation'].sum()
xytest2 = net_job_create_states[net_job_create_states['state'] == 'AL']['2014 Job Creation'].sum()


# In[18]:


fig, ax = plt.subplots(figsize=(20,20))
for i in range(len(ten_year_data['state'].unique())):
    x = np.linspace(-250000,400000,num=52)
    y= np.linspace(0,51,num=52)
    ax.plot(x, y,'w')
    names=sorted_net_job_create['state'],
    ax.annotate('', (sorted_net_job_create['2014 Job Creation'][i],i),(sorted_net_job_create['2005 Job Creation'][i],i), 
        arrowprops={'arrowstyle': 'fancy','lw':2,'color':'blue'}, va='center')
    ax.annotate(sorted_net_job_create['Net Job Creation'][i], (sorted_net_job_create['2014 Job Creation'][i],i+0.5),
                (sorted_net_job_create['2005 Job Creation'][i],i+0.5),va='center')
    #ax.annotate(sorted_net_job_create['2014 Job Creation'][i], (sorted_net_job_create['2005 Job Creation'][i],i+0.5),(sorted_net_job_create['2014 Job Creation'][i],i+0.5),va='center')
    ax.grid()
    ax.annotate(sorted_net_job_create['state'][i], (sorted_net_job_create['2014 Job Creation'][i]-20000,i+0.5),(sorted_net_job_create['2005 Job Creation'][i]-20000,i+.5),va='center')
    plt.xlabel('Net Jobs Created')
    plt.yticks(np.linspace(0,51,num=52),sorted_net_job_create['state'])
    plt.title('Net Job Creation for each US State from 2005 to 2014')


# In[145]:


plt.savefig('net_job_us_state.png')
plt.show()


# In[19]:


data2_2014 = data2_2014.groupby(['fage4']).head(50)

data2_2014[data2_2014['sic1'] == 0]


# In[20]:


age_swap(data2_2014)
#sorting industry job data for 2014
data2_2014_industry = data2_2014[data2_2014['sic1'] == 0]
data2_2014_industry.groupby('fage4').head()


# In[121]:


data2_2014_industry = data2_2014_industry.pivot_table('job_creation', index='fage4')


# In[122]:


data2_2014_industry = data2_2014_industry.drop([0,21])


# In[21]:


#create bar chart detailing jobs created by age of business
trace_bar = go.Bar(x=data2_2014_industry['fage4'],y=data2_2014_industry['job_creation'])
bar_data = [trace_bar]
bar_layout = go.Layout(
    title='Jobs created by age of Business - 2014',
    xaxis = (dict(
        title = 'Age of Business',type='category',
        categoryorder = 'array',categoryarray = (data2_2014_industry['fage4']))
            ),
    yaxis = dict(
        title = 'Number of Jobs')
)
fig = go.Figure(data=bar_data,layout=bar_layout)


# In[22]:


plotly.offline.plot(fig,filename='angled-text-bar',image='png',image_filename = 'job_age_business',image_width = 1632,image_height=1224)


# In[23]:


tot_rates = data2_2014[data2_2014['sic1']==0]


# In[24]:


trace1 = go.Bar(x = tot_rates['fage4'],y = tot_rates['job_creation_rate'], name='Job Creation Rate', marker=dict(color='rgb(26,118,225)'))
trace2 = go.Bar(x = tot_rates['fage4'],y=tot_rates['job_destruction_rate'],name ='Job Destruction Rate', marker=dict(color = 'rgb(55,83,109)'))
trace3 = go.Bar(x=tot_rates['fage4'],y = tot_rates['net_job_creation_rate'], name = 'Net Job Creation Rate', 
                marker=dict(color = 'rgb(50,171,96)'))

data = [trace1, trace2,trace3]
layout = go.Layout(
    title = 'Job Creation rate vs Job Destruction rate by Business Age- 2014',
    xaxis = dict(type = 'category', categoryorder = 'array', categoryarray = tot_rates['fage4']),
    yaxis =dict(title = 'Rate'),
    barmode = 'group',
    bargap = 0.15,
    bargroupgap = 0.1
)


# In[25]:


tot_rates


# In[26]:


tot_rates2 = tot_rates.drop(10) #dropping data from the 0 index, which equates to a business age of 0


# In[27]:


#Graph of net job creation and destruction rates based on age of business
trace1 = go.Bar(x = tot_rates2['fage4'],y = tot_rates2['job_creation_rate'], name='Job Creation Rate', marker=dict(color='rgb(26,118,225)'))
trace2 = go.Bar(x = tot_rates2['fage4'],y=tot_rates2['job_destruction_rate'],name ='Job Destruction Rate', marker=dict(color = 'darkred'))
trace3 = go.Bar(x=tot_rates2['fage4'],y = tot_rates2['net_job_creation_rate'], name = 'Net Job Creation Rate', 
                marker=dict(color = 'rgb(50,171,96)'))

data = [trace1, trace2, trace3]
layout = go.Layout(
    title = 'Job Creation rate, Job Destruction rate, and Net Job Creation rate by Business Age - 2014',
    xaxis = dict(title = 'Age of Business',type = 'category', categoryorder = 'array', categoryarray = tot_rates2['fage4']),
    yaxis =dict(title = 'Rate'),
    barmode = 'group',
    bargap = 0.15,
    bargroupgap = 0.1
)


# In[28]:


fig= go.Figure(data=data,layout=layout)
plotly.offline.plot(fig,filename='style-bar',image='png',image_width = 1632,image_height=1224)


# In[171]:


#The same graph as above, but with the total amount employeed by each business included
trace4 = go.Bar(x = tot_rates2['fage4'],y = tot_rates2['emp'], name='Total Employees', marker=dict(color='purple'))
trace5 = go.Bar(x = tot_rates2['fage4'],y=tot_rates2['job_creation'],name ='Total Job Creation', marker=dict(color = 'rgb(26,118,225)'))
trace6 = go.Bar(x=tot_rates2['fage4'],y = tot_rates2['job_destruction'], name = 'Total Job Destruction', 
                marker=dict(color = 'darkred'))
trace7 = go.Bar(x=tot_rates2['fage4'],y = tot_rates2['net_job_creation'], name = 'Net Job Creation', 
                marker=dict(color = 'darkgreen'))
data = [trace4, trace5, trace6,trace7]
layout = go.Layout(
    title = 'Total Employees, Total Job Creation and Total Job Destruction by Business Age- 2014',
    xaxis = dict(title = 'Age of Business',type = 'category', categoryorder = 'array', categoryarray = tot_rates2['fage4']),
    yaxis =dict(title = 'Rate'),
    barmode = 'group',
    bargap = 0.15,
    bargroupgap = 0.1
)


# In[172]:


fig = go.Figure(data=data,layout=layout)
plotly.offline.plot(fig, filename='style-bar',image='png',image_width = 1632,image_height=1224)


# In[136]:


#gathering more industry data for ten years, 2005 - 2014
industry_2005 = con_1.query(cols2,geo_unit ='us:*', apikey ='4341d0be38fb2dd0481d00ea31d64a940ce22bd4', time = '2005', geo_filter = {})
industry_2006 = con_1.query(cols2,geo_unit ='us:*', apikey ='4341d0be38fb2dd0481d00ea31d64a940ce22bd4', time = '2006', geo_filter = {})
industry_2007 = con_1.query(cols2,geo_unit ='us:*', apikey ='4341d0be38fb2dd0481d00ea31d64a940ce22bd4', time = '2007', geo_filter = {})
industry_2008 = con_1.query(cols2,geo_unit ='us:*', apikey ='4341d0be38fb2dd0481d00ea31d64a940ce22bd4', time = '2008', geo_filter = {})
industry_2009 = con_1.query(cols2,geo_unit ='us:*', apikey ='4341d0be38fb2dd0481d00ea31d64a940ce22bd4', time = '2009', geo_filter = {})
industry_2010 = con_1.query(cols2,geo_unit ='us:*', apikey ='4341d0be38fb2dd0481d00ea31d64a940ce22bd4', time = '2010', geo_filter = {})
industry_2011 = con_1.query(cols2,geo_unit ='us:*', apikey ='4341d0be38fb2dd0481d00ea31d64a940ce22bd4', time = '2011', geo_filter = {})
industry_2012 = con_1.query(cols2,geo_unit ='us:*', apikey ='4341d0be38fb2dd0481d00ea31d64a940ce22bd4', time = '2012', geo_filter = {})
industry_2013 = con_1.query(cols2,geo_unit ='us:*', apikey ='4341d0be38fb2dd0481d00ea31d64a940ce22bd4', time = '2013', geo_filter = {})
industry_2014 = con_1.query(cols2,geo_unit ='us:*', apikey ='4341d0be38fb2dd0481d00ea31d64a940ce22bd4', time = '2014', geo_filter = {})


# In[137]:


#combining all the data into a single dataframe
ten_year_industry = pd.concat([industry_2005,industry_2006,industry_2007,industry_2008,industry_2009,industry_2010,industry_2011,industry_2012,industry_2013,industry_2014])

age_swap(ten_year_industry)


# In[138]:


industry_swap(ten_year_industry) #swapping the industry code identifiers

ten_year_industry.head()


# In[139]:


#sorting all of the data from the above dataframe into series containing information regarding the specific industry
agr_raw = ten_year_industry[ten_year_industry['sic1']=='Agriculture, Forestry, Fishing'].groupby('time').head()
agr_raw_tot = agr_raw[agr_raw['fage4']=='Economy Wide - All Ages']
min_raw = ten_year_industry[ten_year_industry['sic1']=='Mining'].groupby('time').head()
min_raw_tot = min_raw[min_raw['fage4']=='Economy Wide - All Ages']
con_raw = ten_year_industry[ten_year_industry['sic1']=='Construction'].groupby('time').head()
con_raw_tot = con_raw[con_raw['fage4']=='Economy Wide - All Ages']
man_raw = ten_year_industry[ten_year_industry['sic1']=='Manufacturing'].groupby('time').head()
man_raw_tot = man_raw[man_raw['fage4']=='Economy Wide - All Ages']
tran_raw = ten_year_industry[ten_year_industry['sic1']=='Transportation, Communication, and Public Utilities'].groupby('time').head()
tran_raw_tot = tran_raw[tran_raw['fage4']=='Economy Wide - All Ages']
who_raw = ten_year_industry[ten_year_industry['sic1']=='Wholesale Trade'].groupby('time').head()
who_raw_tot = who_raw[who_raw['fage4']=='Economy Wide - All Ages']
ret_raw = ten_year_industry[ten_year_industry['sic1']=='Retail Trade'].groupby('time').head()
ret_raw_tot = ret_raw[ret_raw['fage4']=='Economy Wide - All Ages']
fin_raw = ten_year_industry[ten_year_industry['sic1']=='Finance, Insurance, Real Estate'].groupby('time').head()
fin_raw_tot = fin_raw[fin_raw['fage4']=='Economy Wide - All Ages']
ser_raw = ten_year_industry[ten_year_industry['sic1']=='Services'].groupby('time').head()
ser_raw_tot = ser_raw[ser_raw['fage4']=='Economy Wide - All Ages']


# In[169]:


#creating line plot with every industry series with job creation information
data = [
    go.Scatter(x=agr_raw_tot['time'],y = agr_raw_tot['job_creation'], name = 'Agriculture, Forestry, Fishing'),
    go.Scatter(x=agr_raw_tot['time'],y = min_raw_tot['job_creation'], name = 'Mining'),
    go.Scatter(x=agr_raw_tot['time'],y = con_raw_tot['job_creation'], name = 'Construction'),
    go.Scatter(x=agr_raw_tot['time'],y = man_raw_tot['job_creation'], name = 'Manufacturing'),
    go.Scatter(x=agr_raw_tot['time'],y = tran_raw_tot['job_creation'], name = 'Transportation, Communication, and Public Utilities'),
    go.Scatter(x=agr_raw_tot['time'],y = who_raw_tot['job_creation'], name = 'Wholesale Trade'),
    go.Scatter(x=agr_raw_tot['time'],y = ret_raw_tot['job_creation'], name = 'Retail Trade'),
    go.Scatter(x=agr_raw_tot['time'],y = fin_raw_tot['job_creation'], name = 'Finance, Insurance, Real Estate'),
    go.Scatter(x=agr_raw_tot['time'],y = ser_raw_tot['job_creation'], name = 'Services')
]
layout = go.Layout(title = 'Job Creation by Industry',
    xaxis=dict(
        title='Years',
        titlefont=dict(
            family='Arial, sans-serif',
            size=18
        ),
        showticklabels=True,
    dtick = 1),
    yaxis = dict(
        title = 'Number of created Jobs')
    )
fig = go.Figure(data=data, layout=layout)


# In[170]:


plotly.offline.plot(fig, filename = 'pandas-line-naming-traces',image='png',image_width = 1632,image_height=1224)


# In[173]:


#creating another line plot with job destruction data for each industry over 10 years
data = [
    go.Scatter(x=agr_raw_tot['time'],y = agr_raw_tot['job_destruction'], name = 'Agriculture, Forestry, Fishing'),
    go.Scatter(x=agr_raw_tot['time'],y = min_raw_tot['job_destruction'], name = 'Mining'),
    go.Scatter(x=agr_raw_tot['time'],y = con_raw_tot['job_destruction'], name = 'Construction'),
    go.Scatter(x=agr_raw_tot['time'],y = man_raw_tot['job_destruction'], name = 'Manufacturing'),
    go.Scatter(x=agr_raw_tot['time'],y = tran_raw_tot['job_destruction'], name = 'Transportation, Communication, and Public Utilities'),
    go.Scatter(x=agr_raw_tot['time'],y = who_raw_tot['job_destruction'], name = 'Wholesale Trade'),
    go.Scatter(x=agr_raw_tot['time'],y = ret_raw_tot['job_destruction'], name = 'Retail Trade'),
    go.Scatter(x=agr_raw_tot['time'],y = fin_raw_tot['job_destruction'], name = 'Finance, Insurance, Real Estate'),
    go.Scatter(x=agr_raw_tot['time'],y = ser_raw_tot['job_destruction'], name = 'Services')
]
layout = go.Layout(title='Job Destruction by Industry',
    xaxis=dict(
        title='Years',
        titlefont=dict(
            family='Arial, sans-serif',
            size=18
        ),
        showticklabels=True,
    dtick = 1),
    yaxis = dict(
        title = 'Number of destroyed Jobs')
    )
fig = go.Figure(data=data, layout=layout)


# In[174]:


plotly.offline.plot(fig, filename = 'pandas-line-naming-traces',image='png',image_width = 1632,image_height=1224)

