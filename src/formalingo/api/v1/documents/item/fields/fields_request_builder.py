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
from uuid import UUID
from warnings import warn

if TYPE_CHECKING:
    from ......models.create_field_body import CreateFieldBody
    from .fields400_error import Fields400Error
    from .fields403_error import Fields403Error
    from .fields409_error import Fields409Error
    from .fields_get_response import FieldsGetResponse
    from .fields_post_response import FieldsPostResponse
    from .item.with_f_item_request_builder import WithFItemRequestBuilder

class FieldsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/documents/{id}/fields
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new FieldsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/documents/{id}/fields", path_parameters)
    
    def by_fid(self,fid: UUID) -> WithFItemRequestBuilder:
        """
        Gets an item from the formalingo.api.v1.documents.item.fields.item collection
        param fid: Unique identifier of the item
        Returns: WithFItemRequestBuilder
        """
        if fid is None:
            raise TypeError("fid cannot be null.")
        from .item.with_f_item_request_builder import WithFItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["fid"] = fid
        return WithFItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[FieldsGetResponse]:
        """
        Lists placed and non-positioned document fields. Page zero means no PDF-page placement. Workspace API keys with documents:read can read supporting request definitions without file-download permission. Session/OAuth access to those definitions requires the document creator. Actual uploaded values and downloads require separate authorization.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[FieldsGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .fields_get_response import FieldsGetResponse

        return await self.request_adapter.send_async(request_info, FieldsGetResponse, None)
    
    async def post(self,body: CreateFieldBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[FieldsPostResponse]:
        """
        Creates a placed field or supporting attachment request. For a supporting request, use type=file_upload, options.supporting_attachment=true and a valid assigneeRole; geometry may be omitted or all zero, and isRequired defaults to true. API keys need documents:write; session/OAuth users must be the document creator. File-download permission is not needed to author requests. Optional client id UUID supports identical retry replay; field purpose is immutable.
        param body: Create a placed field or a supporting file_upload request. Supporting requests require options.supporting_attachment=true and an assigned signer; omitted geometry is canonicalized to all zero and Required defaults to true. Ordinary fields require complete page placement. Field purpose is immutable after creation.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[FieldsPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .fields400_error import Fields400Error
        from .fields403_error import Fields403Error
        from .fields409_error import Fields409Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": Fields400Error,
            "403": Fields403Error,
            "409": Fields409Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .fields_post_response import FieldsPostResponse

        return await self.request_adapter.send_async(request_info, FieldsPostResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Lists placed and non-positioned document fields. Page zero means no PDF-page placement. Workspace API keys with documents:read can read supporting request definitions without file-download permission. Session/OAuth access to those definitions requires the document creator. Actual uploaded values and downloads require separate authorization.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: CreateFieldBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a placed field or supporting attachment request. For a supporting request, use type=file_upload, options.supporting_attachment=true and a valid assigneeRole; geometry may be omitted or all zero, and isRequired defaults to true. API keys need documents:write; session/OAuth users must be the document creator. File-download permission is not needed to author requests. Optional client id UUID supports identical retry replay; field purpose is immutable.
        param body: Create a placed field or a supporting file_upload request. Supporting requests require options.supporting_attachment=true and an assigned signer; omitted geometry is canonicalized to all zero and Required defaults to true. Ordinary fields require complete page placement. Field purpose is immutable after creation.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> FieldsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: FieldsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return FieldsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class FieldsRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class FieldsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

