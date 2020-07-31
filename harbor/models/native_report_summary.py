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


class NativeReportSummary(object):
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
        'report_id': 'str',
        'scan_status': 'str',
        'severity': 'str',
        'duration': 'int',
        'summary': 'VulnerabilitySummary',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'complete_percent': 'int'
    }

    attribute_map = {
        'report_id': 'report_id',
        'scan_status': 'scan_status',
        'severity': 'severity',
        'duration': 'duration',
        'summary': 'summary',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'complete_percent': 'complete_percent'
    }

    def __init__(self, report_id=None, scan_status=None, severity=None, duration=None, summary=None, start_time=None, end_time=None, complete_percent=None):  # noqa: E501
        """NativeReportSummary - a model defined in Swagger"""  # noqa: E501
        self._report_id = None
        self._scan_status = None
        self._severity = None
        self._duration = None
        self._summary = None
        self._start_time = None
        self._end_time = None
        self._complete_percent = None
        self.discriminator = None
        if report_id is not None:
            self.report_id = report_id
        if scan_status is not None:
            self.scan_status = scan_status
        if severity is not None:
            self.severity = severity
        if duration is not None:
            self.duration = duration
        if summary is not None:
            self.summary = summary
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if complete_percent is not None:
            self.complete_percent = complete_percent

    @property
    def report_id(self):
        """Gets the report_id of this NativeReportSummary.  # noqa: E501

        id of the native scan report  # noqa: E501

        :return: The report_id of this NativeReportSummary.  # noqa: E501
        :rtype: str
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        """Sets the report_id of this NativeReportSummary.

        id of the native scan report  # noqa: E501

        :param report_id: The report_id of this NativeReportSummary.  # noqa: E501
        :type: str
        """

        self._report_id = report_id

    @property
    def scan_status(self):
        """Gets the scan_status of this NativeReportSummary.  # noqa: E501

        The status of the report generating process  # noqa: E501

        :return: The scan_status of this NativeReportSummary.  # noqa: E501
        :rtype: str
        """
        return self._scan_status

    @scan_status.setter
    def scan_status(self, scan_status):
        """Sets the scan_status of this NativeReportSummary.

        The status of the report generating process  # noqa: E501

        :param scan_status: The scan_status of this NativeReportSummary.  # noqa: E501
        :type: str
        """

        self._scan_status = scan_status

    @property
    def severity(self):
        """Gets the severity of this NativeReportSummary.  # noqa: E501

        The overall severity  # noqa: E501

        :return: The severity of this NativeReportSummary.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this NativeReportSummary.

        The overall severity  # noqa: E501

        :param severity: The severity of this NativeReportSummary.  # noqa: E501
        :type: str
        """

        self._severity = severity

    @property
    def duration(self):
        """Gets the duration of this NativeReportSummary.  # noqa: E501

        The seconds spent for generating the report  # noqa: E501

        :return: The duration of this NativeReportSummary.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this NativeReportSummary.

        The seconds spent for generating the report  # noqa: E501

        :param duration: The duration of this NativeReportSummary.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def summary(self):
        """Gets the summary of this NativeReportSummary.  # noqa: E501


        :return: The summary of this NativeReportSummary.  # noqa: E501
        :rtype: VulnerabilitySummary
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this NativeReportSummary.


        :param summary: The summary of this NativeReportSummary.  # noqa: E501
        :type: VulnerabilitySummary
        """

        self._summary = summary

    @property
    def start_time(self):
        """Gets the start_time of this NativeReportSummary.  # noqa: E501

        The start time of the scan process that generating report  # noqa: E501

        :return: The start_time of this NativeReportSummary.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this NativeReportSummary.

        The start time of the scan process that generating report  # noqa: E501

        :param start_time: The start_time of this NativeReportSummary.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this NativeReportSummary.  # noqa: E501

        The end time of the scan process that generating report  # noqa: E501

        :return: The end_time of this NativeReportSummary.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this NativeReportSummary.

        The end time of the scan process that generating report  # noqa: E501

        :param end_time: The end_time of this NativeReportSummary.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

    @property
    def complete_percent(self):
        """Gets the complete_percent of this NativeReportSummary.  # noqa: E501

        The complete percent of the scanning which value is between 0 and 100  # noqa: E501

        :return: The complete_percent of this NativeReportSummary.  # noqa: E501
        :rtype: int
        """
        return self._complete_percent

    @complete_percent.setter
    def complete_percent(self, complete_percent):
        """Sets the complete_percent of this NativeReportSummary.

        The complete percent of the scanning which value is between 0 and 100  # noqa: E501

        :param complete_percent: The complete_percent of this NativeReportSummary.  # noqa: E501
        :type: int
        """

        self._complete_percent = complete_percent

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
        if issubclass(NativeReportSummary, dict):
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
        if not isinstance(other, NativeReportSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other