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

import uuid
from msrest.pipeline import ClientRawResponse
from msrestazure.azure_exceptions import CloudError

from .. import models


class TransformationsOperations(object):
    """TransformationsOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: Client Api Version. Constant value: "2016-03-01".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2016-03-01"

        self.config = config

    def create_or_replace(
            self, transformation, resource_group_name, job_name, transformation_name, if_match=None, if_none_match=None, custom_headers=None, raw=False, **operation_config):
        """Creates a transformation or replaces an already existing transformation
        under an existing streaming job.

        :param transformation: The definition of the transformation that will
         be used to create a new transformation or replace the existing one
         under the streaming job.
        :type transformation:
         ~azure.mgmt.streamanalytics.models.Transformation
        :param resource_group_name: The name of the resource group that
         contains the resource. You can obtain this value from the Azure
         Resource Manager API or the portal.
        :type resource_group_name: str
        :param job_name: The name of the streaming job.
        :type job_name: str
        :param transformation_name: The name of the transformation.
        :type transformation_name: str
        :param if_match: The ETag of the transformation. Omit this value to
         always overwrite the current transformation. Specify the last-seen
         ETag value to prevent accidentally overwriting concurrent changes.
        :type if_match: str
        :param if_none_match: Set to '*' to allow a new transformation to be
         created, but to prevent updating an existing transformation. Other
         values will result in a 412 Pre-condition Failed response.
        :type if_none_match: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Transformation or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.streamanalytics.models.Transformation or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        # Construct URL
        url = self.create_or_replace.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'jobName': self._serialize.url("job_name", job_name, 'str'),
            'transformationName': self._serialize.url("transformation_name", transformation_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if if_match is not None:
            header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        if if_none_match is not None:
            header_parameters['If-None-Match'] = self._serialize.header("if_none_match", if_none_match, 'str')
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(transformation, 'Transformation')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 201]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        header_dict = {}
        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Transformation', response)
            header_dict = {
                'ETag': 'str',
            }
        if response.status_code == 201:
            deserialized = self._deserialize('Transformation', response)
            header_dict = {
                'ETag': 'str',
            }

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            client_raw_response.add_headers(header_dict)
            return client_raw_response

        return deserialized
    create_or_replace.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StreamAnalytics/streamingjobs/{jobName}/transformations/{transformationName}'}

    def update(
            self, transformation, resource_group_name, job_name, transformation_name, if_match=None, custom_headers=None, raw=False, **operation_config):
        """Updates an existing transformation under an existing streaming job.
        This can be used to partially update (ie. update one or two properties)
        a transformation without affecting the rest the job or transformation
        definition.

        :param transformation: A Transformation object. The properties
         specified here will overwrite the corresponding properties in the
         existing transformation (ie. Those properties will be updated). Any
         properties that are set to null here will mean that the corresponding
         property in the existing transformation will remain the same and not
         change as a result of this PATCH operation.
        :type transformation:
         ~azure.mgmt.streamanalytics.models.Transformation
        :param resource_group_name: The name of the resource group that
         contains the resource. You can obtain this value from the Azure
         Resource Manager API or the portal.
        :type resource_group_name: str
        :param job_name: The name of the streaming job.
        :type job_name: str
        :param transformation_name: The name of the transformation.
        :type transformation_name: str
        :param if_match: The ETag of the transformation. Omit this value to
         always overwrite the current transformation. Specify the last-seen
         ETag value to prevent accidentally overwriting concurrent changes.
        :type if_match: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Transformation or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.streamanalytics.models.Transformation or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        # Construct URL
        url = self.update.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'jobName': self._serialize.url("job_name", job_name, 'str'),
            'transformationName': self._serialize.url("transformation_name", transformation_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if if_match is not None:
            header_parameters['If-Match'] = self._serialize.header("if_match", if_match, 'str')
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(transformation, 'Transformation')

        # Construct and send request
        request = self._client.patch(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        header_dict = {}
        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Transformation', response)
            header_dict = {
                'ETag': 'str',
            }

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            client_raw_response.add_headers(header_dict)
            return client_raw_response

        return deserialized
    update.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StreamAnalytics/streamingjobs/{jobName}/transformations/{transformationName}'}

    def get(
            self, resource_group_name, job_name, transformation_name, custom_headers=None, raw=False, **operation_config):
        """Gets details about the specified transformation.

        :param resource_group_name: The name of the resource group that
         contains the resource. You can obtain this value from the Azure
         Resource Manager API or the portal.
        :type resource_group_name: str
        :param job_name: The name of the streaming job.
        :type job_name: str
        :param transformation_name: The name of the transformation.
        :type transformation_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: Transformation or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.streamanalytics.models.Transformation or
         ~msrest.pipeline.ClientRawResponse
        :raises: :class:`CloudError<msrestazure.azure_exceptions.CloudError>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'jobName': self._serialize.url("job_name", job_name, 'str'),
            'transformationName': self._serialize.url("transformation_name", transformation_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            exp = CloudError(response)
            exp.request_id = response.headers.get('x-ms-request-id')
            raise exp

        header_dict = {}
        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Transformation', response)
            header_dict = {
                'ETag': 'str',
            }

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            client_raw_response.add_headers(header_dict)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StreamAnalytics/streamingjobs/{jobName}/transformations/{transformationName}'}