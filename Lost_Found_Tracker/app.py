import streamlit as st
from services.lost_service import report_lost_item, get_lost_items
from services.found_service import report_found_item, get_found_items
from services.match_service import match_lost_found

st.title("🔍 Lost & Found Item Tracker")

# Tabs for different features
tab1, tab2, tab3 = st.tabs(["Report Lost Item", "Report Found Item", "View Matches"])

# Report Lost Item
with tab1:
    st.header("Report Lost Item")
    user_name = st.text_input("Your Name", key="lost_name")
    lost_item_name = st.text_input("Item Name", key="lost_item")
    lost_description = st.text_area("Description", key="lost_desc")
    lost_location = st.text_input("Location Lost", key="lost_loc")
    lost_date = st.date_input("Date Lost", key="lost_date")
    
    if st.button("Submit Lost Item", key="lost_submit"):
        result = report_lost_item(user_name, lost_item_name, lost_description, lost_location, str(lost_date))
        st.success(result)

    st.subheader("All Lost Items")
    st.dataframe(get_lost_items())

# Report Found Item
with tab2:
    st.header("Report Found Item")
    finder_name = st.text_input("Your Name", key="found_name")
    found_item_name = st.text_input("Item Name", key="found_item")
    found_description = st.text_area("Description", key="found_desc")
    found_location = st.text_input("Location Found", key="found_loc")
    found_date = st.date_input("Date Found", key="found_date")
    contact_info = st.text_input("Your Contact Info", key="found_contact")

    if st.button("Submit Found Item", key="found_submit"):
        result = report_found_item(finder_name, found_item_name, found_description, found_location, str(found_date), contact_info)
        st.success(result)

    st.subheader("All Found Items")
    st.dataframe(get_found_items())

# View Matches
with tab3:
    st.header("Matching Lost & Found Items")
    matches = match_lost_found()
    if matches:
        st.dataframe(matches)
    else:
        st.info("No matches found yet.")
