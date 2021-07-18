admin = "http://18.118.11.105:8000"
main = "http://3.22.27.157:8001"

import requests
 
for i in range(2):
    r = requests.post(admin+"/api/products",data={'title': 'new'+str(i), 'image':'new image'+str(i)})


