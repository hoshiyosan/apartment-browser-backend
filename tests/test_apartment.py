from apartment_browser.coreutils.service import BaseService


def test_base_service_interface():
    assert hasattr(BaseService, "search")
    assert hasattr(BaseService, "get_details")
    assert hasattr(BaseService, "validate")
    assert hasattr(BaseService, "create")
    assert hasattr(BaseService, "update")
    assert hasattr(BaseService, "delete")
