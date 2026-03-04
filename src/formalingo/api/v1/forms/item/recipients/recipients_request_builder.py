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
    from ......models.create_recipient_body import CreateRecipientBody
    from .item.with_r_item_request_builder import WithRItemRequestBuilder
    from .recipients_get_response import RecipientsGetResponse
    from .recipients_post_response import RecipientsPostResponse

class RecipientsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/forms/{id}/recipients
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new RecipientsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/forms/{id}/recipients", path_parameters)
    
    def by_rid(self,rid: UUID) -> WithRItemRequestBuilder:
        """
        Gets an item from the formalingo.api.v1.forms.item.recipients.item collection
        param rid: Unique identifier of the item
        Returns: WithRItemRequestBuilder
        """
        if rid is None:
            raise TypeError("rid cannot be null.")
        from .item.with_r_item_request_builder import WithRItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["rid"] = rid
        return WithRItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[RecipientsGetResponse]:
        """
        List recipients
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[RecipientsGetResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .recipients_get_response import RecipientsGetResponse

        return await self.request_adapter.send_async(request_info, RecipientsGetResponse, None)
    
    async def post(self,body: CreateRecipientBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[RecipientsPostResponse]:
        """
        Creates a form recipient with an optional pre-fill map. The `prefill` field accepts `{ questionId: value }` pairs that are saved as Response records immediately.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[RecipientsPostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .recipients_post_response import RecipientsPostResponse

        return await self.request_adapter.send_async(request_info, RecipientsPostResponse, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        List recipients
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: CreateRecipientBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a form recipient with an optional pre-fill map. The `prefill` field accepts `{ questionId: value }` pairs that are saved as Response records immediately.
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
    
    def with_url(self,raw_url: str) -> RecipientsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: RecipientsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return RecipientsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class RecipientsRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class RecipientsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

