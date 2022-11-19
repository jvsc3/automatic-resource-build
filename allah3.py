import os
import time
from datetime import date
from datetime import time
from _datetime import datetime
import uuid

def main():
    desktop_name = os.path.expanduser("~/Desktop")

    # if desktop name is not "rubid" then exit
    # if desktop_name != "rubid" or desktop_name != "Unknown Developer":
    #     print("Desktop name is not 'rubid'")
    #     exit()

    username = input("Enter your username: ")
    password = input("Enter your password: ")
    hash_code = uuid.uuid4()
    if username == "admin" and password == "admin":

        resource_name = input("Enter a resource name: ")
        # if os.path.isdir(os.path.join(os.path.expanduser("~"), "Desktop", "hy-" + resource_name)):
            print("Resource already exists!")
            overwrite = input("Do you want to delete the resource? (y/n): ")
            if overwrite == "y":
                # delete everything in the resource folder then delete the resource folder
                for file in os.listdir(os.path.join(os.path.expanduser("~"), "Desktop", "hy-" + resource_name)):
                    os.remove(os.path.join(os.path.expanduser("~"), "Desktop", "hy-" + resource_name, file))
                os.rmdir(os.path.join(os.path.expanduser("~"), "Desktop", "hy-" + resource_name))

                print("Resource deleted!")
            else:
                print("Resource not created!")
                exit()
        else:
            os.mkdir(os.path.join(os.path.expanduser("~"), "Desktop", "hy-" + resource_name))
            with open(os.path.join(os.path.expanduser("~"), "Desktop", "hy-" + resource_name, "debug.txt"), "a") as f:
                # create a variable and set it to the random hash code
                f.write("Loaded resource: " + resource_name + "\n")
                # generate uuid
                f.write("Resource Hash: " + str(hash_code) + "\n")
            print("Resource created!")
            # create folder named client, server and shared to that folder
            os.mkdir(os.path.join(os.path.expanduser("~"), "Desktop", "hy-" + resource_name, "client"))
            os.mkdir(os.path.join(os.path.expanduser("~"), "Desktop", "hy-" + resource_name, "server"))
            os.mkdir(os.path.join(os.path.expanduser("~"), "Desktop", "hy-" + resource_name, "shared"))
            # create cl_main.lua to the client folder
            with open(os.path.join(os.path.expanduser("~"), "Desktop", "hy-" + resource_name, "client", "cl_main.lua"), "w") as f:
                f.write("--[[\n")
                f.write("    This is the Hywave file for the resource.\n")
                f.write("    Don't edit anything If you don't know what you're doing!\n")
                f.write("]]\n")
                # add "local resourceType = client" to the cl_main.lua file
                f.write("\nlocal fileType = 'client'\n")
            # create sv_main.lua to the server folder
            with open(os.path.join(os.path.expanduser("~"), "Desktop", "hy-" + resource_name, "server", "sv_main.lua"), "w") as f:
                f.write("--[[\n")
                f.write("    This is the Hywave file for the resource.\n")
                f.write("    Don't edit anything If you don't know what you're doing!\n")
                f.write("]]\n")
                f.write("\nlocal fileType = 'server'\n")
            # create sh_main.lua to the shared folder
            with open(os.path.join(os.path.expanduser("~"), "Desktop", "hy-" + resource_name, "shared", "sh_main.lua"), "w") as f:
                f.write("--[[\n")
                f.write("    This is the Hywave file for the resource.\n")
                f.write("    Don't edit anything If you don't know what you're doing!\n")
                f.write("]]\n")
                f.write("\n")
                f.write("HYX = {}\n")
                f.write("HYX['curData'] = {resource = 'hy-" + resource_name + "', resourceHash = '"+ str(hash_code) + "'}\n\n")
                f.write("function HYX:LoadData()")
                f.write("""
    local data = fileRead('hywave/' .. self.currentResource .. '.db')
    if data then
        local decoded = json.decode(data)
        if decoded then
            self.curData = decoded
        end
    end
end
                """)
                f.write("\n")
            # create config.lua to the server folder
            with open(os.path.join(os.path.expanduser("~"), "Desktop", "hy-" + resource_name, "server", "config.lua"), "w") as f:
                f.write("--[[\n")
                f.write("    This is the Hywave file for the resource.\n")
                f.write("    Don't edit anything If you don't know what you're doing\n")
                f.write("]]\n")
                f.write("\nlocal fileType = 'config'\n")

            # open that resource folder
            os.chdir(os.path.join(os.path.expanduser("~"), "Desktop", "hy-" + resource_name))
            with open(os.path.join(os.path.expanduser("~"), "Desktop", "hy-" + resource_name, "fxmanifest.lua"), "w+") as f:
                # write to the file the following code unpack the parameters
                f.write("--[[\n")
                f.write("    This file is automatically generated by the hy-resource-manager. at " + str(datetime.now()) + "\n")
                f.write("    Do not edit this file manually.\n")
                f.write("]]\n")
                f.write("\n")
                f.write("""
                
fx_version "cerulean"
games { "gta5" }
description "Hywave FiveM Server"

version "0.1.0"
author "Rubidium"

client_scripts {
    "client/*.*",
}

server_scripts {
    "server/*.*"
}

shared_scripts {
    "shared/*.*",
}
                            
                """)
    else:
        print("Wrong username or password!")
        exit()


if __name__ == "__main__":
    main()
    


