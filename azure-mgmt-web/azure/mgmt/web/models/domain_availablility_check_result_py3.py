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


class DomainAvailablilityCheckResult(Model):
    """Domain availablility check result.

    :param name: Name of the domain.
    :type name: str
    :param available: <code>true</code> if domain can be purchased using
     CreateDomain API; otherwise, <code>false</code>.
    :type available: bool
    :param domain_type: Valid values are Regular domain: Azure will charge the
     full price of domain registration, SoftDeleted: Purchasing this domain
     will simply restore it and this operation will not cost anything. Possible
     values include: 'Regular', 'SoftDeleted'
    :type domain_type: str or ~azure.mgmt.web.models.DomainType
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'available': {'key': 'available', 'type': 'bool'},
        'domain_type': {'key': 'domainType', 'type': 'DomainType'},
    }

    def __init__(self, *, name: str=None, available: bool=None, domain_type=None, **kwargs) -> None:
        super(DomainAvailablilityCheckResult, self).__init__(**kwargs)
        self.name = name
        self.available = available
        self.domain_type = domain_type
