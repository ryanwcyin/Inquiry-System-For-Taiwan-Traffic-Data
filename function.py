import pandas as pd


# def read_default_dataset(filepath=r'project2\Inquiry-System-For-Taiwan-Traffic-Data-master\data\default.csv'):
#     df = pd.read_csv(filepath, header=None)
#     df.columns = ['VehicleType',
#                   'DerectionTime_O',
#                   'GantryID_O',
#                   'DerectionTime_D',
#                   'GantryID_D',
#                   'TripLength',
#                   'TripEnd',
#                   'TripInformation']
#     return df

# traffic_df = read_default_dataset()

class TrafficDataHandler:
    def search(self, df, column, keyword):
        r = df[df[column].isin([keyword])]
        if r.empty:
            return df[df[column].astype(str).str.contains(keyword)]
        return r

    def sort(self, df, column, way, num):
        if way == 'ascending':
            acd = True
        elif way == 'non-ascending':
            acd = False
        return df.sort_values(by=[column], ascending=acd)[:num]
    # print(search(traffic_df, 'VehicleType', 31))