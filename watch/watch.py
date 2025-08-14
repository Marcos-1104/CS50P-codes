import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):

    m = re.search(r'src="([^"]+)"', s)
    html = re.search(r'^[<inframe>]',s)

    if not html:
        return None

    if not m:
        return None

    full_url = m.group(1)

    if 'youtube.' in full_url:
        url = full_url.replace("/embed","")
        short_url = re.sub(r'^h.+/','https://youtu.be/', url)
        return short_url
    else:
        return None

if __name__ == "__main__":
    main()
