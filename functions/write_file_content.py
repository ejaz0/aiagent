import os

def write_file(working_directory, file_path, content):
    abs_path = os.path.abspath(working_directory)
    abs_filepath = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_filepath.startswith(abs_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    try:
        if not os.path.isdir(os.path.dirname(abs_filepath)):
            if not os.path.exists(abs_filepath):
                os.makedirs(os.path.dirname(abs_filepath))
        with open(abs_filepath, 'w') as f:
            f.write(content)
    except Exception as e:
        return f"Error: {e}"
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'