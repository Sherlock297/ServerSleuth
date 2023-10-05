# ServerSleuth: Web Server Information Disclosure Checker

## Overview

ServerSleuth is a command-line tool designed to check web server information disclosure by analyzing server headers. It provides insights into potential vulnerabilities and helps fortify web environments against information disclosure risks.

## Features

- Server header analysis for information disclosure assessment.
- User-friendly interface for quick and easy usage.
- Versatile reporting with results displayed in both console and Excel format.

## Installation

Follow these steps to install ServerSleuth:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/serversleuth.git

2. **Navigate to ServerSleuth Directory:**
   ```bash
  cd serversleuth

3. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt

## Usage
ServerSleuth is simple to use. Here are examples of how to run it:

1. **Single URL:**
   ```bash 
   python serversleuth.py -t https://example.com

2. **Multiple URLs from a File:**
   ```bash
   python serversleuth.py -f urls.txt

## Output and Reporting
ServerSleuth produces clear and concise results in a tabular format. The information is displayed in the console and saved in an Excel file for further analysis or sharing.

## Limitations and Considerations
ServerSleuth focuses on server header analysis and may not cover all potential security issues. Users are encouraged to complement its usage with other security tools for comprehensive assessments.

## Security Best Practices
Operate ServerSleuth with responsible and ethical usage. Adhere to security best practices, obtain proper authorization, and use the tool only on systems you are authorized to assess.

## How to Contribute
We welcome contributions and feedback to improve ServerSleuth. Feel free to report issues, share experiences, or contribute to its development.
