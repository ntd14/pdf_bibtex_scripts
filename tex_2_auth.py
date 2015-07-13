## to replace all local files with those from github
### git fetch --all
### git reset --hard origin/master

home_dir = "/home/nick/git/PhDproposal/"

article_file = open(home_dir+"full_article.tex")
article = article_file.readlines()
article_file.close()

for line in article:
    if line.startswith("%==============start ") == True:
        tmp_var = []
        file_name = line.split()[1]
    elif line.startswith("\\begin{a")==True or line.startswith("\\end{a")==True:
            pass
    elif line.startswith("%==============end ") == True:
        tmp_var.pop(0)
        tmp_var.pop(-1)
        #load file.tex
        t_file = open(home_dir+file_name)
        tf = t_file.readlines()
        t_file.close()
        if ''.join(tf).strip() != ''.join(tmp_var).strip():
            print("tf")
            print(''.join(tf).strip())
            print("tmp_var")
            print(''.join(tmp_var).strip())

        #compare file and tmp_var
        #if same - pass
        #f = open(home_dir+file_name,'w')
        #for art_line in tmp_var:
        #    f.write(art_line)

        #f.close()
        del(tmp_var)
    else:
        tmp_var.append(line)


