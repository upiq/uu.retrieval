import unittest2 as unittest


class PkgTest(unittest.TestCase):
    """basic unit tests for package go here"""
    
    def test_pkg_import(self):
        """test basic package imports"""
        import uu.retrieval  # noqa
        from uu.retrieval import interfaces
        from uu.retrieval.indexing import interfaces  # noqa
        from uu.retrieval import indexing  # noqa
        from uu.retrieval import utils  # noqa

