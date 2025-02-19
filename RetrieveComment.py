#!/usr/bin/env python
from requests import get, Session
from bs4 import BeautifulSoup, Comment
from colorama import Fore, Style
from os import get_terminal_size
from argparse import ArgumentParser

class RetrieveComment:
    def __init__(self, args):
        self.args = args
        self.s = Session()
        self.col = get_terminal_size().columns
        self.comment = []
        
    def Retrieve(self):
        soup = BeautifulSoup(self.s.get(self.args.Target).text, "html.parser")
        comment = soup.find_all(string=lambda text: isinstance(text, Comment))
        self.comment = comment
    
    def printed(self):
        with open(f"{self.args.OutputName}", "w") as file:
            print()
            for n, i in enumerate(self.comment):
                file.write(f"[{n}] => {i}\n")
                print(f"{Fore.GREEN}[{n}]{Style.RESET_ALL} => {i}\n" + '-' * self.col + "\n")

    def run(self):
        try:
            self.Retrieve()
            self.printed()
        except Exception as e:
            print(e)

if __name__ == "__main__":
    parser = ArgumentParser(
        description="Retrieve comment is a simple tool that returns comments to the target indicator",
        usage="\n  %(prog)s -T <Target> -O <OutputName>\n")
    parser.add_argument('-T', '--Target', help='target, set target link')
    parser.add_argument('-O', '--OutputName', default="Output.txt", help='Set name of output file')
    args = parser.parse_args()
    
    Rt = RetrieveComment(args)
    Rt.run()