import pandas as pd

df = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth ': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']},
    index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])

print("Original DataFrame:")
print(df)

dict_data_list = list()

_ver = 'v2'
for gg, dd in df.groupby(['school_code','class']):
    print(gg, dict(zip(['school_code','class'], gg)))
    group = dict(zip(['school_code','class'], gg))

    if _ver == 'v1':
        # v1
        ocolumns_list = list()
        for _, data in dd.iterrows():
            #print(gg, _, data)
            data = data.drop(labels=['school_code','class'])
            print(gg, data.to_dict())
            ocolumns_list.append(data.to_dict())
        group['other_columns'] = ocolumns_list
    
        # v2
    elif _ver == 'v2':
        print(gg, dd)
        for _, data in dd.iterrows():
            data = data.drop(labels=['school_code','class'])
        group['other_columns'] = data.to_dict()
    
    dict_data_list.append(group)

print(dict_data_list) 
