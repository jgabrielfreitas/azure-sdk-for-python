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


class OSDisk(Model):
    """Settings for the operating system disk of the virtual machine.

    :param caching: The type of caching to be enabled for the data disks. none
     - The caching mode for the disk is not enabled. readOnly - The caching
     mode for the disk is read only. readWrite - The caching mode for the disk
     is read and write. Default value is none. Possible values include: 'None',
     'ReadOnly', 'ReadWrite'
    :type caching: str or ~azure.mgmt.batch.models.CachingType
    """

    _attribute_map = {
        'caching': {'key': 'caching', 'type': 'CachingType'},
    }

    def __init__(self, caching=None):
        self.caching = caching