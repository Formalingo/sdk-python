from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from .delete_permanent_query_parameter_type import DeletePermanentQueryParameterType
    from .documents_delete_response import DocumentsDeleteResponse
    from .documents_get_response import DocumentsGetResponse
    from .documents_put_request_body import DocumentsPutRequestBody
    from .documents_put_response import DocumentsPutResponse
    from .fields.fields_request_builder import FieldsRequestBuilder
    from .signer_roles.signer_roles_request_builder import SignerRolesRequestBuilder
    from .submissions.submissions_request_builder import SubmissionsRequestBuilder

class DocumentsItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/documents/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new DocumentsItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/documents/{id}{?permanent*}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[DocumentsItemRequestBuilderDeleteQueryParameters]] = None) -> Optional[DocumentsDeleteResponse]:
        """
        Soft-deletes by default. Pass `?permanent=true` to permanently delete.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DocumentsDeleteResponse]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .documents_delete_response import DocumentsDeleteResponse

        return await self.request_adapter.send_async(request_info, DocumentsDeleteResponse, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[DocumentsGetResponse]:
        """
        Get a document
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DocumentsGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .documents_get_response import DocumentsGetResponse

        return await self.request_adapter.send_async(request_info, DocumentsGetResponse, None)
    
    async def put(self,body: DocumentsPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[DocumentsPutResponse]:
        """
        Update a document
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DocumentsPutResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .documents_put_response import DocumentsPutResponse

        return await self.request_adapter.send_async(request_info, DocumentsPutResponse, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[DocumentsItemRequestBuilderDeleteQueryParameters]] = None) -> RequestInformation:
        """
        Soft-deletes by default. Pass `?permanent=true` to permanently delete.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Get a document
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_put_request_information(self,body: DocumentsPutRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update a document
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PUT, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> DocumentsItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: DocumentsItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return DocumentsItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def fields(self) -> FieldsRequestBuilder:
        """
        The fields property
        """
        from .fields.fields_request_builder import FieldsRequestBuilder

        return FieldsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def signer_roles(self) -> SignerRolesRequestBuilder:
        """
        The signerRoles property
        """
        from .signer_roles.signer_roles_request_builder import SignerRolesRequestBuilder

        return SignerRolesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def submissions(self) -> SubmissionsRequestBuilder:
        """
        The submissions property
        """
        from .submissions.submissions_request_builder import SubmissionsRequestBuilder

        return SubmissionsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class DocumentsItemRequestBuilderDeleteQueryParameters():
        """
        Soft-deletes by default. Pass `?permanent=true` to permanently delete.
        """
        permanent: Optional[DeletePermanentQueryParameterType] = None

    
    @dataclass
    class DocumentsItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[DocumentsItemRequestBuilderDeleteQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class DocumentsItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class DocumentsItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

