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


class PreheatPolicy(object):
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
        'name': 'str',
        'description': 'str',
        'project_id': 'int',
        'provider_id': 'int',
        'provider_name': 'str',
        'filters': 'str',
        'trigger': 'str',
        'enabled': 'bool',
        'creation_time': 'datetime',
        'update_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'project_id': 'project_id',
        'provider_id': 'provider_id',
        'provider_name': 'provider_name',
        'filters': 'filters',
        'trigger': 'trigger',
        'enabled': 'enabled',
        'creation_time': 'creation_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, name=None, description=None, project_id=None, provider_id=None, provider_name=None, filters=None, trigger=None, enabled=None, creation_time=None, update_time=None):  # noqa: E501
        """PreheatPolicy - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._description = None
        self._project_id = None
        self._provider_id = None
        self._provider_name = None
        self._filters = None
        self._trigger = None
        self._enabled = None
        self._creation_time = None
        self._update_time = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if project_id is not None:
            self.project_id = project_id
        if provider_id is not None:
            self.provider_id = provider_id
        if provider_name is not None:
            self.provider_name = provider_name
        if filters is not None:
            self.filters = filters
        if trigger is not None:
            self.trigger = trigger
        if enabled is not None:
            self.enabled = enabled
        if creation_time is not None:
            self.creation_time = creation_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        """Gets the id of this PreheatPolicy.  # noqa: E501

        The ID of preheat policy  # noqa: E501

        :return: The id of this PreheatPolicy.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PreheatPolicy.

        The ID of preheat policy  # noqa: E501

        :param id: The id of this PreheatPolicy.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this PreheatPolicy.  # noqa: E501

        The Name of preheat policy  # noqa: E501

        :return: The name of this PreheatPolicy.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PreheatPolicy.

        The Name of preheat policy  # noqa: E501

        :param name: The name of this PreheatPolicy.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this PreheatPolicy.  # noqa: E501

        The Description of preheat policy  # noqa: E501

        :return: The description of this PreheatPolicy.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PreheatPolicy.

        The Description of preheat policy  # noqa: E501

        :param description: The description of this PreheatPolicy.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def project_id(self):
        """Gets the project_id of this PreheatPolicy.  # noqa: E501

        The ID of preheat policy project  # noqa: E501

        :return: The project_id of this PreheatPolicy.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this PreheatPolicy.

        The ID of preheat policy project  # noqa: E501

        :param project_id: The project_id of this PreheatPolicy.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def provider_id(self):
        """Gets the provider_id of this PreheatPolicy.  # noqa: E501

        The ID of preheat policy provider  # noqa: E501

        :return: The provider_id of this PreheatPolicy.  # noqa: E501
        :rtype: int
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this PreheatPolicy.

        The ID of preheat policy provider  # noqa: E501

        :param provider_id: The provider_id of this PreheatPolicy.  # noqa: E501
        :type: int
        """

        self._provider_id = provider_id

    @property
    def provider_name(self):
        """Gets the provider_name of this PreheatPolicy.  # noqa: E501

        The Name of preheat policy provider  # noqa: E501

        :return: The provider_name of this PreheatPolicy.  # noqa: E501
        :rtype: str
        """
        return self._provider_name

    @provider_name.setter
    def provider_name(self, provider_name):
        """Sets the provider_name of this PreheatPolicy.

        The Name of preheat policy provider  # noqa: E501

        :param provider_name: The provider_name of this PreheatPolicy.  # noqa: E501
        :type: str
        """

        self._provider_name = provider_name

    @property
    def filters(self):
        """Gets the filters of this PreheatPolicy.  # noqa: E501

        The Filters of preheat policy  # noqa: E501

        :return: The filters of this PreheatPolicy.  # noqa: E501
        :rtype: str
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this PreheatPolicy.

        The Filters of preheat policy  # noqa: E501

        :param filters: The filters of this PreheatPolicy.  # noqa: E501
        :type: str
        """

        self._filters = filters

    @property
    def trigger(self):
        """Gets the trigger of this PreheatPolicy.  # noqa: E501

        The Trigger of preheat policy  # noqa: E501

        :return: The trigger of this PreheatPolicy.  # noqa: E501
        :rtype: str
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """Sets the trigger of this PreheatPolicy.

        The Trigger of preheat policy  # noqa: E501

        :param trigger: The trigger of this PreheatPolicy.  # noqa: E501
        :type: str
        """

        self._trigger = trigger

    @property
    def enabled(self):
        """Gets the enabled of this PreheatPolicy.  # noqa: E501

        Whether the preheat policy enabled  # noqa: E501

        :return: The enabled of this PreheatPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this PreheatPolicy.

        Whether the preheat policy enabled  # noqa: E501

        :param enabled: The enabled of this PreheatPolicy.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def creation_time(self):
        """Gets the creation_time of this PreheatPolicy.  # noqa: E501

        The Create Time of preheat policy  # noqa: E501

        :return: The creation_time of this PreheatPolicy.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this PreheatPolicy.

        The Create Time of preheat policy  # noqa: E501

        :param creation_time: The creation_time of this PreheatPolicy.  # noqa: E501
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def update_time(self):
        """Gets the update_time of this PreheatPolicy.  # noqa: E501

        The Update Time of preheat policy  # noqa: E501

        :return: The update_time of this PreheatPolicy.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this PreheatPolicy.

        The Update Time of preheat policy  # noqa: E501

        :param update_time: The update_time of this PreheatPolicy.  # noqa: E501
        :type: datetime
        """

        self._update_time = update_time

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
        if issubclass(PreheatPolicy, dict):
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
        if not isinstance(other, PreheatPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other