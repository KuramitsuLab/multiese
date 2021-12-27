
# color_dict.txtのブラックだけタブキーが2つあったので手動で削除

FILE_PATH = './color_dict.txt'
NEW_FILE_PATH = './color.txt'

with open(FILE_PATH, 'r') as f:
    datalist = f.readlines()
    
    new_f = open(NEW_FILE_PATH, 'w')

    for item in datalist:
        name, id = item.split('\t')
        id = id.replace('\n', '')
        
        ITEM = f"color = '{id}'\n@key(色, {name})\n@use('{name}')\n\n"
        new_f.write(ITEM)
    
    new_f.close()
    
