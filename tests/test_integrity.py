import csv,json,re,unittest
from pathlib import Path
from urllib.parse import urlparse
R=Path(__file__).resolve().parent.parent
D=R/'data';S=R/'site'

def load(n):return json.loads((D/(n+'.json')).read_text('utf-8'))
class TestEvidence(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.cases=load('cases');cls.sources=load('sources');cls.chapters=load('chapters');cls.prompts=load('prompts');cls.routes=load('routes');cls.days=load('plan30')
 def test_counts(self):
  self.assertGreaterEqual(len(self.cases),35);self.assertEqual(len(self.chapters),30);self.assertEqual(len(self.prompts),26);self.assertEqual(len(self.days),30);self.assertEqual(len(self.routes),6);self.assertGreaterEqual(len(self.sources),25)
 def test_unique_ids(self):
  for dataset in (self.cases,self.sources,self.chapters,self.prompts,self.routes):
   ids=[x['id'] for x in dataset]
   self.assertEqual(len(ids),len(set(ids)))
 def test_evidence_linkages(self):
  src={s['id'] for s in self.sources}
  for c in self.cases:
   self.assertIn(c['source'],src);self.assertTrue(c['result']);self.assertTrue(c['period']);self.assertTrue(c['caution']);self.assertTrue(c['ai']);self.assertTrue(c['takeaway']);self.assertTrue(c['play']);self.assertFalse(c['profit_disclosed']);self.assertIn(c['evidence_tier'][0],'BCD');self.assertIn(c['id'],(S/'cases'/f'{c["id"]}.html').read_text('utf-8'))
  for ch in self.chapters:
   self.assertTrue(ch['steps']);self.assertGreaterEqual(len(ch['steps']),3)
   for sid in ch['relatedSources']:self.assertIn(sid,src)
 def test_authoritative_sources_have_usable_urls(self):
  for s in self.sources:
   u=urlparse(s['url']);self.assertEqual(u.scheme,'https');self.assertTrue(u.netloc);self.assertLessEqual(s['date'],'2026-11-05');self.assertTrue(s['kind'])
 def test_site_pages_and_nav(self):
  self.assertTrue((S/'about.html').exists())
  index=(S/'index.html').read_text('utf-8');self.assertIn('href="about.html"',index)
  for c in self.chapters:self.assertTrue((S/'chapters'/f'{c["id"]}.html').exists())
  for c in self.cases:self.assertTrue((S/'cases'/f'{c["id"]}.html').exists())
  self.assertEqual(len(list((S/'chapters').glob('*.html'))),30)
  self.assertEqual(len(list((S/'cases').glob('*.html'))),len(self.cases))
  self.assertTrue((S/'assets/model.js').exists())
 def test_daily_complete(self):
  self.assertEqual([x['day'] for x in self.days],list(range(1,31)))
  self.assertTrue(all(x['proof'] and x['gate'] for x in self.days))
 def test_csv_can_be_imported(self):
  paths=list((R/'templates').glob('*.csv'))
  self.assertGreaterEqual(len(paths),14)
  for p in paths:
   with p.open(encoding='utf-8-sig',newline='') as f:
    rows=list(csv.reader(f));self.assertGreaterEqual(len(rows[0]),3);self.assertTrue(all(rows[0]))
  with (D/'cases.csv').open(encoding='utf-8-sig',newline='') as f:self.assertEqual(len(list(csv.reader(f)))-1,len(self.cases))
 def test_docs_contributions_are_present(self):
  self.assertTrue((R/'LICENSE').exists());self.assertTrue((R/'CONTRIBUTING.md').exists());self.assertTrue((R/'.github/workflows/pages.yml').exists())
  self.assertGreaterEqual(len(list((R/'docs').glob('*.md'))),16)
  self.assertEqual(len(list((R/'research').glob('*.md'))),len(self.cases))
  self.assertEqual(len(list((R/'prompts').glob('*.md'))),len(self.prompts))
  self.assertEqual(len(list((R/'content').glob('*.md'))),len(self.chapters))
if __name__=='__main__':unittest.main()
