# Copyright 2010 Jacob Kaplan-Moss
# Copyright 2011 Nebula, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
"""
Exception definitions.
"""


class SDKException(Exception):
    """The base exception class for all exceptions this library raises.
    """
    pass


class AuthorizationFailure(SDKException):
    """Cannot authorize API client."""
    pass


class EndpointException(SDKException):
    """Something is rotten in Service Catalog."""
    pass


class EndpointNotFound(EndpointException):
    """Could not find requested endpoint in Service Catalog."""
    pass


class EmptyCatalog(EndpointNotFound):
    """The service catalog is empty."""
    pass


class NoMatchingPlugin(SDKException):
    """No matching plugins could be created with the provided parameters."""
    pass


class InvalidResponse(SDKException):
    """The response from the server is not valid for this request."""

    def __init__(self, response):
        super(InvalidResponse, self).__init__()
        self.response = response


class HttpException(SDKException):
    def __init__(self, message, details=None):
        super(HttpException, self).__init__(message)
        self.details = details


class MethodNotSupported(SDKException):
    """The resource does not support this operation type."""
    pass