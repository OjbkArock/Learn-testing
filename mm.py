# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 10:04:00 2018

@author: Arock
"""
import re
import codecs
import unicodecsv as csv
import cStringIO
class UnicodeWriter:
    def __init__(self, f, dialect=csv.excel, encoding="utf-8-sig", **kwds):
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, row):
#        print row
        self.writer.writerow([s.encode("utf-8") for s in row])
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        data = self.encoder.encode(data)
        self.stream.write(data)
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)
            
       
        
def writeTotxt(SplitSten):
#    print SplitSten
#    Sp=codecs.open("SplitWords.txt",'w','utf-8')
#    Sp.write(SplitSten)
    writer = UnicodeWriter(open("SplitWords.txt", 'wb'), delimiter=',')
    writer.writerow([SplitSten])



  #对此处进行修改      
#def listToSentence(_list):
    for i in _list:
        str=i.decode('unicode-escape')
        writeTotxt(str)
    
with open('text.txt',"r") as file:
    lines=file.readlines()
    for line in lines:
        all_uni=line.decode("gb2312")
        str=all_uni.strip()
        s_str = str.encode('unicode-escape').decode('string_escape')
        strlist=s_str.split("\u3002")
        listToSentence(strlist)
       
        
        
      
        


#strC=strA.decode("gb2312")
  
#for i in range(0,len(strC)):
#    strB=strA[0:i,2]
#    if re.compile():
#        print strB
    