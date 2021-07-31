import sys
import yaml

config_file_path = ('C:\OrangeShine\Config\config.yml')

def yaml_loader(config_file_path):
    with open (config_file_path, "r") as file_descriptor:
        data = yaml.load (file_descriptor, Loader=yaml.FullLoader)

    return data

data = yaml_loader (config_file_path)

files = data.get('files')

base_path = (files['base_path'])

modules_path = (files['modules_path'])

tests_path = (files['tests_path'])

sys.path.append(modules_path) # Finds modules in the indicated directory.

sys.path.append(tests_path) # Finds tests in the indicated directory.



if __name__ == '__main__':

    import Search_Organizations
    import Search_Tickets
    import Search_Users

    search_database = input('Search for organizations, tickets, users (input 1, 2, 3): ' )
    if search_database == '1':
        Search_Organizations.display_search_items_organizations_database()
        Search_Organizations.receive_search_inputs_organizations_database()

    elif search_database == '2':
        Search_Tickets.display_search_items_tickets_database()
        Search_Tickets.receive_search_inputs_tickets_database()

    elif search_database == '3':
        Search_Users.display_search_items_users_database()
        Search_Users.receive_search_inputs_users_database()