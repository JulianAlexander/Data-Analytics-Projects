
# Heroes of Pymoli - Data Crunching

Here are some observations based on the customer data given:<br>
    1.  Despite the large difference in the amount of purchasing data in either data set, the average purchase price among all customers is almost exactly the same, $2.93 vs $2.92.
 
    2.  Males, accounting for over 81% of the population in both data sets, also made up over 81% of the total revenue. The highest normalized purchase value belongs to the Other / Non-Disclosed group at $4.47.
    
    3. In both data sets, the largest source of the game's revenue comes from the 18 - 22 year old and 22 - 26 year old groups.  However, the highest average purchase belongs to the 38 - 42 year old group (34-38 is the highest, then the 38-42 in the second data set). While they do not make as many purchases as the 18 - 26 year olds, their average purchase is worth $1.47 more in the first data set, and nearly 50 cents more in the second.



```python
import pandas as pd
import os
#read in the first data file
game_data = pd.read_json('purchase_data.json')
```

# Raw Data


```python
game_data.head(10) #display the first 10 rows of data
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
    <tr>
      <th>5</th>
      <td>20</td>
      <td>Male</td>
      <td>10</td>
      <td>Sleepwalker</td>
      <td>1.73</td>
      <td>Tanimnya91</td>
    </tr>
    <tr>
      <th>6</th>
      <td>20</td>
      <td>Male</td>
      <td>153</td>
      <td>Mercenary Sabre</td>
      <td>4.57</td>
      <td>Undjaskla97</td>
    </tr>
    <tr>
      <th>7</th>
      <td>29</td>
      <td>Female</td>
      <td>169</td>
      <td>Interrogator, Blood Blade of the Queen</td>
      <td>3.32</td>
      <td>Iathenudil29</td>
    </tr>
    <tr>
      <th>8</th>
      <td>25</td>
      <td>Male</td>
      <td>118</td>
      <td>Ghost Reaver, Longsword of Magic</td>
      <td>2.77</td>
      <td>Sondenasta63</td>
    </tr>
    <tr>
      <th>9</th>
      <td>31</td>
      <td>Male</td>
      <td>99</td>
      <td>Expiration, Warscythe Of Lost Worlds</td>
      <td>4.53</td>
      <td>Hilaerin92</td>
    </tr>
  </tbody>
</table>
</div>



# Player Count


```python
player_count = game_data['SN'].nunique() #gives the unique player count based on the Screenname column
pc_dict = {'Total Players':[player_count]}
player_count_df = pd.DataFrame(data=pc_dict,index=None)
player_count_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>573</td>
    </tr>
  </tbody>
</table>
</div>



# Purchasing Analysis (Total)


```python
unique_items = game_data['Item ID'].nunique() #gives the unique item count based on the item ID column
total_purchases = game_data['Price'].count() #total count of purchases based on the price column
total_revenue = game_data['Price'].sum()
uniq_rev_dict = {'Number of Unique Items':[unique_items],'Average Price':['\$' + str(round(total_revenue/total_purchases,2))],'Number of Purchases':[total_purchases],'Total Revenue':['\$' + str(round(total_revenue,2))]}
uniq_rev_df = pd.DataFrame(data=uniq_rev_dict,index=None)
uniq_rev_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Price</th>
      <th>Number of Purchases</th>
      <th>Number of Unique Items</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>\$2.93</td>
      <td>780</td>
      <td>183</td>
      <td>\$2286.33</td>
    </tr>
  </tbody>
</table>
</div>



# Gender Demographics


```python
people_data = game_data.groupby('Gender') #Total number of male customers in data set. 
total_male = people_data.count()
male_num = total_male['Age']['Male']

uniq_names = game_data.drop_duplicates('SN',keep='first') 
uniq_male = uniq_names[uniq_names['Gender'] == 'Male'] #gives number of unique male customers

total_fem = total_male['Age']['Female'] #total number of female customers
uniq_fem = uniq_names[uniq_names['Gender'] == 'Female'] #total number of unique female customers

total_peep = total_male['Age']['Other / Non-Disclosed'] #total number of Other-Non/Disclosed purchasers
uniq_peep = uniq_names[uniq_names['Gender'] == 'Other / Non-Disclosed'] #total number of unique O/ND

#percentage breakdowns by gender
per_male = (uniq_male['SN'].count())/(uniq_male['SN'].count() + uniq_fem['SN'].count() + uniq_peep['SN'].count())
per_female = (uniq_fem['SN'].count())/(uniq_male['SN'].count() + uniq_fem['SN'].count() + uniq_peep['SN'].count())
per_peeps = (uniq_peep['SN'].count())/(uniq_male['SN'].count() + uniq_fem['SN'].count() + uniq_peep['SN'].count())

people_count = pd.DataFrame(columns = ['Percentage of Players','Total Count'],index = ['Male','Female','Other / Non-Disclosed'])
people_count['Percentage of Players']['Male'] = (str(round((per_male * 100),2)) + '%')
people_count['Percentage of Players']['Female'] = (str(round((per_female * 100),2)) + '%')
people_count['Percentage of Players']['Other / Non-Disclosed'] = (str(round((per_peeps * 100),2)) + '%')
people_count['Total Count']['Male'] = uniq_male['SN'].count()
people_count['Total Count']['Female'] = uniq_fem['SN'].count()
people_count['Total Count']['Other / Non-Disclosed'] = uniq_peep['SN'].count()
people_count
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>81.15%</td>
      <td>465</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>17.45%</td>
      <td>100</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>1.4%</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>



# Purchasing Analysis (Gender)


```python
#purchase data for males
male_spend = game_data.groupby('Gender')
tot_spend = male_spend['Price'].sum()
m_spend = tot_spend['Male']
avg_m_spend = m_spend / male_num

#purchase data for females
f_spend = tot_spend['Female']
avg_f_spend = f_spend / total_fem

#purchase data for O/ND
p_spend = tot_spend['Other / Non-Disclosed']
avg_o_spend = p_spend / total_peep

purchase_data = pd.DataFrame(columns = ['Purchase Count','Average Purchase Price','Total Purchase Value','Normalized Totals'],index = ['Female','Male','Other / Non-Disclosed'])
purchase_data['Purchase Count']['Female'] = total_male['Age']['Female']
purchase_data['Purchase Count']['Male'] = total_male['Age']['Male']
purchase_data['Purchase Count']['Other / Non-Disclosed'] = total_male['Age']['Other / Non-Disclosed']
purchase_data['Average Purchase Price']['Female'] = ( '\$' + str(round(avg_f_spend,2)))
purchase_data['Average Purchase Price']['Male'] = ( '\$' + str(round(avg_m_spend,2)))
purchase_data['Average Purchase Price']['Other / Non-Disclosed'] = ( '\$' + str(round(avg_o_spend,2)))
purchase_data['Total Purchase Value']['Female'] = ( '\$' + str(round(float(f_spend), 2)))
purchase_data['Total Purchase Value']['Male'] = ( '\$' + str(round(float(m_spend), 2)))
purchase_data['Total Purchase Value']['Other / Non-Disclosed'] = ( '\$' + str(round(float(p_spend), 2)))
purchase_data['Normalized Totals']['Female'] = ( '\$' + str(round(f_spend/(uniq_fem['SN'].count()),2)))
purchase_data['Normalized Totals']['Male'] = ( '\$' + str(round(m_spend/(uniq_male['SN'].count()),2)))
purchase_data['Normalized Totals']['Other / Non-Disclosed'] = ( '\$' + str(round(p_spend/(uniq_peep['SN'].count()),2)))
purchase_data
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>136</td>
      <td>\$2.82</td>
      <td>\$382.91</td>
      <td>\$3.83</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>633</td>
      <td>\$2.95</td>
      <td>\$1867.68</td>
      <td>\$4.02</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
      <td>\$3.25</td>
      <td>\$35.74</td>
      <td>\$4.47</td>
    </tr>
  </tbody>
</table>
</div>



# Age Demographics


```python
bins = [0,10,14,18,22,26,30,34,38,42,46] #binning data by Age
age_ranges = ['0-10','10-14','14-18','18-22','22-26','26-30','30-34','34-38','38-42','42-46']
range_ages = pd.cut(game_data['Age'], bins, labels = age_ranges)
age_bin_list = range_ages.value_counts(ascending = False).sort_index()

age_demo = pd.DataFrame(columns = ['Percentage of Players','Total Count'],index=age_ranges)
uniq_range_ages = pd.cut(uniq_names['Age'], bins, labels = age_ranges)
uniq_age_bin_list = uniq_range_ages.value_counts(ascending = False).sort_index()
for i in range(0,10):
    age_demo['Percentage of Players'][age_demo['Percentage of Players'].index[i]] = round(((uniq_age_bin_list[i]/uniq_age_bin_list.sum()) * 100),2)
    age_demo['Total Count'][age_demo['Total Count'].index[i]] = uniq_age_bin_list[i]
age_demo
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0-10</th>
      <td>3.84</td>
      <td>22</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>3.49</td>
      <td>20</td>
    </tr>
    <tr>
      <th>14-18</th>
      <td>14.66</td>
      <td>84</td>
    </tr>
    <tr>
      <th>18-22</th>
      <td>31.06</td>
      <td>178</td>
    </tr>
    <tr>
      <th>22-26</th>
      <td>26.7</td>
      <td>153</td>
    </tr>
    <tr>
      <th>26-30</th>
      <td>7.68</td>
      <td>44</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>5.93</td>
      <td>34</td>
    </tr>
    <tr>
      <th>34-38</th>
      <td>4.36</td>
      <td>25</td>
    </tr>
    <tr>
      <th>38-42</th>
      <td>1.92</td>
      <td>11</td>
    </tr>
    <tr>
      <th>42-46</th>
      <td>0.35</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



# Purchasing Analysis (Age)


```python
game_data = game_data.assign(Bin = range_ages) #assign the Bin ranges to the data set

age_stats = game_data.groupby('Bin')
bin_spend_average = age_stats['Price'].mean() #mean purchase price for each Age group

bin_spend_total = age_stats['Price'].sum() #total spent by each Age group

uniq_names = uniq_names.assign(Bin = range_ages)
uniq_age_stats = uniq_names.groupby('Bin')
bin_spend_count = uniq_age_stats['Price'].count() #count of unique customers in each Age group

age_df = pd.DataFrame(columns = ['Purchase Count','Average Purchase Price','Total Purchase Value','Normalized Totals'], index = age_ranges)
for i in range(0,10):  
    age_df['Purchase Count'][age_df['Purchase Count'].index[i]] = age_bin_list[i]
    age_df['Average Purchase Price'][age_df['Average Purchase Price'].index[i]] = ('\$' + str(round(bin_spend_total[i]/age_bin_list[i],2)))
    age_df['Total Purchase Value'][age_df['Total Purchase Value'].index[i]] = ('\$' + str(round(bin_spend_total[i],2)))
    age_df['Normalized Totals'][age_df['Normalized Totals'].index[i]] = ('\$' + str(round(bin_spend_total[i]/bin_spend_count[i],2)))
age_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0-10</th>
      <td>32</td>
      <td>\$3.02</td>
      <td>\$96.62</td>
      <td>\$4.39</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>31</td>
      <td>\$2.7</td>
      <td>\$83.79</td>
      <td>\$4.19</td>
    </tr>
    <tr>
      <th>14-18</th>
      <td>111</td>
      <td>\$2.88</td>
      <td>\$319.32</td>
      <td>\$3.8</td>
    </tr>
    <tr>
      <th>18-22</th>
      <td>231</td>
      <td>\$2.93</td>
      <td>\$676.2</td>
      <td>\$3.8</td>
    </tr>
    <tr>
      <th>22-26</th>
      <td>207</td>
      <td>\$2.94</td>
      <td>\$608.02</td>
      <td>\$3.97</td>
    </tr>
    <tr>
      <th>26-30</th>
      <td>63</td>
      <td>\$2.98</td>
      <td>\$187.99</td>
      <td>\$4.27</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>46</td>
      <td>\$3.07</td>
      <td>\$141.24</td>
      <td>\$4.15</td>
    </tr>
    <tr>
      <th>34-38</th>
      <td>37</td>
      <td>\$2.81</td>
      <td>\$104.06</td>
      <td>\$4.16</td>
    </tr>
    <tr>
      <th>38-42</th>
      <td>20</td>
      <td>\$3.13</td>
      <td>\$62.56</td>
      <td>\$5.69</td>
    </tr>
    <tr>
      <th>42-46</th>
      <td>2</td>
      <td>\$3.26</td>
      <td>\$6.53</td>
      <td>\$3.26</td>
    </tr>
  </tbody>
</table>
</div>



# Top Spenders


```python
top_spenders = game_data.sort_values('Price', ascending = False).head() #returns list of customers sorted by price

sn_spend = game_data.groupby('SN')
most_spend = sn_spend['Price'].sum() #sums the price column and filters by Screenname
top_5_spend = most_spend.sort_values(ascending = False).head()

best_cust_data = pd.DataFrame()
for i in range(5): #returns a DataFrame containing the customers who made the most number of purchases
    best_cust =(game_data['SN'] == top_5_spend.index[i])
    best_cust_1 = pd.DataFrame(game_data[best_cust])
    best_cust_data = best_cust_data.append(best_cust_1)
    
#Table containing highest spending customers
best_cust_tab = pd.DataFrame()
for i in range(5):
    best_cust_list = [{'Username':top_5_spend.index[i],'Total Purchases':best_cust_data['Price'][best_cust_data['SN']==top_5_spend.index[i]].count(),'Average Purchase':('\$' + str(round(best_cust_data['Price'][best_cust_data['SN']==top_5_spend.index[i]].mean(),2))),'Total Purchase Value':('\$' + str(round(best_cust_data['Price'][best_cust_data['SN']==top_5_spend.index[i]].sum(),2)))}]
    best_cust_tab = best_cust_tab.append(best_cust_list)
best_cust_tab[best_cust_tab.columns[::-1]]
best_cust_tab.set_index('Username')
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Purchase</th>
      <th>Total Purchase Value</th>
      <th>Total Purchases</th>
    </tr>
    <tr>
      <th>Username</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>\$3.41</td>
      <td>\$17.06</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>\$3.39</td>
      <td>\$13.56</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>\$3.18</td>
      <td>\$12.74</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Haellysu29</th>
      <td>\$4.24</td>
      <td>\$12.73</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Eoda93</th>
      <td>\$3.86</td>
      <td>\$11.58</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>



# Most Popular Items


```python
pop_items_tot = game_data.groupby('Item ID')
pop_items_data = pop_items_tot['Item ID'].count()
pop_items_new = pop_items_data.sort_values(ascending = False).head() #series of the most popular items, sorted by count of Item ID

#creates a DataFrame containing data for the most frequently bought items
popular_items = pd.DataFrame()
for i in range(5):
    popular_items_data = (game_data['Item ID'] == pop_items_new.index[i])
    pop_items_df = pd.DataFrame(game_data[popular_items_data])
    popular_items = popular_items.append(pop_items_df)

popular_items['Item Name'].astype('category')
pop_items = popular_items['Item Name'].unique() #sends the unique names of items into a new list

#creates a DataFrame that summarizes the most popular item data using the series of popular item names and the popular items data frame
popular_items_list = pd.DataFrame()
for i in range(5):
    pop_items_list = [{'Item ID':pop_items_new.index[i],'Item Name':pop_items[i],'Purchase Count':pop_items_new.values[i],'Item Price':('\$' + str(round(popular_items['Price'][popular_items['Item ID']==pop_items_new.index[i]].mean(),2))),'Total Value':('\$' + str(round(popular_items['Price'][popular_items['Item ID'] == pop_items_new.index[i]].sum(),2)))}]
    popular_items_list = popular_items_list.append(pop_items_list)

popular_items_list.set_index('Item ID')
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item Name</th>
      <th>Item Price</th>
      <th>Purchase Count</th>
      <th>Total Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>84</th>
      <td>Arcane Gem</td>
      <td>\$2.23</td>
      <td>11</td>
      <td>\$24.53</td>
    </tr>
    <tr>
      <th>39</th>
      <td>Betrayal, Whisper of Grieving Widows</td>
      <td>\$2.35</td>
      <td>11</td>
      <td>\$25.85</td>
    </tr>
    <tr>
      <th>31</th>
      <td>Trickster</td>
      <td>\$2.07</td>
      <td>9</td>
      <td>\$18.63</td>
    </tr>
    <tr>
      <th>34</th>
      <td>Retribution Axe</td>
      <td>\$4.14</td>
      <td>9</td>
      <td>\$37.26</td>
    </tr>
    <tr>
      <th>175</th>
      <td>Woeful Adamantite Claymore</td>
      <td>\$1.24</td>
      <td>9</td>
      <td>\$11.16</td>
    </tr>
  </tbody>
</table>
</div>



# Most Profitable Items


```python
expen_items = game_data.groupby('Item ID')
expen_items_series = expen_items['Price'].sum().sort_values(ascending = False) #a series of the sum of the prices of the most profitable items, sorted by Item ID

#creates a DataFrame containing data on the most profitable items
expensive_items = pd.DataFrame()
for i in range(5):
    expensive_items_data = (game_data['Item ID'] == expen_items_series.index[i])
    expensive_items_df = pd.DataFrame(game_data[expensive_items_data])
    expensive_items = expensive_items.append(expensive_items_df)

expnitems = expensive_items['Item Name'].unique() #assigns all of the profitable item names to a Series

#creates a DataFrame containing the profitable item data
expen_items_df = pd.DataFrame()
for i in range(5):
    expen_items_data = [{'Item ID':expen_items_series.index[i],'Item Name':expnitems[i], 'Purchase Count':game_data['Item Name'][game_data['Item ID']==expen_items_series.index[i]].count(),'Item Price':('\$' + str(round(game_data['Price'][game_data['Item ID']==expen_items_series.index[i]].mean(),2))),'Total Purchase Value':('\$' + str(round(game_data['Price'][game_data['Item ID']==expen_items_series.index[i]].sum(),2)))}]
    expen_items_df = expen_items_df.append(expen_items_data)

expen_items_df.set_index('Item ID')
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item Name</th>
      <th>Item Price</th>
      <th>Purchase Count</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <td>Retribution Axe</td>
      <td>\$4.14</td>
      <td>9</td>
      <td>\$37.26</td>
    </tr>
    <tr>
      <th>115</th>
      <td>Spectral Diamond Doomblade</td>
      <td>\$4.25</td>
      <td>7</td>
      <td>\$29.75</td>
    </tr>
    <tr>
      <th>32</th>
      <td>Orenmir</td>
      <td>\$4.95</td>
      <td>6</td>
      <td>\$29.7</td>
    </tr>
    <tr>
      <th>103</th>
      <td>Singed Scalpel</td>
      <td>\$4.87</td>
      <td>6</td>
      <td>\$29.22</td>
    </tr>
    <tr>
      <th>107</th>
      <td>Splitter, Foe Of Subtlety</td>
      <td>\$3.61</td>
      <td>8</td>
      <td>\$28.88</td>
    </tr>
  </tbody>
</table>
</div>


