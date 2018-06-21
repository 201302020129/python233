items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line
#if items:
    #html_str="<ul>\n"
for index in range(len(items)):
    
    if index < len(items) and index == len(items) - 1:
        html_str += "<li>{}</li>\n</ul>".format(items[index])
    else:
		html_str += "<li>{}</li>\n".format(items[index])
        
# write your code here


print(html_str)