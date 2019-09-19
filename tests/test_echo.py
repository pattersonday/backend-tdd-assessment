#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import echo
import subprocess

# Your test case class goes here


class TestEcho(unittest.TestCase):

    def setUp(self):
        """This method is called only once during test setup"""
        # Create my own parser to use in my own tests
        self.parser = echo.create_parser()

    def echo_test(self):
        string_test = echo.echo_text("Test")
        integer_test = echo.echo_text(3)
        no_input = echo.echo_text("")
        self.assertEquals(string_test, "Test")
        self.assertEquals(integer_test, "Not a string")
        self.assertEquals(no_input, "")

    def test_help(self):
        """ Running the program without arguments should show usage. """

        # Run the command `python ./echo.py -h` in a separate process, then
        # collect it's output.
        process = subprocess.Popen(
            ["python", "./echo.py", "-h"],
            stdout=subprocess.PIPE)
        stdout, _ = process.communicate()
        usage = open("./USAGE", "r").read()

        self.assertEquals(stdout, usage)

    def test_upper_options(self):
        test_agrs = ['-u', 'Hello World']
        # Test the short option parsing capability
        namespc = self.parser.parse_args(test_agrs)
        self.assertTrue(namespc.upper)

        test_args = ['--upper', 'Hello World']
        # Test that the option flag gets parsed into namespc
        pars = echo.create_parser()
        namespc = pars.parse_args(test_args)
        self.assertTrue(namespc.upper)

        # Test that the text gets transformed correctly
        result = echo.echo_upper('Hello World')
        integer = echo.echo_upper(13)
        no_input = echo.echo_upper('')
        self.assertEquals(result, 'HELLO WORLD')
        self.assertEquals(integer, "Not a string")
        self.assertEquals(no_input, '')

    # def test_upper_short(self):
    #     test_args = ['--upper', 'Hello World']
    #     # Test that the option flag gets parsed into namespace correctly
    #     pars = echo.create_parser()
    #     namespc = pars.parse_args(test_args)
    #     self.assertTrue(namespc.upper)
    #     # Test that the text gets transformed correctly
    #     result = echo.main(test_args)
    #     self.assertEqual(result, 'HELLO WORLD')

    def test_lower_option(self):
        test_args = ['-l', 'Hello World']
        # Test the short option parsing capability
        namespc = self.parser.parse_args(test_args)
        self.assertTrue(namespc.lower)

        test_args = ['--lower', 'Hello World']
        # Test that the option flag gets parsed into namespc
        pars = echo.create_parser()
        namespc = pars.parse_args(test_args)
        self.assertTrue(namespc.lower)

        # Test that the text gets transformed correctly
        result = echo.echo_lower('Hello World')
        integer = echo.echo_lower(23)
        no_input = echo.echo_lower('')
        self.assertEquals(result, 'hello world')
        self.assertEquals(integer, 'Not a string')
        self.assertEquals(no_input, '')

    def test_title_option(self):
        test_args = ['-t', 'Hello World']
        # Test the short option parsing capability
        namespc = self.parser.parse_args(test_args)
        self.assertTrue(namespc.title)

        test_args = ['--title', 'Hello World']
        # Test that the option flag gets parsed into namespc
        pars = echo.create_parser()
        namespc = pars.parse_args(test_args)
        self.assertTrue(namespc.title)

        # Test that the text gets transformed correctly
        result = echo.echo_title('Hello World')
        integer = echo.echo_title(33)
        no_input = echo.echo_title('')
        self.assertEquals(result, 'Hello World')
        self.assertEquals(integer, 'Not a string')
        self.assertEquals(no_input, '')

    def test_all_options(self):
        test_args = ['-tul', 'Hello World']
        # Test the short option parsing capability
        namespc = self.parser.parse_args(test_args)
        self.assertTrue(namespc.upper)
        self.assertTrue(namespc.lower)
        self.assertTrue(namespc.title)

        result = echo.echo_lower(echo.echo_upper(
            echo.echo_title('Hello World')))
        self.assertEquals(result, 'hello world')


if __name__ == '__main__':
    unittest.main()
