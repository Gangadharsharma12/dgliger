# d = ('refillRecordV2', {'originNodeType': 'EXT', 'originHostName': 'ETOPUP', 'originTransactionID': '177370341', 'originTimeStamp': '20231005105131+0500', 'hostName': 'phm1svewvmair1', 'localSequenceNumber': 515384, 'timeStamp': '20231005105132+0500', 'currentServiceClass': 1002, 'voucherBasedRefill': False, 'transactionAmount': '23.150000', 'transactionCurrency': 'MVR', 'refillDivisionAmount': '-5.000000', 'refillType': 2, 'refillProfileID': 'AA', 'segmentationID': 'AA', 'accountNumber': '9609325548', 'accountCurrency': 'MVR', 'subscriberNumber': '9609325548', 'accountInformationBeforeRefill': {'accountFlags': '10000000', 'accountBalance': '0.010000', 'creditClearancePeriod': 20, 'dedicatedAccounts': [{'dedicatedAccountID': 250, 'accountBalance': '5.000000', 'dedicatedAccountUnit': 1}, {'dedicatedAccountID': 1, 'accountExpiryDate': '20231030', 'dedicatedAccountUnit': 5, 'unitBalance': '7'}], 'permanentServiceClass': 1002, 'serviceFeeExpiryDate': '20231216', 'serviceRemovalGracePeriod': 180, 'serviceOffering': 0, 'supervisionExpiryDate': '20231126', 'usageAccumulator': [{'usageAccumulatorID': 2, 'usageAccumulatorValue': 0}, {'usageAccumulatorID': 7, 'usageAccumulatorValue': 0}, {'usageAccumulatorID': 20, 'usageAccumulatorValue': 0}, {'usageAccumulatorID': 21, 'usageAccumulatorValue': 0}], 'offers': [{'offerIdentifier': 1160, 'offerType': 'timer'}, {'offerIdentifier': 1163, 'offerType': 'timer'}, {'offerIdentifier': 1163, 'offerType': 'timer'}, {'offerIdentifier': 1163, 'offerType': 'timer'}, {'offerIdentifier': 1163, 'offerType': 'timer'}]}, 'accountInformationAfterRefill': {'accountFlags': '10000000', 'accountBalance': '18.160000', 'creditClearancePeriod': 20, 'dedicatedAccounts': [{'dedicatedAccountID': 250, 'refillDivisionAmount': '-5.000000', 'accountBalance': '0.000000', 'dedicatedAccountUnit': 1}, {'dedicatedAccountID': 1, 'accountExpiryDate': '20231104', 'dedicatedAccountUnit': 5, 'refillDivisionUnits': '5', 'unitBalance': '12'}], 'permanentServiceClass': 1002, 'serviceFeeExpiryDate': '20231216', 'serviceRemovalGracePeriod': 180, 'serviceOffering': 0, 'supervisionExpiryDate': '20231126', 'usageAccumulator': [{'usageAccumulatorID': 2, 'usageAccumulatorValue': 0}, {'usageAccumulatorID': 7, 'usageAccumulatorValue': 0}, {'usageAccumulatorID': 20, 'usageAccumulatorValue': 0}, {'usageAccumulatorID': 21, 'usageAccumulatorValue': 0}], 'offers': [{'offerIdentifier': 1160, 'offerType': 'timer'}, {'offerIdentifier': 1163, 'offerType': 'timer'}, {'offerIdentifier': 1163, 'offerType': 'timer'}, {'offerIdentifier': 1163, 'offerType': 'timer'}, {'offerIdentifier': 1163, 'offerType': 'timer'}]}, 'maximumServiceFeePeriod': 385, 'maximumSupervisionPeriod': 365, 'activationDate': '20220529', 'welcomeStatus': True, 'accountGroupId': 0, 'selectionTreeParameter': [{'selectionTreeID': '2', 'selectionTreeVersion': 'Refill AIR period 2023091300-MNDFOffer Valid: 20230913T17:32:03+0500 Last modified: 20230923T01:36:11+0500'}, {'selectionTreeID': '1', 'selectionTreeVersion': 'Account refill AIR period 2023091700-MNDFOffer_fix Valid: 20230917T15:10:45+0500 Last modified: 20230923T01:35:50+0500'}, {'selectionTreeID': '1', 'selectionTreeVersion': 'Account division AIR period 2023071100-MVPNOoredooPrepaid5G Valid: 20230711T18:36:06+0500 Last modified: 20230923T01:35:37+0500'}], 'treeDefinedFields': [{'parameterID': 'Reason', 'parameterValue': ('string', 'Raastas Recharge')}], 'requestedRefillType': 0})
# d1 = d[1]
# flattened_data = {}
# for key, value in d1.items():
#     if isinstance(value, dict):
#         for sub_key, sub_value in value.items():
#             flattened_key = f"{key}_{sub_key}"
#             flattened_data[flattened_key] = sub_value
#     else:
#         flattened_data[key] = value
#
# # Print the flattened dictionary
# for key, value in flattened_data.items():
#     print(f"{key}: {value}")


# d = {'dedicatedAccounts': [{'dedicatedAccountID': 250,
#     'refillDivisionAmount': '-5.000000',
#     'accountBalance': '0.000000',
#     'dedicatedAccountUnit': 1},
#    {'dedicatedAccountID': 1,
#     'accountExpiryDate': '20231104',
#     'dedicatedAccountUnit': 5,
#     'refillDivisionUnits': '5',
#     'unitBalance': '12'}]}
#
# print(d["dedicatedAccounts"])


# def containsDuplicate(nums):
#     """
#     :type nums: List[int]
#     :rtype: bool
#     """
#     l = []
#     flag = "false"
#     for each in nums:
#         if each not in l:
#             l.append(each)
#     if l != nums:
#         print("true")
#     else:
#         print(flag)
#
#
# nums = [1, 2, 3, 1]
# containsDuplicate(nums)


import datetime, time
timestamp_print = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
print(timestamp_print)



