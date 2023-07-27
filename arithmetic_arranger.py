import re
def arithmetic_arranger(problems,solve= False):
  line1=[]
  line2=[]
  line3=[]
  line4=[]
  if len(problems)>5:
    return 'Error: Too many problems.'
  for expresion in problems:
    stringi=str(expresion)


    if(re.search("[^\s0-9.+-]", stringi)) :
      if(re.search(" [/]", stringi) or re.search("[*]", stringi)) :
        return "Error: Operator must be '+' or '-'."
      return "Error: Numbers must only contain digits."


    
    expresion = expresion.split()




    
    lst1=''
    lst0=''

    lst1=expresion[2]
    lst0=expresion[0]
    minusy=''
    if len(lst1)>4:
      return 'Error: Numbers cannot be more than four digits.'
    if len(lst0)>4:
      return 'Error: Numbers cannot be more than four digits.'
      

    
    if len(lst1)>len(expresion[0]):
      spacesnum=len(lst1)+2-len(expresion[0])      
      for i in range(spacesnum):
        lst0=' '+lst0
      line1.append(lst0)
          
      lst1=' '+lst1
      lst1=expresion[1]+lst1
      line2.append(lst1)
      
      minusy=''
      for q in range(len(lst0)):
        minusy=minusy+'-'
      line3.append(minusy)     

    
    if len(lst1)<len(expresion[0]):
      spacesnum=len(lst0)+2-len(lst1)
      lst0='  '+lst0
      line1.append(lst0)

      for w in range(spacesnum-1):
        lst1=' '+lst1
      lst1=expresion[1]+lst1
      line2.append(lst1)

      for r in range(len(lst0)):
        minusy=minusy+'-'
      #print(minusy)
      line3.append(minusy)     

    
    if len(lst1)==len(expresion[0]):
      lst0='  '+lst0
      line1.append(lst0)

      lst1=expresion[1]+' '+lst1
      line2.append(lst1)

      for u in range(len(lst0)):
        minusy=minusy+'-'
      line3.append(minusy)    
    if expresion[1]=='+':
      lst4=int(expresion[0])+int(expresion[2])
    else:
      lst4=int(expresion[0])-int(expresion[2])
    lst4=str(lst4)
    for p in range(len(minusy)-len(str(lst4))):
      lst4=' '+lst4
    line4.append(lst4)
    


  
  odp1=''
  odp2=''
  odp3=''
  odp4=''
  
  
  for num in line1:
    odp1=odp1+num+'    '

  odp1=odp1[0:-4]
 # print(odp1)

  for num2 in line2:
    odp2=odp2+num2+'    '

  odp2=odp2[0:-4]
 # print(odp2)

  for num3 in line3:
    odp3=odp3+num3+'    '

  odp3=odp3[0:-4]
 # print(odp3)
  for num4 in line4:
    odp4=odp4+num4+'    '

  odp4=odp4[0:-4]
  print(odp4)
  
  if solve:

    odpowiedz=odp1+'\n'+odp2+'\n'+odp3+'\n'+odp4


  else:
    odpowiedz=odp1+'\n'+odp2+'\n'+odp3
  
  
  
  
  return odpowiedz
  