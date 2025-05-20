import requests

"""
url = input("Enter the url:\n")
"""
def get_proxy_s_list()
   file_name = input("Enter proxys filename: ")
   try:
      file = open(file_name, 'r')
   except:
      print("Error reading file.", end="\n")
   proxys = []
   try:
      i = 0
      for data in file.readlines():
         for line in data.split("\\n"):
            proxys.append(line.split(":"))
            print("proxy number "+str(i)+" with ip "+ip_port[0]+" port "+ip_port[1],end="")
            i++
   except:
      print("Error treating data", end="\n")
   proxys = proxys[:-1]
   return proxys

if __name__ == "__main__":
   proxys = get_proxys_list()
   selected_proxy = input("Enter the number of proxy to use: ", end="\n")
   proxies = {
   'http': proxys[selected_proxy][0]+":"+proxys[selected_proxy][1],
   }
   url = input("Enter url whom you want to send:", end="")
   response = requests.post(url, proxies=proxies)
