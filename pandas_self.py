import pandas as pd

input = pd.read_csv('survey_data.csv')
index = []
for i in range(len(input)):
    item = input['If you are a graduate student, what was your undergraduate institution?'][i]
    if item not in index:
        index.append(item)
output = pd.DataFrame(index=index, columns=['count'])
for i in range(len(input)):
    item = input['If you are a graduate student, what was your undergraduate institution?'][i]
    if pd.notna(output.at[item, 'count']):
        output.at[item, 'count'] = output.at[item, 'count'] + 1
    else:
        output.at[item, 'count'] = 1
output = output.sort_values(by='count', ascending=True)
# save as an output csv file
output.to_csv('undergraduate_institution_count.csv')
print(output)