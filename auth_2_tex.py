home_dir = "/home/nick/git/PhDproposal/"

layout_file = open(home_dir+"layout.md")
layout = layout_file.readlines()
layout_file.close()
full_tex = []

layout.insert(0,"title_authorea.tex")
layout.insert(0,"header.tex")
layout.insert(0,"preamble_authorea.tex")
layout.append("add_bib.tex")

for line in layout:
    cur_tex_file = open(home_dir+line.rstrip())
    cur_tex = cur_tex_file.readlines()
    cur_tex_file.close()
    full_tex.append("%"+"==============start %s ======================"%line.rstrip()+"%"+"\n")
    if line.rstrip() == "Abstract.tex":
        full_tex.append("\\begin{abstract}")
    for tline in cur_tex:
        full_tex.append(tline.rstrip())
    if line.rstrip() == "Abstract.tex":
        full_tex.append("\\end{abstract}")
    full_tex.append("\n"+"%"+"==============end %s ======================"%line.rstrip()+"%")


f = open(home_dir+'full_article.tex','w')
for ele in full_tex:
    f.write(ele+'\n')
f.close()


