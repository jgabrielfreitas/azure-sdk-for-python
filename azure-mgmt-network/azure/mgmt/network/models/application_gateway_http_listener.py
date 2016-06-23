# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .sub_resource import SubResource


class ApplicationGatewayHttpListener(SubResource):
    """
    Http listener of application gateway

    :param id: Resource Id
    :type id: str
    :param frontend_ip_configuration: Gets or sets frontend IP configuration
     resource of application gateway
    :type frontend_ip_configuration: :class:`SubResource
     <azure.mgmt.network.models.SubResource>`
    :param frontend_port: Gets or sets frontend port resource of application
     gateway
    :type frontend_port: :class:`SubResource
     <azure.mgmt.network.models.SubResource>`
    :param protocol: Gets or sets the protocol. Possible values include:
     'Http', 'Https'
    :type protocol: str or :class:`ApplicationGatewayProtocol
     <azure.mgmt.network.models.ApplicationGatewayProtocol>`
    :param host_name: Gets or sets the host name of http listener
    :type host_name: str
    :param ssl_certificate: Gets or sets ssl certificate resource of
     application gateway
    :type ssl_certificate: :class:`SubResource
     <azure.mgmt.network.models.SubResource>`
    :param require_server_name_indication: Gets or sets the
     requireServerNameIndication of http listener
    :type require_server_name_indication: bool
    :param provisioning_state: Gets or sets Provisioning state of the http
     listener resource Updating/Deleting/Failed
    :type provisioning_state: str
    :param name: Gets name of the resource that is unique within a resource
     group. This name can be used to access the resource
    :type name: str
    :param etag: A unique read-only string that changes whenever the resource
     is updated
    :type etag: str
    """ 

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'frontend_ip_configuration': {'key': 'properties.frontendIPConfiguration', 'type': 'SubResource'},
        'frontend_port': {'key': 'properties.frontendPort', 'type': 'SubResource'},
        'protocol': {'key': 'properties.protocol', 'type': 'str'},
        'host_name': {'key': 'properties.hostName', 'type': 'str'},
        'ssl_certificate': {'key': 'properties.sslCertificate', 'type': 'SubResource'},
        'require_server_name_indication': {'key': 'properties.requireServerNameIndication', 'type': 'bool'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, id=None, frontend_ip_configuration=None, frontend_port=None, protocol=None, host_name=None, ssl_certificate=None, require_server_name_indication=None, provisioning_state=None, name=None, etag=None):
        super(ApplicationGatewayHttpListener, self).__init__(id=id)
        self.frontend_ip_configuration = frontend_ip_configuration
        self.frontend_port = frontend_port
        self.protocol = protocol
        self.host_name = host_name
        self.ssl_certificate = ssl_certificate
        self.require_server_name_indication = require_server_name_indication
        self.provisioning_state = provisioning_state
        self.name = name
        self.etag = etag