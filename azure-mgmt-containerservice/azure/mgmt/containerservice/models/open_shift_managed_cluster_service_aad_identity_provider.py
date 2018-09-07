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


class OpenShiftManagedClusterServiceAADIdentityProvider(Model):
    """AADIdentityProvider defines Identity provider for MS AAD.

    :param kind: The kind of the provider.
    :type kind: str
    :param client_id: The clientId password associated with the provider.
    :type client_id: str
    :param secret: The secret password associated with the provider.
    :type secret: str
    :param tenant_id: The tenantId associated with the provider.
    :type tenant_id: str
    """

    _attribute_map = {
        'kind': {'key': 'kind', 'type': 'str'},
        'client_id': {'key': 'clientId', 'type': 'str'},
        'secret': {'key': 'secret', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(OpenShiftManagedClusterServiceAADIdentityProvider, self).__init__(**kwargs)
        self.kind = kwargs.get('kind', None)
        self.client_id = kwargs.get('client_id', None)
        self.secret = kwargs.get('secret', None)
        self.tenant_id = kwargs.get('tenant_id', None)
