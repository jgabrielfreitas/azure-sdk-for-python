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


class ResourceGroupPatchable(Model):
    """Resource group information.

    :param name: The name of the resource group.
    :type name: str
    :param properties:
    :type properties:
     ~azure.mgmt.resource.resources.v2018_05_01.models.ResourceGroupProperties
    :param managed_by: The ID of the resource that manages this resource
     group.
    :type managed_by: str
    :param tags: The tags attached to the resource group.
    :type tags: dict[str, str]
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'ResourceGroupProperties'},
        'managed_by': {'key': 'managedBy', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(ResourceGroupPatchable, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.properties = kwargs.get('properties', None)
        self.managed_by = kwargs.get('managed_by', None)
        self.tags = kwargs.get('tags', None)
