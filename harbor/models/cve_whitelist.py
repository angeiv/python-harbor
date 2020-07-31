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


class CVEWhitelist(object):
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
        'id': 'int',
        'project_id': 'int',
        'expires_at': 'int',
        'items': 'list[CVEWhitelistItem]'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'expires_at': 'expires_at',
        'items': 'items'
    }

    def __init__(self, id=None, project_id=None, expires_at=None, items=None):  # noqa: E501
        """CVEWhitelist - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._project_id = None
        self._expires_at = None
        self._items = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if expires_at is not None:
            self.expires_at = expires_at
        if items is not None:
            self.items = items

    @property
    def id(self):
        """Gets the id of this CVEWhitelist.  # noqa: E501

        ID of the whitelist  # noqa: E501

        :return: The id of this CVEWhitelist.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CVEWhitelist.

        ID of the whitelist  # noqa: E501

        :param id: The id of this CVEWhitelist.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def project_id(self):
        """Gets the project_id of this CVEWhitelist.  # noqa: E501

        ID of the project which the whitelist belongs to.  For system level whitelist this attribute is zero.  # noqa: E501

        :return: The project_id of this CVEWhitelist.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this CVEWhitelist.

        ID of the project which the whitelist belongs to.  For system level whitelist this attribute is zero.  # noqa: E501

        :param project_id: The project_id of this CVEWhitelist.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def expires_at(self):
        """Gets the expires_at of this CVEWhitelist.  # noqa: E501

        the time for expiration of the whitelist, in the form of seconds since epoch.  This is an optional attribute, if it's not set the CVE whitelist does not expire.  # noqa: E501

        :return: The expires_at of this CVEWhitelist.  # noqa: E501
        :rtype: int
        """
        return self._expires_at

    @expires_at.setter
    def expires_at(self, expires_at):
        """Sets the expires_at of this CVEWhitelist.

        the time for expiration of the whitelist, in the form of seconds since epoch.  This is an optional attribute, if it's not set the CVE whitelist does not expire.  # noqa: E501

        :param expires_at: The expires_at of this CVEWhitelist.  # noqa: E501
        :type: int
        """

        self._expires_at = expires_at

    @property
    def items(self):
        """Gets the items of this CVEWhitelist.  # noqa: E501


        :return: The items of this CVEWhitelist.  # noqa: E501
        :rtype: list[CVEWhitelistItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this CVEWhitelist.


        :param items: The items of this CVEWhitelist.  # noqa: E501
        :type: list[CVEWhitelistItem]
        """

        self._items = items

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
        if issubclass(CVEWhitelist, dict):
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
        if not isinstance(other, CVEWhitelist):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
