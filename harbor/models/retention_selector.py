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


class RetentionSelector(object):
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
        'kind': 'str',
        'decoration': 'str',
        'pattern': 'str'
    }

    attribute_map = {
        'kind': 'kind',
        'decoration': 'decoration',
        'pattern': 'pattern'
    }

    def __init__(self, kind=None, decoration=None, pattern=None):  # noqa: E501
        """RetentionSelector - a model defined in Swagger"""  # noqa: E501
        self._kind = None
        self._decoration = None
        self._pattern = None
        self.discriminator = None
        if kind is not None:
            self.kind = kind
        if decoration is not None:
            self.decoration = decoration
        if pattern is not None:
            self.pattern = pattern

    @property
    def kind(self):
        """Gets the kind of this RetentionSelector.  # noqa: E501


        :return: The kind of this RetentionSelector.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this RetentionSelector.


        :param kind: The kind of this RetentionSelector.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def decoration(self):
        """Gets the decoration of this RetentionSelector.  # noqa: E501


        :return: The decoration of this RetentionSelector.  # noqa: E501
        :rtype: str
        """
        return self._decoration

    @decoration.setter
    def decoration(self, decoration):
        """Sets the decoration of this RetentionSelector.


        :param decoration: The decoration of this RetentionSelector.  # noqa: E501
        :type: str
        """

        self._decoration = decoration

    @property
    def pattern(self):
        """Gets the pattern of this RetentionSelector.  # noqa: E501


        :return: The pattern of this RetentionSelector.  # noqa: E501
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """Sets the pattern of this RetentionSelector.


        :param pattern: The pattern of this RetentionSelector.  # noqa: E501
        :type: str
        """

        self._pattern = pattern

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
        if issubclass(RetentionSelector, dict):
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
        if not isinstance(other, RetentionSelector):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
