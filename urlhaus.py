# Standard Library
import re
import urllib.request


def urlhaus_list(file_path: str) -> None:
    url = 'https://urlhaus.abuse.ch/downloads/text_online/'
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as res:
            body = res.read().decode('utf-8')
            pattern = r'\bhttps?:\/\/\b'
            replacement = ''

            with open(file_path, 'w') as f:
                modified_contents = re.sub(pattern, replacement, body)
                f.writelines(modified_contents)
    except urllib.error.HTTPError as err:
        print(err.code)
    except urllib.error.URLError as err:
        print(err.reason)


def main() -> None:
    file_path = 'urllist.txt'
    urlhaus_list(file_path)


if __name__ == "__main__":
    main()
