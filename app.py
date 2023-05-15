# Imports
import streamlit as st
import os
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, List
from web3 import Web3
from dotenv import load_dotenv
load_dotenv("./style.css")


w3 = Web3(Web3.HTTPProvider("HTTP://127.0.0.1:7545"))



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
        "./pictures/plastic.jpeg",
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
        "./pictures/mental.jpeg",
    ],
     "Textile": [
        "Textile",
        "1",
        0.4,
        "./pictures/textile1.png",
    ],
     "Electronics": [
        "Electronic",
        "1",
        0.2,
        "./pictures/pic6electronics.jpeg",
    ],
}

# A list of the product types
recycle_types = ["Paper", "Plastic", "Glass bottles", "Mental", "Textile", "Electronics"]

if "page" not in st.session_state:
    st.session_state.page = 0

def nextpage(): st.session_state.page += 1
def previouspage(): st.session_state.page -= 1
def restart(): st.session_state.page = 0

placeholder = st.empty()
st.button("Next",on_click=nextpage,disabled=(st.session_state.page > 3))
st.button("Previous",on_click=previouspage,disabled=(st.session_state.page > 3))
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
    st.title("About Us")
    st.image("./pictures/aboutus.jpeg", width=400)
    
elif st.session_state.page == 2:
    st.write("#### To help you understand the process of recycling, we provide some information below.")
    st.write("#### Paper waste recycling")
    st.image("./pictures/plastic1.png")
    st.write("#### Glass bottle recycling")
    st.image("./pictures/glass.png")
    st.write("#### Mental waste recycling")
    st.image("./pictures/mental.jpg")
    st.write("#### Steel waste recycling")
    st.image("./pictures/steelprocess.jpg")
    st.write("#### Textiles waste recycling")
    st.image("./pictures/textile.png")
    st.write("#### Electronics waste recycling")
    st.image("./pictures/electronic.jpg")

else:
    with placeholder:
        st.write("This is the end")
        st.button("Restart",on_click=restart)


#Streamlit application style
st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)


################################################################################

# Streamlit Sidebar Code - Start
@st.cache(allow_output_mutation=True)
def load_contract():

    # Load the contract ABI
    with open(Path('./recycletoken')) as f:
        RecycleToken = json.load(f)

    contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

    # Load the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=RecycleToken
    )

    return contract

contract = load_contract()


###########################################

# Create sidebar

st.sidebar.markdown("# Product Account Address and Ethernet Balance in Ether")

account = accounts = w3.eth.accounts

st.sidebar.write("0x4e14Be5A89718A300bb068a18b4274A6b42B6859")

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


# Write the `token` calculation to the Streamlit sidebar
st_total = st.sidebar.write(amount)



def transfer_funds(recipient_address, amount):
    sender_address = "0x4e14Be5A89718A300bb068a18b4274A6b42B6859"
    # Implement the transfer logic here
    # This function will be called when the button is clicked
    st.write(f"Transferred {amount} funds from {sender_address} to {recipient_address}")
# Streamlit app layout
st.title("Wallet Transfer")
st.write("Enter the details below and click 'Transfer' to initiate the transfer.")
recipient_address = st.text_input("Recipient Address")
amount = st.number_input("Amount", min_value=0.0)
transfer_button = st.button("Transfer")
# Check if the transfer button is clicked
if transfer_button:
    if recipient_address and amount > 0:
        transfer_funds(recipient_address, amount)
    else:
        st.write("Please provide a valid recipient address and amount to initiate the transfer.")


###########################################
st.sidebar.title("Support Us")

st.sidebar.write("To support us, you can swap ETH and USDC to our token RTK using the links below:")
if st.sidebar.button('Swap ETH to RTK'):
    st.sidebar.markdown('[Swap ETH to RTK on PancakeSwap](https://pancakeswap.finance/liquidity/56?chain=goerli)')

if st.sidebar.button('Swap USDC to RTK'):
    st.sidebar.markdown('[Swap USDC to RTK on PancakeSwap](https://pancakeswap.finance/swap?chain=goerli&outputCurrency=0xFc81527762b47819ebD33A8[…]f9&inputCurrency=0x07865c6E87B9F70255377e024ace6630C1Eaa37F')

    


