import time
from datetime import datetime as dt

hosts_test   = "hosts"
hosts_path   = "/etc/hosts"
redirect     = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com"]

while True:
    tdy = dt.now()
    if (dt(tdy.year, tdy.month, tdy.day, 8) < dt.now() < dt(tdy.year, tdy.month, tdy.day, 18)):
        print("Working Hours...")
        with open(hosts_test, "r+") as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        print("Party Hours!!!")
        with open(hosts_test, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(5)
