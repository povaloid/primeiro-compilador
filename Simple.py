import sys
import Scanner
from pathlib import Path

class Lox:
    had_error = False

    @staticmethod
    def main(args):
        if len(args) > 1:
            print("Usage: pySimple [script]")
            sys.exit(64)
        elif len(args) == 1:
            Lox.run_file(args[0])
        else:
            Lox.run_prompt()

    @staticmethod
    def run_file(path):
        try:
            bytes_content = Path(path).read_bytes()
            Lox.run(bytes_content.decode())
        except IOError as e:
            print(f"Error reading file {path}: {e}")
            sys.exit(1)

    @staticmethod
    def run_prompt():
        try:
            while True:
                print("> ", end='')
                line = input()
                if line is None or line == "":
                    break
                Lox.run(line)
                Lox.had_error = False
        except KeyboardInterrupt:
            print("\nExiting prompt...")

    @staticmethod
    def run(source):
        scanner = Scanner(source)
        tokens = scanner.scan_tokens()

        # For now, just print the tokens.
        for token in tokens:
            print(token)

        if Lox.had_error:
            sys.exit(65)

    @staticmethod
    def error(line, message):
        Lox.report(line, "", message)

    @staticmethod
    def report(line, where, message):
        print(f"[line {line}] Error{where}: {message}", file=sys.stderr)
        Lox.had_error = True

