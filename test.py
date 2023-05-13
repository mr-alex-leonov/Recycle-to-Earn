# Imports
import streamlit as st
from dataclasses import dataclass
from typing import Any, List
from web3 import Web3
from dotenv import load_dotenv
load_dotenv("./style.css")


w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))


from crypto_wallet import generate_account, get_balance, send_transaction

# Streamlit application headings
st.title("Recycle2Earn!")

st.write("## Help Reutilize Waste and Get Paid!")

st.text(" \n")


products_database = {
    "Paper": [
        "Paper",
        "1",
        0.2,
        "./pictures/pic2.jpeg",
    ],
    "Plastic": [
        "Plastic",
        "1",
        0.4,
        "./pictures/pic2plastic.jpeg",
    ],
    "Glass bottles": [
        "Glass bottle",
        "1",
        0.2,
        "./pictures/pic3glass.jpeg",
    ],
    "Mental": [
        "Mental",
        "1",
        0.2,
        "./pictures/pic4mental.jpeg",
    ],
     "Textile": [
        "Textile",
        "1",
        0.4,
        "./pictures/pic5textile.jpeg",
    ],
     "Electronics": [
        "Electronic",
        "1",
        0.2,
        "./pictures/pic6electronics.jpeg",
    ],
}

# A list of the product types
recycle_types = ["Paper", "Plastic", "Glass bottles", "Mentals", "Textile", "Electronics"]

if "page" not in st.session_state:
    st.session_state.page = 0

def nextpage(): st.session_state.page += 1
def previouspage(): st.session_state.page -= 1
def restart(): st.session_state.page = 0

placeholder = st.empty()
st.button("Next",on_click=nextpage,disabled=(st.session_state.page > 3))
st.button("Previous",on_click=previouspage,disabled=(st.session_state.page >= 1))
if st.session_state.page == 0:

    def get_products():

        """Display the database of products information."""
    db_list = list(products_database.values())

    for number in range(len(recycle_types)):
        st.image(db_list[number][3], width=200)
        st.write("#### Types: ", db_list[number][0])
        st.write("Unit: ", db_list[number][1], "kg")
        st.write("Token Earned: ", db_list[number][2])
        st.text(" \n")

elif st.session_state.page == 1:
    # Replace the text with a chart:
    st.write("This is how paper waste recycling")
    st.image("./pictures/plastic1.png")
    st.image("./pictures/glass.png")
    st.image("./pictures/mental.jpg")
    st.image("./pictures/steelprocess.jpg")
    st.image("./pictures/textile.png")
    st.image("./pictures/electronic.jpg")
elif st.session_state.page == 2:
# Replace the chart with several elements:
    with placeholder.container():
        st.write("This is one element")
        st.write("This is another")
        st.metric("Page:", value=st.session_state.page)

else:
    with placeholder:
        st.write("This is the end")
        st.button("Restart",on_click=restart)

#Streamlit application style
st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)


def transfer_funds(sender_address, recipient_address, amount):
    # Implement the transfer logic here
    # This function will be called when the button is clicked
    st.write(f"Transferred {amount} funds from {sender_address} to {recipient_address}")
# Streamlit app layout
st.title("Wallet Transfer")
st.write("Enter the details below and click 'Transfer' to initiate the transfer.")
sender_address = st.text_input("Sender Address")
recipient_address = st.text_input("Recipient Address")
amount = st.number_input("Amount", min_value=0.0)
transfer_button = st.button("Transfer")
# Check if the transfer button is clicked
if transfer_button:
    if sender_address and recipient_address and amount > 0:
        transfer_funds(sender_address, recipient_address, amount)
    else:
        st.write("Please provide valid input to initiate the transfer.")


################################################################################
# Streamlit Sidebar Code - Start

st.sidebar.markdown("## Product Account Address and Ethernet Balance in Ether")

account = generate_account()

st.sidebar.write(account.address)

balance = st.sidebar.write(get_balance(w3, account.address))

person = st.sidebar.selectbox("Select Recycle Types", recycle_types)

amount = st.sidebar.number_input("Amount of Material in kilograms")

st.sidebar.markdown("### Product Types, and Ethereum Address")

# Identify the product types
products = products_database[person][0]

# Write the products name to the sidebar
st.sidebar.write(products)

# Identify the token earned
token_earned = products_database[person][2]

# Write the token earned to the sidebar
st.sidebar.write(token_earned)


# Write the products' name to the sidebar

st.sidebar.markdown("## Total Token in Ether")


# Write the `wage` calculation to the Streamlit sidebar
st_total = st.sidebar.write(amount)



if st.sidebar.button("RECYCLE!"):

    
    transaction_hash = send_transaction(w3, account)

    # Markdown for the transaction hash
    st.sidebar.markdown("#### Validated Transaction Hash")

    # Write the returned transaction hash to the screen
    st.sidebar.write(transaction_hash)

    # Celebrate your successful payment
    st.balloons()

    get_products()


