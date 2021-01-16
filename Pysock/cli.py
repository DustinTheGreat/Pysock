#!/usr/bin/env python3import argparse

import argparse


def main():
    """
    runner that handles parsing logic
    """
    parser = argparse.ArgumentParser(description='Scanner for websocket vulnerabilities')
    parser.add_argument('-u','--engine', help='Please enter the full uri for the websocket server)', required=True)
    # add subparsers for summary mode and search mode
    subparsers = parser.add_subparsers(help='help for subcommands')

    parser_search = subparsers.add_parser('attack', help='search help')

    parser_search.add_argument('-a', '--query', help='Query string to search engine for', default="all")
    parser_search.add_argument('-t', '--timeout', type=int, help='Page of the result to return details for (default: 1)', default=1)
    parser_search.add_argument('-x', '--cert', help='use a ssl certificate', default=None)

    parser_summary = subparsers.add_parser('summary', help='summary help')
    parser_summary.add_argument('-s', '--show', type=int, help='Show engine description (default: 1)', default=1)


if __name__ == '__main__':
	main()




