import re

log_file_path = 'system_logs.txt'
error_log_file_path = 'error_logs.txt'

error_pattern = re.compile(r'ERROR|FAIL|EXCEPTION', re.IGNORECASE)

def analyze_log_file(log_file_path, error_log_file_path):
    try:
        with open(log_file_path, 'r') as log_file, open(error_log_file_path, 'w') as error_log_file:
            for line in log_file:
                if error_pattern.search(line):
                    error_log_file.write(line)
        print(f"Errors successfully saved to {error_log_file_path}.")
    except FileNotFoundError:
        print(f"{log_file_path} file not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    analyze_log_file(log_file_path, error_log_file_path)
