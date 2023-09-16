import urllib.request


def urlhaus_list():
    url = 'https://urlhaus.abuse.ch/downloads/text_online/'
    filename = 'urlhaus.txt'
    
    with open(filename, 'w'):
        pass
    
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as res:
            body = res.read().decode('utf-8')
            with open(filename, 'w') as f:
                f.writelines(body)
    except urllib.error.HTTPError as err:
        print(err.code)
    except urllib.error.URLError as err:
        print(err.reason)


def main():
    # ここに処理を書く
    urlhaus_list()


if __name__ == "__main__":
    main()
