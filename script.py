# import subprocess
# import pyspark
# import os
# import datetime
# import logging
# import traceback
# from pyspark.sql import SparkSession
# from pyspark.sql.functions import lit
#
# # # log_filename = "raw_load_" + datetime.datetime.now().strftime("%Y-%m-%d") + ".log"
# # # log_file = os.path.join("/var/landing/dwh/temp-dir/oracle_load_raw_log_files/", log_filename)
# # # logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s\n")
# #
# spark = SparkSession.builder.master("local[1]") \
#                     .appName('dwh_etl') \
#                     .getOrCreate()
# spark.sparkContext.setLogLevel("WARN")
# user = "dwhcloud"
# password = "Sdfus#482"
# server = "10.10.93.94"
# port = 1521
# service_name = 'DWH.OOREDOO.MV'
# jdbcUrl = f"jdbc:oracle:thin:@{server}:{port}/{service_name}"
# jdbcDriver = "oracle.jdbc.driver.OracleDriver"
# # # timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S.%f")
# # # path = '/var/landing/dwh/temp-dir/output/'
# #
# #
# df = spark.read.option('header', True).csv("C:/Users/DammannagariGangadha/Desktop/new/meta.csv")
# df = df.where("is_active == 1")
# meta_df = df.toPandas()
#
# for index, row in meta_df.iterrows():
#     table_name = row['source_tablename']
#     query = row['query']
#     file_path = row['landing_path'].strip()
#     adls_path = row['adls_path'].strip()
#     query = query.replace("|", ",")
#     print(f"Query Execute Started for {table_name}")
#     logging.info(f"Query Execute Started for {table_name}\n")
#     query_start_time = datetime.datetime.now()
#
#     try:
#         df = spark.read.format("jdbc") \
#             .option("url", jdbcUrl) \
#             .option("query", query) \
#             .option("user", user) \
#             .option("password", password) \
#             .option("driver", jdbcDriver) \
#             .load()
#
#
#
#
#
#
# def flatten_dict(dd, separator='_', prefix=''):
#     print(dd)
#     res = {}
#     for key, value in dd.items():
#         print(key, ':', value)
#         if isinstance(value, dict):
#             res.update(flatten_dict(value, separator, prefix + key + separator))
#         else:
#             res[prefix + key] = value
#             print(res)
#             print("\n")
#     return res
#
#
# nested_dict = {'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}
# d = flatten_dict(nested_dict)
# print(d)

# file = ('refillRecordV2', {'originNodeType': 'EXT', 'originHostName': 'ETOPUP', 'originTransactionID': '177370341', 'originTimeStamp': '20231005105131+0500', 'hostName': 'phm1svewvmair1', 'localSequenceNumber': 515384, 'timeStamp': '20231005105132+0500', 'currentServiceClass': 1002, 'voucherBasedRefill': False, 'transactionAmount': '23.150000', 'transactionCurrency': 'MVR', 'refillDivisionAmount': '-5.000000', 'refillType': 2, 'refillProfileID': 'AA', 'segmentationID': 'AA', 'accountNumber': '9609325548', 'accountCurrency': 'MVR', 'subscriberNumber': '9609325548', 'accountInformationBeforeRefill': {'accountFlags': '10000000', 'accountBalance': '0.010000', 'creditClearancePeriod': 20, 'dedicatedAccounts': [{'dedicatedAccountID': 250, 'accountBalance': '5.000000', 'dedicatedAccountUnit': 1}, {'dedicatedAccountID': 1, 'accountExpiryDate': '20231030', 'dedicatedAccountUnit': 5, 'unitBalance': '7'}], 'permanentServiceClass': 1002, 'serviceFeeExpiryDate': '20231216', 'serviceRemovalGracePeriod': 180, 'serviceOffering': 0, 'supervisionExpiryDate': '20231126', 'usageAccumulator': [{'usageAccumulatorID': 2, 'usageAccumulatorValue': 0}, {'usageAccumulatorID': 7, 'usageAccumulatorValue': 0}, {'usageAccumulatorID': 20, 'usageAccumulatorValue': 0}, {'usageAccumulatorID': 21, 'usageAccumulatorValue': 0}], 'offers': [{'offerIdentifier': 1160, 'offerType': 'timer'}, {'offerIdentifier': 1163, 'offerType': 'timer'}, {'offerIdentifier': 1163, 'offerType': 'timer'}, {'offerIdentifier': 1163, 'offerType': 'timer'}, {'offerIdentifier': 1163, 'offerType': 'timer'}]}, 'accountInformationAfterRefill': {'accountFlags': '10000000', 'accountBalance': '18.160000', 'creditClearancePeriod': 20, 'dedicatedAccounts': [{'dedicatedAccountID': 250, 'refillDivisionAmount': '-5.000000', 'accountBalance': '0.000000', 'dedicatedAccountUnit': 1}, {'dedicatedAccountID': 1, 'accountExpiryDate': '20231104', 'dedicatedAccountUnit': 5, 'refillDivisionUnits': '5', 'unitBalance': '12'}], 'permanentServiceClass': 1002, 'serviceFeeExpiryDate': '20231216', 'serviceRemovalGracePeriod': 180, 'serviceOffering': 0, 'supervisionExpiryDate': '20231126', 'usageAccumulator': [{'usageAccumulatorID': 2, 'usageAccumulatorValue': 0}, {'usageAccumulatorID': 7, 'usageAccumulatorValue': 0}, {'usageAccumulatorID': 20, 'usageAccumulatorValue': 0}, {'usageAccumulatorID': 21, 'usageAccumulatorValue': 0}], 'offers': [{'offerIdentifier': 1160, 'offerType': 'timer'}, {'offerIdentifier': 1163, 'offerType': 'timer'}, {'offerIdentifier': 1163, 'offerType': 'timer'}, {'offerIdentifier': 1163, 'offerType': 'timer'}, {'offerIdentifier': 1163, 'offerType': 'timer'}]}, 'maximumServiceFeePeriod': 385, 'maximumSupervisionPeriod': 365, 'activationDate': '20220529', 'welcomeStatus': True, 'accountGroupId': 0, 'selectionTreeParameter': [{'selectionTreeID': '2', 'selectionTreeVersion': 'Refill AIR period 2023091300-MNDFOffer Valid: 20230913T17:32:03+0500 Last modified: 20230923T01:36:11+0500'}, {'selectionTreeID': '1', 'selectionTreeVersion': 'Account refill AIR period 2023091700-MNDFOffer_fix Valid: 20230917T15:10:45+0500 Last modified: 20230923T01:35:50+0500'}, {'selectionTreeID': '1', 'selectionTreeVersion': 'Account division AIR period 2023071100-MVPNOoredooPrepaid5G Valid: 20230711T18:36:06+0500 Last modified: 20230923T01:35:37+0500'}], 'treeDefinedFields': [{'parameterID': 'Reason', 'parameterValue': ('string', 'Raastas Recharge')}], 'requestedRefillType': 0})
# file = file[1]
data_After = []
d1 = {'dedicatedAccounts': [{'dedicatedAccountID': 250, 'accountBalance': '5.000000','dedicatedAccountUnit': 1}, {'dedicatedAccountID': 1,'accountExpiryDate': '20231030','dedicatedAccountUnit': 5,'unitBalance': '7'}]}
d2 = {'dedicatedAccounts': [{'dedicatedAccountID': 250,'refillDivisionAmount': '-5.000000','accountBalance': '0.000000','dedicatedAccountUnit': 1},{'dedicatedAccountID': 1,'accountExpiryDate': '20231104','dedicatedAccountUnit': 5,'refillDivisionUnits': '5', 'unitBalance': '12'}]}

for i in d1['dedicatedAccounts']:
    data_After_dict = {}
    for k, v in i.items():
        data_After_dict[f'beforeRefill_{k}'] = i[k]
    data_After.append(data_After_dict)
print(data_After)
data_Before = []

for i in d2['dedicatedAccounts']:
    data_Before_dict = {}
    for k, v in i.items():
        data_Before_dict[f'AfterRefill_{k}'] = i[k]
    data_Before.append(data_Before_dict)
print(data_Before)

