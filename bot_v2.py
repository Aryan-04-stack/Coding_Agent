import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from Coding_Agent.functions.files_info import schema_get_files_info
from Coding_Agent.functions.files_data import schema_get_files_data
from Coding_Agent.functions.write_file import schema_write_file
from Coding_Agent.functions.run_python import schema_run_file
from Coding_Agent.functions.call_function import call_function
def main():
    load_dotenv()
    api_key = os.environ.get("api_key")
    client = genai.Client(api_key = api_key)
    System_prompt = """
        You are a helpful AI coding agent.

        When a user asks a question or makes a request, make a function call plan.
        You can perform the following operations:

        - List files and directories
        - Read file contents
        - Write to a file(create or update)
        - Run Python files with optional arguments

        All paths you provide should be relative to the working directory.

        You do not need to specify the working directory in your function calls
        as it is automatically injected for security reasons.
        """
    if len(sys.argv) <2:
         print("please Enter prompt!!")
         sys.exit(1)

    data_flag = False

    prompt = sys.argv[1] 

    if len(sys.argv) ==3 and sys.argv[2] == "--data":
     data_flag = True   

    messages = [
        types.Content(role = "user",parts = [types.Part(text = prompt)])
    ]

    avail_functions = types.Tool(
        function_declarations = [
            schema_get_files_info,
            schema_get_files_data,
            schema_write_file,
            schema_run_file,
        ]
    )
    config = types.GenerateContentConfig(
        tools = [avail_functions],
        system_instruction=System_prompt
    )
    max_iter = 8
    max_tool_calls = 8
    tool_call_count = 0
    for _ in range(0,max_iter):
        response  = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=messages,
            config=config
        )
        if response is None or response.usage_metadata is None:
            print("response is malformed")
            return
        if data_flag:
            print(f"User : {prompt}")
            print(f"Prompt tokens : {response.usage_metadata.prompt_token_count}")
            print(f"candidate tokens : {response.usage_metadata.candidates_token_count}")
        if response.candidates:
            for candidate in response.candidates:
                if candidate is None or candidate.content is None:
                    continue
                messages.append(candidate.content)
        if response.function_calls:
            for function_call_part in response.function_calls:
                if tool_call_count>=max_tool_calls:
                    print("Maximum tool-call limit reached. Stopping agent.")
                    return
                tool_call_count+=1
                result = call_function(function_call_part,data_flag)
                messages.append(result)
        else:
            print(response.text) 
            return       
main()