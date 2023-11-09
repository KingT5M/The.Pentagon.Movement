import json

# Function to read the existing JSON file, add new data, and save it back
def add_script_to_json(input_file, new_script_file, output_file, beginning_lines, ending_lines):
    # Read the existing JSON file
    try:
        with open(input_file, 'r') as json_file:
            existing_data = json.load(json_file)
    except (FileNotFoundError, json.JSONDecodeError):
        # If the JSON file doesn't exist or is invalid, initialize with an empty content list
        existing_data = {"content": []}

    # Read the new script and process it
    with open(new_script_file, 'r') as file:
        lines = file.readlines()

    # Remove blank lines and add quotes
    processed_lines = ['"' + line.strip() + '",' for line in lines if line.strip()]

    # Combine existing content, beginning lines, processed content, and ending lines
    new_content = beginning_lines + processed_lines + ending_lines

    # Append the new content to the existing data
    existing_data["content"].extend(new_content)

    # Save the updated JSON structure as a JSON file
    with open(output_file, 'w') as json_file:
        json.dump(existing_data, json_file, indent=4)

if __name__ == "__main__":
    input_file = "C:\\Users\\T5M\\Documents\\GitHub\\The.Pentagon.Movement\\TRAINING DATASET\\PROCESSED-SCRIPT.json"  # Change this to your existing JSON file
    new_script_file = "C:\\Users\\T5M\\Documents\\GitHub\\The.Pentagon.Movement\\TRAINING DATASET\\RAW-SCRIPT.txt"  # Change this to the new script text file
    output_file = "C:\\Users\\T5M\\Documents\\GitHub\\The.Pentagon.Movement\\TRAINING DATASET\\CONCATENATED-SCRIPT.json"  # Change this to the output JSON file

    # Lines to include at the beginning and end of the JSON structure
    beginning_lines = [
        "Welcome back to The Freedom of Information!,",
    ]
    ending_lines = [
        "Follow us for more fascinating stories about the past!",
    ]

    add_script_to_json(input_file, new_script_file, output_file, beginning_lines, ending_lines)
    print(f"New script has been added and saved to {output_file}")
