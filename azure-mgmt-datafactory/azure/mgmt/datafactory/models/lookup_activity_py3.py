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

from .execution_activity_py3 import ExecutionActivity


class LookupActivity(ExecutionActivity):
    """Lookup activity.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param name: Required. Activity name.
    :type name: str
    :param description: Activity description.
    :type description: str
    :param depends_on: Activity depends on condition.
    :type depends_on: list[~azure.mgmt.datafactory.models.ActivityDependency]
    :param user_properties: Activity user properties.
    :type user_properties: dict[str, str]
    :param type: Required. Constant filled by server.
    :type type: str
    :param linked_service_name: Linked service reference.
    :type linked_service_name:
     ~azure.mgmt.datafactory.models.LinkedServiceReference
    :param policy: Activity policy.
    :type policy: ~azure.mgmt.datafactory.models.ActivityPolicy
    :param source: Required. Dataset-specific source properties, same as copy
     activity source.
    :type source: ~azure.mgmt.datafactory.models.CopySource
    :param dataset: Required. Lookup activity dataset reference.
    :type dataset: ~azure.mgmt.datafactory.models.DatasetReference
    :param first_row_only: Whether to return first row or all rows. Default
     value is true. Type: boolean (or Expression with resultType boolean).
    :type first_row_only: object
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True},
        'source': {'required': True},
        'dataset': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'depends_on': {'key': 'dependsOn', 'type': '[ActivityDependency]'},
        'user_properties': {'key': 'userProperties', 'type': '{str}'},
        'type': {'key': 'type', 'type': 'str'},
        'linked_service_name': {'key': 'linkedServiceName', 'type': 'LinkedServiceReference'},
        'policy': {'key': 'policy', 'type': 'ActivityPolicy'},
        'source': {'key': 'typeProperties.source', 'type': 'CopySource'},
        'dataset': {'key': 'typeProperties.dataset', 'type': 'DatasetReference'},
        'first_row_only': {'key': 'typeProperties.firstRowOnly', 'type': 'object'},
    }

    def __init__(self, *, name: str, source, dataset, additional_properties=None, description: str=None, depends_on=None, user_properties=None, linked_service_name=None, policy=None, first_row_only=None, **kwargs) -> None:
        super(LookupActivity, self).__init__(additional_properties=additional_properties, name=name, description=description, depends_on=depends_on, user_properties=user_properties, linked_service_name=linked_service_name, policy=policy, **kwargs)
        self.source = source
        self.dataset = dataset
        self.first_row_only = first_row_only
        self.type = 'Lookup'
