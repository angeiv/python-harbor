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

class GCHistory(object):
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
        'job_name': 'str',
        'job_kind': 'str',
        'job_parameters': 'str',
        'schedule': 'ScheduleObj',
        'job_status': 'str',
        'deleted': 'bool',
        'creation_time': 'datetime',
        'update_time': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'job_name': 'job_name',
        'job_kind': 'job_kind',
        'job_parameters': 'job_parameters',
        'schedule': 'schedule',
        'job_status': 'job_status',
        'deleted': 'deleted',
        'creation_time': 'creation_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, job_name=None, job_kind=None, job_parameters=None, schedule=None, job_status=None, deleted=None, creation_time=None, update_time=None):  # noqa: E501
        """GCHistory - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._job_name = None
        self._job_kind = None
        self._job_parameters = None
        self._schedule = None
        self._job_status = None
        self._deleted = None
        self._creation_time = None
        self._update_time = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if job_name is not None:
            self.job_name = job_name
        if job_kind is not None:
            self.job_kind = job_kind
        if job_parameters is not None:
            self.job_parameters = job_parameters
        if schedule is not None:
            self.schedule = schedule
        if job_status is not None:
            self.job_status = job_status
        if deleted is not None:
            self.deleted = deleted
        if creation_time is not None:
            self.creation_time = creation_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        """Gets the id of this GCHistory.  # noqa: E501

        the id of gc job.  # noqa: E501

        :return: The id of this GCHistory.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GCHistory.

        the id of gc job.  # noqa: E501

        :param id: The id of this GCHistory.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def job_name(self):
        """Gets the job_name of this GCHistory.  # noqa: E501

        the job name of gc job.  # noqa: E501

        :return: The job_name of this GCHistory.  # noqa: E501
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this GCHistory.

        the job name of gc job.  # noqa: E501

        :param job_name: The job_name of this GCHistory.  # noqa: E501
        :type: str
        """

        self._job_name = job_name

    @property
    def job_kind(self):
        """Gets the job_kind of this GCHistory.  # noqa: E501

        the job kind of gc job.  # noqa: E501

        :return: The job_kind of this GCHistory.  # noqa: E501
        :rtype: str
        """
        return self._job_kind

    @job_kind.setter
    def job_kind(self, job_kind):
        """Sets the job_kind of this GCHistory.

        the job kind of gc job.  # noqa: E501

        :param job_kind: The job_kind of this GCHistory.  # noqa: E501
        :type: str
        """

        self._job_kind = job_kind

    @property
    def job_parameters(self):
        """Gets the job_parameters of this GCHistory.  # noqa: E501

        the job parameters of gc job.  # noqa: E501

        :return: The job_parameters of this GCHistory.  # noqa: E501
        :rtype: str
        """
        return self._job_parameters

    @job_parameters.setter
    def job_parameters(self, job_parameters):
        """Sets the job_parameters of this GCHistory.

        the job parameters of gc job.  # noqa: E501

        :param job_parameters: The job_parameters of this GCHistory.  # noqa: E501
        :type: str
        """

        self._job_parameters = job_parameters

    @property
    def schedule(self):
        """Gets the schedule of this GCHistory.  # noqa: E501


        :return: The schedule of this GCHistory.  # noqa: E501
        :rtype: ScheduleObj
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this GCHistory.


        :param schedule: The schedule of this GCHistory.  # noqa: E501
        :type: ScheduleObj
        """

        self._schedule = schedule

    @property
    def job_status(self):
        """Gets the job_status of this GCHistory.  # noqa: E501

        the status of gc job.  # noqa: E501

        :return: The job_status of this GCHistory.  # noqa: E501
        :rtype: str
        """
        return self._job_status

    @job_status.setter
    def job_status(self, job_status):
        """Sets the job_status of this GCHistory.

        the status of gc job.  # noqa: E501

        :param job_status: The job_status of this GCHistory.  # noqa: E501
        :type: str
        """

        self._job_status = job_status

    @property
    def deleted(self):
        """Gets the deleted of this GCHistory.  # noqa: E501

        if gc job was deleted.  # noqa: E501

        :return: The deleted of this GCHistory.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this GCHistory.

        if gc job was deleted.  # noqa: E501

        :param deleted: The deleted of this GCHistory.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def creation_time(self):
        """Gets the creation_time of this GCHistory.  # noqa: E501

        the creation time of gc job.  # noqa: E501

        :return: The creation_time of this GCHistory.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this GCHistory.

        the creation time of gc job.  # noqa: E501

        :param creation_time: The creation_time of this GCHistory.  # noqa: E501
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def update_time(self):
        """Gets the update_time of this GCHistory.  # noqa: E501

        the update time of gc job.  # noqa: E501

        :return: The update_time of this GCHistory.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this GCHistory.

        the update time of gc job.  # noqa: E501

        :param update_time: The update_time of this GCHistory.  # noqa: E501
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
        if issubclass(GCHistory, dict):
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
        if not isinstance(other, GCHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
