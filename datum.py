from datetime import date

print(["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"][date(2009,*[int(i)for i in input().split()][::-1]).isoweekday()-1])
