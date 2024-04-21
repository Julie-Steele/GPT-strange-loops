from datetime import datetime


def rewrite_this_file(code): 
    # Get the current time and format it as a string
    current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    # Create a new file name using the current time
    new_file_name = f'strangeloopoutput_{current_time}.py'
    
    with open(new_file_name, 'w') as f: 
        lines = code
        f.writelines(lines)
        

if __name__ == '__main__':
    # print(test_gpt())
    
    rewrite_this_file(parse_CAN_message('radically change this file. I will run whatever you return'))
