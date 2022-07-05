# pylint: disable=too-many-lines
# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Optional, TypeVar

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import AsyncHttpResponse
from azure.core.rest import HttpRequest
from azure.core.tracing.decorator_async import distributed_trace_async
from azure.mgmt.core.exceptions import ARMErrorFormat

from ... import models as _models
from ..._vendor import _convert_request
from ...operations._configuration_operations import build_get_request, build_patch_request
T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class ConfigurationOperations:
    """ConfigurationOperations async operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure.mgmt.eventhub.v2022_01_01_preview.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = _models

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    @distributed_trace_async
    async def patch(
        self,
        resource_group_name: str,
        cluster_name: str,
        parameters: "_models.ClusterQuotaConfigurationProperties",
        **kwargs: Any
    ) -> Optional["_models.ClusterQuotaConfigurationProperties"]:
        """Replace all specified Event Hubs Cluster settings with those contained in the request body.
        Leaves the settings not specified in the request body unmodified.

        :param resource_group_name: Name of the resource group within the azure subscription.
        :type resource_group_name: str
        :param cluster_name: The name of the Event Hubs Cluster.
        :type cluster_name: str
        :param parameters: Parameters for creating an Event Hubs Cluster resource.
        :type parameters:
         ~azure.mgmt.eventhub.v2022_01_01_preview.models.ClusterQuotaConfigurationProperties
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ClusterQuotaConfigurationProperties, or the result of cls(response)
        :rtype: ~azure.mgmt.eventhub.v2022_01_01_preview.models.ClusterQuotaConfigurationProperties or
         None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[Optional["_models.ClusterQuotaConfigurationProperties"]]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2022-01-01-preview")  # type: str
        content_type = kwargs.pop('content_type', "application/json")  # type: Optional[str]

        _json = self._serialize.body(parameters, 'ClusterQuotaConfigurationProperties')

        request = build_patch_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            cluster_name=cluster_name,
            api_version=api_version,
            content_type=content_type,
            json=_json,
            template_url=self.patch.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200, 201, 202]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('ClusterQuotaConfigurationProperties', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('ClusterQuotaConfigurationProperties', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    patch.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/clusters/{clusterName}/quotaConfiguration/default"}  # type: ignore


    @distributed_trace_async
    async def get(
        self,
        resource_group_name: str,
        cluster_name: str,
        **kwargs: Any
    ) -> "_models.ClusterQuotaConfigurationProperties":
        """Get all Event Hubs Cluster settings - a collection of key/value pairs which represent the
        quotas and settings imposed on the cluster.

        :param resource_group_name: Name of the resource group within the azure subscription.
        :type resource_group_name: str
        :param cluster_name: The name of the Event Hubs Cluster.
        :type cluster_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: ClusterQuotaConfigurationProperties, or the result of cls(response)
        :rtype: ~azure.mgmt.eventhub.v2022_01_01_preview.models.ClusterQuotaConfigurationProperties
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["_models.ClusterQuotaConfigurationProperties"]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))

        api_version = kwargs.pop('api_version', "2022-01-01-preview")  # type: str

        
        request = build_get_request(
            subscription_id=self._config.subscription_id,
            resource_group_name=resource_group_name,
            cluster_name=cluster_name,
            api_version=api_version,
            template_url=self.get.metadata['url'],
        )
        request = _convert_request(request)
        request.url = self._client.format_url(request.url)

        pipeline_response = await self._client._pipeline.run(  # pylint: disable=protected-access
            request,
            stream=False,
            **kwargs
        )
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            error = self._deserialize.failsafe_deserialize(_models.ErrorResponse, pipeline_response)
            raise HttpResponseError(response=response, model=error, error_format=ARMErrorFormat)

        deserialized = self._deserialize('ClusterQuotaConfigurationProperties', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized

    get.metadata = {'url': "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.EventHub/clusters/{clusterName}/quotaConfiguration/default"}  # type: ignore

