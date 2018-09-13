def conf(file,keyword,str,pattem=0):
    if pattem == 0:
        if str == '\r':
            pass
        else:
            with open(file,'r') as f_old:
                lines = f_old.readlines()
            with open(file,'w') as f_new:
                for line in lines:
                    if keyword in line:
                        line = line.replace(keyword,str)
                    f_new.write(line)
    else:
       if str == '\r':
           pass
       else:
           with open(file,'r') as f_old:
                lines = f_old.readlines()
           with open(file,'w') as f_new:
                for line in lines:
                    if keyword in line:
                        line = line.replace('123456',str)
                    f_new.write(line)