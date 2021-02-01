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

class Schedule(object):
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
        'status': 'str',
        'creation_time': 'datetime',
        'update_time': 'datetime',
        'schedule': 'ScheduleObj',
        'parameters': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'creation_time': 'creation_time',
        'update_time': 'update_time',
        'schedule': 'schedule',
        'parameters': 'parameters'
    }

    def __init__(self, id=None, status=None, creation_time=None, update_time=None, schedule=None, parameters=None):  # noqa: E501
        """Schedule - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._status = None
        self._creation_time = None
        self._update_time = None
        self._schedule = None
        self._parameters = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if creation_time is not None:
            self.creation_time = creation_time
        if update_time is not None:
            self.update_time = update_time
        if schedule is not None:
            self.schedule = schedule
        if parameters is not None:
            self.parameters = parameters

    @property
    def id(self):
        """Gets the id of this Schedule.  # noqa: E501

        The id of the schedule.  # noqa: E501

        :return: The id of this Schedule.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Schedule.

        The id of the schedule.  # noqa: E501

        :param id: The id of this Schedule.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def status(self):
        """Gets the status of this Schedule.  # noqa: E501

        The status of the schedule.  # noqa: E501

        :return: The status of this Schedule.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Schedule.

        The status of the schedule.  # noqa: E501

        :param status: The status of this Schedule.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def creation_time(self):
        """Gets the creation_time of this Schedule.  # noqa: E501

        the creation time of the schedule.  # noqa: E501

        :return: The creation_time of this Schedule.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this Schedule.

        the creation time of the schedule.  # noqa: E501

        :param creation_time: The creation_time of this Schedule.  # noqa: E501
        :type: datetime
        """

        self._creation_time = creation_time

    @property
    def update_time(self):
        """Gets the update_time of this Schedule.  # noqa: E501

        the update time of the schedule.  # noqa: E501

        :return: The update_time of this Schedule.  # noqa: E501
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this Schedule.

        the update time of the schedule.  # noqa: E501

        :param update_time: The update_time of this Schedule.  # noqa: E501
        :type: datetime
        """

        self._update_time = update_time

    @property
    def schedule(self):
        """Gets the schedule of this Schedule.  # noqa: E501


        :return: The schedule of this Schedule.  # noqa: E501
        :rtype: ScheduleObj
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this Schedule.


        :param schedule: The schedule of this Schedule.  # noqa: E501
        :type: ScheduleObj
        """

        self._schedule = schedule

    @property
    def parameters(self):
        """Gets the parameters of this Schedule.  # noqa: E501

        The parameters of schedule job  # noqa: E501

        :return: The parameters of this Schedule.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this Schedule.

        The parameters of schedule job  # noqa: E501

        :param parameters: The parameters of this Schedule.  # noqa: E501
        :type: dict(str, object)
        """

        self._parameters = parameters

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
        if issubclass(Schedule, dict):
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
        if not isinstance(other, Schedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
