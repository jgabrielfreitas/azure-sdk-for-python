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

from .deployed_service_replica_detail_info import DeployedServiceReplicaDetailInfo


class DeployedStatelessServiceInstanceDetailInfo(DeployedServiceReplicaDetailInfo):
    """Information about a stateless instance running in a code package. Note that
    DeployedServiceReplicaQueryResult will contain duplicate data like
    ServiceKind, ServiceName, PartitionId and InstanceId.

    All required parameters must be populated in order to send to Azure.

    :param service_name: Full hierarchical name of the service in URI format
     starting with `fabric:`.
    :type service_name: str
    :param partition_id: An internal ID used by Service Fabric to uniquely
     identify a partition. This is a randomly generated GUID when the service
     was created. The partition ID is unique and does not change for the
     lifetime of the service. If the same service was deleted and recreated the
     IDs of its partitions would be different.
    :type partition_id: str
    :param current_service_operation: Specifies the current active life-cycle
     operation on a stateful service replica or stateless service instance.
     Possible values include: 'Unknown', 'None', 'Open', 'ChangeRole', 'Close',
     'Abort'
    :type current_service_operation: str or
     ~azure.servicefabric.models.ServiceOperationName
    :param current_service_operation_start_time_utc: The start time of the
     current service operation in UTC format.
    :type current_service_operation_start_time_utc: datetime
    :param reported_load: List of load reported by replica.
    :type reported_load:
     list[~azure.servicefabric.models.LoadMetricReportInfo]
    :param service_kind: Required. Constant filled by server.
    :type service_kind: str
    :param instance_id: Id of a stateless service instance. InstanceId is used
     by Service Fabric to uniquely identify an instance of a partition of a
     stateless service. It is unique within a partition and does not change for
     the lifetime of the instance. If the instance has failed over on the same
     or different node, it will get a different value for the InstanceId.
    :type instance_id: str
    :param deployed_service_replica_query_result: Information about a
     stateless service instance deployed on a node.
    :type deployed_service_replica_query_result:
     ~azure.servicefabric.models.DeployedStatelessServiceInstanceInfo
    """

    _validation = {
        'service_kind': {'required': True},
    }

    _attribute_map = {
        'service_name': {'key': 'ServiceName', 'type': 'str'},
        'partition_id': {'key': 'PartitionId', 'type': 'str'},
        'current_service_operation': {'key': 'CurrentServiceOperation', 'type': 'str'},
        'current_service_operation_start_time_utc': {'key': 'CurrentServiceOperationStartTimeUtc', 'type': 'iso-8601'},
        'reported_load': {'key': 'ReportedLoad', 'type': '[LoadMetricReportInfo]'},
        'service_kind': {'key': 'ServiceKind', 'type': 'str'},
        'instance_id': {'key': 'InstanceId', 'type': 'str'},
        'deployed_service_replica_query_result': {'key': 'DeployedServiceReplicaQueryResult', 'type': 'DeployedStatelessServiceInstanceInfo'},
    }

    def __init__(self, **kwargs):
        super(DeployedStatelessServiceInstanceDetailInfo, self).__init__(**kwargs)
        self.instance_id = kwargs.get('instance_id', None)
        self.deployed_service_replica_query_result = kwargs.get('deployed_service_replica_query_result', None)
        self.service_kind = 'Stateless'
