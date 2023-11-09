# Function to read a text file, remove blank lines, and format it within a JSON structure
def process_text_file(input_file, output_file, beginning_lines, ending_lines):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Remove blank lines and add quotes
    processed_lines = ['"' + line.strip() + '",' for line in lines if line.strip()]

    # Combine beginning lines, processed content, and ending lines
    json_content = {
        "content": beginning_lines + processed_lines + ending_lines
    }

    # Save the JSON structure as a text file
    with open(output_file, 'w') as output_file:
        output_file.write("{\n")
        for key, value in json_content.items():
            output_file.write(f'"{key}": [\n')
            output_file.write('\n'.join(value) + '\n')
            output_file.write("],\n")
        output_file.write("}")

if __name__ == "__main__":
    input_file = "C:\\Users\\T5M\\Documents\\GitHub\\The.Pentagon.Movement\\TRAINING DATASET\\RAW-SCRIPT.txt"  # Change this to your input text file
    output_file = "C:\\Users\\T5M\\Documents\\GitHub\\The.Pentagon.Movement\\TRAINING DATASET\\PROCESSED-SCRIPT.json"  # Change this to your desired output JSON file

    # Lines to include at the beginning and end of the JSON structure
    beginning_lines = [
        "Welcome back to The Freedom of Information!,",
    ]
    ending_lines = [
        "Follow us for more enchanting romantic tales!",
    ]

    process_text_file(input_file, output_file, beginning_lines, ending_lines)
    print(f"Text file has been processed and saved to {output_file}")
