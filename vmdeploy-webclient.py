#!/usr/bin/env python3
#import sys
#import os
import MySQLdb as mysql
import streamlit as st

#file = '.my.cnf'

#path = os.path.abspath(f'{file}')

db = 'infra'

#mydb = mysql.connect(database=f"{db}", read_default_file=f"{path}")
mydb = mysql.connect(database=f"{db}", read_default_file=f"~/.my.cnf")


c = mydb.cursor()



#def virt_host_query():
    #SELECT cluster_name FROM cluster;
#    c.execute("SELECT virt_host FROM cluster")
#    records = c.fetchall()
#    if not records:
#       print("check your the virt host query")
#       sys.exit()
#    for r in records:
#      print (r[0])

c.execute("SELECT virt_host FROM cluster")
records1 = c.fetchall()
if not records1:
  print("check your the virt host query")
  sys.exit()
for i in records1:
  #print (r[0])
  test = i[0]



#def cluster_list_query():
#    #SELECT cluster_name FROM cluster;
#    c.execute("SELECT cluster_name FROM cluster")
#    records = c.fetchall()
#    if not records:
#       print("check your the cluster query")
#       sys.exit()
#    for r in records:
#      print (r[0])

c.execute("SELECT cluster_name FROM cluster")
records2 = c.fetchall()
#records2 = c.fetchone()
if not records2:
  print("check your the cluster query")
  sys.exit()
#for r in records2:
  #print (r[0])
#  test2 = r[0]
test2 = records2[0]
test3 = records2[1]
test4 = records2[2]
#print(test2)
#print(test3)
#print(test4)





#st.title("Deploy VM")

#option_cluster =  st.selectbox("Select virt host",[f"{test2}",f"{test3}",f"{test4}"])


#option_cluster 


#cluster_list()
#virt_host_list()





try:
    commit = mydb.commit()
except Exception as error:
    print("Trying to commit query somting happend", error)

try:
    c.close()
    mydb.close()
except:
    print("Trying to close database connection somthing went wrong")
