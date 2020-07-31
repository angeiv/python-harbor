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


class RetentionMetadata(object):
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
        'templates': 'list[RetentionRuleMetadata]',
        'scope_selectors': 'list[RetentionSelectorMetadata]',
        'tag_selectors': 'list[RetentionSelectorMetadata]'
    }

    attribute_map = {
        'templates': 'templates',
        'scope_selectors': 'scope_selectors',
        'tag_selectors': 'tag_selectors'
    }

    def __init__(self, templates=None, scope_selectors=None, tag_selectors=None):  # noqa: E501
        """RetentionMetadata - a model defined in Swagger"""  # noqa: E501
        self._templates = None
        self._scope_selectors = None
        self._tag_selectors = None
        self.discriminator = None
        if templates is not None:
            self.templates = templates
        if scope_selectors is not None:
            self.scope_selectors = scope_selectors
        if tag_selectors is not None:
            self.tag_selectors = tag_selectors

    @property
    def templates(self):
        """Gets the templates of this RetentionMetadata.  # noqa: E501

        templates  # noqa: E501

        :return: The templates of this RetentionMetadata.  # noqa: E501
        :rtype: list[RetentionRuleMetadata]
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        """Sets the templates of this RetentionMetadata.

        templates  # noqa: E501

        :param templates: The templates of this RetentionMetadata.  # noqa: E501
        :type: list[RetentionRuleMetadata]
        """

        self._templates = templates

    @property
    def scope_selectors(self):
        """Gets the scope_selectors of this RetentionMetadata.  # noqa: E501

        supported scope selectors  # noqa: E501

        :return: The scope_selectors of this RetentionMetadata.  # noqa: E501
        :rtype: list[RetentionSelectorMetadata]
        """
        return self._scope_selectors

    @scope_selectors.setter
    def scope_selectors(self, scope_selectors):
        """Sets the scope_selectors of this RetentionMetadata.

        supported scope selectors  # noqa: E501

        :param scope_selectors: The scope_selectors of this RetentionMetadata.  # noqa: E501
        :type: list[RetentionSelectorMetadata]
        """

        self._scope_selectors = scope_selectors

    @property
    def tag_selectors(self):
        """Gets the tag_selectors of this RetentionMetadata.  # noqa: E501

        supported tag selectors  # noqa: E501

        :return: The tag_selectors of this RetentionMetadata.  # noqa: E501
        :rtype: list[RetentionSelectorMetadata]
        """
        return self._tag_selectors

    @tag_selectors.setter
    def tag_selectors(self, tag_selectors):
        """Sets the tag_selectors of this RetentionMetadata.

        supported tag selectors  # noqa: E501

        :param tag_selectors: The tag_selectors of this RetentionMetadata.  # noqa: E501
        :type: list[RetentionSelectorMetadata]
        """

        self._tag_selectors = tag_selectors

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
        if issubclass(RetentionMetadata, dict):
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
        if not isinstance(other, RetentionMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
