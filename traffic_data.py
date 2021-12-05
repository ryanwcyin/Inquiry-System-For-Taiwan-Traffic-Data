import pandas as pd
from dataclasses import dataclass
import streamlit as st

@dataclass
class TrafficData:
    data: pd.DataFrame

    
    @classmethod
    def from_file(cls, filepath):
        _data = pd.read_csv(filepath, header=None)
        _data.columns = ['VehicleType',
                    'DerectionTime_O',
                    'GantryID_O',
                    'DerectionTime_D',
                    'GantryID_D',
                    'TripLength',
                    'TripEnd',
                    'TripInformation']
        return cls(_data)