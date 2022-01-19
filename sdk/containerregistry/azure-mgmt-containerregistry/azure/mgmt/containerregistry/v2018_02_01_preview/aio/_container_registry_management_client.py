# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, Awaitable, Optional, TYPE_CHECKING

from azure.core.rest import AsyncHttpResponse, HttpRequest
from azure.mgmt.core import AsyncARMPipelineClient
from msrest import Deserializer, Serializer

from .. import models
from ._configuration import ContainerRegistryManagementClientConfiguration
from .operations import BuildStepsOperations, BuildTasksOperations, BuildsOperations, RegistriesOperations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from azure.core.credentials_async import AsyncTokenCredential

class ContainerRegistryManagementClient:
    """ContainerRegistryManagementClient.

    :ivar builds: BuildsOperations operations
    :vartype builds:
     azure.mgmt.containerregistry.v2018_02_01_preview.aio.operations.BuildsOperations
    :ivar build_steps: BuildStepsOperations operations
    :vartype build_steps:
     azure.mgmt.containerregistry.v2018_02_01_preview.aio.operations.BuildStepsOperations
    :ivar build_tasks: BuildTasksOperations operations
    :vartype build_tasks:
     azure.mgmt.containerregistry.v2018_02_01_preview.aio.operations.BuildTasksOperations
    :ivar registries: RegistriesOperations operations
    :vartype registries:
     azure.mgmt.containerregistry.v2018_02_01_preview.aio.operations.RegistriesOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials_async.AsyncTokenCredential
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param base_url: Service URL. Default value is 'https://management.azure.com'.
    :type base_url: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        credential: "AsyncTokenCredential",
        subscription_id: str,
        base_url: str = "https://management.azure.com",
        **kwargs: Any
    ) -> None:
        self._config = ContainerRegistryManagementClientConfiguration(credential=credential, subscription_id=subscription_id, **kwargs)
        self._client = AsyncARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)
        self._serialize.client_side_validation = False
        self.builds = BuildsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.build_steps = BuildStepsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.build_tasks = BuildTasksOperations(self._client, self._config, self._serialize, self._deserialize)
        self.registries = RegistriesOperations(self._client, self._config, self._serialize, self._deserialize)


    def _send_request(
        self,
        request: HttpRequest,
        **kwargs: Any
    ) -> Awaitable[AsyncHttpResponse]:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = await client._send_request(request)
        <AsyncHttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.AsyncHttpResponse
        """

        request_copy = deepcopy(request)
        request_copy.url = self._client.format_url(request_copy.url)
        return self._client.send_request(request_copy, **kwargs)

    async def close(self) -> None:
        await self._client.close()

    async def __aenter__(self) -> "ContainerRegistryManagementClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *exc_details) -> None:
        await self._client.__aexit__(*exc_details)
