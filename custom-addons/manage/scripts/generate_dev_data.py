import os

def write_text(text, file):
    with open(file, 'a') as f:
        f.write(text)


###### Writers ######

# Developers
def write_dev(list_line, demo_file):
    write_text(f'{" "*8}<record id="dev_{list_line[0]}" model="res.partner">\n',demo_file)  
    write_text(f'{" "*12}<field name="name">{list_line[1]}</field>\n',demo_file)
    write_text(f'{" "*12}<field name="access_code">{list_line[2]}</field>\n',demo_file)
    write_text(f'{" "*12}<field name="is_developer">True</field>\n',demo_file)
    write_text(f'{" "*8}</record>\n',demo_file)

# Project
def write_project(list_line, demo_file):
    write_text(f'{" "*8}<record id="project_{list_line[0]}" model="manage.project">\n',demo_file)  
    write_text(f'{" "*12}<field name="name">{list_line[1]}</field>\n',demo_file)
    write_text(f'{" "*8}</record>\n',demo_file)  

# History
def write_history(list_line, demo_file):
    write_text(f'{" "*8}<record id="history_{list_line[0]}" model="manage.history">\n',demo_file)  
    write_text(f'{" "*12}<field name="name">{list_line[1]}</field>\n',demo_file)
    write_text(f'{" "*12}<field name="project" ref="project_1" />\n',demo_file)
    write_text(f'{" "*8}</record>\n',demo_file)


###### Generators ######

# Developers
def devs_generator(f_source, demo_file):
    write_text(f'<odoo>\n', demo_file)
    write_text(f'{" "*4}<data>\n', demo_file)

    with open(f_source, 'r') as f:
        for line in f:
            list_line = line.strip().split(',')
            write_dev(list_line, demo_file)

    write_text(f'{" "*4}</data>\n', demo_file)
    write_text(f'</odoo>\n', demo_file)         

# Project
def projects_generator(f_source, demo_file):
    write_text(f'<odoo>\n', demo_file)
    write_text(f'{" "*4}<data>\n', demo_file)

    with open(f_source, 'r') as f:
        for line in f:
            list_line = line.strip().split(',')
            write_project(list_line, demo_file)

    write_text(f'{" "*4}</data>\n', demo_file)
    write_text(f'</odoo>\n', demo_file)

# History
def histories_generator(f_source, demo_file):
    write_text(f'<odoo>\n', demo_file)
    write_text(f'{" "*4}<data>\n', demo_file)

    with open(f_source, 'r') as f:
        for line in f:
            list_line = line.strip().split(',')
            write_history(list_line, demo_file)

    write_text(f'{" "*4}</data>\n', demo_file)
    write_text(f'</odoo>\n', demo_file)


def main():
    path_dir_demo = os.path.join(os.path.dirname(__file__), '../demo') #custom-addons/manage/demo'
    path_dir_source = os.path.join(os.path.dirname(__file__), '../csv') #'custom-addons/manage/csv'

    # Developers
    if os.path.exists(os.path.join(path_dir_demo, 'devs.xml')):
        os.remove(os.path.join(path_dir_demo, 'devs.xml'))
    devs_generator(
        os.path.join(path_dir_source, 'dev_data.csv'), 
        os.path.join(path_dir_demo, 'devs.xml')
        )

    # Project
    if os.path.exists(os.path.join(path_dir_demo, 'projects.xml')):
        os.remove(os.path.join(path_dir_demo, 'projects.xml'))
    projects_generator(
        os.path.join(path_dir_source, 'project_data.csv'), 
        os.path.join(path_dir_demo, 'projects.xml')
        )

    # History
    if os.path.exists(os.path.join(path_dir_demo, 'histories.xml')):
        os.remove(os.path.join(path_dir_demo, 'histories.xml'))
    histories_generator(
        os.path.join(path_dir_source, 'history_data.csv'), 
        os.path.join(path_dir_demo, 'histories.xml')
        )

if __name__ == '__main__':
    main()