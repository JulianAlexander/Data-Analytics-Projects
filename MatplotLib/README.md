

```python
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
```


```python
csvpath_city = os.path.join('raw_data','city_data.csv')
pyber_city_df = pd.read_csv(csvpath_city)
csvpath_ride = os.path.join('raw_data','ride_data.csv')
pyber_ride_df = pd.read_csv(csvpath_ride)
```


```python
pyber_city_df.head()
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
      <th>city</th>
      <th>driver_count</th>
      <th>type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Nguyenbury</td>
      <td>8</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2</th>
      <td>East Douglas</td>
      <td>12</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>3</th>
      <td>West Dawnfurt</td>
      <td>34</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Rodriguezburgh</td>
      <td>52</td>
      <td>Urban</td>
    </tr>
  </tbody>
</table>
</div>




```python
pyber_city_df['type'].value_counts()
```




    Urban       66
    Suburban    42
    Rural       18
    Name: type, dtype: int64




```python
pyber_gcity = pyber_ride_df.groupby('city')
pyber_gcity.head()
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
      <th>city</th>
      <th>date</th>
      <th>fare</th>
      <th>ride_id</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Sarabury</td>
      <td>2016-01-16 13:49:27</td>
      <td>38.35</td>
      <td>5403689035038</td>
    </tr>
    <tr>
      <th>1</th>
      <td>South Roy</td>
      <td>2016-01-02 18:42:34</td>
      <td>17.49</td>
      <td>4036272335942</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Wiseborough</td>
      <td>2016-01-21 17:35:29</td>
      <td>44.18</td>
      <td>3645042422587</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Spencertown</td>
      <td>2016-07-31 14:53:22</td>
      <td>6.87</td>
      <td>2242596575892</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Nguyenbury</td>
      <td>2016-07-09 04:42:44</td>
      <td>6.28</td>
      <td>1543057793673</td>
    </tr>
    <tr>
      <th>5</th>
      <td>New Jeffrey</td>
      <td>2016-02-22 18:36:25</td>
      <td>36.01</td>
      <td>9757888452346</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Port Johnstad</td>
      <td>2016-06-07 02:39:58</td>
      <td>17.15</td>
      <td>4352278259335</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Jacobfort</td>
      <td>2016-09-20 20:58:37</td>
      <td>22.98</td>
      <td>1500221409082</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Travisville</td>
      <td>2016-01-15 17:32:02</td>
      <td>27.39</td>
      <td>850152768361</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Sandymouth</td>
      <td>2016-11-16 07:27:00</td>
      <td>21.61</td>
      <td>2389035050524</td>
    </tr>
    <tr>
      <th>10</th>
      <td>New Andreamouth</td>
      <td>2016-04-11 07:20:48</td>
      <td>7.72</td>
      <td>9992929847990</td>
    </tr>
    <tr>
      <th>11</th>
      <td>New Christine</td>
      <td>2016-09-13 15:06:42</td>
      <td>24.89</td>
      <td>7918411468537</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Stewartview</td>
      <td>2016-03-29 05:15:56</td>
      <td>23.88</td>
      <td>6778235889588</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Rodriguezburgh</td>
      <td>2016-09-05 05:20:39</td>
      <td>4.54</td>
      <td>9650770953139</td>
    </tr>
    <tr>
      <th>14</th>
      <td>West Sydneyhaven</td>
      <td>2016-08-02 21:18:44</td>
      <td>12.87</td>
      <td>7994760397230</td>
    </tr>
    <tr>
      <th>15</th>
      <td>Swansonbury</td>
      <td>2016-07-11 18:42:11</td>
      <td>39.30</td>
      <td>744481862626</td>
    </tr>
    <tr>
      <th>16</th>
      <td>Lisatown</td>
      <td>2016-07-05 18:09:14</td>
      <td>5.82</td>
      <td>6370359473201</td>
    </tr>
    <tr>
      <th>17</th>
      <td>East Erin</td>
      <td>2016-11-03 01:03:05</td>
      <td>7.51</td>
      <td>4744239092530</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Port Martinberg</td>
      <td>2016-01-06 17:11:30</td>
      <td>8.66</td>
      <td>7298562820881</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Wiseborough</td>
      <td>2016-09-12 18:43:41</td>
      <td>26.83</td>
      <td>9304728540000</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Edwardsbury</td>
      <td>2016-02-27 03:55:54</td>
      <td>20.17</td>
      <td>8514523868075</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Jacobfort</td>
      <td>2016-06-12 17:01:29</td>
      <td>34.47</td>
      <td>4135673527977</td>
    </tr>
    <tr>
      <th>22</th>
      <td>Pamelahaven</td>
      <td>2016-03-26 12:56:57</td>
      <td>36.43</td>
      <td>3015329826849</td>
    </tr>
    <tr>
      <th>23</th>
      <td>Fosterside</td>
      <td>2016-08-12 11:52:41</td>
      <td>28.08</td>
      <td>133077693483</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Jacobfort</td>
      <td>2016-09-17 12:38:58</td>
      <td>38.25</td>
      <td>2182376146051</td>
    </tr>
    <tr>
      <th>25</th>
      <td>West Sydneyhaven</td>
      <td>2016-08-23 14:49:59</td>
      <td>36.12</td>
      <td>5885997568611</td>
    </tr>
    <tr>
      <th>26</th>
      <td>West Alexis</td>
      <td>2016-01-16 00:33:02</td>
      <td>26.62</td>
      <td>1574788996743</td>
    </tr>
    <tr>
      <th>27</th>
      <td>Carrollfort</td>
      <td>2016-06-24 20:11:11</td>
      <td>6.45</td>
      <td>1092683495142</td>
    </tr>
    <tr>
      <th>28</th>
      <td>New David</td>
      <td>2016-01-12 20:48:43</td>
      <td>38.68</td>
      <td>5229089333754</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Stewartview</td>
      <td>2016-10-15 05:26:40</td>
      <td>11.74</td>
      <td>8402784599831</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2308</th>
      <td>West Kevintown</td>
      <td>2016-06-25 08:04:12</td>
      <td>24.53</td>
      <td>8188407925972</td>
    </tr>
    <tr>
      <th>2310</th>
      <td>Hernandezshire</td>
      <td>2016-04-11 04:44:50</td>
      <td>10.41</td>
      <td>9823290002445</td>
    </tr>
    <tr>
      <th>2312</th>
      <td>East Troybury</td>
      <td>2016-02-29 07:26:19</td>
      <td>14.01</td>
      <td>6867080292206</td>
    </tr>
    <tr>
      <th>2313</th>
      <td>Kennethburgh</td>
      <td>2016-02-29 21:50:59</td>
      <td>47.48</td>
      <td>12105457917</td>
    </tr>
    <tr>
      <th>2314</th>
      <td>Shelbyhaven</td>
      <td>2016-04-21 19:22:03</td>
      <td>37.19</td>
      <td>5142074323359</td>
    </tr>
    <tr>
      <th>2315</th>
      <td>North Whitney</td>
      <td>2016-02-21 18:20:14</td>
      <td>42.01</td>
      <td>3306522110065</td>
    </tr>
    <tr>
      <th>2319</th>
      <td>Jacksonfort</td>
      <td>2016-06-09 23:01:40</td>
      <td>24.63</td>
      <td>978305304720</td>
    </tr>
    <tr>
      <th>2322</th>
      <td>Stevensport</td>
      <td>2016-10-30 16:24:21</td>
      <td>22.81</td>
      <td>3116198466324</td>
    </tr>
    <tr>
      <th>2323</th>
      <td>East Troybury</td>
      <td>2016-07-01 12:48:05</td>
      <td>12.88</td>
      <td>5989452220219</td>
    </tr>
    <tr>
      <th>2324</th>
      <td>Matthewside</td>
      <td>2016-02-23 17:46:29</td>
      <td>59.65</td>
      <td>241191157535</td>
    </tr>
    <tr>
      <th>2327</th>
      <td>West Kevintown</td>
      <td>2016-07-24 13:41:23</td>
      <td>11.78</td>
      <td>2001192693573</td>
    </tr>
    <tr>
      <th>2328</th>
      <td>Erikport</td>
      <td>2016-01-18 07:11:45</td>
      <td>10.66</td>
      <td>9287766069118</td>
    </tr>
    <tr>
      <th>2331</th>
      <td>Erikport</td>
      <td>2016-11-28 05:51:38</td>
      <td>23.38</td>
      <td>6392257942917</td>
    </tr>
    <tr>
      <th>2333</th>
      <td>Kennethburgh</td>
      <td>2016-03-22 18:04:29</td>
      <td>25.67</td>
      <td>1480709392474</td>
    </tr>
    <tr>
      <th>2334</th>
      <td>Kennethburgh</td>
      <td>2016-03-22 12:38:48</td>
      <td>36.54</td>
      <td>7210244842844</td>
    </tr>
    <tr>
      <th>2336</th>
      <td>Stevensport</td>
      <td>2016-05-11 12:08:25</td>
      <td>41.83</td>
      <td>1591306474620</td>
    </tr>
    <tr>
      <th>2338</th>
      <td>New Johnbury</td>
      <td>2016-05-03 04:52:29</td>
      <td>40.71</td>
      <td>2918447130656</td>
    </tr>
    <tr>
      <th>2340</th>
      <td>Stevensport</td>
      <td>2016-10-13 03:36:59</td>
      <td>52.99</td>
      <td>9771737428375</td>
    </tr>
    <tr>
      <th>2342</th>
      <td>Shelbyhaven</td>
      <td>2016-06-12 16:57:25</td>
      <td>30.18</td>
      <td>2015025942653</td>
    </tr>
    <tr>
      <th>2344</th>
      <td>Shelbyhaven</td>
      <td>2016-07-22 05:59:01</td>
      <td>10.64</td>
      <td>1406024986969</td>
    </tr>
    <tr>
      <th>2346</th>
      <td>Matthewside</td>
      <td>2016-02-23 00:43:51</td>
      <td>40.84</td>
      <td>8665248512368</td>
    </tr>
    <tr>
      <th>2351</th>
      <td>Stevensport</td>
      <td>2016-02-22 02:45:07</td>
      <td>19.91</td>
      <td>808097865942</td>
    </tr>
    <tr>
      <th>2352</th>
      <td>South Elizabethmouth</td>
      <td>2016-11-23 07:47:18</td>
      <td>46.39</td>
      <td>1939838068038</td>
    </tr>
    <tr>
      <th>2354</th>
      <td>Jacksonfort</td>
      <td>2016-10-01 13:41:00</td>
      <td>34.17</td>
      <td>7750597960630</td>
    </tr>
    <tr>
      <th>2356</th>
      <td>Horneland</td>
      <td>2016-03-25 02:05:42</td>
      <td>20.04</td>
      <td>5729327140644</td>
    </tr>
    <tr>
      <th>2362</th>
      <td>Matthewside</td>
      <td>2016-05-18 02:00:30</td>
      <td>48.67</td>
      <td>2049161404256</td>
    </tr>
    <tr>
      <th>2363</th>
      <td>Matthewside</td>
      <td>2016-08-08 14:02:35</td>
      <td>24.97</td>
      <td>2872494724827</td>
    </tr>
    <tr>
      <th>2365</th>
      <td>South Elizabethmouth</td>
      <td>2016-07-19 09:35:59</td>
      <td>31.09</td>
      <td>2959749591417</td>
    </tr>
    <tr>
      <th>2367</th>
      <td>New Johnbury</td>
      <td>2016-08-29 02:36:06</td>
      <td>18.83</td>
      <td>7368222134792</td>
    </tr>
    <tr>
      <th>2374</th>
      <td>South Elizabethmouth</td>
      <td>2016-04-21 10:20:09</td>
      <td>16.50</td>
      <td>5702608059064</td>
    </tr>
  </tbody>
</table>
<p>618 rows × 4 columns</p>
</div>



# Bubble Plot of Ride Share Data


```python
city_fare = pyber_gcity['fare'].sum()
city_count = pyber_gcity['city'].count()

avg_city = pyber_gcity['fare'].sum()/pyber_gcity['city'].count()
```


```python
merge_pyber = pd.merge(pyber_ride_df,pyber_city_df, on='city')
```


```python
urban_city = merge_pyber[merge_pyber['type']=='Urban']['city'].value_counts()
```




    Swansonbury         34
    Port Johnstad       34
    South Louis         32
    Jacobfort           31
    Williamshire        31
    Arnoldview          31
    West Peter          31
    Alvarezhaven        31
    West Brandy         30
    Stewartview         30
    West Dawnfurt       29
    Carrollfort         29
    West Oscar          29
    Kelseyland          28
    New Andreamouth     28
    Lisaville           28
    East Erin           28
    New David           28
    Kimberlychester     27
    Smithhaven          27
    Edwardsbury         27
    Sandymouth          27
    Port Samantha       27
    Sarabury            27
    Spencertown         26
    Nguyenbury          26
    Alyssaberg          26
    Torresshire         26
    Lake Jennaton       25
    Lake Jeffreyland    25
                        ..
    Fosterside          24
    Russellport         23
    Rodriguezburgh      23
    Travisville         23
    Lisatown            23
    New Aaron           22
    Lake Sarashire      22
    Antoniomouth        22
    South Roy           22
    East Douglas        22
    Port Josephfurt     22
    New Christine       22
    Lake Stevenbury     21
    South Bryanstad     21
    Davidtown           21
    West Jefferyfurt    21
    Mooreview           21
    Port Martinberg     21
    Maryside            21
    Pearsonberg         20
    New Maryport        20
    Yolandafurt         20
    West Alexis         20
    Aprilchester        19
    Wiseborough         19
    Kellershire         19
    Eriktown            19
    West Sydneyhaven    18
    Vickimouth          15
    Pamelahaven         15
    Name: city, Length: 66, dtype: int64




```python
urban_sum = merge_pyber[merge_pyber['type']=='Urban']['fare'].sum()
avg_urban = pyber_gcity['fare'].sum() / urban_city
avg_urban = avg_urban.dropna()
```




    Alvarezhaven         23.928710
    Alyssaberg           20.609615
    Antoniomouth         23.625000
    Aprilchester         21.981579
    Arnoldview           25.106452
    Carrollfort          25.395517
    Davidtown            22.978095
    Davistown            21.497200
    East Douglas         26.169091
    East Erin            24.478214
    Edwardsbury          26.876667
    Eriktown             25.478947
    Fosterside           23.034583
    Jacobfort            24.779355
    Kellershire          24.169474
    Kelseyland           21.806429
    Kimberlychester      22.947037
    Lake Jeffreyland     27.334800
    Lake Jennaton        25.349600
    Lake Sarashire       26.610000
    Lake Stevenbury      24.657619
    Lisatown             22.225217
    Lisaville            28.428929
    Maryside             26.844286
    Mooreview            29.520476
    New Aaron            26.861818
    New Andreamouth      24.966786
    New Christine        24.157727
    New David            27.084286
    New Jeffrey          24.130000
                           ...    
    Port Martinberg      22.329524
    Port Samantha        27.047407
    Prattfurt            23.346667
    Rodriguezburgh       21.332609
    Russellport          22.486087
    Sandymouth           23.105926
    Sarabury             23.490000
    Smithhaven           22.788889
    South Bryanstad      24.598571
    South Josephville    26.823750
    South Louis          27.087500
    South Roy            26.031364
    Spencertown          23.681154
    Stewartview          21.614000
    Swansonbury          27.464706
    Torresshire          24.207308
    Travisville          27.220870
    Vickimouth           21.474667
    West Alexis          19.523000
    West Brandy          24.157667
    West Brittanyton     25.436250
    West Dawnfurt        22.330345
    West Jefferyfurt     21.072857
    West Oscar           24.280000
    West Peter           24.875484
    West Sydneyhaven     22.368333
    Williamshire         26.990323
    Wiseborough          22.676842
    Yolandafurt          27.205500
    Zimmermanmouth       28.301667
    Length: 66, dtype: float64




```python
urban_dcount = pyber_city_df[pyber_city_df['type']=='Urban']
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
      <th>city</th>
      <th>driver_count</th>
      <th>type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Kelseyland</td>
      <td>63</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Nguyenbury</td>
      <td>8</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>2</th>
      <td>East Douglas</td>
      <td>12</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>3</th>
      <td>West Dawnfurt</td>
      <td>34</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Rodriguezburgh</td>
      <td>52</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>5</th>
      <td>South Josephville</td>
      <td>4</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>6</th>
      <td>West Sydneyhaven</td>
      <td>70</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Travisville</td>
      <td>37</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Torresshire</td>
      <td>70</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Lisaville</td>
      <td>66</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Mooreview</td>
      <td>34</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Smithhaven</td>
      <td>67</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Carrollfort</td>
      <td>55</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Port Josephfurt</td>
      <td>28</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Lake Jeffreyland</td>
      <td>15</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>15</th>
      <td>South Louis</td>
      <td>12</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>16</th>
      <td>West Peter</td>
      <td>61</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>17</th>
      <td>Kimberlychester</td>
      <td>13</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>18</th>
      <td>Alyssaberg</td>
      <td>67</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>19</th>
      <td>Sarabury</td>
      <td>46</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>20</th>
      <td>Yolandafurt</td>
      <td>7</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>21</th>
      <td>Edwardsbury</td>
      <td>11</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>22</th>
      <td>New Andreamouth</td>
      <td>42</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>23</th>
      <td>New David</td>
      <td>31</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>24</th>
      <td>Arnoldview</td>
      <td>41</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>25</th>
      <td>Williamshire</td>
      <td>70</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>26</th>
      <td>Lisatown</td>
      <td>47</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>27</th>
      <td>New Aaron</td>
      <td>60</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>28</th>
      <td>Swansonbury</td>
      <td>64</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>29</th>
      <td>Fosterside</td>
      <td>69</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>36</th>
      <td>Spencertown</td>
      <td>68</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>37</th>
      <td>Russellport</td>
      <td>9</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>38</th>
      <td>Maryside</td>
      <td>20</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>39</th>
      <td>West Alexis</td>
      <td>47</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>40</th>
      <td>Port Samantha</td>
      <td>55</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>41</th>
      <td>Eriktown</td>
      <td>15</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>42</th>
      <td>Pamelahaven</td>
      <td>30</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Aprilchester</td>
      <td>49</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>44</th>
      <td>South Roy</td>
      <td>35</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>45</th>
      <td>Pearsonberg</td>
      <td>43</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>46</th>
      <td>Sandymouth</td>
      <td>11</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>47</th>
      <td>East Erin</td>
      <td>43</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>48</th>
      <td>Port Johnstad</td>
      <td>22</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>49</th>
      <td>Vickimouth</td>
      <td>13</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>50</th>
      <td>Jacobfort</td>
      <td>52</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>51</th>
      <td>South Bryanstad</td>
      <td>73</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>52</th>
      <td>West Oscar</td>
      <td>11</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>53</th>
      <td>Antoniomouth</td>
      <td>21</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>54</th>
      <td>Stewartview</td>
      <td>49</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>55</th>
      <td>West Brandy</td>
      <td>12</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>56</th>
      <td>Davidtown</td>
      <td>73</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>57</th>
      <td>Kellershire</td>
      <td>51</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>58</th>
      <td>Zimmermanmouth</td>
      <td>45</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>59</th>
      <td>Port Martinberg</td>
      <td>44</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>60</th>
      <td>Lake Sarashire</td>
      <td>8</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>61</th>
      <td>Prattfurt</td>
      <td>43</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>62</th>
      <td>Davistown</td>
      <td>25</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>63</th>
      <td>West Jefferyfurt</td>
      <td>65</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>64</th>
      <td>Lake Jennaton</td>
      <td>65</td>
      <td>Urban</td>
    </tr>
    <tr>
      <th>65</th>
      <td>Alvarezhaven</td>
      <td>21</td>
      <td>Urban</td>
    </tr>
  </tbody>
</table>
<p>66 rows × 3 columns</p>
</div>




```python
rural_city = merge_pyber[merge_pyber['type']=='Rural']['city'].value_counts()
rural_sum = merge_pyber[merge_pyber['type']=='Rural']['fare'].sum()
avg_rural = pyber_gcity['fare'].sum() / rural_city
avg_rural = avg_rural.dropna()
rural_dcount = pyber_city_df[pyber_city_df['type']=='Rural']
rural_dcount
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
      <th>city</th>
      <th>driver_count</th>
      <th>type</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>108</th>
      <td>South Elizabethmouth</td>
      <td>3</td>
      <td>Rural</td>
    </tr>
    <tr>
      <th>109</th>
      <td>East Troybury</td>
      <td>3</td>
      <td>Rural</td>
    </tr>
    <tr>
      <th>110</th>
      <td>Kinghaven</td>
      <td>3</td>
      <td>Rural</td>
    </tr>
    <tr>
      <th>111</th>
      <td>New Johnbury</td>
      <td>6</td>
      <td>Rural</td>
    </tr>
    <tr>
      <th>112</th>
      <td>Erikport</td>
      <td>3</td>
      <td>Rural</td>
    </tr>
    <tr>
      <th>113</th>
      <td>Jacksonfort</td>
      <td>6</td>
      <td>Rural</td>
    </tr>
    <tr>
      <th>114</th>
      <td>Shelbyhaven</td>
      <td>9</td>
      <td>Rural</td>
    </tr>
    <tr>
      <th>115</th>
      <td>Matthewside</td>
      <td>4</td>
      <td>Rural</td>
    </tr>
    <tr>
      <th>116</th>
      <td>Kennethburgh</td>
      <td>3</td>
      <td>Rural</td>
    </tr>
    <tr>
      <th>117</th>
      <td>South Joseph</td>
      <td>3</td>
      <td>Rural</td>
    </tr>
    <tr>
      <th>118</th>
      <td>Manuelchester</td>
      <td>7</td>
      <td>Rural</td>
    </tr>
    <tr>
      <th>119</th>
      <td>Stevensport</td>
      <td>6</td>
      <td>Rural</td>
    </tr>
    <tr>
      <th>120</th>
      <td>North Whitney</td>
      <td>10</td>
      <td>Rural</td>
    </tr>
    <tr>
      <th>121</th>
      <td>East Stephen</td>
      <td>6</td>
      <td>Rural</td>
    </tr>
    <tr>
      <th>122</th>
      <td>East Leslie</td>
      <td>9</td>
      <td>Rural</td>
    </tr>
    <tr>
      <th>123</th>
      <td>Hernandezshire</td>
      <td>10</td>
      <td>Rural</td>
    </tr>
    <tr>
      <th>124</th>
      <td>Horneland</td>
      <td>8</td>
      <td>Rural</td>
    </tr>
    <tr>
      <th>125</th>
      <td>West Kevintown</td>
      <td>5</td>
      <td>Rural</td>
    </tr>
  </tbody>
</table>
</div>




```python
merge_pyber[merge_pyber['type']=='Suburban']
sub_test = pyber_city_df[pyber_city_df['type']=='Suburban'].groupby('city')
sub_test.sum()
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
      <th>driver_count</th>
    </tr>
    <tr>
      <th>city</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Anitamouth</th>
      <td>16</td>
    </tr>
    <tr>
      <th>Campbellport</th>
      <td>26</td>
    </tr>
    <tr>
      <th>Carrollbury</th>
      <td>4</td>
    </tr>
    <tr>
      <th>Clarkstad</th>
      <td>21</td>
    </tr>
    <tr>
      <th>Conwaymouth</th>
      <td>18</td>
    </tr>
    <tr>
      <th>East Cherylfurt</th>
      <td>9</td>
    </tr>
    <tr>
      <th>East Jenniferchester</th>
      <td>22</td>
    </tr>
    <tr>
      <th>Floresberg</th>
      <td>7</td>
    </tr>
    <tr>
      <th>Jasonfort</th>
      <td>25</td>
    </tr>
    <tr>
      <th>Jeffreyton</th>
      <td>8</td>
    </tr>
    <tr>
      <th>Johnland</th>
      <td>13</td>
    </tr>
    <tr>
      <th>Kyleton</th>
      <td>12</td>
    </tr>
    <tr>
      <th>Lake Brenda</th>
      <td>24</td>
    </tr>
    <tr>
      <th>Martinmouth</th>
      <td>5</td>
    </tr>
    <tr>
      <th>New Brandonborough</th>
      <td>9</td>
    </tr>
    <tr>
      <th>New Cindyborough</th>
      <td>20</td>
    </tr>
    <tr>
      <th>New Jessicamouth</th>
      <td>22</td>
    </tr>
    <tr>
      <th>New Lynn</th>
      <td>20</td>
    </tr>
    <tr>
      <th>New Michelleberg</th>
      <td>9</td>
    </tr>
    <tr>
      <th>New Samanthaside</th>
      <td>16</td>
    </tr>
    <tr>
      <th>North Tara</th>
      <td>14</td>
    </tr>
    <tr>
      <th>North Tracyfort</th>
      <td>18</td>
    </tr>
    <tr>
      <th>Paulfort</th>
      <td>13</td>
    </tr>
    <tr>
      <th>Port Alexandria</th>
      <td>27</td>
    </tr>
    <tr>
      <th>Port Guytown</th>
      <td>26</td>
    </tr>
    <tr>
      <th>Port James</th>
      <td>18</td>
    </tr>
    <tr>
      <th>Port Jose</th>
      <td>11</td>
    </tr>
    <tr>
      <th>Port Michelleview</th>
      <td>16</td>
    </tr>
    <tr>
      <th>Rodriguezview</th>
      <td>10</td>
    </tr>
    <tr>
      <th>Sarahview</th>
      <td>18</td>
    </tr>
    <tr>
      <th>South Gracechester</th>
      <td>19</td>
    </tr>
    <tr>
      <th>South Jennifer</th>
      <td>6</td>
    </tr>
    <tr>
      <th>South Shannonborough</th>
      <td>9</td>
    </tr>
    <tr>
      <th>Thomastown</th>
      <td>1</td>
    </tr>
    <tr>
      <th>Tiffanyton</th>
      <td>21</td>
    </tr>
    <tr>
      <th>Webstertown</th>
      <td>26</td>
    </tr>
    <tr>
      <th>West Evan</th>
      <td>4</td>
    </tr>
    <tr>
      <th>West Pamelaborough</th>
      <td>27</td>
    </tr>
    <tr>
      <th>West Paulport</th>
      <td>5</td>
    </tr>
    <tr>
      <th>West Tony</th>
      <td>17</td>
    </tr>
    <tr>
      <th>Williamchester</th>
      <td>26</td>
    </tr>
  </tbody>
</table>
</div>




```python
sub_city = merge_pyber[merge_pyber['type']=='Suburban']['city'].value_counts()
sub_sum = merge_pyber[merge_pyber['type']=='Suburban']['fare'].sum()
avg_sub = pyber_gcity['fare'].sum() / sub_city
avg_sub = avg_sub.dropna()
sub_dcount = pyber_city_df[pyber_city_df['type']=='Suburban'].groupby('city')
sub_dcount['driver_count'].sum()
```




    city
    Anitamouth              16
    Campbellport            26
    Carrollbury              4
    Clarkstad               21
    Conwaymouth             18
    East Cherylfurt          9
    East Jenniferchester    22
    Floresberg               7
    Jasonfort               25
    Jeffreyton               8
    Johnland                13
    Kyleton                 12
    Lake Brenda             24
    Martinmouth              5
    New Brandonborough       9
    New Cindyborough        20
    New Jessicamouth        22
    New Lynn                20
    New Michelleberg         9
    New Samanthaside        16
    North Tara              14
    North Tracyfort         18
    Paulfort                13
    Port Alexandria         27
    Port Guytown            26
    Port James              18
    Port Jose               11
    Port Michelleview       16
    Rodriguezview           10
    Sarahview               18
    South Gracechester      19
    South Jennifer           6
    South Shannonborough     9
    Thomastown               1
    Tiffanyton              21
    Webstertown             26
    West Evan                4
    West Pamelaborough      27
    West Paulport            5
    West Tony               17
    Williamchester          26
    Name: driver_count, dtype: int64




```python
fig, ax = plt.subplots(figsize=(12,7))
ax.scatter(urban_city, avg_urban, urban_dcount['driver_count']*10, c ='red', alpha=0.6,edgecolors="grey",linewidth=2)
ax.scatter(sub_city, avg_sub, sub_dcount['driver_count'].sum()*10, c = 'blue', alpha=0.6,edgecolors="grey",linewidth=2)
ax.scatter(rural_city, avg_rural, rural_dcount['driver_count']*10, c = 'yellow', alpha=0.6,edgecolors="grey",linewidth=2)
ax.text(1.2,.5, "Circle size corresponds to driver count", horizontalalignment='center', verticalalignment = 'center', transform=ax.transAxes)
plt.xlim(-1,40)
plt.xlabel('Number of Rides')
plt.ylabel('Average Cost of Ride')
plt.title('Cost of Pyber Rides per city type')
plt.legend(('Urban','Suburban','Rural'),fancybox = True, markerscale = .5, scatterpoints = 1, loc='best')
```




    <matplotlib.legend.Legend at 0x1a345a13630>




```python
plt.show()
```


![png](output_15_0.png)


# Total Rides by City Type


```python
pie_data = merge_pyber['type'].value_counts()
pie_data_1 = []
pie_data_1 = [(pie_data[i]) for i in range(0,len(pie_data))]
#for i in range(3):
 #   pie_data_1.append(pie_data[i])
#pie_data = merge_pyber[['type','fare']]
#pie_data['type'].value_counts()
pie_data_1
```




    [1625, 657, 125]




```python
labels = ['Urban','Suburban','Rural']
colors = ['Lightcoral','LightBlue','Yellow']
explode = (0.1,0,0)
plt.pie(pie_data_1,explode=explode,labels=labels,colors=colors,autopct="%1.1f%%",shadow=True, startangle=140)
plt.axis('equal')
plt.title("% of Total Rides by City Type")
```




    Text(0.5,1,'% of Total Rides by City Type')




```python
plt.show()
```


![png](output_19_0.png)


# Total Fares by City Type


```python
merge_pyber = pd.merge(pyber_ride_df,pyber_city_df, on='city')
test = merge_pyber.groupby('type')
test_2 = test['fare'].sum()
fare_list = [(test_2[i]) for i in range(0,len(test_2))]
fare_list
```




    [4255.090000000002, 20335.690000000006, 40078.339999999967]




```python
labels = ['Rural','Suburban','Urban']
colors = ['Yellow','LightBlue','Lightcoral']
explode = (0,0,0.1)
plt.pie(fare_list,explode=explode,labels=labels,colors=colors,autopct="%1.1f%%",shadow=True, startangle=140)
plt.axis('equal')
plt.title("% of Total Fares by City Type")
```




    Text(0.5,1,'% of Total Fares by City Type')




```python
plt.show()
```


![png](output_23_0.png)


# Total Drivers by City Type


```python
test['driver_count'].sum()
```




    type
    Rural         727
    Suburban     9730
    Urban       64501
    Name: driver_count, dtype: int64




```python
pyber_dcount = test['driver_count'].sum()
dcount_list = [pyber_dcount[i] for i in range(0,len(pyber_dcount))]
dcount_list
```




    [727, 9730, 64501]




```python
labels = ['Rural','Suburban','Urban']
colors = ['Yellow','LightBlue','Lightcoral']
explode = (0,0,0.1)
plt.pie(dcount_list,explode=explode,labels=labels,colors=colors,autopct="%1.1f%%",shadow=True, startangle=140)
plt.axis('equal')
plt.title("% of Total Drivers by City Type")
```




    Text(0.5,1,'% of Total Drivers by City Type')




```python
plt.show()
```


![png](output_28_0.png)

