import numpy as np

class Preprocessing:

    def __init__(self, data):
        self.data = data

    def z_score_normalizaion_set(self, data):
        mean = dict()
        std = dict()
        for column in data.columns:
            try:
                mean[column] = data[column].mean()
                std[column] = data[column].std()
                data[column] = (data[column] - mean[column]) / std[column]
            except TypeError:
                continue
        return data, mean, std

    def z_score_normalizaion(self, data, mean, std):
        for column in data.columns:
            try:
                data[column] = (data[column] - mean[column]) / std[column]
            except KeyError:
                continue
        return data

    def data_preprocess(self, data, test=False, mean=None, std=None):
        droplist = ['ekmo_number', 'life_quality_place_rating', 'ecology', 'cleanness', 'public_services',
                    'neighbourhood', 'children_places', 'sport_and_outdoor',
                    'shops_and_malls', 'public_transport', 'security', 'life_costs', 'epirank_avia', 'epirank_train',
                    'epirank_avia_cat', 'epirank_train_cat']
        """for col in data.columns:
            if data[col].isnull().sum() * 100 / len(data) > 27:
                print(col, data[col].isnull().sum() * 100 / len(data))
                del data[col]"""
        data = data.drop(droplist, axis='columns')
        if test == False:
            rows_and_nan = np.array(data.isnull().sum(axis=1))
            index_to_drop = []
            for i in range(len(rows_and_nan)):
                if rows_and_nan[i] > 20:
                    index_to_drop.append(i)
            data = data.drop(data.index[index_to_drop])
            data = data.reset_index()
            data = data.drop(['Unnamed: 0'], axis='columns')
            del data['index']
        else:
            data = data.drop(['inf_rate'], axis='columns')
            data.index = data['Unnamed: 0']
            data = data.drop(['Unnamed: 0'], axis='columns')
        data.fillna(data.mean(), inplace=True)

        data1 = data.copy()
        urban50over_share = data1['urban_50-54_years'] + data1['urban_55-59_years'] + data1['urban_60-64_years'] + \
                            data1['urban_65-69_years']
        urban50over_share += data1['urban_70-74_years'] + data1['urban_75-79_years'] + data1['urban_80-84_years'] + \
                             data1['urban_85-89_years'] + data1['urban_90-94_years']
        urban50over_share /= data1['urban']
        data1.insert(len(data1.columns), 'urban50over_share', urban50over_share, False)
        data1.insert(len(data1.columns), 'tubercul_share',
                     data1['num_patients_tubercul_2017'] / data1['whole_population'], False)

        droplist0 = ['urban_50-54_years', 'urban_55-59_years', 'urban_60-64_years', 'urban_65-69_years',
                     'urban_70-74_years', 'urban_75-79_years',
                     'urban_80-84_years', 'urban_85-89_years', 'urban_90-94_years', 'rural_50-54_years',
                     'rural_55-59_years', 'rural_60-64_years',
                     'rural_65-69_years', 'rural_70-74_years', 'rural_75-79_years', 'rural_80-84_years',
                     'rural_85-89_years', 'rural_90-94_years', 'num_patients_tubercul_1992',
                     'num_patients_tubercul_1993', 'num_patients_tubercul_1994', 'num_patients_tubercul_1995',
                     'num_patients_tubercul_1996',
                     'num_patients_tubercul_1997', 'num_patients_tubercul_1998', 'num_patients_tubercul_1999',
                     'num_patients_tubercul_2000',
                     'num_patients_tubercul_2001', 'num_patients_tubercul_2002', 'num_patients_tubercul_2003',
                     'num_patients_tubercul_2004',
                     'num_patients_tubercul_2005', 'num_patients_tubercul_2006', 'num_patients_tubercul_2007',
                     'num_patients_tubercul_2008',
                     'num_patients_tubercul_2009', 'num_patients_tubercul_2010', 'num_patients_tubercul_2011',
                     'num_patients_tubercul_2012',
                     'num_patients_tubercul_2013', 'num_patients_tubercul_2014', 'num_patients_tubercul_2015',
                     'num_patients_tubercul_2016', 'num_patients_tubercul_2017',
                     'name', 'district', 'subject', 'name', 'district', 'avg_temp_min', 'avg_temp_max', 'avg_temp_std',
                     'humidity_min', 'humidity_max', 'humidity_std',
                     'pressure_min', 'pressure_max', 'pressure_std', 'wind_speed_ms_min', 'wind_speed_ms_max',
                     'wind_speed_ms_std',
                     'epirank_bus_cat', 'ivl_number', 'ekmo_per_100k', 'volume_serv_transport_2017',
                     'volume_serv_post_2017', 'volume_serv_telecom_2017', 'volume_serv_others_2017',
                     'volume_serv_veterinary_2017', 'volume_serv_housing_2017', 'volume_serv_education_2017',
                     'rural', 'num_phones_rural_2018', 'work_ratio_55-64_years', 'work_ratio_15-64_years',
                     'work_ratio_25-54_years', 'volume_serv_culture_2017',
                     'bus_april_travel_18', 'num_phones_urban_2019', 'lat', 'lng']
        data1 = data1.drop(droplist0, axis='columns')

        data1['urban'] = data1['urban'] / data1['whole_population']

        services = ['volume_serv_chargeable_2017', 'volume_serv_accommodation_2017',
                    'volume_serv_medicine_2017', 'volume_serv_disabled_2017',
                    'volume_serv_sport_2017', 'volume_serv_hotels_2017', 'volume_serv_tourism_2017',
                    'volume_serv_sanatorium_2017']

        for i in services:
            data1[i] /= data1['whole_population']

        if test:
            X = self.z_score_normalizaion(data1, mean, std)
            return X
        else:
            y = data1['inf_rate']
            X = data1.drop(['inf_rate'], axis='columns')
            X, mean, std = self.z_score_normalizaion_set(X)
            return y, X, mean, std


