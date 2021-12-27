
# color_dict.txtのブラックだけタブキーが2つあったので手動で削除

import os

DIR_PATH = os.path.dirname(__file__)
FILE_PATH = DIR_PATH + '/color_dict.txt'
NEW_FILE_PATH = DIR_PATH + '/color_keyword.txt'

with open(FILE_PATH, 'r') as f:
    datalist = f.readlines()
    
    new_f = open(NEW_FILE_PATH, 'w')

    for item in datalist:
        name, id = item.split('\t')
        id = id.replace('\n', '')
        
        ITEM = f"color = '{id}'\n@key(色, {name})\n@use('{name}')\n\n"
        new_f.write(ITEM)
    
    new_f.close()
    
