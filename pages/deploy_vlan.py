import MySQLdb as mysql
import streamlit as st

db = 'infra'

mydb = mysql.connect(database=f"{db}", read_default_file=f"~/.my.cnf")

c = mydb.cursor()


def check_vlan(vlan):
    c.execute("""SELECT vlan FROM vlan WHERE vlan = %s""", (vlan,))
    result_vlan = c.fetchone()
    if result_vlan is None:
        return None
    vlan = result_vlan[0]

    if vlan is None:
        return None
    else:
        return vlan


def check_vlanid(vlanid):
    c.execute("""SELECT vlan FROM vlan WHERE vlanid = %s""", (vlanid,))
    result_vlanid = c.fetchone()
    if result_vlanid is None:
        return None
    vlanid = result_vlanid[0]

    if vlanid is None:
        return None
    else:
        return vlanid


def check_prefix(prefix):
    c.execute("""SELECT prefix FROM vlan WHERE prefix = %s""", (prefix,))
    result = c.fetchone()
    if result is None:
        return None
    prefix = result[0]

    if prefix is None:
        return None
    else:
        return prefix


st.title("Deploy vlan")

with st.form("vlan form"):
    vlan_name = st.text_input("vlan name")
    st.warning('Please input a hostname')

    vlan_id = st.text_input("vlanid")
    st.warning('Please input a vlanid')

    vlan_prefix = st.text_input("vlan prefix like 192.168.1.0/24")
    st.warning('Please input prefix')

    state = st.text_input("vlan state if valid input new,present,absent")
    st.warning('Please input prefix')

    submitted = st.form_submit_button("Submit")

    if check_vlan(vlan_name) is not None:
        st.error("vlan exist")
        st.stop()
    elif check_vlanid(vlan_id) is not None:
        st.error("vlanid exist")
        st.stop()
    elif check_prefix(vlan_prefix) is not None:
        st.error("prefix exist")
        st.stop()
    elif submitted:
        c.execute("""INSERT INTO vlan (vlan,vlanid,prefix,state) VALUES (%s,%s,%s,%s)""",
                  (vlan_name, vlan_id, vlan_prefix, state))

try:
    commit = mydb.commit()
except Exception as error:
    print("Trying to commit query somting happend", error)

try:
    c.close()
    mydb.close()
except:
    print("Trying to close database connection somthing went wrong")
