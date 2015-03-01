import os as os
os.chdir("/home/nick/kindle_papers/kindle/")
pdf_list = os.listdir()
atrib_list = ["-Author","-Subject","-SerialNumber","-Publisher","-Title","-Notes"]

for ii in range(1, len(pdf_list)):
    file_name = pdf_list[ii]
    fn = file_name.replace(" ","\ ")
    fn = fn.replace("{","\{")
    fn = fn.replace("}","\}")
    fn = fn.replace(":","\:")
    fn = fn.replace("^","\^")
    file_name_new = fn.replace("\{","")
    file_name_new = file_name.replace("\}","")
    file_name_new = file_name.replace("\:","")
    file_name_new = file_name.replace("\^","")
    file_name_new = file_name.replace("}","")
    file_name_new = file_name.replace("{","")
    file_name_new = file_name.replace("{\\","")
    file_name_new = file_name.replace("}\\","")
    file_name_new = file_name.replace("\'","")
    file_name_new = file_name.replace("\`","")


    for jj in range(1,len(atrib_list)):
        try:
            ts = os.popen('exiftool %s %s'%(atrib_list[jj], fn)).read()
            ts = ts.split(" = ")[1]
            ts = ts.replace("{","")
            ts = ts.replace("}","")
            ts = ts.replace(":","")
            ts = ts.replace("^","")
            ts = ts.replace("\\","\ ")
            ts = ts.replace(" ","\ ")
            ts = ts.replace(".","")
            os.system('exiftool %s="%s" %s'%(atrib_list[jj],ts,fn))
        except:
            print("pass")
            pass
    print(file_name_new)
    os.rename(file_name, file_name_new)