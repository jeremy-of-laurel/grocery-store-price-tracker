# Grocery Store Price Tracker
The Grocery Store Price tracker is a desktop application written in Python using the PySimpleGUI framework.

## Basics
A fresh download of the application will contain a file named 'table_data.template.py'. This file must be renamed to 'table_data.py' for the application to function.  

![image one](/assets/readme_images/table_data_template.png)

Once the file is renamed, the application can be started by running the __init__.py file.  

![image two](/assets/readme_images/initial_window_blank.png)

To begin adding items, click the Add button. You will be presented with a window to enter the following:

- Item Name
- Store 1 Name
- Price for Store 1
- Store 2 Name
- Price for Store 2
- Any extra information for the item

![image three](/assets/readme_images/add_item_window.png)

After clicking Save, the item will be saved into the table_data.py file and persisted on your list going forward.  

![image four](/assets/readme_images/initial_window_with_item.png)

Your table_data.py file will continue to grow as you add more items. You also have the ability to edit an item entry or delete it entirely.

![image five](/assets/readme_images/table_data_file.png)

Selecting an item row in your list will bring the 'Item Information' into view on the right hand side.

![image six](/assets/readme_images/initial_window_more_items.png)

## Features to Come
- More quality of life, such as eliminating the need to manually rename the 'table_data.template.py' file.
- Possibly a more appealing styling.