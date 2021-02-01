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

class Metadata(object):
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
        'id': 'str',
        'name': 'str',
        'icon': 'str',
        'maintainers': 'list[str]',
        'version': 'str',
        'source': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'icon': 'icon',
        'maintainers': 'maintainers',
        'version': 'version',
        'source': 'source'
    }

    def __init__(self, id=None, name=None, icon=None, maintainers=None, version=None, source=None):  # noqa: E501
        """Metadata - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._icon = None
        self._maintainers = None
        self._version = None
        self._source = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if icon is not None:
            self.icon = icon
        if maintainers is not None:
            self.maintainers = maintainers
        if version is not None:
            self.version = version
        if source is not None:
            self.source = source

    @property
    def id(self):
        """Gets the id of this Metadata.  # noqa: E501

        id  # noqa: E501

        :return: The id of this Metadata.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Metadata.

        id  # noqa: E501

        :param id: The id of this Metadata.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Metadata.  # noqa: E501

        name  # noqa: E501

        :return: The name of this Metadata.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Metadata.

        name  # noqa: E501

        :param name: The name of this Metadata.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def icon(self):
        """Gets the icon of this Metadata.  # noqa: E501

        icon  # noqa: E501

        :return: The icon of this Metadata.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this Metadata.

        icon  # noqa: E501

        :param icon: The icon of this Metadata.  # noqa: E501
        :type: str
        """

        self._icon = icon

    @property
    def maintainers(self):
        """Gets the maintainers of this Metadata.  # noqa: E501

        maintainers  # noqa: E501

        :return: The maintainers of this Metadata.  # noqa: E501
        :rtype: list[str]
        """
        return self._maintainers

    @maintainers.setter
    def maintainers(self, maintainers):
        """Sets the maintainers of this Metadata.

        maintainers  # noqa: E501

        :param maintainers: The maintainers of this Metadata.  # noqa: E501
        :type: list[str]
        """

        self._maintainers = maintainers

    @property
    def version(self):
        """Gets the version of this Metadata.  # noqa: E501

        version  # noqa: E501

        :return: The version of this Metadata.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Metadata.

        version  # noqa: E501

        :param version: The version of this Metadata.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def source(self):
        """Gets the source of this Metadata.  # noqa: E501

        source  # noqa: E501

        :return: The source of this Metadata.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Metadata.

        source  # noqa: E501

        :param source: The source of this Metadata.  # noqa: E501
        :type: str
        """

        self._source = source

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
        if issubclass(Metadata, dict):
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
        if not isinstance(other, Metadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
