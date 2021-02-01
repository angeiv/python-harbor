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

class ProjectReq(object):
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
        'project_name': 'str',
        'public': 'bool',
        'metadata': 'ProjectMetadata',
        'cve_allowlist': 'CVEAllowlist',
        'storage_limit': 'int',
        'registry_id': 'int'
    }

    attribute_map = {
        'project_name': 'project_name',
        'public': 'public',
        'metadata': 'metadata',
        'cve_allowlist': 'cve_allowlist',
        'storage_limit': 'storage_limit',
        'registry_id': 'registry_id'
    }

    def __init__(self, project_name=None, public=None, metadata=None, cve_allowlist=None, storage_limit=None, registry_id=None):  # noqa: E501
        """ProjectReq - a model defined in Swagger"""  # noqa: E501
        self._project_name = None
        self._public = None
        self._metadata = None
        self._cve_allowlist = None
        self._storage_limit = None
        self._registry_id = None
        self.discriminator = None
        if project_name is not None:
            self.project_name = project_name
        if public is not None:
            self.public = public
        if metadata is not None:
            self.metadata = metadata
        if cve_allowlist is not None:
            self.cve_allowlist = cve_allowlist
        if storage_limit is not None:
            self.storage_limit = storage_limit
        if registry_id is not None:
            self.registry_id = registry_id

    @property
    def project_name(self):
        """Gets the project_name of this ProjectReq.  # noqa: E501

        The name of the project.  # noqa: E501

        :return: The project_name of this ProjectReq.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this ProjectReq.

        The name of the project.  # noqa: E501

        :param project_name: The project_name of this ProjectReq.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def public(self):
        """Gets the public of this ProjectReq.  # noqa: E501

        deprecated, reserved for project creation in replication  # noqa: E501

        :return: The public of this ProjectReq.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this ProjectReq.

        deprecated, reserved for project creation in replication  # noqa: E501

        :param public: The public of this ProjectReq.  # noqa: E501
        :type: bool
        """

        self._public = public

    @property
    def metadata(self):
        """Gets the metadata of this ProjectReq.  # noqa: E501


        :return: The metadata of this ProjectReq.  # noqa: E501
        :rtype: ProjectMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ProjectReq.


        :param metadata: The metadata of this ProjectReq.  # noqa: E501
        :type: ProjectMetadata
        """

        self._metadata = metadata

    @property
    def cve_allowlist(self):
        """Gets the cve_allowlist of this ProjectReq.  # noqa: E501


        :return: The cve_allowlist of this ProjectReq.  # noqa: E501
        :rtype: CVEAllowlist
        """
        return self._cve_allowlist

    @cve_allowlist.setter
    def cve_allowlist(self, cve_allowlist):
        """Sets the cve_allowlist of this ProjectReq.


        :param cve_allowlist: The cve_allowlist of this ProjectReq.  # noqa: E501
        :type: CVEAllowlist
        """

        self._cve_allowlist = cve_allowlist

    @property
    def storage_limit(self):
        """Gets the storage_limit of this ProjectReq.  # noqa: E501

        The storage quota of the project.  # noqa: E501

        :return: The storage_limit of this ProjectReq.  # noqa: E501
        :rtype: int
        """
        return self._storage_limit

    @storage_limit.setter
    def storage_limit(self, storage_limit):
        """Sets the storage_limit of this ProjectReq.

        The storage quota of the project.  # noqa: E501

        :param storage_limit: The storage_limit of this ProjectReq.  # noqa: E501
        :type: int
        """

        self._storage_limit = storage_limit

    @property
    def registry_id(self):
        """Gets the registry_id of this ProjectReq.  # noqa: E501

        The ID of referenced registry when creating the proxy cache project  # noqa: E501

        :return: The registry_id of this ProjectReq.  # noqa: E501
        :rtype: int
        """
        return self._registry_id

    @registry_id.setter
    def registry_id(self, registry_id):
        """Sets the registry_id of this ProjectReq.

        The ID of referenced registry when creating the proxy cache project  # noqa: E501

        :param registry_id: The registry_id of this ProjectReq.  # noqa: E501
        :type: int
        """

        self._registry_id = registry_id

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
        if issubclass(ProjectReq, dict):
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
        if not isinstance(other, ProjectReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other