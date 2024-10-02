# LogAnalyzer
This project is a simple log analyzer that reads a specified log file (`system_logs.txt`) and extracts lines that contain errors, failures, or exceptions. The extracted lines are saved to a separate file (`error_logs.txt`) for easier review.

## Features
- Extracts error lines from log files.
- Supports error keywords: ERROR, FAIL, EXCEPTION.
- Case-insensitive search for error keywords.
- Saves extracted errors to a separate file.

## Installation
To run the Log Analyzer, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/berfinisildak/LogAnalyzer.git
   cd LogAnalyzer
   ```

2. Ensure you have Python installed (version 3.x recommended).

## Usage
Place your log file (`system_logs.txt`) in the same directory as the script. Then run the following command:

```bash
python LogAnalyzer.py
