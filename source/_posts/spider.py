import requests
import time
from multiprocessing.dummy import Pool

def query(url):
    requests.get(url)

start = time.time() 
for i in range(100):
    query('https://baidu.com')
end = time.time()
print(f'time = {end-start}')

# five pool
start = time.time()
url_list = []
for i in range(100):
    url_list.append('https://baidu.com')
pool = Pool(5)
pool.map(query,url_list)
end = time.time()
print(f'time2 = {end - start}')