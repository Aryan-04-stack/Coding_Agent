import os
from google.genai import types
def write_file(work_dir , file_path,content):
    abs_working_dir = os.path.abspath(work_dir)
    abs_file_path = os.path.abspath(os.path.join(abs_working_dir,file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error :"{file_path}" is not in the working directory'
    parent_dir = os.path.dirname(abs_file_path) #from whole file path stores onlt dir path
    if not os.path.isdir(parent_dir):
        try:
            os.makedirs(parent_dir)
        except Exception as e:
            return f'could not create parent dir :{parent_dir} = {e}'
    try:
        with open(abs_file_path,"w") as file:
            file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters)'
    except Exception as e:
        return f'failed to write to file :"{file_path}", {e}'          

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Overwrites to the existing files or writes to a new file if it doesn't exist(and creates required parent dir safely), constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="contents to write to file as a string.",
            ),
        },
    ),
)