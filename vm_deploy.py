#!/usr/bin/env python3
import sys
import re
import array
import unicodedata
import MySQLdb as mysql
import streamlit as st

db = 'infra'

mydb = mysql.connect(database=f"{db}", read_default_file=f"~/.my.cnf")

c = mydb.cursor()


def convert_tuple(tup):
    # initialize an empty string
    string = ''
    for item in tup:
        string = string + item
    return string


def is_valid_domain(string):
    # Regex to check valid
    # domain name.
    regex = "^((?!-)[A-Za-z0-9-]" + "{1,63}(?<!-)\\.)" + "+[A-Za-z]{2,6}"

    # Compile the ReGex
    p = re.compile(regex)

    # If the string is empty
    # return false
    if string is None:
        return False

    # Return if the string
    # matched the ReGex
    if re.search(p, string):
        return True
    else:
        return False


def page1():
    c.execute("SELECT virt_host FROM cluster")
    records1 = c.fetchall()
    if not records1:
        print("check your the virt host query")
        sys.exit()
    pve_host_list = (list(records1))
    pve_host1 = (convert_tuple(pve_host_list[0]))
    pve_host2 = (convert_tuple(pve_host_list[1]))
    pve_host3 = (convert_tuple(pve_host_list[2]))

    st.title("Deploy VM")

    option_pve_host = st.selectbox("Select proxmox hosts", [f"{pve_host1}", f"{pve_host2}", f"{pve_host3}"])
    option_vlan = st.selectbox("Select Vlan", ["test", "prod"])
    option_domain = st.selectbox("Select cluster", ["no.habbfarm.net", "habbfarm.net"])

    c.execute("""SELECT cluster_name FROM cluster WHERE virt_host = %s""", (option_pve_host,))
    records2 = c.fetchone()
    if not records1:
        print("check your cluster query")
        sys.exit()
    cluster = records2[0]

    hostname = st.text_input("Server Hostname")

    fqdn = f"{hostname}.{option_domain}"

    if not hostname:
        st.warning('Please input a hostname')
    elif not is_valid_domain(fqdn):
        st.error("Hostname is not valid")
    elif not hostname and not is_valid_domain(fqdn):
        c.execute("""INSERT HOSTS cluster_name FROM cluster WHERE virt_host = %s""", (option_pve_host,))

    # clicked = st.button("deploy")
    # if clicked:
    #    #m = "VM is deploying"
page1()

try:
    commit = c.commit()
except Exception as error:
    print("Trying to commit query somting happend", error)

try:
    c.close()
except:
    print("Trying to close database connection somthing went wrong")
