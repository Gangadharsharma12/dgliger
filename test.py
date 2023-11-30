# d = {'selectionTreeParameter': [{'selectionTreeID': '2', 'selectionTreeVersion': 'Refill AIR period 2023091300-MNDFOffer Valid: 20230913T17:32:03+0500 Last modified: 20230923T01:36:11+0500'},{'selectionTreeID': '1','selectionTreeVersion': 'Account refill AIR period 2023091700-MNDFOffer_fix Valid: 20230917T15:10:45+0500 Last modified: 20230923T01:35:50+0500'},{'selectionTreeID': '1', 'selectionTreeVersion': 'Account division AIR period 2023071100-MVPNOoredooPrepaid5G Valid: 20230711T18:36:06+0500 Last modified: 20230923T01:35:37+0500'}]}
# print(d['selectionTreeParameter'][0]["selectionTreeID"])

file = ('refillRecordV2', {'originNodeType': 'EXT', 'originHostName': 'ETOPUP', 'originTransactionID': '177370341', 'originTimeStamp': '20231005105131+0500', 'hostName': 'phm1svewvmair1', 'localSequenceNumber': 515384, 'timeStamp': '20231005105132+0500', 'currentServiceClass': 1002, 'voucherBasedRefill': False, 'transactionAmount': '23.150000', 'transactionCurrency': 'MVR', 'refillDivisionAmount': '-5.000000', 'refillType': 2, 'refillProfileID': 'AA', 'segmentationID': 'AA', 'accountNumber': '9609325548', 'accountCurrency': 'MVR', 'subscriberNumber': '9609325548', 'accountInformationBeforeRefill': {'accountFlags': '10000000', 'accountBalance': '0.010000', 'creditClearancePeriod': 20, 'dedicatedAccounts': [{'dedicatedAccountID': 250, 'accountBalance': '5.000000', 'dedicatedAccountUnit': 1}, {'dedicatedAccountID': 1, 'accountExpiryDate': '20231030', 'dedicatedAccountUnit': 5, 'unitBalance': '7'}], 'permanentServiceClass': 1002, 'serviceFeeExpiryDate': '20231216', 'serviceRemovalGracePeriod': 180, 'serviceOffering': 0, 'supervisionExpiryDate': '20231126', 'usageAccumulator': [{'usageAccumulatorID': 2, 'usageAccumulatorValue': 0}, {'usageAccumulatorID': 7, 'usageAccumulatorValue': 0}, {'usageAccumulatorID': 20, 'usageAccumulatorValue': 0}, {'usageAccumulatorID': 21, 'usageAccumulatorValue': 0}], 'offers': [{'offerIdentifier': 1160, 'offerType': 'timer'}, {'offerIdentifier': 1163, 'offerType': 'timer'}, {'offerIdentifier': 1163, 'offerType': 'timer'}, {'offerIdentifier': 1163, 'offerType': 'timer'}, {'offerIdentifier': 1163, 'offerType': 'timer'}]}, 'accountInformationAfterRefill': {'accountFlags': '10000000', 'accountBalance': '18.160000', 'creditClearancePeriod': 20, 'dedicatedAccounts': [{'dedicatedAccountID': 250, 'refillDivisionAmount': '-5.000000', 'accountBalance': '0.000000', 'dedicatedAccountUnit': 1}, {'dedicatedAccountID': 1, 'accountExpiryDate': '20231104', 'dedicatedAccountUnit': 5, 'refillDivisionUnits': '5', 'unitBalance': '12'}], 'permanentServiceClass': 1002, 'serviceFeeExpiryDate': '20231216', 'serviceRemovalGracePeriod': 180, 'serviceOffering': 0, 'supervisionExpiryDate': '20231126', 'usageAccumulator': [{'usageAccumulatorID': 2, 'usageAccumulatorValue': 0}, {'usageAccumulatorID': 7, 'usageAccumulatorValue': 0}, {'usageAccumulatorID': 20, 'usageAccumulatorValue': 0}, {'usageAccumulatorID': 21, 'usageAccumulatorValue': 0}], 'offers': [{'offerIdentifier': 1160, 'offerType': 'timer'}, {'offerIdentifier': 1163, 'offerType': 'timer'}, {'offerIdentifier': 1163, 'offerType': 'timer'}, {'offerIdentifier': 1163, 'offerType': 'timer'}, {'offerIdentifier': 1163, 'offerType': 'timer'}]}, 'maximumServiceFeePeriod': 385, 'maximumSupervisionPeriod': 365, 'activationDate': '20220529', 'welcomeStatus': True, 'accountGroupId': 0, 'selectionTreeParameter': [{'selectionTreeID': '2', 'selectionTreeVersion': 'Refill AIR period 2023091300-MNDFOffer Valid: 20230913T17:32:03+0500 Last modified: 20230923T01:36:11+0500'}, {'selectionTreeID': '1', 'selectionTreeVersion': 'Account refill AIR period 2023091700-MNDFOffer_fix Valid: 20230917T15:10:45+0500 Last modified: 20230923T01:35:50+0500'}, {'selectionTreeID': '1', 'selectionTreeVersion': 'Account division AIR period 2023071100-MVPNOoredooPrepaid5G Valid: 20230711T18:36:06+0500 Last modified: 20230923T01:35:37+0500'}], 'treeDefinedFields': [{'parameterID': 'Reason', 'parameterValue': ('string', 'Raastas Recharge')}], 'requestedRefillType': 0})
file = file[1]

# accountInformationAfterRefill = [{'dedicatedAccountID': 250,   'refillDivisionAmount': '-5.000000',   'accountBalance': '0.000000',   'dedicatedAccountUnit': 1},  {'dedicatedAccountID': 1,   'accountExpiryDate': '20231104',   'dedicatedAccountUnit': 5,   'refillDivisionUnits': '5',   'unitBalance': '12'}]
# accountInformationBeforeRefill = [{'dedicatedAccountID': 250,  'accountBalance': '5.000000',  'dedicatedAccountUnit': 1}, {'dedicatedAccountID': 1,  'accountExpiryDate': '20231030',  'dedicatedAccountUnit': 5,  'unitBalance': '7'}]
data_After = []

for i in file['accountInformationAfterRefill']['dedicatedAccounts']:
    data_After_dict = {}
    for k, v in i.items():
        data_After_dict[f'afterReFill_{k}'] = i[k]
    data_After.append(data_After_dict)
print(data_After)
data_Before = []

for i in file['accountInformationBeforeRefill']['dedicatedAccounts']:
    data_Before_dict = {}
    for k, v in i.items():
        data_Before_dict[f'beforeReFill_{k}'] = i[k]
    data_Before.append(data_Before_dict)
print(data_Before)

detailed_account = []
for i in range(max(len(data_After), len(data_Before))):
    d = {}
    d.update(data_After[i])
    d.update(data_Before[i])
    print(d)
    detailed_account.append(d)
print(detailed_account)