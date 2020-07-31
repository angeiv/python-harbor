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


class ReplicationPolicy(object):
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
        'src_registry': 'Registry',
        'dest_registry': 'Registry',
        'dest_namespace': 'str',
        'trigger': 'ReplicationTrigger',
        'filters': 'list[ReplicationFilter]',
        'deletion': 'bool',
        'override': 'bool',
        'enabled': 'bool',
        'creation_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'src_registry': 'src_registry',
        'dest_registry': 'dest_registry',
        'dest_namespace': 'dest_namespace',
        'trigger': 'trigger',
        'filters': 'filters',
        'deletion': 'deletion',
        'override': 'override',
        'enabled': 'enabled',
        'creation_time': 'creation_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, name=None, description=None, src_registry=None, dest_registry=None, dest_namespace=None, trigger=None, filters=None, deletion=None, override=None, enabled=None, creation_time=None, update_time=None):  # noqa: E501
        """ReplicationPolicy - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._description = None
        self._src_registry = None
        self._dest_registry = None
        self._dest_namespace = None
        self._trigger = None
        self._filters = None
        self._deletion = None
        self._override = None
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
        if src_registry is not None:
            self.src_registry = src_registry
        if dest_registry is not None:
            self.dest_registry = dest_registry
        if dest_namespace is not None:
            self.dest_namespace = dest_namespace
        if trigger is not None:
            self.trigger = trigger
        if filters is not None:
            self.filters = filters
        if deletion is not None:
            self.deletion = deletion
        if override is not None:
            self.override = override
        if enabled is not None:
            self.enabled = enabled
        if creation_time is not None:
            self.creation_time = creation_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        """Gets the id of this ReplicationPolicy.  # noqa: E501

        The policy ID.  # noqa: E501

        :return: The id of this ReplicationPolicy.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReplicationPolicy.

        The policy ID.  # noqa: E501

        :param id: The id of this ReplicationPolicy.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ReplicationPolicy.  # noqa: E501

        The policy name.  # noqa: E501

        :return: The name of this ReplicationPolicy.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReplicationPolicy.

        The policy name.  # noqa: E501

        :param name: The name of this ReplicationPolicy.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ReplicationPolicy.  # noqa: E501

        The description of the policy.  # noqa: E501

        :return: The description of this ReplicationPolicy.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ReplicationPolicy.

        The description of the policy.  # noqa: E501

        :param description: The description of this ReplicationPolicy.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def src_registry(self):
        """Gets the src_registry of this ReplicationPolicy.  # noqa: E501


        :return: The src_registry of this ReplicationPolicy.  # noqa: E501
        :rtype: Registry
        """
        return self._src_registry

    @src_registry.setter
    def src_registry(self, src_registry):
        """Sets the src_registry of this ReplicationPolicy.


        :param src_registry: The src_registry of this ReplicationPolicy.  # noqa: E501
        :type: Registry
        """

        self._src_registry = src_registry

    @property
    def dest_registry(self):
        """Gets the dest_registry of this ReplicationPolicy.  # noqa: E501


        :return: The dest_registry of this ReplicationPolicy.  # noqa: E501
        :rtype: Registry
        """
        return self._dest_registry

    @dest_registry.setter
    def dest_registry(self, dest_registry):
        """Sets the dest_registry of this ReplicationPolicy.


        :param dest_registry: The dest_registry of this ReplicationPolicy.  # noqa: E501
        :type: Registry
        """

        self._dest_registry = dest_registry

    @property
    def dest_namespace(self):
        """Gets the dest_namespace of this ReplicationPolicy.  # noqa: E501

        The destination namespace.  # noqa: E501

        :return: The dest_namespace of this ReplicationPolicy.  # noqa: E501
        :rtype: str
        """
        return self._dest_namespace

    @dest_namespace.setter
    def dest_namespace(self, dest_namespace):
        """Sets the dest_namespace of this ReplicationPolicy.

        The destination namespace.  # noqa: E501

        :param dest_namespace: The dest_namespace of this ReplicationPolicy.  # noqa: E501
        :type: str
        """

        self._dest_namespace = dest_namespace

    @property
    def trigger(self):
        """Gets the trigger of this ReplicationPolicy.  # noqa: E501


        :return: The trigger of this ReplicationPolicy.  # noqa: E501
        :rtype: ReplicationTrigger
        """
        return self._trigger

    @trigger.setter
    def trigger(self, trigger):
        """Sets the trigger of this ReplicationPolicy.


        :param trigger: The trigger of this ReplicationPolicy.  # noqa: E501
        :type: ReplicationTrigger
        """

        self._trigger = trigger

    @property
    def filters(self):
        """Gets the filters of this ReplicationPolicy.  # noqa: E501

        The replication policy filter array.  # noqa: E501

        :return: The filters of this ReplicationPolicy.  # noqa: E501
        :rtype: list[ReplicationFilter]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this ReplicationPolicy.

        The replication policy filter array.  # noqa: E501

        :param filters: The filters of this ReplicationPolicy.  # noqa: E501
        :type: list[ReplicationFilter]
        """

        self._filters = filters

    @property
    def deletion(self):
        """Gets the deletion of this ReplicationPolicy.  # noqa: E501

        Whether to replicate the deletion operation.  # noqa: E501

        :return: The deletion of this ReplicationPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._deletion

    @deletion.setter
    def deletion(self, deletion):
        """Sets the deletion of this ReplicationPolicy.

        Whether to replicate the deletion operation.  # noqa: E501

        :param deletion: The deletion of this ReplicationPolicy.  # noqa: E501
        :type: bool
        """

        self._deletion = deletion

    @property
    def override(self):
        """Gets the override of this ReplicationPolicy.  # noqa: E501

        Whether to override the resources on the destination registry.  # noqa: E501

        :return: The override of this ReplicationPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._override

    @override.setter
    def override(self, override):
        """Sets the override of this ReplicationPolicy.

        Whether to override the resources on the destination registry.  # noqa: E501

        :param override: The override of this ReplicationPolicy.  # noqa: E501
        :type: bool
        """

        self._override = override

    @property
    def enabled(self):
        """Gets the enabled of this ReplicationPolicy.  # noqa: E501

        Whether the policy is enabled or not.  # noqa: E501

        :return: The enabled of this ReplicationPolicy.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ReplicationPolicy.

        Whether the policy is enabled or not.  # noqa: E501

        :param enabled: The enabled of this ReplicationPolicy.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def creation_time(self):
        """Gets the creation_time of this ReplicationPolicy.  # noqa: E501

        The create time of the policy.  # noqa: E501

        :return: The creation_time of this ReplicationPolicy.  # noqa: E501
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this ReplicationPolicy.

        The create time of the policy.  # noqa: E501

        :param creation_time: The creation_time of this ReplicationPolicy.  # noqa: E501
        :type: str
        """

        self._creation_time = creation_time

    @property
    def update_time(self):
        """Gets the update_time of this ReplicationPolicy.  # noqa: E501

        The update time of the policy.  # noqa: E501

        :return: The update_time of this ReplicationPolicy.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ReplicationPolicy.

        The update time of the policy.  # noqa: E501

        :param update_time: The update_time of this ReplicationPolicy.  # noqa: E501
        :type: str
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
        if issubclass(ReplicationPolicy, dict):
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
        if not isinstance(other, ReplicationPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
