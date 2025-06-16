import os

def write_file(working_directory, file, content):
    try:
        wd_path = os.path.abspath(working_directory)
        #file_path = os.path.abspath(file)
        full_path = os.path.abspath(os.path.join(wd_path, file))
        
        if not full_path.startswith(wd_path):
            return f'Error: Cannot write to "{file}" as it is outside the permitted working directory'
        if not os.path.exists(os.path.dirname(full_path)):
            os.makedirs(os.path.dirname(full_path))
        with open(full_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"