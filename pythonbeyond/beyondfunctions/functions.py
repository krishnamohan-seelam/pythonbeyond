

def hyper_volume(length,*dimensions):
    volume  = length
    for dimension in dimensions:
        volume *= dimension
    return volume

def create_html_tag(**tag_attributes):
    html_tag = "<"
    for key,value in tag_attributes.items():
        html_tag += ' {k} = "{v}"'.format(k=key,v=str(value))
    html_tag += ">"
    return html_tag

if __name__ == "__main__":
    print("calling hypervolume with single argument:",hyper_volume(2))
    print("calling hypervolume with two arguments:",hyper_volume(2,3))
    print("calling hypervolume with three arguments:",hyper_volume(2,3,4))
    html_tag = create_html_tag(img="sample.png",alt="sample image")
    print(html_tag)