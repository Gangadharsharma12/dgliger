# # This script is used for loading the data from oracle to parquet file
#
#
# import logging
# import os
import csv
import pandas as pd
import datetime
import time
import pyarrow as pa
import pyarrow.parquet as pq
#
#
# load_date = datetime.datetime.fromtimestamp(time.time()).strftime('%y-%m-%d')
# # print(load_date)     23-11-16
#
# # audit_path = r'C:\ADLS_DEV\audit\Prod_ref_data_load'  [path where audit logs are stored]
#
# def get_current_timestamp():
#
#     return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")



# class OracleData:
#
#     def __init__(self, user, password, host, port, service_name):
#
#         self.user = user
#
#         self.password = password
#
#         self.host = host
#
#         self.port = port
#
#         self.service_name = service_name
#
#         self.current_date = current_date
#
#         self.currentdate = currentdate
#
#         self.current_time = current_time



audit = {'load_status': 'STARTED',

                         'update_datetime': datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'),

                         'insert_timestamp': datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'),

                         "error": None}

# print(audit["update_datetime"])
# print(audit["insert_timestamp"])
current_date = (datetime.datetime.fromtimestamp(time.time()) + datetime.timedelta(minutes=30)).strftime('%Y-%m-%d')


# l = [4, 5, 8, 9, 6, 10]
# # op = [0, 2, 1, 0, 1, 1, 1]
# l1 = []
# x1 = len(l) - 1
# for x, y in enumerate(l):
#     if x != x1:
#         l1.append(l[x+1] - l[x])
# print(l1)


# Sample_List = ['abc', 'xyz', 'aba', '1221']
# c = 0
# for each in Sample_List:
#     if len(each) > 2:
#         if each[0] == each[len(each) - 1]:
#             c += 1
# print(c)

