import os
from Coding_Agent.functions.files_info import get_files_info
from Coding_Agent.functions.files_data import get_files_data
from Coding_Agent.functions.write_file import write_file
from Coding_Agent.functions.run_python import run_file
from google.genai import types

work_dir = "test"
def call_function(function_call_part , verbose = False):
    if verbose:
        print(f"Calling Function: {function_call_part.name} ({function_call_part.args})")
    else:
        print(f"Calling Function: {function_call_part.name}")
    result = ""     
    if function_call_part.name == "get_files_info" :
       result = get_files_info(work_dir,**function_call_part.args) 
    if function_call_part.name == "get_files_data" :
       result = get_files_data(work_dir,**function_call_part.args) 
    if function_call_part.name == "write_file" :
       result = write_file(work_dir,**function_call_part.args) 
    if function_call_part.name == "run_file" :
       result = run_file(work_dir,**function_call_part.args) 

    if result == "":
       
        return types.Content(
            role="user",
            parts=[
                types.Part.from_function_response(
                    name = function_call_part.name,
                    response = {"error ": f"Unknown function : {function_call_part.name}"}
                )
            ],
        )  
    return types.Content(
                role="user",
                parts=[
                    types.Part.from_function_response(
                        name = function_call_part.name,
                        response = {"result" : result}
                    )
                ],
            )  
