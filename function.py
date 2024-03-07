import os

def save_simulation_result_ori(simulation_result, folder_path):
    file_name = "Simulation_1.txt"
    file_path = os.path.join(folder_path, file_name)
    
    # Check if the file already exists
    if os.path.exists(file_path):
        # Find the next available file name
        i = 2
        while True:
            file_name = f"Simulation_{i}.txt"
            file_path = os.path.join(folder_path, file_name)
            if not os.path.exists(file_path):
                break
            i += 1
    
    # Save the simulation result to the file
    with open(file_path, "w") as file:
        file.write(simulation_result)

def save_simulation_result_with_name(simulation_result, folder_path):
    # Extract the first line of the simulation result
    first_line = simulation_result.split('\n')[0]

    # Extract the content after "# Disaster:"
    try:
        disaster_name = first_line.split('# Disaster: ')[1]
    except IndexError:
        disaster_name = "Simulation_ErrorName"

    # Create the file name
    file_name = f"{disaster_name}.txt"

    # Check if the file already exists
    if os.path.exists(os.path.join(folder_path, file_name)):
        # Find the next available file name
        i = 2
        while True:
            file_name = f"{disaster_name}_{i}.txt"
            if not os.path.exists(os.path.join(folder_path, file_name)):
                break
            i += 1

    # Save the simulation result to the file
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, "w") as file:
        file.write(simulation_result)
    
    return disaster_name

def save_report_with_name(report, context, folder_path, disaster_name):
    # Save the report as .md file
    report_file_name = f"{disaster_name}_report.md"
    report_file_path = os.path.join(folder_path, report_file_name)
    with open(report_file_path, "w") as report_file:
        report_file.write(report)

    # Save the context as .md file
    context_file_name = f"{disaster_name}_events.md"
    context_file_path = os.path.join(folder_path, context_file_name)
    with open(context_file_path, "w") as context_file:
        context_file.write(context)