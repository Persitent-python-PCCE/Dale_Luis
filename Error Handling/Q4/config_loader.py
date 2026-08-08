def load_config(path):
    
    try:
        f=open(path, "r")
        for  line in f:
            print(line.strip()) 
        f.close()
    except FileNotFoundError as fe:
        return print(fe)
    except IOError as ie:
        return print(ie)
    finally:
        print("config load attempt finished\n")
    
    
load_config(r"C:\Users\daler\Desktop\Projects\DaleLuis Persistent training\Error Handling\Q4\app.config")
load_config(r"C:\Users\daler\Desktop\Projects\DaleLuis Persistent training\Error Handling\Q4\does_not_exist.cfg")