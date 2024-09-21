from django.http import HttpResponse
from django.shortcuts import render

def members(request):
    return render(request, 'index.html')

def Analyzer(request):
     #  get the text
     djtext=request.POST.get('text', 'default')
     remove=request.POST.get('removepu', 'off')
     capletter=request.POST.get('uppercase', 'off')
     newlineremover=request.POST.get('newlineremover', 'off')
     extra=request.POST.get('extra', 'off')
     char_counter=request.POST.get('char_counter', 'off')
     Analyzed=djtext
    
     if remove == 'on':
           Punctations= '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
           remanalyzed=''
           for char in Analyzed:
               if char not in Punctations:
                  remanalyzed=remanalyzed + char
           Analyzed=remanalyzed
          
     if capletter =='on':
        capanalyzed=''
        capanalyzed=  Analyzed.upper()
        Analyzed=capanalyzed
      
     if newlineremover == 'on':
           newanalyzed=''
           for char in Analyzed:
                if  char!='\n'and char!="\r":
                  
                  newanalyzed=newanalyzed + char
                else:
                  print("no")
                  print("pre", newanalyzed)
           Analyzed=newanalyzed
     
     if extra == 'on':
           extranalyzed=''
           for index,char in  enumerate(Analyzed):
               if not(Analyzed[index]==' ' and Analyzed[index+1]==' '):
                    extranalyzed= extranalyzed+char  

           Analyzed=extranalyzed
     
     if char_counter == 'on':
           counter=0
           for char in Analyzed:
             if char != " ":
              counter=counter+1
           Analyzed=counter
           
     params={'Analyzed_text': Analyzed}
     return render(request,'Analyzer.html', params)
    
    
     
     
     
     
     
     