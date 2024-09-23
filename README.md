# Indovina - A Simple E-Commerce System

# Overview
Indovina is a simple e-commerce system that allows users to browse, add items to their cart, and make payments. 
The system supports two types of users: buyers and sellers. 
Buyers can purchase food, drinks, snacks, and medicines, while sellers can manage the inventory of these items.

# Features
User Roles : Supports both buyer and seller.
※ For Seller, need to input a password

Product Categories : Users can navigate through various sections including Foods, Drinks, Snacks, and Meds.

Buyer Features :
* Display Product : Buyer can browse items that displayed by seller on each catgories.
* Shopping Cart : Buyers have their own cart.
* Add Item to Cart : Buyers can add item they want to buy to the cart.
* Discard Item from Cart : Buyers can discard item they have added from cart.
* Payment : Buyer can pay for the item in the cart (checkout)
  ※ Once buyer in payment feature, buyer can’t go back (must pay first)
* Exit : Buyer can go back to user roles menu

Seller Features : 
* Display Product : Seller can browse items that displayed on each catgories
* Add items to various section : Seller can add new items and add stock to the choosen section.
* Erase items on each section : Seller can erase items on each section. 
  ※ Erased items, not reducing stock
* Exit : Seller can go back to user roles menu

# User Guide
Choose Role: Upon startup, the user will be prompted to select either "Buyer" or "Seller".

Buyer Functionality:
* Browse Sections: Buyers can choose from different sections: Foods, Drinks, Snacks, and Meds.
* Add to Cart: Buyers can select items to add to their shopping cart.
* Discard Items: Buyers can remove items from their cart if needed.
* Payment: Buyers can finalize their purchases and receive a change if they pay more than the total.

Seller Functionality:
* Display Items: Sellers can view the items available in each section.
* Add Items: Sellers can add new items to the inventory or update the stock of existing items.
* Remove Items: Sellers can remove items from the inventory.

# Inventory Structure
Each product category has the following attributes :
* Foods : 
Name, Stock, Spice Level (Spicy/Mild), Portion Size(Big/Medium/Small), Price
* Drinks : 
Name, Stock, Category (Alcohol/Non-alcohol), Portion Size(Big/Medium/Small), Price
* Snacks : 
Name, Stock, Portion Size(Big/Medium/Small), Price
* Meds : 
Name, Stock, Indication, Price

# Code Explanation
The program uses the tabulate library to display data in a table format for better readability.
Various functions handle different functionalities, including displaying items, adding to the cart, discarding items, and processing payments.
The inventory is managed through lists, and indexing is implemented to ensure the correct items are referenced.

# Requirements
* Python 3.x
* tabulate library (Install using pip install tabulate)
