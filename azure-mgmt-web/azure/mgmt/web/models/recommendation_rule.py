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


class RecommendationRule(Model):
    """
    Represents a recommendation rule that the recommendation engine can perform

    :param name: Unique name of the rule
    :type name: str
    :param display_name: UI friendly name of the rule
    :type display_name: str
    :param message: Localized name of the rule (Good for UI)
    :type message: str
    :param recommendation_id: Recommendation ID of an associated
     recommendation object tied to the rule, if exists.
     If such an object doesn't exist, it is set to null.
    :type recommendation_id: str
    :param description: Localized detailed description of the rule
    :type description: str
    :param action_name: Name of action that is recommended by this rule in
     string
    :type action_name: str
    :param enabled: On/off flag indicating the rule is currently enabled or
     disabled.
    :type enabled: int
    :param level: Level of impact indicating how critical this rule is.
     Possible values include: 'Critical', 'Warning', 'Information',
     'NonUrgentSuggestion'
    :type level: str
    :param channels: List of available channels that this rule applies.
     Possible values include: 'Notification', 'Api', 'Email', 'All'
    :type channels: str
    """ 

    _validation = {
        'level': {'required': True},
        'channels': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'display_name': {'key': 'displayName', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'recommendation_id': {'key': 'recommendationId', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'action_name': {'key': 'actionName', 'type': 'str'},
        'enabled': {'key': 'enabled', 'type': 'int'},
        'level': {'key': 'level', 'type': 'NotificationLevel'},
        'channels': {'key': 'channels', 'type': 'Channels'},
    }

    def __init__(self, level, channels, name=None, display_name=None, message=None, recommendation_id=None, description=None, action_name=None, enabled=None, **kwargs):
        self.name = name
        self.display_name = display_name
        self.message = message
        self.recommendation_id = recommendation_id
        self.description = description
        self.action_name = action_name
        self.enabled = enabled
        self.level = level
        self.channels = channels
