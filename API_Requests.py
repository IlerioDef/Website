import requests

test_url = "http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=02/03/2001&date_req2=14/03/2001&VAL_NM_RQ=R01235"
"""date_req1 = period starting date
date_trq2 = period ending date
VAL_NM_RQ = unique currency code used by Central Bank
"""
cbr = requests.get(test_url)
print(cbr)
