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

from msrest.serialization import Model


class ResourceType(Model):
    """
    Resource Type

    :param name: Gets or sets the resource type name
    :type name: str
    :param display_name: Gets or sets the resource type display name
    :type display_name: str
    :param operations: Gets or sets the resource type operations
    :type operations: list of :class:`ProviderOperation
     <azure.mgmt.authorization.models.ProviderOperation>`
    """ 

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'operations': {'key': 'operations', 'type': '[ProviderOperation]'},
    }

    def __init__(self, name=None, display_name=None, operations=None, **kwargs):
        self.name = name
        self.display_name = display_name
        self.operations = operations
