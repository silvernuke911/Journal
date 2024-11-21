import datetime

filename = "Journal.txt"

# make a feature that lets it access entries.

def journal_entry(date_time):
    print(f'Journal Entry for {date_time}:\n')
    entry_lines = []
    empty_line_count = 0  # Keeps track of consecutive empty lines
    
    while True:
        line = input()  # Collect input from the user
        
        if line == "":  # Check for empty line
            empty_line_count += 1
        else:
            if empty_line_count == 2:  # Two empty lines = paragraph break
                entry_lines.append("\n \n")  # Add an empty line for paragraph break
            # Reset empty_line_count when entering a non-empty line
            empty_line_count = 0
            entry_lines.append(line)
        
        if empty_line_count == 3:  # Three empty lines = submit
            break  # End the entry
        
    # Join the lines into a single string with paragraph breaks
    entry = "\n \n".join(entry_lines)
    return entry

def record_journal_entry(filename):
    # Get the current date and time
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Get the journal entry from the user
    entry = journal_entry(current_time)
    
    # Check if the entry is not blank
    if entry:
        with open(filename, "a") as file:
            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            file.write(f"\n{current_time}\n\n")
            file.write(f"{entry}\n\n")
        print("Entry recorded successfully!")
        input("Press Enter to exit")
    else:
        print("Entry cannot be blank. Please try again.")
        
if __name__ == '__main__':
    record_journal_entry(filename)
