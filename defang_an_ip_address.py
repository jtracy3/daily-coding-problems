"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]"
"""
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--address', type=str, dest='address', help='Add IPv4 address')
args = parser.parse_args()
address = args.address


class Solution:
    """ Solution for Defang IP Problem """

    def __init__(self, address):
        self.address = self.__check_valid(address)

    @staticmethod
    def __check_valid(ipv4):
        """
        Checks if the IPv4 provided is valid

        Parameters
        ---------
            ipv4 (str): an IPv4 address

        Returns
        -------
            IPv4 if a valid IP address
        """
        valid_str_regex = r'\d{,3}\.\d{,3}\.\d{,3}\.\d{,3}'
        if re.match(valid_str_regex, ipv4) is None:
            raise ValueError('Not a valid IPv4 address')
        return ipv4

    def defang_ip(self):
        print(re.sub(r'\.', '[.]', self.address))
        return re.sub(r'\.', '[.]', self.address)


Solution(address).defang_ip()
