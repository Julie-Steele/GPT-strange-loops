import openai
import json
import subprocess
from joblib import Memory
import sys
import yaml

from datetime import datetime





def test_gpt(prompt='What is the capital of the US?'): 
    return client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[{'role':'user', 'content': prompt}],
    ).choices[0].message.content
    







def call_gpt(prompt): 
    with open(__file__, 'r+') as f:
        return client.chat.completions.create(
                model='gpt-3.5-turbo',
                messages= [{'role':'system', 'content':'You are an expert python coder'}, 
                    {'role':'user', 'content': prompt + ' The current file\'s code is' + str(f.readlines())}, 
                    #{'role':'user', 'content': prompt + 'the current file\'s code is'}, 
                    ],
                    
                functions = [
            {
            'name': 'edit-this-file',
            'description': 'rewrites this file that calls the next API call with the code you provide',
            'parameters': {
                'type': 'object', 
                'properties': {
                'code': {
                    'type': 'string', 
                    'description': 'code that will replace this file '
                },
                },
                'required': ['code']
            }
            }
            ],
                function_call={'name': 'edit-this-file'}

 )
    





def parse_CAN_message(prompt): 
    try:
        # Assuming call_gpt() is correctly implemented and returns a structured response
        response = call_gpt(prompt)
        can_message = response.choices[0].message
        arguments = can_message.function_call.arguments
        print(type(arguments))
        arg_json = json.loads(arguments)
        code = arg_json['code']
        print(code)
        
        return code 
    
    
    except json.JSONDecodeError as e:
        print(f'JSON parsing error: {e}')
        return None
    except KeyError as e:
        print(f'Key error: {e} - The response may not be structured as expected.')
        return None
    except Exception as e:
        print(f'An error occurred: {e}')
        return None






if __name__ == '__main__':
    # print(test_gpt())
    
    rewrite_this_file(parse_CAN_message('change this file, quite a lot to do something more interesting, keep a similar format, whatever you return will be run'))
