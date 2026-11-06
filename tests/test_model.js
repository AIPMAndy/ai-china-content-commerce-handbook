const { test } = require('node:test');
const assert = require('node:assert/strict');
const m = require('../site/assets/model.js');
const base = {orders:100, price:99, cost:40, shipping:7, packaging:1, refundRate:12, platformRate:4, affiliateRate:0, returnLoss:5, ads:800, labor:300, fixed:100};
test('商家模型分清支付GMV、退款后收入、净贡献',()=>{
 const x=m.merchant(base);assert.equal(x.gmv,9900);assert.equal(x.netRevenue,8712);assert.equal(x.keptOrders,88);assert.equal(x.returns,12);assert.equal(x.net,2783.52);assert.equal(x.contribution,3983.52);
});
test('商家退款比例为100%，收入不能凭空出现',()=>{
 const x=m.merchant({...base,refundRate:100});assert.equal(x.netRevenue,0);assert.equal(x.gmv,9900);assert.ok(x.net<0);
});
test('商家100单不可视为100单已履约',()=>{
 const x=m.merchant({...base,refundRate:37});assert.equal(x.keptOrders,63);assert.equal(x.returns,37);
});
test('负数和超过100%费率要拦截',()=>{
 assert.throws(()=>m.merchant({...base,refundRate:120}),RangeError);assert.throws(()=>m.merchant({...base,price:-1}),RangeError);assert.throws(()=>m.merchant({...base,ads:Infinity}),RangeError);
});
test('达人佣金按未退货GMV算，扣内容和样品成本',()=>{
 const x=m.creator({orders:100,price:100,refundRate:20,commissionRate:10,samples:180,content:120,ads:200,other:40});assert.equal(x.gmv,10000);assert.equal(x.gross,800);assert.equal(x.net,260);
});
test('达人零订单不能误判赚钱',()=>{
 const x=m.creator({orders:0,price:100,refundRate:10,commissionRate:10,samples:50,content:100,ads:0,other:0});assert.equal(x.gross,0);assert.equal(x.net,-150);
});
test('B端服务费减交付工时、外包、获客与工具',()=>{
 const x=m.service({clients:2,fee:4500,hours:20,hourly:100,outsourcing:500,tools:500,acquisition:400,other:100});assert.equal(x.netRevenue,9000);assert.equal(x.delivery,5000);assert.equal(x.net,3000);
});
test('B端零客户应仍计入固定费用',()=>{
 const x=m.service({clients:0,fee:4500,hours:20,hourly:100,outsourcing:500,tools:500,acquisition:400,other:100});assert.equal(x.net,-1000);
});
test('完整SKU教学模拟数与经济账模型一致',()=>{
 const x=m.merchant({orders:100,price:69,cost:24,shipping:6,packaging:1,refundRate:10,platformRate:4,affiliateRate:0,returnLoss:3,ads:400,labor:200,fixed:0});
 assert.equal(x.gmv,6900);assert.equal(x.netRevenue,6210);assert.equal(x.net,2471.6);
});
