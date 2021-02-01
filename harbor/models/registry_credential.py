# coding: utf-8

"""
    Harbor API

    These APIs provide services for manipulating Harbor project.  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class RegistryCredential(object):
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
        'type': 'str',
        'access_key': 'str',
        'access_secret': 'str'
    }

    attribute_map = {
        'type': 'type',
        'access_key': 'access_key',
        'access_secret': 'access_secret'
    }

    def __init__(self, type=None, access_key=None, access_secret=None):  # noqa: E501
        """RegistryCredential - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._access_key = None
        self._access_secret = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if access_key is not None:
            self.access_key = access_key
        if access_secret is not None:
            self.access_secret = access_secret

    @property
    def type(self):
        """Gets the type of this RegistryCredential.  # noqa: E501

        Credential type, such as 'basic', 'oauth'.  # noqa: E501

        :return: The type of this RegistryCredential.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RegistryCredential.

        Credential type, such as 'basic', 'oauth'.  # noqa: E501

        :param type: The type of this RegistryCredential.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def access_key(self):
        """Gets the access_key of this RegistryCredential.  # noqa: E501

        Access key, e.g. user name when credential type is 'basic'.  # noqa: E501

        :return: The access_key of this RegistryCredential.  # noqa: E501
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this RegistryCredential.

        Access key, e.g. user name when credential type is 'basic'.  # noqa: E501

        :param access_key: The access_key of this RegistryCredential.  # noqa: E501
        :type: str
        """

        self._access_key = access_key

    @property
    def access_secret(self):
        """Gets the access_secret of this RegistryCredential.  # noqa: E501

        Access secret, e.g. password when credential type is 'basic'.  # noqa: E501

        :return: The access_secret of this RegistryCredential.  # noqa: E501
        :rtype: str
        """
        return self._access_secret

    @access_secret.setter
    def access_secret(self, access_secret):
        """Sets the access_secret of this RegistryCredential.

        Access secret, e.g. password when credential type is 'basic'.  # noqa: E501

        :param access_secret: The access_secret of this RegistryCredential.  # noqa: E501
        :type: str
        """

        self._access_secret = access_secret

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
        if issubclass(RegistryCredential, dict):
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
        if not isinstance(other, RegistryCredential):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
