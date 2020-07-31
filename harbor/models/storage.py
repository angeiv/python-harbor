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


class Storage(object):
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
        'total': 'int',
        'free': 'int'
    }

    attribute_map = {
        'total': 'total',
        'free': 'free'
    }

    def __init__(self, total=None, free=None):  # noqa: E501
        """Storage - a model defined in Swagger"""  # noqa: E501
        self._total = None
        self._free = None
        self.discriminator = None
        if total is not None:
            self.total = total
        if free is not None:
            self.free = free

    @property
    def total(self):
        """Gets the total of this Storage.  # noqa: E501

        Total volume size.  # noqa: E501

        :return: The total of this Storage.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this Storage.

        Total volume size.  # noqa: E501

        :param total: The total of this Storage.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def free(self):
        """Gets the free of this Storage.  # noqa: E501

        Free volume size.  # noqa: E501

        :return: The free of this Storage.  # noqa: E501
        :rtype: int
        """
        return self._free

    @free.setter
    def free(self, free):
        """Sets the free of this Storage.

        Free volume size.  # noqa: E501

        :param free: The free of this Storage.  # noqa: E501
        :type: int
        """

        self._free = free

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
        if issubclass(Storage, dict):
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
        if not isinstance(other, Storage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
