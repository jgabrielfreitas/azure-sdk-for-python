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


class ExportError(Model):
    """The export error details.

    :param id: The error Id.
    :type id: str
    :param run_step_result_id: The run step result Id.
    :type run_step_result_id: str
    :param connector_id: The connector Id.
    :type connector_id: str
    :param type: The type of error.
    :type type: str
    :param error_code: The error code.
    :type error_code: str
    :param message: The export error message.
    :type message: str
    :param server_error_detail: The server error detail.
    :type server_error_detail: str
    :param time_first_occured: The date and time when the export error first
     occurred.
    :type time_first_occured: datetime
    :param retry_count: The retry count.
    :type retry_count: int
    :param cs_object_id: The cloud object Id.
    :type cs_object_id: str
    :param dn: The distinguished name.
    :type dn: str
    :param min_limit: The minimum limit.
    :type min_limit: str
    :param max_limit: The maximum limit.
    :type max_limit: str
    :param cloud_anchor: The name of the cloud anchor.
    :type cloud_anchor: str
    :param attribute_name: The attribute name.
    :type attribute_name: str
    :param attribute_value: The attribute value.
    :type attribute_value: str
    :param attribute_multi_value: Indicates if the attribute is multi valued
     or not.
    :type attribute_multi_value: bool
    :param object_id_conflict: The object Id with which there was an attribute
     conflict.
    :type object_id_conflict: str
    :param sam_account_name: The SAM account name.
    :type sam_account_name: str
    :param ad_object_type: The AD object type
    :type ad_object_type: str
    :param ad_object_guid: The AD object guid.
    :type ad_object_guid: str
    :param ad_display_name: The display name for the AD object.
    :type ad_display_name: str
    :param ad_source_of_authority: The source of authority for the AD object.
    :type ad_source_of_authority: str
    :param ad_source_anchor: The AD source anchor.
    :type ad_source_anchor: str
    :param ad_user_principal_name: The user principal name for the AD object.
    :type ad_user_principal_name: str
    :param ad_distinguished_name: The distinguished name for the AD object.
    :type ad_distinguished_name: str
    :param ad_mail: The email for the AD object.
    :type ad_mail: str
    :param time_occured: The date and time of occurrance.
    :type time_occured: datetime
    :param aad_object_type: The AAD side object type.
    :type aad_object_type: str
    :param aad_object_guid: The AAD side object guid.
    :type aad_object_guid: str
    :param aad_display_name: The AAD side display name
    :type aad_display_name: str
    :param aad_source_of_authority: The AAD side source of authority for the
     object.
    :type aad_source_of_authority: str
    :param aad_user_principal_name: The AAD side user principal name.
    :type aad_user_principal_name: str
    :param aad_distringuished_name: The AAD side distinguished name for the
     object.
    :type aad_distringuished_name: str
    :param aad_mail: The AAD side email for the object.
    :type aad_mail: str
    :param last_dir_sync_time: The date and time of last sync run.
    :type last_dir_sync_time: datetime
    :param modified_attribute_value: The modified attribute value.
    :type modified_attribute_value: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'run_step_result_id': {'key': 'runStepResultId', 'type': 'str'},
        'connector_id': {'key': 'connectorId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'error_code': {'key': 'errorCode', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'server_error_detail': {'key': 'serverErrorDetail', 'type': 'str'},
        'time_first_occured': {'key': 'timeFirstOccured', 'type': 'iso-8601'},
        'retry_count': {'key': 'retryCount', 'type': 'int'},
        'cs_object_id': {'key': 'csObjectId', 'type': 'str'},
        'dn': {'key': 'dn', 'type': 'str'},
        'min_limit': {'key': 'minLimit', 'type': 'str'},
        'max_limit': {'key': 'maxLimit', 'type': 'str'},
        'cloud_anchor': {'key': 'cloudAnchor', 'type': 'str'},
        'attribute_name': {'key': 'attributeName', 'type': 'str'},
        'attribute_value': {'key': 'attributeValue', 'type': 'str'},
        'attribute_multi_value': {'key': 'attributeMultiValue', 'type': 'bool'},
        'object_id_conflict': {'key': 'objectIdConflict', 'type': 'str'},
        'sam_account_name': {'key': 'samAccountName', 'type': 'str'},
        'ad_object_type': {'key': 'adObjectType', 'type': 'str'},
        'ad_object_guid': {'key': 'adObjectGuid', 'type': 'str'},
        'ad_display_name': {'key': 'adDisplayName', 'type': 'str'},
        'ad_source_of_authority': {'key': 'adSourceOfAuthority', 'type': 'str'},
        'ad_source_anchor': {'key': 'adSourceAnchor', 'type': 'str'},
        'ad_user_principal_name': {'key': 'adUserPrincipalName', 'type': 'str'},
        'ad_distinguished_name': {'key': 'adDistinguishedName', 'type': 'str'},
        'ad_mail': {'key': 'adMail', 'type': 'str'},
        'time_occured': {'key': 'timeOccured', 'type': 'iso-8601'},
        'aad_object_type': {'key': 'aadObjectType', 'type': 'str'},
        'aad_object_guid': {'key': 'aadObjectGuid', 'type': 'str'},
        'aad_display_name': {'key': 'aadDisplayName', 'type': 'str'},
        'aad_source_of_authority': {'key': 'aadSourceOfAuthority', 'type': 'str'},
        'aad_user_principal_name': {'key': 'aadUserPrincipalName', 'type': 'str'},
        'aad_distringuished_name': {'key': 'aadDistringuishedName', 'type': 'str'},
        'aad_mail': {'key': 'aadMail', 'type': 'str'},
        'last_dir_sync_time': {'key': 'lastDirSyncTime', 'type': 'iso-8601'},
        'modified_attribute_value': {'key': 'modifiedAttributeValue', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, run_step_result_id: str=None, connector_id: str=None, type: str=None, error_code: str=None, message: str=None, server_error_detail: str=None, time_first_occured=None, retry_count: int=None, cs_object_id: str=None, dn: str=None, min_limit: str=None, max_limit: str=None, cloud_anchor: str=None, attribute_name: str=None, attribute_value: str=None, attribute_multi_value: bool=None, object_id_conflict: str=None, sam_account_name: str=None, ad_object_type: str=None, ad_object_guid: str=None, ad_display_name: str=None, ad_source_of_authority: str=None, ad_source_anchor: str=None, ad_user_principal_name: str=None, ad_distinguished_name: str=None, ad_mail: str=None, time_occured=None, aad_object_type: str=None, aad_object_guid: str=None, aad_display_name: str=None, aad_source_of_authority: str=None, aad_user_principal_name: str=None, aad_distringuished_name: str=None, aad_mail: str=None, last_dir_sync_time=None, modified_attribute_value: str=None, **kwargs) -> None:
        super(ExportError, self).__init__(**kwargs)
        self.id = id
        self.run_step_result_id = run_step_result_id
        self.connector_id = connector_id
        self.type = type
        self.error_code = error_code
        self.message = message
        self.server_error_detail = server_error_detail
        self.time_first_occured = time_first_occured
        self.retry_count = retry_count
        self.cs_object_id = cs_object_id
        self.dn = dn
        self.min_limit = min_limit
        self.max_limit = max_limit
        self.cloud_anchor = cloud_anchor
        self.attribute_name = attribute_name
        self.attribute_value = attribute_value
        self.attribute_multi_value = attribute_multi_value
        self.object_id_conflict = object_id_conflict
        self.sam_account_name = sam_account_name
        self.ad_object_type = ad_object_type
        self.ad_object_guid = ad_object_guid
        self.ad_display_name = ad_display_name
        self.ad_source_of_authority = ad_source_of_authority
        self.ad_source_anchor = ad_source_anchor
        self.ad_user_principal_name = ad_user_principal_name
        self.ad_distinguished_name = ad_distinguished_name
        self.ad_mail = ad_mail
        self.time_occured = time_occured
        self.aad_object_type = aad_object_type
        self.aad_object_guid = aad_object_guid
        self.aad_display_name = aad_display_name
        self.aad_source_of_authority = aad_source_of_authority
        self.aad_user_principal_name = aad_user_principal_name
        self.aad_distringuished_name = aad_distringuished_name
        self.aad_mail = aad_mail
        self.last_dir_sync_time = last_dir_sync_time
        self.modified_attribute_value = modified_attribute_value
