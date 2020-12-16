def add_time(starttime, periodlonger, day=False):

  hr , min , ampm = starttime.replace(':',' ').split() 

  hrext , minext  = periodlonger.split(':')  

  newmin  = int(min ) + int(minext )
    
  newhr=(int(min )//60) + (int(minext )//60)+int(hr ) + int(hrext)   

  if newmin >=60:     
    newhr += 1
    newmin -= 60
  if newmin<60:
    if newmin < 10:
      newmin = '0' + str(newmin)         
    else:
      newmin = str(newmin)  
   
  hrmix = newhr
  finalampm = int()
  startampm = ampm
   

  while newhr >= 13:
     newhr -= 12    
  
  while hrmix >= 12: 
    if ampm == "AM": 
      ampm=  "PM"
    elif ampm=="PM":
      ampm=  "AM"
    finalampm += 1
    hrmix -= 12

  if finalampm % 2 != 0:
    if startampm == "AM":
      finalampm -= 1
    elif startampm == "PM":
      finalampm += 1
   
  finalday =int( finalampm / 2)

  finalresult = f"{str(newhr)}:{str(newmin)} {ampm}"

  days = ["Saturday","Sunday","Monday",    "Tuesday","Wednesday","Thursday","Friday"]

  if day != False :         
    finalresult += f", {days[(int(((days.index(day.title())) + finalday) % 7))]}"

  if finalday<1:
    pass
  elif finalday ==1:
    finalresult += " (next day)"   
  else:
    finalresult += f" ({int(finalday)} days later)"

  return finalresult

  #reference:   https://repl.it/@BeauCarnes/fcc-time-calculator#time_calculator.pyc