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
    from ....models.create_form_body import CreateFormBody
    from .forms400_error import Forms400Error
    from .forms401_error import Forms401Error
    from .forms_get_response import FormsGetResponse
    from .forms_post_response import FormsPostResponse
    from .get_status_query_parameter_type import GetStatusQueryParameterType
    from .item.forms_item_request_builder import FormsItemRequestBuilder

class FormsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/forms
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new FormsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/forms{?limit*,page*,status*}", path_parameters)
    
    def by_id(self,id: UUID) -> FormsItemRequestBuilder:
        """
        Gets an item from the formalingo.api.v1.forms.item collection
        param id: Unique identifier of the item
        Returns: FormsItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.forms_item_request_builder import FormsItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return FormsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[FormsRequestBuilderGetQueryParameters]] = None) -> Optional[FormsGetResponse]:
        """
        List forms
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[FormsGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .forms400_error import Forms400Error
        from .forms401_error import Forms401Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "401": Forms401Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .forms_get_response import FormsGetResponse

        return await self.request_adapter.send_async(request_info, FormsGetResponse, error_mapping)
    
    async def post(self,body: CreateFormBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[FormsPostResponse]:
        """
        Create a form
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[FormsPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .forms400_error import Forms400Error
        from .forms401_error import Forms401Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": Forms400Error,
            "401": Forms401Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .forms_post_response import FormsPostResponse

        return await self.request_adapter.send_async(request_info, FormsPostResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[FormsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        List forms
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: CreateFormBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Create a form
        param body: The request body
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
    
    def with_url(self,raw_url: str) -> FormsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: FormsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return FormsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class FormsRequestBuilderGetQueryParameters():
        """
        List forms
        """
        limit: Optional[int] = None

        page: Optional[int] = None

        status: Optional[GetStatusQueryParameterType] = None

    
    @dataclass
    class FormsRequestBuilderGetRequestConfiguration(RequestConfiguration[FormsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class FormsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

