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
    from ......models.start_document_parse_job_body import StartDocumentParseJobBody
    from ......models.start_document_parse_job_response import StartDocumentParseJobResponse
    from .item.with_job_item_request_builder import WithJobItemRequestBuilder
    from .start_document_parse_job_response400_error import StartDocumentParseJobResponse400Error
    from .start_document_parse_job_response403_error import StartDocumentParseJobResponse403Error
    from .start_document_parse_job_response404_error import StartDocumentParseJobResponse404Error

class ParseJobsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1/documents/{id}/parse-jobs
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ParseJobsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1/documents/{id}/parse-jobs", path_parameters)
    
    def by_job_id(self,job_id: UUID) -> WithJobItemRequestBuilder:
        """
        Gets an item from the formalingo.api.v1.documents.item.parseJobs.item collection
        param job_id: Unique identifier of the item
        Returns: WithJobItemRequestBuilder
        """
        if job_id is None:
            raise TypeError("job_id cannot be null.")
        from .item.with_job_item_request_builder import WithJobItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["jobId"] = job_id
        return WithJobItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: StartDocumentParseJobBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[StartDocumentParseJobResponse]:
        """
        Creates an AI-assisted document parse job. Requires the `documents:parse_ai` permission in addition to `write:documents`.
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[StartDocumentParseJobResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from .start_document_parse_job_response400_error import StartDocumentParseJobResponse400Error
        from .start_document_parse_job_response403_error import StartDocumentParseJobResponse403Error
        from .start_document_parse_job_response404_error import StartDocumentParseJobResponse404Error

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": StartDocumentParseJobResponse400Error,
            "403": StartDocumentParseJobResponse403Error,
            "404": StartDocumentParseJobResponse404Error,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.start_document_parse_job_response import StartDocumentParseJobResponse

        return await self.request_adapter.send_async(request_info, StartDocumentParseJobResponse, error_mapping)
    
    def to_post_request_information(self,body: StartDocumentParseJobBody, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates an AI-assisted document parse job. Requires the `documents:parse_ai` permission in addition to `write:documents`.
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
    
    def with_url(self,raw_url: str) -> ParseJobsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ParseJobsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ParseJobsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ParseJobsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

