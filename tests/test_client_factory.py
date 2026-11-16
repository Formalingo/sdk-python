import unittest
from unittest.mock import patch

import httpx
from kiota_http.httpx_request_adapter import HttpxRequestAdapter

from formalingo import FormalingoClient, create_client


class ClientFactoryTests(unittest.IsolatedAsyncioTestCase):
    async def test_uses_the_production_api_by_default(self):
        async with httpx.AsyncClient(transport=httpx.MockTransport(lambda _: httpx.Response(200))) as http_client:
            with patch(
                "formalingo.HttpxRequestAdapter",
                side_effect=lambda auth: HttpxRequestAdapter(auth, http_client=http_client),
            ):
                client = create_client("af_live_test_only")

            self.assertIsInstance(client, FormalingoClient)
            self.assertEqual(client.request_adapter.base_url, "https://app.formalingo.com")

    async def test_sends_bearer_auth_to_the_overridden_api_url(self):
        requests = []

        def respond(request):
            requests.append(request)
            return httpx.Response(200, json={"success": True, "data": []})

        async with httpx.AsyncClient(transport=httpx.MockTransport(respond)) as http_client:
            with patch(
                "formalingo.HttpxRequestAdapter",
                side_effect=lambda auth: HttpxRequestAdapter(auth, http_client=http_client),
            ):
                client = create_client("af_live_test_only", "http://127.0.0.1:35817")

            response = await client.api.v1.forms.get()

        self.assertTrue(response.success)
        self.assertEqual(len(requests), 1)
        self.assertEqual(str(requests[0].url), "http://127.0.0.1:35817/api/v1/forms")
        self.assertEqual(requests[0].headers["Authorization"], "Bearer af_live_test_only")

    def test_rejects_an_empty_api_key_without_echoing_credentials(self):
        for key in ("", " ", None):
            with self.subTest(key=key), self.assertRaisesRegex(ValueError, "non-empty string"):
                create_client(key)

    async def test_rejects_foreign_origins_before_sending_credentials(self):
        requests = []

        def respond(request):
            requests.append(request)
            return httpx.Response(200, json={"success": True, "data": []})

        async with httpx.AsyncClient(transport=httpx.MockTransport(respond)) as http_client:
            with patch(
                "formalingo.HttpxRequestAdapter",
                side_effect=lambda auth: HttpxRequestAdapter(auth, http_client=http_client),
            ):
                client = create_client("af_live_never_send")

            for url in (
                "https://other.example/api/v1/forms",
                "https://app.formalingo.com:444/api/v1/forms",
                "http://app.formalingo.com/api/v1/forms",
            ):
                with self.subTest(url=url):
                    with self.assertRaisesRegex(ValueError, "configured API origin") as error:
                        await client.api.v1.forms.with_url(url).get()
                    self.assertNotIn("af_live_never_send", str(error.exception))

        self.assertEqual(requests, [])

    async def test_accepts_the_same_origin_with_an_explicit_default_port(self):
        requests = []

        def respond(request):
            requests.append(request)
            return httpx.Response(200, json={"success": True, "data": []})

        async with httpx.AsyncClient(transport=httpx.MockTransport(respond)) as http_client:
            with patch(
                "formalingo.HttpxRequestAdapter",
                side_effect=lambda auth: HttpxRequestAdapter(auth, http_client=http_client),
            ):
                client = create_client("af_live_test_only")

            await client.api.v1.forms.with_url("https://app.formalingo.com:443/api/v1/forms").get()

        self.assertEqual(len(requests), 1)
        self.assertEqual(requests[0].headers["Authorization"], "Bearer af_live_test_only")

    def test_rejects_invalid_or_credentialed_base_urls(self):
        for base_url in (
            "ftp://app.formalingo.com",
            "https://user:password@app.formalingo.com",
            "https://app.formalingo.com:bad",
            "/api",
        ):
            with self.subTest(base_url=base_url), self.assertRaises(ValueError):
                create_client("af_live_test_only", base_url)


if __name__ == "__main__":
    unittest.main()
