from pathlib import Path
import unittest
ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"

class PublicWebsiteQualityTests(unittest.TestCase):
    def test_public_contact_links_are_consistent(self):
        for path in [SITE / "index.html", SITE / "about.html", SITE / "chapters" / "01.html", SITE / "cases" / "C001.html"]:
            content = path.read_text(encoding="utf-8")
            with self.subTest(path=path.name):
                for term in ["AIPMAndy", "https://metaver.vip/", "https://www.a6no1.cn/"]:
                    self.assertIn(term, content)
    def test_pages_have_canonical_and_title(self):
        for path in [SITE / "index.html", SITE / "about.html", SITE / "chapters" / "01.html", SITE / "cases" / "C001.html"]:
            text = path.read_text(encoding="utf-8")
            with self.subTest(path=path.name):
                self.assertIn('<link rel="canonical"', text)
                self.assertIn("<title>", text)
    def test_geo_and_sitemap_exist(self):
        self.assertTrue((SITE / "sitemap.xml").exists())
        self.assertTrue((SITE / "llms.txt").exists())
        self.assertIn("Sitemap:", (SITE / "robots.txt").read_text(encoding="utf-8"))

if __name__ == "__main__": unittest.main()
