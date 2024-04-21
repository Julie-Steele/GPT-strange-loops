import openai
import json
import subprocess
from joblib import Memory
import sys
import yaml

from datetime import datetime




client = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
)






def test_gpt(prompt='What is the capital of the US?'): 
    return client.messages.create(
        model='gpt-3.5-turbo',
        messages=[{'role':'user', 'content': prompt}],
    ).choices[0].message.content
    


def default_model_if_none(model=None):
    if model is None:
        model = 'gpt-3.5-turbo'
        #model = 'gpt-4'
    return model



def call_model(prompt): 
    with open(__file__, 'r+') as f:
        return client.messages.create(
            model='gpt-3.5-turbo',
            messages= [{'role':'system', 'content':'You are an expert python coder'}, 
                {'role':'user', 'content': prompt + ' The current file\'s code is' + str(f.readlines())}, 
                #{'role':'user', 'content': prompt + 'the current file\'s code is'}, 
                ],

)
    



def parse_message(prompt): 
    try:
        # Assuming call_model() is correctly implemented and returns a structured response
        response = call_model(prompt)
        message = response.choices[0].message
        arguments = message.function_call.arguments
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



def rewrite_new_file(code): 
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    new_file_name = f'strangeloopoutput_{current_time}.py'
    
    with open(new_file_name, 'w') as f: 
        lines = code
        f.writelines(lines)
    

if __name__ == '__main__':
    # print(test_gpt())
    
    rewrite_new_file(parse_message('change this file, quite a lot to do something more interesting, keep a similar format, whatever you return will be run'))
