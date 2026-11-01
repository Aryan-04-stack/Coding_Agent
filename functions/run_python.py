import os
from google.genai import types
import subprocess
def run_file(work_dir,file_path,args = []):
    abs_working_dir = os.path.abspath(work_dir)
    abs_file_path = os.path.abspath(os.path.join(work_dir,file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error :"{file_path}" is not in the working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error :"{file_path}" is not a file'
    if not file_path.endswith(".py"):
        return f'Error : "{file_path}" is not a python file'

    try:
        final_args = ["python",file_path]
        final_args.extend(args)
        output = subprocess.run(
            final_args,
            cwd = abs_working_dir,
            capture_output=True,
            text=True,timeout=30
        )
        final = f"""
        STDOUT :{output.stdout}
        STDERR :{output.stderr}\n"""
        if output.returncode != 0:
            final += f"Process exited with code {output.returncode}"
        return final    
    except Exception as e:
        return f"ERROR :executing python file : {e}"

schema_run_file = types.FunctionDeclaration(
    name="run_file",
    description="Runs the python file with python interpreter. Accepts additional CLI args as an optional array.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type = types.Type.STRING,
                description="contents to write to file as a string.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING
                ),
                description="An optional array of strings to be used as the CLI args for the python file",
            ),
        },
    ),
)    
    