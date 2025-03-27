import traceback

try:
    with open('diary.txt', 'a') as diary_file:
        while True:
            # Get input from user
            entry = input("What happened today? " if diary_file.tell() == 0 else "What else? ")
            
            # Write entry to file with newline
            diary_file.write(entry + '\n')
            
            # Check if user is done
            if entry == "done for now":
                break

except Exception as e:
    trace_back = traceback.extract_tb(e.__traceback__)
    stack_trace = list()
    for trace in trace_back:
        stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
    print(f"Exception type: {type(e).__name__}")
    message = str(e)
    if message:
        print(f"Exception message: {message}")
    print(f"Stack trace: {stack_trace}")
