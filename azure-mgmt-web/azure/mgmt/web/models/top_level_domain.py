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

from .resource import Resource


class TopLevelDomain(Resource):
    """
    A top level domain object

    :param id: Resource Id
    :type id: str
    :param name: Resource Name
    :type name: str
    :param location: Resource Location
    :type location: str
    :param type: Resource type
    :type type: str
    :param tags: Resource tags
    :type tags: dict
    :param top_level_domain_name: Name of the top level domain
    :type top_level_domain_name: str
    :param privacy: If true then the top level domain supports domain privacy
    :type privacy: bool
    """ 

    _validation = {
        'location': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'top_level_domain_name': {'key': 'properties.name', 'type': 'str'},
        'privacy': {'key': 'properties.privacy', 'type': 'bool'},
    }

    def __init__(self, location, id=None, name=None, type=None, tags=None, top_level_domain_name=None, privacy=None, **kwargs):
        super(TopLevelDomain, self).__init__(id=id, name=name, location=location, type=type, tags=tags, **kwargs)
        self.top_level_domain_name = top_level_domain_name
        self.privacy = privacy
