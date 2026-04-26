DEMO_ELI_PREFIX = "https://demo.plaza.cr/eli/"


def is_demo_eli_uri(uri: str) -> bool:
    return uri.startswith(DEMO_ELI_PREFIX) and len(uri) > len(DEMO_ELI_PREFIX)
