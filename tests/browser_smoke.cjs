const {chromium} = require('playwright');
const fs = require('fs');
const path = require('path');
const assert = require('node:assert/strict');
(async()=>{
 const browser=await chromium.launch({headless:true});
 const proof=path.resolve('artifacts/browser-qa');
 fs.mkdirSync(proof,{recursive:true});
 try{
  for(const width of [360,390,1280]){
   const page=await browser.newPage({viewport:{width,height:850},acceptDownloads:true});
   const errors=[];page.on('pageerror',error=>errors.push(error.message));
   await page.goto('http://127.0.0.1:8765/',{waitUntil:'load'});
   await page.waitForSelector('#chapterGrid .card');
   assert.match(await page.locator('#chapterCount').innerText(),/30\/30/);
   assert.match(await page.locator('#caseCount').innerText(),/37\/37/);
   assert.equal(await page.locator('#sourceGrid .resource').count(),29);
   assert.match(await page.locator('#sourceGrid .resource').first().innerText(),/来源台账日期 2026-11-05（非实时核验）/);
   assert.equal(await page.locator('#exportCalc').isDisabled(),false);
   await page.locator('#f-cost').fill('');
   assert.equal(await page.locator('#exportCalc').isDisabled(),true,'cannot export missing input');
   assert.equal(await page.locator('#copyCalc').isDisabled(),true,'cannot copy invalid estimate');
   assert.match(await page.locator('#calcResults').innerText(),/不能自动当作0/);
   await page.locator('#f-cost').fill('40');
   await page.locator('#f-orders').fill('1.5');
   assert.equal(await page.locator('#exportCalc').isDisabled(),true,'fractional orders are invalid');
   await page.locator('#f-orders').fill('100');
   assert.equal(await page.locator('#exportCalc').isDisabled(),false);
   const downloadReady=page.waitForEvent('download');
   await page.locator('#exportCalc').click();
   const download=await downloadReady;
   const exported=fs.readFileSync(await download.path(),'utf8');
   assert.match(download.suggestedFilename(),/测算明细|经济账/);
   assert.match(exported,/教学假设\/用户自填/);
   assert.match(exported,/订单|orders/);
   assert.match(exported,/净贡献|net/);
   await page.locator('#chapterSearch').fill('选品');
   assert.match(await page.locator('#chapterCount').innerText(),/\/30/);
   await page.locator('#chapterSearch').fill('');
   assert.match(await page.locator('#chapterCount').innerText(),/30\/30/);
   const overflow=await page.evaluate(()=>document.documentElement.scrollWidth-window.innerWidth);
   assert.ok(overflow<=2,'horizontal overflow at '+width+'px: '+overflow);
   assert.deepEqual(errors,[],'browser console errors');
   if(width===390||width===1280)await page.locator('#tools').screenshot({path:path.join(proof,'calc-'+width+'.png')});
   console.log('PASS viewport='+width+' source=29 missing-data=blocked fractional-orders=blocked CSV=verified');
   await page.close();
  }
 }finally{await browser.close()}
})().catch(error=>{console.error(error);process.exit(1)});
