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

class RetentionExecutionTask(object):
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
        'execution_id': 'int',
        'repository': 'str',
        'job_id': 'str',
        'status': 'str',
        'status_code': 'int',
        'status_revision': 'int',
        'start_time': 'str',
        'end_time': 'str',
        'total': 'int',
        'retained': 'int'
    }

    attribute_map = {
        'id': 'id',
        'execution_id': 'execution_id',
        'repository': 'repository',
        'job_id': 'job_id',
        'status': 'status',
        'status_code': 'status_code',
        'status_revision': 'status_revision',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'total': 'total',
        'retained': 'retained'
    }

    def __init__(self, id=None, execution_id=None, repository=None, job_id=None, status=None, status_code=None, status_revision=None, start_time=None, end_time=None, total=None, retained=None):  # noqa: E501
        """RetentionExecutionTask - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._execution_id = None
        self._repository = None
        self._job_id = None
        self._status = None
        self._status_code = None
        self._status_revision = None
        self._start_time = None
        self._end_time = None
        self._total = None
        self._retained = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if execution_id is not None:
            self.execution_id = execution_id
        if repository is not None:
            self.repository = repository
        if job_id is not None:
            self.job_id = job_id
        if status is not None:
            self.status = status
        if status_code is not None:
            self.status_code = status_code
        if status_revision is not None:
            self.status_revision = status_revision
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if total is not None:
            self.total = total
        if retained is not None:
            self.retained = retained

    @property
    def id(self):
        """Gets the id of this RetentionExecutionTask.  # noqa: E501


        :return: The id of this RetentionExecutionTask.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RetentionExecutionTask.


        :param id: The id of this RetentionExecutionTask.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def execution_id(self):
        """Gets the execution_id of this RetentionExecutionTask.  # noqa: E501


        :return: The execution_id of this RetentionExecutionTask.  # noqa: E501
        :rtype: int
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        """Sets the execution_id of this RetentionExecutionTask.


        :param execution_id: The execution_id of this RetentionExecutionTask.  # noqa: E501
        :type: int
        """

        self._execution_id = execution_id

    @property
    def repository(self):
        """Gets the repository of this RetentionExecutionTask.  # noqa: E501


        :return: The repository of this RetentionExecutionTask.  # noqa: E501
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this RetentionExecutionTask.


        :param repository: The repository of this RetentionExecutionTask.  # noqa: E501
        :type: str
        """

        self._repository = repository

    @property
    def job_id(self):
        """Gets the job_id of this RetentionExecutionTask.  # noqa: E501


        :return: The job_id of this RetentionExecutionTask.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this RetentionExecutionTask.


        :param job_id: The job_id of this RetentionExecutionTask.  # noqa: E501
        :type: str
        """

        self._job_id = job_id

    @property
    def status(self):
        """Gets the status of this RetentionExecutionTask.  # noqa: E501


        :return: The status of this RetentionExecutionTask.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RetentionExecutionTask.


        :param status: The status of this RetentionExecutionTask.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def status_code(self):
        """Gets the status_code of this RetentionExecutionTask.  # noqa: E501


        :return: The status_code of this RetentionExecutionTask.  # noqa: E501
        :rtype: int
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this RetentionExecutionTask.


        :param status_code: The status_code of this RetentionExecutionTask.  # noqa: E501
        :type: int
        """

        self._status_code = status_code

    @property
    def status_revision(self):
        """Gets the status_revision of this RetentionExecutionTask.  # noqa: E501


        :return: The status_revision of this RetentionExecutionTask.  # noqa: E501
        :rtype: int
        """
        return self._status_revision

    @status_revision.setter
    def status_revision(self, status_revision):
        """Sets the status_revision of this RetentionExecutionTask.


        :param status_revision: The status_revision of this RetentionExecutionTask.  # noqa: E501
        :type: int
        """

        self._status_revision = status_revision

    @property
    def start_time(self):
        """Gets the start_time of this RetentionExecutionTask.  # noqa: E501


        :return: The start_time of this RetentionExecutionTask.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this RetentionExecutionTask.


        :param start_time: The start_time of this RetentionExecutionTask.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this RetentionExecutionTask.  # noqa: E501


        :return: The end_time of this RetentionExecutionTask.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this RetentionExecutionTask.


        :param end_time: The end_time of this RetentionExecutionTask.  # noqa: E501
        :type: str
        """

        self._end_time = end_time

    @property
    def total(self):
        """Gets the total of this RetentionExecutionTask.  # noqa: E501


        :return: The total of this RetentionExecutionTask.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this RetentionExecutionTask.


        :param total: The total of this RetentionExecutionTask.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def retained(self):
        """Gets the retained of this RetentionExecutionTask.  # noqa: E501


        :return: The retained of this RetentionExecutionTask.  # noqa: E501
        :rtype: int
        """
        return self._retained

    @retained.setter
    def retained(self, retained):
        """Sets the retained of this RetentionExecutionTask.


        :param retained: The retained of this RetentionExecutionTask.  # noqa: E501
        :type: int
        """

        self._retained = retained

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
        if issubclass(RetentionExecutionTask, dict):
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
        if not isinstance(other, RetentionExecutionTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other