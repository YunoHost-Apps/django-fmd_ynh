from bx_py_utils.test_utils.unittest_utils import BaseDocTests

import django_fmd_ynh


class DocTests(BaseDocTests):
    def test_doctests(self):
        self.run_doctests(
            modules=(django_fmd_ynh,),
        )
