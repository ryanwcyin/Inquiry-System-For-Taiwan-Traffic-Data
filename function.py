import pandas as pd


class TrafficDataHandler:
    def search(self, df, column, keyword):
        r = df[df[column].isin([keyword])]
        if r.empty:
            return df[df[column].astype(str).str.contains(keyword)]
        return r

    def sort(self, df, column, way, num):
        if way == 'ascending':
            acd = True
        elif way == 'descending':
            acd = False
        return df.sort_values(by=[column], ascending=acd)[:num]
