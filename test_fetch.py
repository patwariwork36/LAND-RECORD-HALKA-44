import urllib.request
import time
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vTbjfinOHxrL4cMudTQs4lw3xCBHJzSQ_fURjbGD2QhSnvBbcpoHN2KiIgWamJCHmDtkxCuQaOyHyej/pub?gid=1125745063&single=true&output=csv&t=123"

start = time.time()
req = urllib.request.Request(url)
req.add_header('User-Agent', 'Mozilla/5.0')
try:
    response = urllib.request.urlopen(req)
    data = response.read()
    print(f"Success! {len(data)} bytes downloaded in {time.time()-start:.2f}s")
    print(data[:100])
except Exception as e:
    print("Error:", e)
