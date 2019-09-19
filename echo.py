#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "pattersonday w/guidance from madarp's demo and astephens91"


import sys
import argparse


def echo_text(text):
    if isinstance(text, basestring):
        return text
    else:
        return "Not a string"


def echo_upper(text):
    if isinstance(text, basestring):
        return text.upper()
    else:
        return "Not a string"


def echo_lower(text):
    if isinstance(text, basestring):
        return text.lower()
    else:
        return "Not a string"


def echo_title(text):
    if isinstance(text, basestring):
        return text.title()
    else:
        return "Not a string"


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(
        description='Perform transformation on input text.')
    parser.add_argument('-u', '--upper', action='store_true',
                        help='convert text to uppercase')
    parser.add_argument('-l', '--lower', action='store_true',
                        help='convert text to lowercase')
    parser.add_argument('-t', '--title', action='store_true',
                        help='convert text to titlecase')
    parser.add_argument('text', help='text to be manipulated')
    return parser


def main(args):
    """Implementation of echo"""
    par = create_parser()
    # Pass in actual arg list to parse instead of using sys.argv default
    namespace = par.parse_args(args)
    print('Cmd line arguments: {}'.format(namespace))

    text = namespace.text
    upper_flag = namespace.upper
    lower_flag = namespace.lower
    title_flag = namespace.title

    # Perform the requested text transformation:
    if upper_flag:
        text = echo_upper(text)

    if lower_flag:
        text = echo_lower(text)

    if title_flag:
        text = echo_title(text)

    return text


if __name__ == '__main__':
    print(main(sys.argv[1:]))
