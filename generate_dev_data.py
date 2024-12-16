import os

def write_text(text, file):
    with open(file, 'a') as f:
        f.write(text)

def write_dev(list_line, demo_file):
    write_text(f'{" "*8}<record id="dev_{list_line[0]}" model="res.partner">\n',demo_file)  
    write_text(f'{" "*12}<field name="name">{list_line[1]}</field>\n',demo_file)
    write_text(f'{" "*12}<field name="access_code">{list_line[2]}</field>\n',demo_file)
    write_text(f'{" "*12}<field name="is_developer">True</field>\n',demo_file)
    write_text(f'{" "*8}</record>\n',demo_file)

def devs_generator(f_source, demo_file):
    write_text(f'<odoo>\n', demo_file)
    write_text(f'{" "*4}<data>\n', demo_file)

    with open(f_source, 'r') as f:
        for line in f:
            list_line = line.strip().split(',')
            print(list_line)
            write_dev(list_line, demo_file)

    write_text(f'{" "*4}</data>\n', demo_file)
    write_text(f'</odoo>\n', demo_file)         


def main():
    if os.path.exists('custom-addons/manage/demo/devs.xml'):
        os.remove('custom-addons/manage/demo/devs.xml')
    devs_generator('dev_data.csv', 'custom-addons/manage/demo/devs.xml')


if __name__ == '__main__':
    main()