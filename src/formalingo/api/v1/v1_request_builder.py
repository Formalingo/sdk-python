from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .analytics.analytics_request_builder import AnalyticsRequestBuilder
    from .deliveries.deliveries_request_builder import DeliveriesRequestBuilder
    from .documents.documents_request_builder import DocumentsRequestBuilder
    from .forms.forms_request_builder import FormsRequestBuilder
    from .integrations.integrations_request_builder import IntegrationsRequestBuilder
    from .quota.quota_request_builder import QuotaRequestBuilder

class V1RequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/v1
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new V1RequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/v1", path_parameters)
    
    @property
    def analytics(self) -> AnalyticsRequestBuilder:
        """
        The analytics property
        """
        from .analytics.analytics_request_builder import AnalyticsRequestBuilder

        return AnalyticsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def deliveries(self) -> DeliveriesRequestBuilder:
        """
        The deliveries property
        """
        from .deliveries.deliveries_request_builder import DeliveriesRequestBuilder

        return DeliveriesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def documents(self) -> DocumentsRequestBuilder:
        """
        The documents property
        """
        from .documents.documents_request_builder import DocumentsRequestBuilder

        return DocumentsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def forms(self) -> FormsRequestBuilder:
        """
        The forms property
        """
        from .forms.forms_request_builder import FormsRequestBuilder

        return FormsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def integrations(self) -> IntegrationsRequestBuilder:
        """
        The integrations property
        """
        from .integrations.integrations_request_builder import IntegrationsRequestBuilder

        return IntegrationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def quota(self) -> QuotaRequestBuilder:
        """
        The quota property
        """
        from .quota.quota_request_builder import QuotaRequestBuilder

        return QuotaRequestBuilder(self.request_adapter, self.path_parameters)
    

