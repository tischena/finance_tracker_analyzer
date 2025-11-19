"""
Loads database connection parameters from a configuration file.

The function reads the specified .ini file, retrieves the settings from the
given section, and returns them as a dictionary that can be used to build a
database connection.

Parameters:
    filename (str): Path to the configuration file. Defaults to "db/database.ini".
    section (str): Section name inside the configuration file. Defaults to "postgresql".

Returns:
    dict: A dictionary containing the database connection parameters.

Raises:
    Exception: If the specified section is not found in the configuration file.
"""

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