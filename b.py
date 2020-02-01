from bs4 import BeautifulSoup
from bs4.builder import builder_registry
import requests
import csv

url="https://issues.apache.org/jira/browse/CAMEL-10597"
r=requests.get(url)
#soup=BeautifulSoup(r.content,"html")

#xml_doc = open('xml_doc')
#soup = BeautifulSoup(r.content, 'xml')
#soup = BeautifulSoup(xml_doc,'lxml')



doc = open('xml_file')
soup = BeautifulSoup(doc, 'lxml')
#print(soup)
print( builder_registry.lookup('html').DEFAULT_CDATA_LIST_ATTRIBUTES)



#print( builder_registry.lookup('html').DEFAULT_CDATA_LIST_ATTRIBUTES)
#print(soup.prettify())

tag = soup.title
type(tag)
print(tag)
people={}
date ={}
for i in range(1):

    typee= soup.type
    title = soup.summary
    prio = soup.priority
    resol = soup.resolution
    description = soup.status
    people[0] = soup.assignee
    detail = soup.p
    date[0] = soup.created
    date[1] = soup.updated
    date[2] = soup.resolved
    people[1]= soup.reporter
    votes = soup.votes
    watch= soup.watches

comment={}
i=0
for i in soup.find_all("comment"):
    comment[i]= i.find("p", recursive=True)
 #   print(comment[i])

################
j = 0
hints = []
hints_value = []


hints = soup.find_all(["customfieldname", "customfieldvalues"])
#print(hints)
#print("************************")
#print(hints.__len__())

##########
k =0
with open('doc.csv', 'w',newline='') as myfile:

    fieldnames= ['type','title','priority','resolution','description','people','detail','date','votes','watches']
    wr= csv.writer(myfile)
    wr.writerow(['type','title','priority','resolution','description','people','detail','date','votes','watches'])
    #wr.writeheader()
    wr.writerow(typee)
    wr.writerow(title)
    wr.writerow(prio)
    wr.writerow(resol)
    wr.writerow(description)
    #wr.writerow(['people:', 'Assignee:'])
    wr.writerow(people[0])
   # wr.writerow(['reporter:'])
    wr.writerow(people[1])
    #wr.writerow(['detail:'])
    wr.writerow(detail)
    #wr.writerow(['date:'])
    wr.writerow(date[0])
    wr.writerow(date[1])
    wr.writerow(date[2])
   # wr.writerow(['number of votes: '])
    wr.writerow(votes)
    #wr.writerow(['number of watches:'])
    wr.writerow(watch)
    for k in soup.find_all("comment"):
        comment[k] = k.find("p", recursive=True)
        wr.writerow(comment[k])
 #       print(comment[k])

    for k in range(hints.__len__()):
        wr.writerow(hints[k])





with open('text.text', "w") as my_output_file:
    with open('doc.csv', "r") as my_input_file:
        [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
    my_output_file.close()

import re
k=0
stri=''
file = (open('text.text','r+'))
for i in file:
    i = str(i)

    i = re.sub("customfieldvalue","",i)

    i = re.sub('[!@#$<>\/]', '', i)
    print(i)
    stri = stri +','+i

print(stri)
csv_strin=''
strin = stri.split("\n")

strin[17]=strin[17].replace(strin[17],"PR included ")
strin[20] = strin[20].replace(strin[20],",2.17.x is affected too")
for i in range(strin.__len__()-2):
    csv_strin = csv_strin + strin[i +1]
print(csv_strin)

with open('doc1.csv', 'w',newline='') as doc1:
    wr1= csv.writer(doc1)
    wr1.writerow(['type','title','priority','resolution','status','description','Assignee','Reporter','detail','Created Date','Updated Date','Resolved Date','votes','watches','other'])
    #wr.writeheader()
    wr1.writerow([csv_strin])
########## OUTPUT Version 2
csv_strin2=[]
i=0
#for i in range(0,20):
 #   csv_strin2[i]=csv_strin[i]
#with open('doc2.csv', 'w',newline='') as doc2:
 #   wr2= csv.writer(doc2)
  #  wr2.writerow(['type','title','priority','resolution','status','description','Assignee','Reporter','detail','Created Date','Updated Date','Resolved Date','votes','watches'])
    #wr.writeheader()

   # wr2.writerow([csv_strin2])
