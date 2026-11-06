(function(){'use strict';
  function manualCopy(value){
    var area=document.createElement('textarea');
    area.value=value;area.setAttribute('readonly','');
    area.style.position='fixed';area.style.left='-9999px';
    document.body.appendChild(area);area.select();
    var ok=false;
    try{ok=document.execCommand('copy');}catch(e){ok=false;}
    area.remove();return ok;
  }
  document.addEventListener('click',function(event){
    var btn=event.target.closest('.js-copy-wechat');
    if(!btn)return;
    var value=btn.getAttribute('data-wechat')||'AIPMAndy';
    var panel=btn.closest('.contact-panel')||document;
    var status=panel.querySelector('.contact-feedback');
    function show(ok){if(status)status.textContent=ok?'已复制：'+value+'，打开微信搜索添加':'复制失败，请打开微信搜索：'+value;}
    if(navigator.clipboard&&navigator.clipboard.writeText){
      navigator.clipboard.writeText(value).then(function(){show(true)},function(){show(manualCopy(value))});
    }else{show(manualCopy(value));}
  });
})();
