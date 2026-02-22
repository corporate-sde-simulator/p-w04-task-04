"""Tests for Distributed cache invalidation protocol."""
import pytest, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from cacheInvalidator import CacheInvalidator
from peerManager import PeerManager

class TestMain:
    def test_basic(self):
        obj = CacheInvalidator()
        assert obj.process({"key": "val"}) is not None
    def test_empty(self):
        obj = CacheInvalidator()
        assert obj.process(None) is None
    def test_stats(self):
        obj = CacheInvalidator()
        obj.process({"x": 1})
        assert obj.get_stats()["processed"] == 1

class TestSupport:
    def test_basic(self):
        obj = PeerManager()
        assert obj.process({"key": "val"}) is not None

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
