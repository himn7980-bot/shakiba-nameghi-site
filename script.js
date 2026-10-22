// Header shadow on scroll, mobile menu, current year.
(function(){
  var root=document.documentElement;
  var header=document.querySelector('.site-header');
  var btn=document.querySelector('.menu-btn');
  var panel=document.getElementById('panel');

  function onScroll(){header&&header.classList.toggle('scrolled',window.scrollY>8)}
  onScroll();window.addEventListener('scroll',onScroll,{passive:true});

  function setMenu(open){
    root.classList.toggle('menu-open',open);
    if(btn)btn.setAttribute('aria-expanded',String(open));
  }
  if(btn){
    btn.addEventListener('click',function(){setMenu(!root.classList.contains('menu-open'))});
    panel&&panel.addEventListener('click',function(e){if(e.target.closest('a'))setMenu(false)});
    document.addEventListener('keydown',function(e){if(e.key==='Escape'&&root.classList.contains('menu-open')){setMenu(false);btn.focus()}});
    document.addEventListener('click',function(e){if(root.classList.contains('menu-open')&&!e.target.closest('.site-header'))setMenu(false)});
    window.addEventListener('resize',function(){if(window.innerWidth>900)setMenu(false)});
  }

  var y=document.querySelector('.yr-now');
  if(y){
    var n=new Date().getFullYear();
    var lang=root.lang;
    y.textContent=lang==='fa'?n.toLocaleString('fa-IR',{useGrouping:false}):String(n);
  }
})();
