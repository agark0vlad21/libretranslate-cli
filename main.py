#! /usr/bin/python3

import argparse

parser = argparse.ArgumentParser(description="Simple CLI for LibreTranslate.org")
parser.add_argument("-s", "--source", type=str, default="auto", help="source text language (default is auto)")
parser.add_argument("-t", "--target", type=str, help="target language", required=True)
args = parser.parse_args()

from requests import get, post
import readline

languages = str(get("https://libretranslate.org/languages").json())

if args.target not in languages or len(args.target) != 2:
    print("invalid target language")
    exit(1)
elif args.source not in languages or len(args.source) != 2:
    print("invalid source language")
    exit(2)

while True:
    try:
        print(post("https://libretranslate.org/translate", json={
    "q": input(": "),
    "source": args.source,
    "target": args.target,
    "format": "text",
    "api_key": ""
}, headers={
    "Content-Type": "application/json"}).json()["translatedText"])
    except (KeyboardInterrupt, EOFError):
        print("\nBye!")
        exit(3)
    except KeyError:
        print("can't get translation")
