import os
import random
import base64


n_technologies = 0


###### Utils ######
def random_technologies():
    global n_technologies
    n_tech_linked = random.randint(1, n_technologies)
    technologies_linked = []
    cont = 0
    while cont < n_tech_linked:
        tech_id = f'technology_{random.randint(1, n_technologies)}' 
        if tech_id not in technologies_linked:
            technologies_linked.append(tech_id)
            cont += 1
    return technologies_linked

def eval_str_technologies():
    eval_str = "[(6, 0, ["
    for tech_id in random_technologies():
        eval_str += f"ref('{tech_id}'), "
    return eval_str[:-2] + "])]"

def get_base64_image(image_name):
    # abrir el fichero de la imagen como binario y en modo lectura
    with open(os.path.join(os.path.dirname(__file__), '../images', f'{image_name}.png'), 'rb') as image_file:
        # codificar la imagen en base64 y decodificarla a utf-8 para poder escribirla en el fichero xml
        base64_image = base64.b64encode(image_file.read()).decode('utf-8')
    return base64_image

def write_text(text, file):
    with open(file, 'a') as f:
        f.write(text)


###### Writers ######

# Developers
def write_dev(list_line, demo_file):
    write_text(f'{" "*8}<record id="dev_{list_line[0]}" model="res.partner">\n',demo_file)  
    write_text(f'{" "*12}<field name="name">{list_line[1]}</field>\n',demo_file)
    write_text(f'{" "*12}<field name="last_login" eval="(datetime.now().strftime(\'%Y-%m-%d\'))"></field>\n',demo_file)
    write_text(f'{" "*12}<field name="access_code">{list_line[2]}</field>\n',demo_file)
    write_text(f'{" "*12}<field name="is_developer">True</field>\n',demo_file)
    write_text(f'{" "*12}<field name="technologies" eval="{eval_str_technologies()}" />\n',demo_file)
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

# Technology
def write_technology(list_line, demo_file):
    write_text(f'{" "*8}<record id="technology_{list_line[0]}" model="manage.technology">\n',demo_file)
    write_text(f'{" "*12}<field name="photo">{get_base64_image(list_line[1])}</field>\n',demo_file)
    write_text(f'{" "*12}<field name="name">{list_line[1]}</field>\n',demo_file)
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

# Technology
def technologies_generator(f_source, demo_file):
    write_text(f'<odoo>\n', demo_file)
    write_text(f'{" "*4}<data>\n', demo_file)

    global n_technologies
    with open(f_source, 'r') as f:
        for line in f:
            list_line = line.strip().split(',')
            n_technologies += 1
            write_technology(list_line, demo_file)

    write_text(f'{" "*4}</data>\n', demo_file)
    write_text(f'</odoo>\n', demo_file)


def main():
    path_dir_demo = os.path.join(os.path.dirname(__file__), '../demo') #custom-addons/manage/demo'
    path_dir_source = os.path.join(os.path.dirname(__file__), '../csv') #'custom-addons/manage/csv'

    # Technology
    if os.path.exists(os.path.join(path_dir_demo, 'technologies.xml')):
        os.remove(os.path.join(path_dir_demo, 'technologies.xml'))
    technologies_generator(
        os.path.join(path_dir_source, 'technology_data.csv'), 
        os.path.join(path_dir_demo, 'technologies.xml')
        )

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