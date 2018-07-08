import os
import sys
import requests

def my_download(url):
    file_name = url.split("/")[-1]
    response = requests.get(url, verify=True, auth=('user', 'pass'))
    with open(file_name,'wb') as fout:
        fout.write(response.content)
    return os.getcwd() + "\\" + file_name;

if __name__ == "__main__":
    
    try:
        if (len(sys.argv) > 1):
            input_links = sys.argv[1]
            print "Input links in file: %s" % input_links
    except Exception, err:
        print Exception, err
        print "Input file must be set"
        
    # TODO: implement output directory save
    #out_dir = sys.argv[2];
    
    link_lines = []
    with open(input_links, "r") as f:
        link_lines = f.readlines();
    
    for link_line in link_lines:
        if (link_line != None):
            link_line = link_line.strip()
            if (link_line != ""):
                print "Start download: %s" % link_line
                file_name = my_download(link_line)
                print "Done: %s " %(file_name)
        