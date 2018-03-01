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


class ClusterCreateParameters(Model):
    """Parameters supplied to the Create operation.

    All required parameters must be populated in order to send to Azure.

    :param location: Required. The region in which to create the cluster.
    :type location: str
    :param tags: The user specified tags associated with the Cluster.
    :type tags: dict[str, str]
    :param vm_size: Required. The size of the virtual machines in the cluster.
     All virtual machines in a cluster are the same size. For information about
     available VM sizes for clusters using images from the Virtual Machines
     Marketplace (see Sizes for Virtual Machines (Linux) or Sizes for Virtual
     Machines (Windows). Batch AI service supports all Azure VM sizes except
     STANDARD_A0 and those with premium storage (STANDARD_GS, STANDARD_DS, and
     STANDARD_DSV2 series).
    :type vm_size: str
    :param vm_priority: dedicated or lowpriority. Default is dedicated.
     Possible values include: 'dedicated', 'lowpriority'. Default value:
     "dedicated" .
    :type vm_priority: str or ~azure.mgmt.batchai.models.VmPriority
    :param scale_settings: Desired scale for the cluster.
    :type scale_settings: ~azure.mgmt.batchai.models.ScaleSettings
    :param virtual_machine_configuration: Settings for OS image and mounted
     data volumes.
    :type virtual_machine_configuration:
     ~azure.mgmt.batchai.models.VirtualMachineConfiguration
    :param node_setup: Setup to be done on all compute nodes in the cluster.
    :type node_setup: ~azure.mgmt.batchai.models.NodeSetup
    :param user_account_settings: Required. Settings for user account that
     will be created on all compute nodes of the cluster.
    :type user_account_settings:
     ~azure.mgmt.batchai.models.UserAccountSettings
    :param subnet: Specifies the identifier of the subnet. .
    :type subnet: ~azure.mgmt.batchai.models.ResourceId
    """

    _validation = {
        'location': {'required': True},
        'vm_size': {'required': True},
        'user_account_settings': {'required': True},
    }

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'vm_size': {'key': 'properties.vmSize', 'type': 'str'},
        'vm_priority': {'key': 'properties.vmPriority', 'type': 'VmPriority'},
        'scale_settings': {'key': 'properties.scaleSettings', 'type': 'ScaleSettings'},
        'virtual_machine_configuration': {'key': 'properties.virtualMachineConfiguration', 'type': 'VirtualMachineConfiguration'},
        'node_setup': {'key': 'properties.nodeSetup', 'type': 'NodeSetup'},
        'user_account_settings': {'key': 'properties.userAccountSettings', 'type': 'UserAccountSettings'},
        'subnet': {'key': 'properties.subnet', 'type': 'ResourceId'},
    }

    def __init__(self, *, location: str, vm_size: str, user_account_settings, tags=None, vm_priority="dedicated", scale_settings=None, virtual_machine_configuration=None, node_setup=None, subnet=None, **kwargs) -> None:
        super(ClusterCreateParameters, self).__init__(**kwargs)
        self.location = location
        self.tags = tags
        self.vm_size = vm_size
        self.vm_priority = vm_priority
        self.scale_settings = scale_settings
        self.virtual_machine_configuration = virtual_machine_configuration
        self.node_setup = node_setup
        self.user_account_settings = user_account_settings
        self.subnet = subnet