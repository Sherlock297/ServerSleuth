import requests
import argparse
from colorama import Fore, init
from prettytable import PrettyTable
import openpyxl
import os

init(autoreset=True)

# Banner Design
banner = """
===================================================================
        _______  _______  _______  _______  _______
       |   _   ||   _   ||  _    ||   _   ||   _   |
       |  |_|  ||  |_|  || |_|   ||  |_|  ||  | |  |
       |       ||       ||       ||       ||  |_|  |
       |_______||_______||_______||_______||____   |
                                               |  |
                                      _______ |__|
===================================================================
           Web Server Info Checker V1.0 by Sherlock297
===================================================================
"""

def display_banner():
    print(Fore.CYAN + banner)

def check_server_headers(url):
    result = {'Target URL': url, 'Server Header': ''}

    try:
        response = requests.get(url)
        headers = response.headers

        # Check for the Server header
        if 'Server' in headers:
            result['Server Header'] = headers['Server']
        else:
            result['Server Header'] = 'Not found'

    except requests.exceptions.RequestException as e:
        result['Server Header'] = f"Error: {e}"

    return result

def save_to_excel(results, output_file):
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Write header
    sheet['A1'] = 'Target URL'
    sheet['B1'] = 'Server Header'

    # Write data
    for idx, result in enumerate(results, start=2):
        sheet[f'A{idx}'] = result['Target URL']
        sheet[f'B{idx}'] = result['Server Header']

    workbook.save(output_file)
    print(Fore.GREEN + f"\nResults saved to '{output_file}' in Excel format.")

def main():
    parser = argparse.ArgumentParser(description="Web Server Information Disclosure Checker", add_help=False)
    parser.add_argument("-t", "--target_url", help="URL of the target website")
    parser.add_argument("-f", "--input_file", help="File containing multiple target URLs")
    parser.add_argument("-o", "--output_file", default="output.xlsx", help="Output Excel file name")
    parser.add_argument("--help", action="store_true", help="Show this help message and exit")
    parser.add_argument("--version", action="store_true", help="Show version information and exit")

    args = parser.parse_args()

    if args.version:
        print("Web Server Info Checker v1.0")
        return

    if args.help:
        display_banner()
        parser.print_help()
        return

    display_banner()

    results = []

    if args.target_url:
        result = check_server_headers(args.target_url)
        results.append(result)
    elif args.input_file:
        if not os.path.exists(args.input_file):
            print(Fore.RED + "Error: Input file not found.")
            return

        with open(args.input_file, 'r') as file:
            for line in file:
                url = line.strip()
                if url:
                    result = check_server_headers(url)
                    results.append(result)

    if not results:
        print(Fore.YELLOW + "No target URLs provided. Use -t for a single URL or -f for multiple URLs in a file.")
        return

    # Display results in a table
    table = PrettyTable()
    table.field_names = ["Target URL", "Server Header"]

    for result in results:
        table.add_row([result['Target URL'], result['Server Header']])

    print(table)

    # Save results to Excel file
    save_to_excel(results, args.output_file)

if __name__ == "__main__":
    main()
