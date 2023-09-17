import re
import urllib.error
import urllib.request


def urlhaus_list(output_file_path: str) -> None:
    """
    Downloads a text file from 'https://urlhaus.abuse.ch/downloads/text_online/'
    and replaces all occurrences of 'http://' or 'https://' with an empty string.
    The modified contents are then written to a file specified by 'output_file_path'.

    Args:
        output_file_path (str): The path to the file where the modified contents will be written.

    Returns:
        None
    """
    url = 'https://urlhaus.abuse.ch/downloads/text_online/'

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            pattern = r'https?://'
            replacement = ''

            with open(output_file_path, 'w') as file:
                modified_contents = re.sub(pattern, replacement, body)
                file.write(modified_contents)
    
    except urllib.error.HTTPError as e:
        print(e.code)
    
    except urllib.error.URLError as e:
        print(e.reason)


def main() -> None:
    """
    The main function that executes the program.

    This function reads a file containing a list of URLs and calls the `urlhaus_list` function to process each URL.

    Parameters:
        None

    Returns:
        None
    """
    file_path = 'urllist.txt'
    urlhaus_list(file_path)


if __name__ == "__main__":
    main()
