from Atid_storess.page.pageTest import AtidStore_page


class Test_posetive(AtidStore_page):

    def test_store(self):
        atid_page = AtidStore_page()
        atid_page.open()
        atid_page.execute_test_store()

    def test_men(self):
        atid_page = AtidStore_page()
        atid_page.open()
        atid_page.execute_men_acceseries()

    def test_women(self):
        atid_page = AtidStore_page()
        atid_page.open()
        atid_page.execute_test_Women_product()

    def test_accessories(self):

        atid_page = AtidStore_page()
        atid_page.open()
        atid_page.execute_accsesories_product()






