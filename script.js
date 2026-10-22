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

// ---------- Motion ----------
(function(){
  var root=document.documentElement;
  var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Cursor spotlight on dark cards (desktop pointers only)
  document.querySelectorAll('.skill,.rep').forEach(function(card){
    card.addEventListener('pointermove',function(e){
      var r=card.getBoundingClientRect();
      card.style.setProperty('--mx',(e.clientX-r.left)+'px');
      card.style.setProperty('--my',(e.clientY-r.top)+'px');
    });
    card.addEventListener('pointerleave',function(){card.style.removeProperty('--mx');card.style.removeProperty('--my');});
  });

  if(reduce||!('IntersectionObserver' in window))return;
  root.classList.add('js-motion');

  // Scroll reveal with a stagger inside each group
  var groups=['.head','.profile','.facts > div','.skills > .skill','.projs > .proj','.reps > .rep','.timeline > li','.stats > .stat','.contact .lead','.contact .actions','.channels > li'];
  groups.forEach(function(sel){
    var parents=new Map();
    document.querySelectorAll(sel).forEach(function(el){
      if(el.closest('.hero-text'))return;
      var p=el.parentElement,n=parents.get(p)||0;parents.set(p,n+1);
      el.classList.add('rv');el.style.setProperty('--i',Math.min(n,6));
    });
  });
  var io=new IntersectionObserver(function(entries){
    entries.forEach(function(en){if(en.isIntersecting){en.target.classList.add('on');io.unobserve(en.target);}});
  },{threshold:.15,rootMargin:'0px 0px -8% 0px'});
  document.querySelectorAll('.rv').forEach(function(el){io.observe(el)});

  // Counting stats (handles Persian digits)
  var fa='۰۱۲۳۴۵۶۷۸۹';
  function toLatin(s){return s.replace(/[۰-۹]/g,function(d){return fa.indexOf(d)})}
  function toFa(n){return String(n).replace(/\d/g,function(d){return fa[d]})}
  var sio=new IntersectionObserver(function(entries){
    entries.forEach(function(en){
      if(!en.isIntersecting)return;sio.unobserve(en.target);
      var el=en.target,raw=el.textContent.trim(),persian=/[۰-۹]/.test(raw),end=parseInt(toLatin(raw),10);
      if(isNaN(end))return;
      var start=end>1000?end-30:0,t0=null,dur=1400;
      function step(t){
        if(!t0)t0=t;var k=Math.min(1,(t-t0)/dur),v=Math.round(start+(end-start)*(1-Math.pow(1-k,3)));
        el.textContent=persian?toFa(v):String(v);if(k<1)requestAnimationFrame(step);
      }
      requestAnimationFrame(step);
    });
  },{threshold:.6});
  document.querySelectorAll('.stat b').forEach(function(b){sio.observe(b)});

  // Timeline fills as you scroll through it
  var tl=document.querySelector('.timeline');
  if(tl){
    var items=tl.querySelectorAll('li');
    var tick=function(){
      var r=tl.getBoundingClientRect(),vh=window.innerHeight,mark=vh*.62;
      var f=Math.max(0,Math.min(1,(mark-r.top)/r.height));
      tl.style.setProperty('--fill',f.toFixed(3));
      items.forEach(function(li){li.classList.toggle('lit',li.getBoundingClientRect().top+10<mark)});
    };
    tick();window.addEventListener('scroll',function(){requestAnimationFrame(tick)},{passive:true});window.addEventListener('resize',tick);
  }
})();
