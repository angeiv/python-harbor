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


class ComponentHealthStatus(object):
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
        'name': 'str',
        'status': 'str',
        'error': 'str'
    }

    attribute_map = {
        'name': 'name',
        'status': 'status',
        'error': 'error'
    }

    def __init__(self, name=None, status=None, error=None):  # noqa: E501
        """ComponentHealthStatus - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._status = None
        self._error = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if error is not None:
            self.error = error

    @property
    def name(self):
        """Gets the name of this ComponentHealthStatus.  # noqa: E501

        The component name  # noqa: E501

        :return: The name of this ComponentHealthStatus.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ComponentHealthStatus.

        The component name  # noqa: E501

        :param name: The name of this ComponentHealthStatus.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def status(self):
        """Gets the status of this ComponentHealthStatus.  # noqa: E501

        The health status of component  # noqa: E501

        :return: The status of this ComponentHealthStatus.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ComponentHealthStatus.

        The health status of component  # noqa: E501

        :param status: The status of this ComponentHealthStatus.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def error(self):
        """Gets the error of this ComponentHealthStatus.  # noqa: E501

        (optional) The error message when the status is \"unhealthy\"  # noqa: E501

        :return: The error of this ComponentHealthStatus.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this ComponentHealthStatus.

        (optional) The error message when the status is \"unhealthy\"  # noqa: E501

        :param error: The error of this ComponentHealthStatus.  # noqa: E501
        :type: str
        """

        self._error = error

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
        if issubclass(ComponentHealthStatus, dict):
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
        if not isinstance(other, ComponentHealthStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
