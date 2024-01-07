import sys
import MySQLdb as mysql
import streamlit as st

db = 'infra'

mydb = mysql.connect(database=f"{db}", read_default_file=f"~/.my.cnf")

c = mydb.cursor()


def check_cluster(cluster):
    c.execute("""SELECT cluster_name FROM cluster WHERE cluster_name = %s""", (cluster,))
    result_cluster = c.fetchone()
    if result_cluster is None:
        return None
    cluster = result_cluster[0]

    if cluster is None:
        return None
    else:
        return cluster


def check_virt_host(virt_host_name):
    c.execute("""SELECT virt_host FROM cluster WHERE virt_host = %s""", (virt_host_name,))
    result_virt_host = c.fetchone()
    if result_virt_host is None:
        return None
    virt_host_name = result_virt_host[0]

    if virt_host_name:
        return None
    else:
        return virt_host_name


st.title("Add cluster and virtualization host")

with st.form("vlan form"):
    virt_host = st.text_input("virtualization host")
    st.warning('Please input a virtualization host')

    cluster_name = st.text_input("cluster name")
    st.warning('Please input a cluster name')

    submitted = st.form_submit_button("Submit")

    if check_virt_host(virt_host) is not None:
        st.error("virtualization host exist")
        st.stop()
    elif check_cluster(cluster_name) is not None:
        st.error("cluster exist")
        st.stop()
    elif submitted:
        c.execute("""INSERT INTO cluster (cluster_name) VALUES (%s)""", (cluster_name,))
        c.execute("""INSERT INTO cluster (virt_host) VALUES (%s)""", (virt_host,))

try:
    commit = c.commit()
except Exception as error:
    print("Trying to commit query something happened", error)

try:
    c.close()
except:
    print("Trying to close database connection somthing went wrong")
