import sys
import re
import array
import unicodedata
import MySQLdb as mysql
import streamlit as st

db = 'infra'

mydb = mysql.connect(database=f"{db}", read_default_file=f"~/.my.cnf")

c = mydb.cursor()


def check_vlan(vlan):
    c.execute("""SELECT vlan FROM vlan WHERE vlan = %s""", (vlan_name,))
    result_vlan = c.fetchone()
    if result_vlan is None:
        return None
    vlan = result_vlan[0]

    if vlan is None:
        return None
    else:
        return vlan


def check_vlanid(vlanid):
    c.execute("""SELECT vlan FROM vlan WHERE vlanid = %s""", (vlan_id,))
    result_vlanid = c.fetchone()
    if result_vlanid is None:
        return None
    vlanid = result_vlanid[0]

    if vlanid:
        return vlanid


st.title("Deploy vlan")

vlan_name = st.text_input("vlan name")
st.warning('Please input a hostname')

if check_vlan(vlan_name) is not None:
    st.error("vlan exist")

vlan_id = st.text_input("vlanid")
st.warning('Please input a vlanid')

if check_vlanid(vlan_id) is not None:
    st.error("vlanid exist")

vlan_prefix = st.text_input("vlan prefix like 192.168.1.0/24")
st.warning('Please input prefix')


# c.execute("""INSERT HOSTS cluster_name FROM cluster WHERE virt_host = %s""", (option_pve_host,))

try:
    commit = mydb.commit()
except Exception as error:
    print("Trying to commit query somting happend", error)

try:
    c.close()
    mydb.close()
except:
    print("Trying to close database connection somthing went wrong")
