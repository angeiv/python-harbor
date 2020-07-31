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


class ConfigurationsResponse(object):
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
        'auth_mode': 'StringConfigItem',
        'count_per_project': 'IntegerConfigItem',
        'email_from': 'StringConfigItem',
        'email_host': 'StringConfigItem',
        'email_port': 'IntegerConfigItem',
        'email_identity': 'StringConfigItem',
        'email_username': 'StringConfigItem',
        'email_ssl': 'BoolConfigItem',
        'email_insecure': 'BoolConfigItem',
        'ldap_url': 'StringConfigItem',
        'ldap_base_dn': 'StringConfigItem',
        'ldap_filter': 'StringConfigItem',
        'ldap_scope': 'int',
        'ldap_uid': 'StringConfigItem',
        'ldap_search_dn': 'str',
        'ldap_timeout': 'IntegerConfigItem',
        'ldap_group_attribute_name': 'StringConfigItem',
        'ldap_group_base_dn': 'StringConfigItem',
        'ldap_group_search_filter': 'StringConfigItem',
        'ldap_group_search_scope': 'IntegerConfigItem',
        'ldap_group_admin_dn': 'StringConfigItem',
        'oidc_client_id': 'StringConfigItem',
        'oidc_endpoint': 'StringConfigItem',
        'oidc_name': 'StringConfigItem',
        'oidc_scope': 'StringConfigItem',
        'oidc_verify_cert': 'BoolConfigItem',
        'project_creation_restriction': 'StringConfigItem',
        'quota_per_project_enable': 'BoolConfigItem',
        'read_only': 'BoolConfigItem',
        'self_registration': 'BoolConfigItem',
        'storage_per_project': 'IntegerConfigItem',
        'token_expiration': 'IntegerConfigItem',
        'verify_remote_cert': 'BoolConfigItem',
        'scan_all_policy': 'ConfigurationsScanAllPolicy'
    }

    attribute_map = {
        'auth_mode': 'auth_mode',
        'count_per_project': 'count_per_project',
        'email_from': 'email_from',
        'email_host': 'email_host',
        'email_port': 'email_port',
        'email_identity': 'email_identity',
        'email_username': 'email_username',
        'email_ssl': 'email_ssl',
        'email_insecure': 'email_insecure',
        'ldap_url': 'ldap_url',
        'ldap_base_dn': 'ldap_base_dn',
        'ldap_filter': 'ldap_filter',
        'ldap_scope': 'ldap_scope',
        'ldap_uid': 'ldap_uid',
        'ldap_search_dn': 'ldap_search_dn',
        'ldap_timeout': 'ldap_timeout',
        'ldap_group_attribute_name': 'ldap_group_attribute_name',
        'ldap_group_base_dn': 'ldap_group_base_dn',
        'ldap_group_search_filter': 'ldap_group_search_filter',
        'ldap_group_search_scope': 'ldap_group_search_scope',
        'ldap_group_admin_dn': 'ldap_group_admin_dn',
        'oidc_client_id': 'oidc_client_id',
        'oidc_endpoint': 'oidc_endpoint',
        'oidc_name': 'oidc_name',
        'oidc_scope': 'oidc_scope',
        'oidc_verify_cert': 'oidc_verify_cert',
        'project_creation_restriction': 'project_creation_restriction',
        'quota_per_project_enable': 'quota_per_project_enable',
        'read_only': 'read_only',
        'self_registration': 'self_registration',
        'storage_per_project': 'storage_per_project',
        'token_expiration': 'token_expiration',
        'verify_remote_cert': 'verify_remote_cert',
        'scan_all_policy': 'scan_all_policy'
    }

    def __init__(self, auth_mode=None, count_per_project=None, email_from=None, email_host=None, email_port=None, email_identity=None, email_username=None, email_ssl=None, email_insecure=None, ldap_url=None, ldap_base_dn=None, ldap_filter=None, ldap_scope=None, ldap_uid=None, ldap_search_dn=None, ldap_timeout=None, ldap_group_attribute_name=None, ldap_group_base_dn=None, ldap_group_search_filter=None, ldap_group_search_scope=None, ldap_group_admin_dn=None, oidc_client_id=None, oidc_endpoint=None, oidc_name=None, oidc_scope=None, oidc_verify_cert=None, project_creation_restriction=None, quota_per_project_enable=None, read_only=None, self_registration=None, storage_per_project=None, token_expiration=None, verify_remote_cert=None, scan_all_policy=None):  # noqa: E501
        """ConfigurationsResponse - a model defined in Swagger"""  # noqa: E501
        self._auth_mode = None
        self._count_per_project = None
        self._email_from = None
        self._email_host = None
        self._email_port = None
        self._email_identity = None
        self._email_username = None
        self._email_ssl = None
        self._email_insecure = None
        self._ldap_url = None
        self._ldap_base_dn = None
        self._ldap_filter = None
        self._ldap_scope = None
        self._ldap_uid = None
        self._ldap_search_dn = None
        self._ldap_timeout = None
        self._ldap_group_attribute_name = None
        self._ldap_group_base_dn = None
        self._ldap_group_search_filter = None
        self._ldap_group_search_scope = None
        self._ldap_group_admin_dn = None
        self._oidc_client_id = None
        self._oidc_endpoint = None
        self._oidc_name = None
        self._oidc_scope = None
        self._oidc_verify_cert = None
        self._project_creation_restriction = None
        self._quota_per_project_enable = None
        self._read_only = None
        self._self_registration = None
        self._storage_per_project = None
        self._token_expiration = None
        self._verify_remote_cert = None
        self._scan_all_policy = None
        self.discriminator = None
        if auth_mode is not None:
            self.auth_mode = auth_mode
        if count_per_project is not None:
            self.count_per_project = count_per_project
        if email_from is not None:
            self.email_from = email_from
        if email_host is not None:
            self.email_host = email_host
        if email_port is not None:
            self.email_port = email_port
        if email_identity is not None:
            self.email_identity = email_identity
        if email_username is not None:
            self.email_username = email_username
        if email_ssl is not None:
            self.email_ssl = email_ssl
        if email_insecure is not None:
            self.email_insecure = email_insecure
        if ldap_url is not None:
            self.ldap_url = ldap_url
        if ldap_base_dn is not None:
            self.ldap_base_dn = ldap_base_dn
        if ldap_filter is not None:
            self.ldap_filter = ldap_filter
        if ldap_scope is not None:
            self.ldap_scope = ldap_scope
        if ldap_uid is not None:
            self.ldap_uid = ldap_uid
        if ldap_search_dn is not None:
            self.ldap_search_dn = ldap_search_dn
        if ldap_timeout is not None:
            self.ldap_timeout = ldap_timeout
        if ldap_group_attribute_name is not None:
            self.ldap_group_attribute_name = ldap_group_attribute_name
        if ldap_group_base_dn is not None:
            self.ldap_group_base_dn = ldap_group_base_dn
        if ldap_group_search_filter is not None:
            self.ldap_group_search_filter = ldap_group_search_filter
        if ldap_group_search_scope is not None:
            self.ldap_group_search_scope = ldap_group_search_scope
        if ldap_group_admin_dn is not None:
            self.ldap_group_admin_dn = ldap_group_admin_dn
        if oidc_client_id is not None:
            self.oidc_client_id = oidc_client_id
        if oidc_endpoint is not None:
            self.oidc_endpoint = oidc_endpoint
        if oidc_name is not None:
            self.oidc_name = oidc_name
        if oidc_scope is not None:
            self.oidc_scope = oidc_scope
        if oidc_verify_cert is not None:
            self.oidc_verify_cert = oidc_verify_cert
        if project_creation_restriction is not None:
            self.project_creation_restriction = project_creation_restriction
        if quota_per_project_enable is not None:
            self.quota_per_project_enable = quota_per_project_enable
        if read_only is not None:
            self.read_only = read_only
        if self_registration is not None:
            self.self_registration = self_registration
        if storage_per_project is not None:
            self.storage_per_project = storage_per_project
        if token_expiration is not None:
            self.token_expiration = token_expiration
        if verify_remote_cert is not None:
            self.verify_remote_cert = verify_remote_cert
        if scan_all_policy is not None:
            self.scan_all_policy = scan_all_policy

    @property
    def auth_mode(self):
        """Gets the auth_mode of this ConfigurationsResponse.  # noqa: E501


        :return: The auth_mode of this ConfigurationsResponse.  # noqa: E501
        :rtype: StringConfigItem
        """
        return self._auth_mode

    @auth_mode.setter
    def auth_mode(self, auth_mode):
        """Sets the auth_mode of this ConfigurationsResponse.


        :param auth_mode: The auth_mode of this ConfigurationsResponse.  # noqa: E501
        :type: StringConfigItem
        """

        self._auth_mode = auth_mode

    @property
    def count_per_project(self):
        """Gets the count_per_project of this ConfigurationsResponse.  # noqa: E501


        :return: The count_per_project of this ConfigurationsResponse.  # noqa: E501
        :rtype: IntegerConfigItem
        """
        return self._count_per_project

    @count_per_project.setter
    def count_per_project(self, count_per_project):
        """Sets the count_per_project of this ConfigurationsResponse.


        :param count_per_project: The count_per_project of this ConfigurationsResponse.  # noqa: E501
        :type: IntegerConfigItem
        """

        self._count_per_project = count_per_project

    @property
    def email_from(self):
        """Gets the email_from of this ConfigurationsResponse.  # noqa: E501


        :return: The email_from of this ConfigurationsResponse.  # noqa: E501
        :rtype: StringConfigItem
        """
        return self._email_from

    @email_from.setter
    def email_from(self, email_from):
        """Sets the email_from of this ConfigurationsResponse.


        :param email_from: The email_from of this ConfigurationsResponse.  # noqa: E501
        :type: StringConfigItem
        """

        self._email_from = email_from

    @property
    def email_host(self):
        """Gets the email_host of this ConfigurationsResponse.  # noqa: E501


        :return: The email_host of this ConfigurationsResponse.  # noqa: E501
        :rtype: StringConfigItem
        """
        return self._email_host

    @email_host.setter
    def email_host(self, email_host):
        """Sets the email_host of this ConfigurationsResponse.


        :param email_host: The email_host of this ConfigurationsResponse.  # noqa: E501
        :type: StringConfigItem
        """

        self._email_host = email_host

    @property
    def email_port(self):
        """Gets the email_port of this ConfigurationsResponse.  # noqa: E501


        :return: The email_port of this ConfigurationsResponse.  # noqa: E501
        :rtype: IntegerConfigItem
        """
        return self._email_port

    @email_port.setter
    def email_port(self, email_port):
        """Sets the email_port of this ConfigurationsResponse.


        :param email_port: The email_port of this ConfigurationsResponse.  # noqa: E501
        :type: IntegerConfigItem
        """

        self._email_port = email_port

    @property
    def email_identity(self):
        """Gets the email_identity of this ConfigurationsResponse.  # noqa: E501


        :return: The email_identity of this ConfigurationsResponse.  # noqa: E501
        :rtype: StringConfigItem
        """
        return self._email_identity

    @email_identity.setter
    def email_identity(self, email_identity):
        """Sets the email_identity of this ConfigurationsResponse.


        :param email_identity: The email_identity of this ConfigurationsResponse.  # noqa: E501
        :type: StringConfigItem
        """

        self._email_identity = email_identity

    @property
    def email_username(self):
        """Gets the email_username of this ConfigurationsResponse.  # noqa: E501


        :return: The email_username of this ConfigurationsResponse.  # noqa: E501
        :rtype: StringConfigItem
        """
        return self._email_username

    @email_username.setter
    def email_username(self, email_username):
        """Sets the email_username of this ConfigurationsResponse.


        :param email_username: The email_username of this ConfigurationsResponse.  # noqa: E501
        :type: StringConfigItem
        """

        self._email_username = email_username

    @property
    def email_ssl(self):
        """Gets the email_ssl of this ConfigurationsResponse.  # noqa: E501


        :return: The email_ssl of this ConfigurationsResponse.  # noqa: E501
        :rtype: BoolConfigItem
        """
        return self._email_ssl

    @email_ssl.setter
    def email_ssl(self, email_ssl):
        """Sets the email_ssl of this ConfigurationsResponse.


        :param email_ssl: The email_ssl of this ConfigurationsResponse.  # noqa: E501
        :type: BoolConfigItem
        """

        self._email_ssl = email_ssl

    @property
    def email_insecure(self):
        """Gets the email_insecure of this ConfigurationsResponse.  # noqa: E501


        :return: The email_insecure of this ConfigurationsResponse.  # noqa: E501
        :rtype: BoolConfigItem
        """
        return self._email_insecure

    @email_insecure.setter
    def email_insecure(self, email_insecure):
        """Sets the email_insecure of this ConfigurationsResponse.


        :param email_insecure: The email_insecure of this ConfigurationsResponse.  # noqa: E501
        :type: BoolConfigItem
        """

        self._email_insecure = email_insecure

    @property
    def ldap_url(self):
        """Gets the ldap_url of this ConfigurationsResponse.  # noqa: E501


        :return: The ldap_url of this ConfigurationsResponse.  # noqa: E501
        :rtype: StringConfigItem
        """
        return self._ldap_url

    @ldap_url.setter
    def ldap_url(self, ldap_url):
        """Sets the ldap_url of this ConfigurationsResponse.


        :param ldap_url: The ldap_url of this ConfigurationsResponse.  # noqa: E501
        :type: StringConfigItem
        """

        self._ldap_url = ldap_url

    @property
    def ldap_base_dn(self):
        """Gets the ldap_base_dn of this ConfigurationsResponse.  # noqa: E501


        :return: The ldap_base_dn of this ConfigurationsResponse.  # noqa: E501
        :rtype: StringConfigItem
        """
        return self._ldap_base_dn

    @ldap_base_dn.setter
    def ldap_base_dn(self, ldap_base_dn):
        """Sets the ldap_base_dn of this ConfigurationsResponse.


        :param ldap_base_dn: The ldap_base_dn of this ConfigurationsResponse.  # noqa: E501
        :type: StringConfigItem
        """

        self._ldap_base_dn = ldap_base_dn

    @property
    def ldap_filter(self):
        """Gets the ldap_filter of this ConfigurationsResponse.  # noqa: E501


        :return: The ldap_filter of this ConfigurationsResponse.  # noqa: E501
        :rtype: StringConfigItem
        """
        return self._ldap_filter

    @ldap_filter.setter
    def ldap_filter(self, ldap_filter):
        """Sets the ldap_filter of this ConfigurationsResponse.


        :param ldap_filter: The ldap_filter of this ConfigurationsResponse.  # noqa: E501
        :type: StringConfigItem
        """

        self._ldap_filter = ldap_filter

    @property
    def ldap_scope(self):
        """Gets the ldap_scope of this ConfigurationsResponse.  # noqa: E501

        0-LDAP_SCOPE_BASE, 1-LDAP_SCOPE_ONELEVEL, 2-LDAP_SCOPE_SUBTREE  # noqa: E501

        :return: The ldap_scope of this ConfigurationsResponse.  # noqa: E501
        :rtype: int
        """
        return self._ldap_scope

    @ldap_scope.setter
    def ldap_scope(self, ldap_scope):
        """Sets the ldap_scope of this ConfigurationsResponse.

        0-LDAP_SCOPE_BASE, 1-LDAP_SCOPE_ONELEVEL, 2-LDAP_SCOPE_SUBTREE  # noqa: E501

        :param ldap_scope: The ldap_scope of this ConfigurationsResponse.  # noqa: E501
        :type: int
        """

        self._ldap_scope = ldap_scope

    @property
    def ldap_uid(self):
        """Gets the ldap_uid of this ConfigurationsResponse.  # noqa: E501


        :return: The ldap_uid of this ConfigurationsResponse.  # noqa: E501
        :rtype: StringConfigItem
        """
        return self._ldap_uid

    @ldap_uid.setter
    def ldap_uid(self, ldap_uid):
        """Sets the ldap_uid of this ConfigurationsResponse.


        :param ldap_uid: The ldap_uid of this ConfigurationsResponse.  # noqa: E501
        :type: StringConfigItem
        """

        self._ldap_uid = ldap_uid

    @property
    def ldap_search_dn(self):
        """Gets the ldap_search_dn of this ConfigurationsResponse.  # noqa: E501

        The DN of the user to do the search.  # noqa: E501

        :return: The ldap_search_dn of this ConfigurationsResponse.  # noqa: E501
        :rtype: str
        """
        return self._ldap_search_dn

    @ldap_search_dn.setter
    def ldap_search_dn(self, ldap_search_dn):
        """Sets the ldap_search_dn of this ConfigurationsResponse.

        The DN of the user to do the search.  # noqa: E501

        :param ldap_search_dn: The ldap_search_dn of this ConfigurationsResponse.  # noqa: E501
        :type: str
        """

        self._ldap_search_dn = ldap_search_dn

    @property
    def ldap_timeout(self):
        """Gets the ldap_timeout of this ConfigurationsResponse.  # noqa: E501


        :return: The ldap_timeout of this ConfigurationsResponse.  # noqa: E501
        :rtype: IntegerConfigItem
        """
        return self._ldap_timeout

    @ldap_timeout.setter
    def ldap_timeout(self, ldap_timeout):
        """Sets the ldap_timeout of this ConfigurationsResponse.


        :param ldap_timeout: The ldap_timeout of this ConfigurationsResponse.  # noqa: E501
        :type: IntegerConfigItem
        """

        self._ldap_timeout = ldap_timeout

    @property
    def ldap_group_attribute_name(self):
        """Gets the ldap_group_attribute_name of this ConfigurationsResponse.  # noqa: E501


        :return: The ldap_group_attribute_name of this ConfigurationsResponse.  # noqa: E501
        :rtype: StringConfigItem
        """
        return self._ldap_group_attribute_name

    @ldap_group_attribute_name.setter
    def ldap_group_attribute_name(self, ldap_group_attribute_name):
        """Sets the ldap_group_attribute_name of this ConfigurationsResponse.


        :param ldap_group_attribute_name: The ldap_group_attribute_name of this ConfigurationsResponse.  # noqa: E501
        :type: StringConfigItem
        """

        self._ldap_group_attribute_name = ldap_group_attribute_name

    @property
    def ldap_group_base_dn(self):
        """Gets the ldap_group_base_dn of this ConfigurationsResponse.  # noqa: E501


        :return: The ldap_group_base_dn of this ConfigurationsResponse.  # noqa: E501
        :rtype: StringConfigItem
        """
        return self._ldap_group_base_dn

    @ldap_group_base_dn.setter
    def ldap_group_base_dn(self, ldap_group_base_dn):
        """Sets the ldap_group_base_dn of this ConfigurationsResponse.


        :param ldap_group_base_dn: The ldap_group_base_dn of this ConfigurationsResponse.  # noqa: E501
        :type: StringConfigItem
        """

        self._ldap_group_base_dn = ldap_group_base_dn

    @property
    def ldap_group_search_filter(self):
        """Gets the ldap_group_search_filter of this ConfigurationsResponse.  # noqa: E501


        :return: The ldap_group_search_filter of this ConfigurationsResponse.  # noqa: E501
        :rtype: StringConfigItem
        """
        return self._ldap_group_search_filter

    @ldap_group_search_filter.setter
    def ldap_group_search_filter(self, ldap_group_search_filter):
        """Sets the ldap_group_search_filter of this ConfigurationsResponse.


        :param ldap_group_search_filter: The ldap_group_search_filter of this ConfigurationsResponse.  # noqa: E501
        :type: StringConfigItem
        """

        self._ldap_group_search_filter = ldap_group_search_filter

    @property
    def ldap_group_search_scope(self):
        """Gets the ldap_group_search_scope of this ConfigurationsResponse.  # noqa: E501


        :return: The ldap_group_search_scope of this ConfigurationsResponse.  # noqa: E501
        :rtype: IntegerConfigItem
        """
        return self._ldap_group_search_scope

    @ldap_group_search_scope.setter
    def ldap_group_search_scope(self, ldap_group_search_scope):
        """Sets the ldap_group_search_scope of this ConfigurationsResponse.


        :param ldap_group_search_scope: The ldap_group_search_scope of this ConfigurationsResponse.  # noqa: E501
        :type: IntegerConfigItem
        """

        self._ldap_group_search_scope = ldap_group_search_scope

    @property
    def ldap_group_admin_dn(self):
        """Gets the ldap_group_admin_dn of this ConfigurationsResponse.  # noqa: E501


        :return: The ldap_group_admin_dn of this ConfigurationsResponse.  # noqa: E501
        :rtype: StringConfigItem
        """
        return self._ldap_group_admin_dn

    @ldap_group_admin_dn.setter
    def ldap_group_admin_dn(self, ldap_group_admin_dn):
        """Sets the ldap_group_admin_dn of this ConfigurationsResponse.


        :param ldap_group_admin_dn: The ldap_group_admin_dn of this ConfigurationsResponse.  # noqa: E501
        :type: StringConfigItem
        """

        self._ldap_group_admin_dn = ldap_group_admin_dn

    @property
    def oidc_client_id(self):
        """Gets the oidc_client_id of this ConfigurationsResponse.  # noqa: E501


        :return: The oidc_client_id of this ConfigurationsResponse.  # noqa: E501
        :rtype: StringConfigItem
        """
        return self._oidc_client_id

    @oidc_client_id.setter
    def oidc_client_id(self, oidc_client_id):
        """Sets the oidc_client_id of this ConfigurationsResponse.


        :param oidc_client_id: The oidc_client_id of this ConfigurationsResponse.  # noqa: E501
        :type: StringConfigItem
        """

        self._oidc_client_id = oidc_client_id

    @property
    def oidc_endpoint(self):
        """Gets the oidc_endpoint of this ConfigurationsResponse.  # noqa: E501


        :return: The oidc_endpoint of this ConfigurationsResponse.  # noqa: E501
        :rtype: StringConfigItem
        """
        return self._oidc_endpoint

    @oidc_endpoint.setter
    def oidc_endpoint(self, oidc_endpoint):
        """Sets the oidc_endpoint of this ConfigurationsResponse.


        :param oidc_endpoint: The oidc_endpoint of this ConfigurationsResponse.  # noqa: E501
        :type: StringConfigItem
        """

        self._oidc_endpoint = oidc_endpoint

    @property
    def oidc_name(self):
        """Gets the oidc_name of this ConfigurationsResponse.  # noqa: E501


        :return: The oidc_name of this ConfigurationsResponse.  # noqa: E501
        :rtype: StringConfigItem
        """
        return self._oidc_name

    @oidc_name.setter
    def oidc_name(self, oidc_name):
        """Sets the oidc_name of this ConfigurationsResponse.


        :param oidc_name: The oidc_name of this ConfigurationsResponse.  # noqa: E501
        :type: StringConfigItem
        """

        self._oidc_name = oidc_name

    @property
    def oidc_scope(self):
        """Gets the oidc_scope of this ConfigurationsResponse.  # noqa: E501


        :return: The oidc_scope of this ConfigurationsResponse.  # noqa: E501
        :rtype: StringConfigItem
        """
        return self._oidc_scope

    @oidc_scope.setter
    def oidc_scope(self, oidc_scope):
        """Sets the oidc_scope of this ConfigurationsResponse.


        :param oidc_scope: The oidc_scope of this ConfigurationsResponse.  # noqa: E501
        :type: StringConfigItem
        """

        self._oidc_scope = oidc_scope

    @property
    def oidc_verify_cert(self):
        """Gets the oidc_verify_cert of this ConfigurationsResponse.  # noqa: E501


        :return: The oidc_verify_cert of this ConfigurationsResponse.  # noqa: E501
        :rtype: BoolConfigItem
        """
        return self._oidc_verify_cert

    @oidc_verify_cert.setter
    def oidc_verify_cert(self, oidc_verify_cert):
        """Sets the oidc_verify_cert of this ConfigurationsResponse.


        :param oidc_verify_cert: The oidc_verify_cert of this ConfigurationsResponse.  # noqa: E501
        :type: BoolConfigItem
        """

        self._oidc_verify_cert = oidc_verify_cert

    @property
    def project_creation_restriction(self):
        """Gets the project_creation_restriction of this ConfigurationsResponse.  # noqa: E501


        :return: The project_creation_restriction of this ConfigurationsResponse.  # noqa: E501
        :rtype: StringConfigItem
        """
        return self._project_creation_restriction

    @project_creation_restriction.setter
    def project_creation_restriction(self, project_creation_restriction):
        """Sets the project_creation_restriction of this ConfigurationsResponse.


        :param project_creation_restriction: The project_creation_restriction of this ConfigurationsResponse.  # noqa: E501
        :type: StringConfigItem
        """

        self._project_creation_restriction = project_creation_restriction

    @property
    def quota_per_project_enable(self):
        """Gets the quota_per_project_enable of this ConfigurationsResponse.  # noqa: E501


        :return: The quota_per_project_enable of this ConfigurationsResponse.  # noqa: E501
        :rtype: BoolConfigItem
        """
        return self._quota_per_project_enable

    @quota_per_project_enable.setter
    def quota_per_project_enable(self, quota_per_project_enable):
        """Sets the quota_per_project_enable of this ConfigurationsResponse.


        :param quota_per_project_enable: The quota_per_project_enable of this ConfigurationsResponse.  # noqa: E501
        :type: BoolConfigItem
        """

        self._quota_per_project_enable = quota_per_project_enable

    @property
    def read_only(self):
        """Gets the read_only of this ConfigurationsResponse.  # noqa: E501


        :return: The read_only of this ConfigurationsResponse.  # noqa: E501
        :rtype: BoolConfigItem
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this ConfigurationsResponse.


        :param read_only: The read_only of this ConfigurationsResponse.  # noqa: E501
        :type: BoolConfigItem
        """

        self._read_only = read_only

    @property
    def self_registration(self):
        """Gets the self_registration of this ConfigurationsResponse.  # noqa: E501


        :return: The self_registration of this ConfigurationsResponse.  # noqa: E501
        :rtype: BoolConfigItem
        """
        return self._self_registration

    @self_registration.setter
    def self_registration(self, self_registration):
        """Sets the self_registration of this ConfigurationsResponse.


        :param self_registration: The self_registration of this ConfigurationsResponse.  # noqa: E501
        :type: BoolConfigItem
        """

        self._self_registration = self_registration

    @property
    def storage_per_project(self):
        """Gets the storage_per_project of this ConfigurationsResponse.  # noqa: E501


        :return: The storage_per_project of this ConfigurationsResponse.  # noqa: E501
        :rtype: IntegerConfigItem
        """
        return self._storage_per_project

    @storage_per_project.setter
    def storage_per_project(self, storage_per_project):
        """Sets the storage_per_project of this ConfigurationsResponse.


        :param storage_per_project: The storage_per_project of this ConfigurationsResponse.  # noqa: E501
        :type: IntegerConfigItem
        """

        self._storage_per_project = storage_per_project

    @property
    def token_expiration(self):
        """Gets the token_expiration of this ConfigurationsResponse.  # noqa: E501


        :return: The token_expiration of this ConfigurationsResponse.  # noqa: E501
        :rtype: IntegerConfigItem
        """
        return self._token_expiration

    @token_expiration.setter
    def token_expiration(self, token_expiration):
        """Sets the token_expiration of this ConfigurationsResponse.


        :param token_expiration: The token_expiration of this ConfigurationsResponse.  # noqa: E501
        :type: IntegerConfigItem
        """

        self._token_expiration = token_expiration

    @property
    def verify_remote_cert(self):
        """Gets the verify_remote_cert of this ConfigurationsResponse.  # noqa: E501


        :return: The verify_remote_cert of this ConfigurationsResponse.  # noqa: E501
        :rtype: BoolConfigItem
        """
        return self._verify_remote_cert

    @verify_remote_cert.setter
    def verify_remote_cert(self, verify_remote_cert):
        """Sets the verify_remote_cert of this ConfigurationsResponse.


        :param verify_remote_cert: The verify_remote_cert of this ConfigurationsResponse.  # noqa: E501
        :type: BoolConfigItem
        """

        self._verify_remote_cert = verify_remote_cert

    @property
    def scan_all_policy(self):
        """Gets the scan_all_policy of this ConfigurationsResponse.  # noqa: E501


        :return: The scan_all_policy of this ConfigurationsResponse.  # noqa: E501
        :rtype: ConfigurationsScanAllPolicy
        """
        return self._scan_all_policy

    @scan_all_policy.setter
    def scan_all_policy(self, scan_all_policy):
        """Sets the scan_all_policy of this ConfigurationsResponse.


        :param scan_all_policy: The scan_all_policy of this ConfigurationsResponse.  # noqa: E501
        :type: ConfigurationsScanAllPolicy
        """

        self._scan_all_policy = scan_all_policy

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
        if issubclass(ConfigurationsResponse, dict):
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
        if not isinstance(other, ConfigurationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
