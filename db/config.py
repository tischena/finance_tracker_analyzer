from configparser import ConfigParser

def config(filename="db/database.ini", section="postgresql"):
    """Create a database connection using the configuration file."""
    parser = ConfigParser()
    parser.read(filename)


    db = {}
    # Check if the file exists
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception("Section {0} not found in the {1} file".format(section, filename))
    
    return db
    
    #print(db)
    
#config()