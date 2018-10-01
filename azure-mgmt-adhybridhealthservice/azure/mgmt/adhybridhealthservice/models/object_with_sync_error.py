# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ObjectWithSyncError(Model):
    """The objects with sync errors.

    :param source_of_authority: The source of authority.
    :type source_of_authority: str
    :param display_name: The display name.
    :type display_name: str
    :param object_type: The object type.
    :type object_type: str
    :param attribute_name: The attribute name.
    :type attribute_name: str
    :param attribute_value: The attribute value.
    :type attribute_value: str
    :param modififed_value: The modified value.
    :type modififed_value: str
    :param user_principal_name: The user principal name.
    :type user_principal_name: str
    :param object_guid: The object guid.
    :type object_guid: str
    :param attribute_multi_values: Indicates if the attribute is multi-valued
     or not.
    :type attribute_multi_values: bool
    :param min_limit: The minimum limit.
    :type min_limit: str
    :param max_limit: The maximum limit.
    :type max_limit: str
    :param distinguished_name: The distinguished name.
    :type distinguished_name: str
    :param mail: The email.
    :type mail: str
    :param time_occured: The date and time of occurrance.
    :type time_occured: datetime
    :param error_type: The error type.
    :type error_type: str
    :param source_anchor: The source anchor.
    :type source_anchor: str
    """

    _attribute_map = {
        'source_of_authority': {'key': 'sourceOfAuthority', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'object_type': {'key': 'objectType', 'type': 'str'},
        'attribute_name': {'key': 'attributeName', 'type': 'str'},
        'attribute_value': {'key': 'attributeValue', 'type': 'str'},
        'modififed_value': {'key': 'modififedValue', 'type': 'str'},
        'user_principal_name': {'key': 'userPrincipalName', 'type': 'str'},
        'object_guid': {'key': 'objectGuid', 'type': 'str'},
        'attribute_multi_values': {'key': 'attributeMultiValues', 'type': 'bool'},
        'min_limit': {'key': 'minLimit', 'type': 'str'},
        'max_limit': {'key': 'maxLimit', 'type': 'str'},
        'distinguished_name': {'key': 'distinguishedName', 'type': 'str'},
        'mail': {'key': 'mail', 'type': 'str'},
        'time_occured': {'key': 'timeOccured', 'type': 'iso-8601'},
        'error_type': {'key': 'errorType', 'type': 'str'},
        'source_anchor': {'key': 'sourceAnchor', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ObjectWithSyncError, self).__init__(**kwargs)
        self.source_of_authority = kwargs.get('source_of_authority', None)
        self.display_name = kwargs.get('display_name', None)
        self.object_type = kwargs.get('object_type', None)
        self.attribute_name = kwargs.get('attribute_name', None)
        self.attribute_value = kwargs.get('attribute_value', None)
        self.modififed_value = kwargs.get('modififed_value', None)
        self.user_principal_name = kwargs.get('user_principal_name', None)
        self.object_guid = kwargs.get('object_guid', None)
        self.attribute_multi_values = kwargs.get('attribute_multi_values', None)
        self.min_limit = kwargs.get('min_limit', None)
        self.max_limit = kwargs.get('max_limit', None)
        self.distinguished_name = kwargs.get('distinguished_name', None)
        self.mail = kwargs.get('mail', None)
        self.time_occured = kwargs.get('time_occured', None)
        self.error_type = kwargs.get('error_type', None)
        self.source_anchor = kwargs.get('source_anchor', None)
