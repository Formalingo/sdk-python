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
    from .expire400_error import Expire400Error
    from .expire403_error import Expire403Error
    from .expire404_error import Expire404Error
    from .expire409_error import Expire409Error
    from .expire_post_request_body import ExpirePostRequestBody
    from .expire_post_response import ExpirePostResponse

class ExpireRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/documents/{id}/submissions/{sid}/expire
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ExpireRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/documents/{id}/submissions/{sid}/expire", path_parameters)
    
    async def post(self,body: ExpirePostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ExpirePostResponse]:
        """
        Requires submissions:write. Immediately expires all active links on a completely unsigned, unsealed submission. Retains answers, consent and audit evidence. Repeating the request is safe. Completed or partially signed submissions and active send capabilities remain protected.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ExpirePostResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .expire400_error import Expire400Error
        from .expire403_error import Expire403Error
        from .expire404_error import Expire404Error
        from .expire409_error import Expire409Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": Expire400Error,
            "403": Expire403Error,
            "404": Expire404Error,
            "409": Expire409Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .expire_post_response import ExpirePostResponse

        return await self.request_adapter.send_async(request_info, ExpirePostResponse, error_mapping)
    
    def to_post_request_information(self,body: ExpirePostRequestBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Requires submissions:write. Immediately expires all active links on a completely unsigned, unsealed submission. Retains answers, consent and audit evidence. Repeating the request is safe. Completed or partially signed submissions and active send capabilities remain protected.
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
    
    def with_url(self,raw_url: str) -> ExpireRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ExpireRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ExpireRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ExpireRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

