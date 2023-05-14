from django.shortcuts import render, redirect
import requests
from datetime import datetime
# Create your views here.
from django.http import JsonResponse

_30stock = ['ACB', 'BID', 'BVH', 'CTG', 'DHG', 'DPM', 'EIB', 'FPT', 'GAS', 'GMD', 'HDB', 'HPG', 'MBB', 'MSN', 'MWG', 'NVL', 'PNJ', 'REE', 'ROS', 'SAB', 'SBT', 'SSI', 'STB', 'TCB', 'TPB', 'VCB', 'VHM', 'VIC', 'VJC', 'VPB']
API = "https://finfo-api.vndirect.com.vn/v4/stock_prices/"

def get_stock(request, stock):
  query = 'code:' + stock
  params = {
            "sort": "date",
            "size": request.GET['size'],
            # "page": 1,
            "q": query
        }
  headers = {
      'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
      'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36 Edg/112.0.1722.34',
  }
  # res = requests.get("https://finfo-api.vndirect.com.vn/v4/stock_prices?sort=date&size=1500&q=code:SSI~date:gte:2021-08-20" , headers = headers)
  res = requests.get(API , params = params , headers = headers)
  data = (res.json())['data']
  index = len(data)
  for item in data:
    date_time_str = item['date'] + ' ' + item['time']
    date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')
    item['timestamp'] = date_time_obj.timestamp()
    item['index'] = index 
    index = index -1
  sorted_timestamp = sorted(data, key=lambda x: x['timestamp'])
  # for i in sorted_timestamp:
  #   print(i['date'], i['time'], i['timestamp'])
  return JsonResponse({'data' : sorted_timestamp})


from django.contrib.auth.decorators import login_required
@login_required
def dashboard(request):
  return render(request , 'home/dashboard.html' , context={'user' : request.user.username})

