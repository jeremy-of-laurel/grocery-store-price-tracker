# Grocery Store Price Tracker
The Grocery Store Price tracker is a desktop application written in Python using the PySimpleGUI framework.  

It's purpose is to help eliminate the friction of comparing prices of items from your local grocery stores.  

The idea is that after you come home from shopping, you use your receipt to enter the prices of frequent items you buy. If you go to a different grocery store, you can add the prices for that store for the same items.  

This gives you a side-by-side price comparison, allowing you to easily distinguish which items you may want to buy from which store, with the ultimate goal of **saving you money!**

## Basics
A fresh download of the application will contain a file named 'table_data.template.py'. This file must be renamed to 'table_data.py' for the application to function.  

Once the file is renamed, the application can be started by running the **app.py** file.  

![image one](/assets/readme_images/initial_window_blank.png)

To begin adding items, click the Add button. You will be presented with a window to enter the following:

- Item Name
- Store 1 Name
- Price for Store 1
- Store 2 Name
- Price for Store 2
- Any extra information for the item

![image two](/assets/readme_images/add_item_window.png)

After clicking Save, the item record will be saved into the table_data.py file and persisted on your list going forward.  

![image three](/assets/readme_images/initial_window_with_item.png)

Your table_data.py file will continue to grow as you add more items. You also have the ability to edit an item record, or delete it entirely, via the GUI.

![image four](/assets/readme_images/table_data_file.png)

Selecting an item row in your list will bring the 'Item Information' into view on the right hand side.

![image five](/assets/readme_images/initial_window_more_items.png)

## Features Planned
- More quality of life, such as eliminating the need to manually rename the 'table_data.template.py' file.
- Possibly a more attractive styling.