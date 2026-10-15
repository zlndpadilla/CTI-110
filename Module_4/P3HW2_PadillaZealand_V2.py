# Zealand Padilla
# 10/15/2026
# Use if/else statements to determine overtime pay

# python -m streamlit run P3HW2_PadillaZealand_V2.py

import streamlit as st

st.title("PayCheck Calculator")

# Get name
name = st.text_input("Enter employee name: ")

# Get hours worked
hours_worked = st.number_input("Enter hours worked: ")

# Get pay rate
pay_rate = st.number_input("Enter hourly pay rate: $")

# Calculate pay
if hours_worked > 40:
    ot_hours = hours_worked - 40
    ot_pay = ot_hours * pay_rate * 1.5
    reg_pay = pay_rate * 40
else:
    ot_hours = 0
    ot_pay = 0
    reg_pay = pay_rate * hours_worked

gross_pay = reg_pay + ot_pay

# Display pay statistics using st.write instead of print
st.write("Overtime Hours:", ot_hours)
st.write("Overtime Pay:", ot_pay)
st.write("RegHour Pay:", reg_pay)
st.write("Gross Pay:", gross_pay)
