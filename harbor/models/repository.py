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


class Repository(object):
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
        'name': 'str',
        'description': 'str',
        'artifact_count': 'int',
        'pull_count': 'int',
        'creation_time': 'datetime',
        'update_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'name': 'name',
        'description': 'description',
        'artifact_count': 'artifact_count',
        'pull_count': 'pull_count',
        'creation_time': 'creation_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, project_id=None, name=None, description=None, artifact_count=None, pull_count=None, creation_time=None, update_time=None):  # noqa: E501
        """Repository - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._project_id = None
        self._name = None
        self._description = None
        self._artifact_count = None
        self._pull_count = None
        self._creation_time = None
        self._update_time = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if artifact_count is not None:
            self.artifact_count = artifact_count
        if pull_count is not None:
            self.pull_count = pull_count
        if creation_time is not None:
            self.creation_time = creation_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        """Gets the id of this Repository.  # noqa: E501

        The ID of the repository  # noqa: E501

        :return: The id of this Repository.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Repository.

        The ID of the repository  # noqa: E501

        :param id: The id of this Repository.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def project_id(self):
        """Gets the project_id of this Repository.  # noqa: E501

        The ID of the project that the repository belongs to  # noqa: E501

        :return: The project_id of this Repository.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Repository.

        The ID of the project that the repository belongs to  # noqa: E501

        :param project_id: The project_id of this Repository.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def name(self):
        """Gets the name of this Repository.  # noqa: E501

        The name of the repository  # noqa: E501

        :return: The name of this Repository.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Repository.

        The name of the repository  # noqa: E501

        :param name: The name of this Repository.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this Repository.  # noqa: E501

        The description of the repository  # noqa: E501

        :return: The description of this Repository.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Repository.

        The description of the repository  # noqa: E501

        :param description: The description of this Repository.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def artifact_count(self):
        """Gets the artifact_count of this Repository.  # noqa: E501

        The count of the artifacts inside the repository  # noqa: E501

        :return: The artifact_count of this Repository.  # noqa: E501
        :rtype: int
        """
        return self._artifact_count

    @artifact_count.setter
    def artifact_count(self, artifact_count):
        """Sets the artifact_count of this Repository.

        The count of the artifacts inside the repository  # noqa: E501

        :param artifact_count: The artifact_count of this Repository.  # noqa: E501
        :type: int
        """

        self._artifact_count = artifact_count

    @property
    def pull_count(self):
        """Gets the pull_count of this Repository.  # noqa: E501

        The count that the artifact inside the repository pulled  # noqa: E501

        :return: The pull_count of this Repository.  # noqa: E501
        :rtype: int
        """
        return self._pull_count

    @pull_count.setter
    def pull_count(self, pull_count):
        """Sets the pull_count of this Repository.

        The count that the artifact inside the repository pulled  # noqa: E501

        :param pull_count: The pull_count of this Repository.  # noqa: E501
        :type: int
        """

        self._pull_count = pull_count

    @property
    def creation_time(self):
        """Gets the creation_time of this Repository.  # noqa: E501

        The creation time of the repository  # noqa: E501

        :return: The creation_time of this Repository.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this Repository.

        The creation time of the repository  # noqa: E501

        :param creation_time: The creation_time of this Repository.  # noqa: E501
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def update_time(self):
        """Gets the update_time of this Repository.  # noqa: E501

        The update time of the repository  # noqa: E501

        :return: The update_time of this Repository.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this Repository.

        The update time of the repository  # noqa: E501

        :param update_time: The update_time of this Repository.  # noqa: E501
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
        if issubclass(Repository, dict):
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
        if not isinstance(other, Repository):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
