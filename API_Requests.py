import requests

test_url = "http://www.cbr.ru/scripts/XML_dynamic.asp"
payload = {"date_req1:": "01/01/2022", "date_req2": "01/01/2022", "VAL_NM_RQ": "R01235"}
"""date_req1 = period starting date
date_trq2 = period ending date
VAL_NM_RQ = unique currency code used by Central Bank
"""

cbr = requests.get(test_url, params=payload)
var = cbr.json
##### https://cbr.ru/scripts/XML_val.asp?d=0 - currency codes
print(var)
