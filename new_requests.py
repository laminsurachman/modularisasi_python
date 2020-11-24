import requests
url = 'https://detik.com'
try:
     response = requests.get(url)
     if response.status_code ==200:
         print(f'success!{response.status_code}')
         print(f'content{response.text}')
     else:
         print(f'woops,ada kesalahan {response.status_code}')


except Exception as e:
        print('there is an error',e)
print('Program ended')