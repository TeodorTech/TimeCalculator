
def add_time():
 week = dict()
 times = ["11:55 PM", "500:10"]
 week = {1: "Monday" , 2:"Thuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday" , 7:"Sunday" }
#finding the day
 t1 = times[0].split()[0]
 h1 = int(t1.split(":")[0])
 m1 = int(t1.split(":")[1])
 h2 = int(times[1].split(":")[0])
 m2 = int(times[1].split(":")[1])
 a= int(h1 + h2)
 b  = int(m1 + m2)
 zone= times[0]
 area = zone.split()[1]

 x = 0
#If we have the day
 if len(times) == 3:
  for day in week:
         if times[2] == week[day]:
             d = day
             break
  if area == "PM":
     #work for PM
   while h2 >= 24:
      h2 = h2 - 24
      x = x + 1
   while a > 12:
      a = a - 12
   else:
    if b < 59:
            print(a, ":", b, "PM","(", x, "days later)")
    else:
        a = a + 1
        b = b - 60
        if a < 12:
            print(a, ":", b, "PM")
        else:
            if (d+x) <= 7:
             print(a - 12, ":", b, "AMA",week[d+x],"(",d+x,"days later)")
            else:print(a - 12, ":", b, "AMA","(",d+x,"days later)")
  else:
      #work for AM
    while h2 >= 24:
          h2 = h2 - 24
          x = x + 1
    while a > 12:
          a = a - 12
          x = x + 1
    else:
      if b < 59:
         print(a, ":", b, "AM","(", x, "days later)")
      else:
          a = a + 1
          b = b - 60
          if a < 12:
                  print(a, ":", b, "AM","(", x, "days later)")
          else:
                  print(a - 12, ":", b, "PM","(", week[x], "days later)")

# if we dobt have the day
 else:
    if len(times) == 2:
        if area == "PM":
            # work for PM
            while h2 >= 24:
                h2 = h2 - 24
                x = x + 1
            while a > 12:
                a = a - 12
            else:
                if b < 59:
                    print(a, ":", b, "PM", "(", x, "days later)")
                else:
                    a = a + 1
                    b = b - 60
                    if a < 12:
                        print(a, ":", b, "PM")
                    else:
                        print(a - 12, ":", b, "AMA","(", x, "days later)")
        else:
            # work for AM
            while h2 >= 24:
                h2 = h2 - 24
                x = x + 1
            while a > 12:
                a = a - 12
                x = x + 1
            else:
                if b < 59:
                    print(a, ":", b, "AM", "(", x, "days later)")
                else:
                    a = a + 1
                    b = b - 60
                    if a < 12:
                        print(a, ":", b, "AM", "(", x, "days later)")
                    else:
                        print(a - 12, ":", b, "PM", "(", week[x], "days later)")

add_time()