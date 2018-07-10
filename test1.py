def create_cast_list(filename):
    cast_list = []
    # use with to open the file filename
    with open() as f:
    # 读取文档内容并赋值到F        
    # and add the actor name to cast_list
        for line in f:# 
            line_data = line.split(',')
            cast_list.append(line_data[0])
            #print(type(f))
        print(f)
    return cast_list
print(create_cast_list("artest"))