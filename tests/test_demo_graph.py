from pathlib import Path


def test_demo_graph_uses_demo_uris_and_law_decree_relation():
    text = Path("data/demo/canonical/demo.ttl").read_text(encoding="utf-8")

    assert "https://demo.plaza.cr/eli/" in text
    legacy_legal_scheme = "plaza-demo://" + "eli/"
    assert legacy_legal_scheme not in text
    assert "eli:based_on" in text
    assert "eli:basis_for" in text
    assert "eli:applies" not in text


def test_no_root_research_or_profiles_directories():
    assert not Path("research").exists()
    assert not Path("profiles").exists()
