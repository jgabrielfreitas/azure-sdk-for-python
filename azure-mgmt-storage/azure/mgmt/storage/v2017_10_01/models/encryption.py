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


class Encryption(Model):
    """The encryption settings on the storage account.

    :param services: List of services which support encryption.
    :type services: ~azure.mgmt.storage.v2017_10_01.models.EncryptionServices
    :param key_source: The encryption keySource (provider). Possible values
     (case-insensitive):  Microsoft.Storage, Microsoft.Keyvault. Possible
     values include: 'Microsoft.Storage', 'Microsoft.Keyvault'. Default value:
     "Microsoft.Storage" .
    :type key_source: str or ~azure.mgmt.storage.v2017_10_01.models.KeySource
    :param key_vault_properties: Properties provided by key vault.
    :type key_vault_properties:
     ~azure.mgmt.storage.v2017_10_01.models.KeyVaultProperties
    """

    _validation = {
        'key_source': {'required': True},
    }

    _attribute_map = {
        'services': {'key': 'services', 'type': 'EncryptionServices'},
        'key_source': {'key': 'keySource', 'type': 'str'},
        'key_vault_properties': {'key': 'keyvaultproperties', 'type': 'KeyVaultProperties'},
    }

    def __init__(self, services=None, key_source="Microsoft.Storage", key_vault_properties=None):
        self.services = services
        self.key_source = key_source
        self.key_vault_properties = key_vault_properties
