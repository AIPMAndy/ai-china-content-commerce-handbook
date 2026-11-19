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

    def test_all_generated_chapters_and_cases_expose_grounded_jsonld(self):
        import json
        import re
        import html
        for folder in ("chapters", "cases"):
            pages = sorted((SITE / folder).glob("*.html"))
            self.assertGreater(len(pages), 0)
            for page in pages:
                text = page.read_text(encoding="utf-8")
                with self.subTest(path=str(page.relative_to(SITE))):
                    match = re.search(r'<script type="application/ld\+json">([^<]+)</script>', text)
                    self.assertIsNotNone(match, "missing machine-readable evidence")
                    entity = json.loads(html.unescape(match.group(1)))
                    self.assertEqual(entity["@type"], "Article")
                    self.assertEqual(entity["author"]["url"], "https://metaver.vip/")
                    self.assertEqual(entity["publisher"]["url"], "https://www.a6no1.cn/")
                    self.assertEqual(entity["mainEntityOfPage"]["@id"], "https://aipmandy.github.io/ai-china-content-commerce-handbook/" + str(page.relative_to(SITE)).replace("\\", "/"))
                    self.assertTrue(entity["citation"])
                    self.assertNotIn("datePublished", entity, "source ledger date is not publication date")
                    self.assertIn("来源台账日期", text)
                    if folder == "cases":
                        self.assertIn("第三方披露案例", text)
                        self.assertIn("台账日期不等于本次实时核验日期", text)

    def test_calculator_export_and_historical_source_date(self):
        homepage=(SITE / "index.html").read_text(encoding="utf-8")
        script=(SITE / "assets" / "app.js").read_text(encoding="utf-8")
        model=(SITE / "assets" / "model.js").read_text(encoding="utf-8")
        self.assertIn('id="exportCalc"', homepage)
        self.assertIn("lastCalc=null", script)
        self.assertIn("缺失项不能自动当作0", script)
        self.assertIn("来源台账日期", script)
        self.assertIn("function whole(n,name)", model)
        self.assertIn("内容电商经济账-教学测算.csv", script)

if __name__ == "__main__": unittest.main()
