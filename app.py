import PySimpleGUI as sg
import json

from table_data import table_data as td

tf: dict = {'font':('Roboto', 12), 'background_color':'#48454a', 'sbar_trough_color': '#48454a', 'sbar_background_color': '#29272A'}
bf: dict = {'font':('Roboto', 12), 'button_color':'#48454a'}
te: dict = {'font':('Roboto', 12), 'background_color':'#29272A', 'expand_x':'True', 'justification':'center'}
pu: dict = {'background_color':'#29272A'}

# Temporary declaration
info = ''

# Fetch data from table_data.py
data = []

for k in td.keys():
    row = list(td[k].values())
    data.append(row)

print(data)

# GUI layout
layout_main = [[sg.Table(values=data, key='TABLE', enable_events=True, headings=['Item', 'Store 1', 'Price 1', 'Store 2', 'Price 2'], **tf), sg.T(info, key='INFO', size=(30, 10), font=('Roboto', 12), background_color='#29272A')],
          [sg.B('Add', key='ADD', p=((140, 5), (0, 0)), **bf), sg.B('Change', key='CHANGE', disabled=True, **bf), sg.B('Delete', key='DELETE', disabled=True, **bf)]]

window_main = sg.Window('Grocery Price Tracker', layout_main, background_color='#29272A')

# Program loop
while True:
    event, values = window_main.read()

    if event == None:
        break

    elif event == 'TABLE':
        if values[event] != []: # Verifies a delete didn't just occur
            data_selected = [data[row] for row in values[event]]
            data_selected = [i for i in data_selected[0]]
            window_main['CHANGE'].update(disabled=False)
            window_main['DELETE'].update(disabled=False)
            # Update info text
            info = data_selected[-1]
            window_main['INFO'].update(info)

    elif event == 'ADD':
        layout_add = [
            [sg.T('New Item', **te)],
            [sg.T(key='ITMERR', visible=False, **te)],
            [sg.P(**pu), sg.I('', key='ADDITM', size=(20, 5)), sg.P(**pu)],
            [sg.HorizontalSeparator()],
            [sg.T('Store 1', **te)],
            [sg.T(key='STR1ERR', visible=False, **te)],
            [sg.P(**pu), sg.I('', key='ADDSTR1', size=(20, 5)), sg.P(**pu)],
            [sg.T('Price 1', **te)],
            [sg.T(key='PRC1ERR', visible=False, **te)],
            [sg.P(**pu), sg.I('', key='ADDPRC1', size=(10, 5)), sg.P(**pu)],
            [sg.HorizontalSeparator()],
            [sg.T('Store 2', **te)],
            [sg.T(key='STR2ERR', visible=False, **te)],
            [sg.P(**pu), sg.I('', key='ADDSTR2', size=(20, 5)), sg.P(**pu)],
            [sg.T('Price 2', **te)],
            [sg.T(key='PRC2ERR', visible=False, **te)],
            [sg.P(**pu), sg.I('', key='ADDPRC2', size=(10, 5)), sg.P(**pu)],
            [sg.HorizontalSeparator()],
            [sg.T('Item Information', **te)],
            [sg.Multiline('', key='ADDINF', size=(20, 5))],
            [sg.Push(**pu), sg.B('Save', key='SAVE', **bf), sg.Push(**pu)]]
    
        window_add = sg.Window('Add Item', layout_add, background_color='#29272A')

        while True:
            event, values = window_add.read()

            if event == None:
                break

            elif event == 'SAVE':
                # Update table_data dictionary
                with open('table_data.py', 'w') as file:
                    rows = list(td.keys())
                    rows = [int(row) for row in rows]
                    
                    if len(rows) >= 1:
                        last_key = rows[-1]
                        next_key = last_key + 1
                    else:
                        last_key = None
                        next_key = 0

                    td.update({str(next_key): {"item": values['ADDITM'],
                                        "store1": values['ADDSTR1'],
                                        "price1": values['ADDPRC1'],
                                        "store2": values['ADDSTR2'],
                                        "price2": values['ADDPRC2'],
                                        "info": values['ADDINF'],}})
                    file.write('table_data = ' + json.dumps(td, indent=4))

                new_row = [window_add['ADDITM'].get(), window_add["ADDSTR1"].get(),
                           window_add['ADDPRC1'].get(), window_add["ADDSTR2"].get(),
                           window_add['ADDPRC2'].get(), window_add['ADDINF'].get()]

                data.append(new_row)
                window_main['TABLE'].update(data)
                break

            print(event, values)

        window_add.close()

    elif event == 'CHANGE':
        layout_change = [
        [sg.T('Item', **te)],
        [sg.T(key='ITMERR', visible=False)],
        [sg.P(**pu), sg.I(data_selected[0], key='ITM', size=(20, 5)), sg.P(**pu)],
        [sg.HorizontalSeparator()],
        [sg.T('Store 1', **te)],
        [sg.T(key='STR1ERR', visible=False)],
        [sg.P(**pu), sg.I(data_selected[1], key='STR1', size=(20, 5)), sg.P(**pu)],
        [sg.T('Price 1', **te)],
        [sg.T(key='PRC1ERR', visible=False)],
        [sg.P(**pu), sg.I(data_selected[2], key='PRC1', size=(10, 5)), sg.P(**pu)],
        [sg.HorizontalSeparator()],
        [sg.T('Store 2', **te)],
        [sg.T(key='STR2ERR', visible=False)],
        [sg.P(**pu), sg.I(data_selected[3], key='STR2', size=(20, 5)), sg.P(**pu)],
        [sg.T('Price 2', **te)],
        [sg.T(key='PRC2ERR', visible=False)],
        [sg.P(**pu), sg.I(data_selected[4], key='PRC2', size=(10, 5)), sg.P(**pu)],
        [sg.HorizontalSeparator()],
        [sg.T('Item Information', **te)],
        [sg.Multiline(data_selected[5], key='INF', size=(20, 5))],
        [sg.P(**pu), sg.B('Save', key='SAVE', **bf), sg.P(**pu)]]

        window_change = sg.Window('Edit Item', layout_change, background_color='#29272A')

        while True:
            event, values = window_change.read()

            if event == None:
                break
            elif event == 'SAVE':
                with open('table_data.py', 'w') as file:
                    data_selected_index = data.index(data_selected)

                    td.update({str(data_selected_index): {"item": values['ITM'],
                                        "store1": values['STR1'],
                                        "price1": values['PRC1'],
                                        "store2": values['STR2'],
                                        "price2": values['PRC2'],
                                        "info": values['INF'],}})
                    file.write('table_data = ' + json.dumps(td, indent=4))

                # Replace selected row values with new values
                data[data_selected_index][0] = values['ITM']
                data[data_selected_index][1] = values['STR1']
                data[data_selected_index][2] = values['PRC1']
                data[data_selected_index][3] = values['STR2']
                data[data_selected_index][4] = values['PRC2']
                data[data_selected_index][5] = values['INF']

                window_main['TABLE'].update(data)
                break

        window_change.close()

    elif event == 'DELETE':
        # Remove row from table_data
        with open('table_data.py', 'w') as file:
            data_selected_index = data.index(data_selected)
            td.pop(str(data_selected_index))
            # Reset key numerals
            key = 0
            key_order = [key for key in td.keys()]
            key_len = len(key_order)
            new_keys = []
            while len(new_keys) < key_len:
                new_keys.append(str(key))
                key += 1
            print('new_keys', new_keys)

            td = dict(zip(new_keys, list(td.values())))

            file.write('table_data = ' + json.dumps(td, indent=4))

        # Update UI
        data.remove(data_selected)
        info = ''
        window_main['TABLE'].update(data)
        window_main['INFO'].update(info)
        window_main['DELETE'].update(disabled=True)

    print(event, values)

# Close window
window_main.close()