import codecademylib3
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head())

utm_source_users = ad_clicks.groupby('utm_source').user_id.count().reset_index()
#print(utm_source_users)

ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
#print(ad_clicks)

clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
clicks_pivot = clicks_by_source.pivot(
  columns = 'is_click',
  index = 'utm_source',
  values = 'user_id'
).reset_index()
print(clicks_by_source)


clicks_pivot['percent_clicked'] = round((clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False]) * 100), 1)
print(clicks_pivot)

experimental_clicks = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
print(experimental_clicks)

percentage_clicks = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index().pivot(
  columns = 'is_click',
  index = 'experimental_group',
  values = 'user_id'
).reset_index()
print(percentage_clicks)
percentage_clicks['Percentge'] = round((percentage_clicks[True] / (percentage_clicks[True] + percentage_clicks[False]) * 100), 1)
print(percentage_clicks)

a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
print(a_clicks)
percent_byday_a = a_clicks.groupby(['is_click', 'day']).user_id.count().reset_index().pivot(
  columns = 'is_click',
  index = 'day',
  values = 'user_id'
).reset_index()
percent_byday_a['Percent'] = round((percent_byday_a[True] / (percent_byday_a[True] + percent_byday_a[False]) * 100), 1)
print(percent_byday_a)

b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']
percent_byday_b = b_clicks.groupby(['is_click', 'day']).user_id.count().reset_index().pivot(
  columns = 'is_click',
  index = 'day',
  values = 'user_id'
).reset_index()
percent_byday_b['Percent'] = round((percent_byday_b[True] / (percent_byday_b[True] + percent_byday_b[False]) * 100), 1)
print(percent_byday_b)


