import os

def get_file_content(working_directory, file):
    try:
        wd_path = os.path.abspath(working_directory)
        #file_path = os.path.abspath(file)
        full_path = os.path.abspath(os.path.join(wd_path, file))
        MAX_CHARS = 10000

        if not full_path.startswith(wd_path):
            return f'Error: Cannot read "{file}" as it is outside the permitted working directory'
        
        if not os.path.isfile(full_path):
            return f'Error: File not found or is not a regular file: "{file}"'

        with open(full_path, "r") as f:
            file_content_string = f.read(MAX_CHARS+1)
            if len(file_content_string) > MAX_CHARS:
                file_content_string = file_content_string[:MAX_CHARS]
                file_content_string += f' [...File "{file}" truncated at 10000 characters]'
        return file_content_string
    except Exception as e:
        return f"Error: {e}"