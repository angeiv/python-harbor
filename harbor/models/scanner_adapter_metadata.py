# coding: utf-8

"""
    Harbor API

    These APIs provide services for manipulating Harbor project.  # noqa: E501

    OpenAPI spec version: 1.10.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class ScannerAdapterMetadata(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'Scanner',
        'capabilities': 'list[ScannerCapability]',
        'properties': 'dict(str, str)'
    }

    attribute_map = {
        'name': 'name',
        'capabilities': 'capabilities',
        'properties': 'properties'
    }

    def __init__(self, name=None, capabilities=None, properties=None):  # noqa: E501
        """ScannerAdapterMetadata - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._capabilities = None
        self._properties = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if capabilities is not None:
            self.capabilities = capabilities
        if properties is not None:
            self.properties = properties

    @property
    def name(self):
        """Gets the name of this ScannerAdapterMetadata.  # noqa: E501


        :return: The name of this ScannerAdapterMetadata.  # noqa: E501
        :rtype: Scanner
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ScannerAdapterMetadata.


        :param name: The name of this ScannerAdapterMetadata.  # noqa: E501
        :type: Scanner
        """

        self._name = name

    @property
    def capabilities(self):
        """Gets the capabilities of this ScannerAdapterMetadata.  # noqa: E501


        :return: The capabilities of this ScannerAdapterMetadata.  # noqa: E501
        :rtype: list[ScannerCapability]
        """
        return self._capabilities

    @capabilities.setter
    def capabilities(self, capabilities):
        """Sets the capabilities of this ScannerAdapterMetadata.


        :param capabilities: The capabilities of this ScannerAdapterMetadata.  # noqa: E501
        :type: list[ScannerCapability]
        """

        self._capabilities = capabilities

    @property
    def properties(self):
        """Gets the properties of this ScannerAdapterMetadata.  # noqa: E501


        :return: The properties of this ScannerAdapterMetadata.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ScannerAdapterMetadata.


        :param properties: The properties of this ScannerAdapterMetadata.  # noqa: E501
        :type: dict(str, str)
        """

        self._properties = properties

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ScannerAdapterMetadata, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ScannerAdapterMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
