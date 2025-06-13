import os

def get_files_info(working_directory, directory=None):
    try:
        
        if directory == None or directory == ".":
            directory = os.path.abspath(working_directory)
        
        if os.path.isabs(directory):
            dir_path = os.path.abspath(directory)
        
        if not os.path.isabs(directory):
            dir_path = os.path.join(os.path.abspath(working_directory),directory)
        

        #print(f"directory absolute path: {os.path.abspath(directory)}")
        #print(f"working_directory absolute path: {os.path.abspath(working_directory)}")
        
        if not dir_path.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
                    
        if not os.path.isdir(dir_path):
            return f'Error: "{directory}" is not a directory'
        
        files = []
        for item in os.listdir(dir_path):
            item_path = os.path.join(dir_path, item)
            #print(item_path)
            files.append(f"- {item}: file_size={os.path.getsize(item_path)}, is_dir={os.path.isdir(item_path)}")
        return "\n".join(files)

    except Exception as e:
        return f'Error: {e}'




