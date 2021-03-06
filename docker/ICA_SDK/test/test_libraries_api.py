# coding: utf-8

"""
    IAP Services

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import ICA_SDK
from ICA_SDK.api.libraries_api import LibrariesApi  # noqa: E501
from ICA_SDK.rest import ApiException


class TestLibrariesApi(unittest.TestCase):
    """LibrariesApi unit test stubs"""

    def setUp(self):
        self.api = ICA_SDK.api.libraries_api.LibrariesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_library(self):
        """Test case for create_library

        Create library.  # noqa: E501
        """
        pass

    def test_disassociate_library_prep_kit_from_library(self):
        """Test case for disassociate_library_prep_kit_from_library

        Disassociate library prep kit and index adapter kit from library.  # noqa: E501
        """
        pass

    def test_get_library(self):
        """Test case for get_library

        Get library details.  # noqa: E501
        """
        pass

    def test_list_libraries(self):
        """Test case for list_libraries

        Get a list of libraries.  # noqa: E501
        """
        pass

    def test_merge_library_acl(self):
        """Test case for merge_library_acl

        Merge the access control list of a library.  # noqa: E501
        """
        pass

    def test_remove_library_acl(self):
        """Test case for remove_library_acl

        Remove the access control list of a library.  # noqa: E501
        """
        pass

    def test_replace_library_acl(self):
        """Test case for replace_library_acl

        Replace the access control list of a library.  # noqa: E501
        """
        pass

    def test_update_library(self):
        """Test case for update_library

        Update library.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
