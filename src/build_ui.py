# -*- coding: utf-8 -*-
import os


def get_all_file(root_dir):
    for lists in os.listdir(root_dir):
        path = os.path.join(root_dir, lists)
        yield path
        if os.path.isdir(path):
            for file in get_all_file(path):
                yield file


if __name__ == '__main__':
    for file_name in get_all_file(os.path.dirname(__file__)):
        file_path = os.path.dirname(file_name)
        ext = os.path.splitext(file_name)[-1]
        name = os.path.splitext(os.path.basename(file_name))[0]
        if os.path.isfile(file_name) and ext == '.ui':
            os.system('pyuic5 "{0}" -o "{1}"'.format(file_name, os.path.join(file_path, "Ui_"+name+'.py')))
