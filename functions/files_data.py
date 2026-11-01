import os
from Coding_Agent.config import max_chars
from google.genai import types
def get_files_data(work_dir,file_path):
    abs_working_dir = os.path.abspath(work_dir)
    abs_file_path = os.path.abspath(os.path.join(work_dir,file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error :"{file_path}" is not in the working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error :"{file_path}" is not a file'
    file_content = ""
    try:
        with open(abs_file_path,"r") as file:
            file_content = file.read(max_chars)
            if len(file_content)>=max_chars:
                file_content += f'([...F "{file_path}"truncated at 10000 characters])'
        return file_content   
    except Exception as e:
        return f"Exception reading file : {e}"

schema_get_files_data = types.FunctionDeclaration(
    name="get_files_data",
    description="Gets the contents of the given file as a string, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file from thw working directory.",
            ),
        },
    ),
)    