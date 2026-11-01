import os
from google.genai import types
def get_files_info(work_dir,dir = "."):
    abs_working_dir = os.path.abspath(work_dir)
    abs_dir = os.path.abspath(os.path.join(work_dir,dir))
    if not abs_dir.startswith(abs_working_dir):
        return f'Error :"{dir}" is not in the working directory'
    contents = os.listdir(abs_dir)
    response = ""
    for content in contents:
        content_path = os.path.join(abs_dir,content)
        is_dir = os.path.isdir(content_path) #can't write content as it gives only folder and file name ad we need whole path
        size = os.path.getsize(content_path)
        response += f"- {content}: file_size = {size} bytes , is_dir = {is_dir}\n"
    return response    


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "dir": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists the working directory itself.",
            ),
        },
    ),
)

