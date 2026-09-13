const reduceMotion=window.matchMedia('(prefers-reduced-motion: reduce)').matches;

const header=document.querySelector('header');
const onScroll=()=>header?.classList.toggle('scrolled',window.scrollY>24);
onScroll();window.addEventListener('scroll',onScroll,{passive:true});

if(!reduceMotion){
  const io=new IntersectionObserver((entries)=>{
    entries.forEach((entry)=>{
      if(entry.isIntersecting){entry.target.classList.add('is-visible');io.unobserve(entry.target)}
    })
  },{threshold:.12,rootMargin:'0px 0px -6%'});
  document.querySelectorAll('[data-reveal]').forEach(el=>io.observe(el));
}

const mobileNavToggle=document.querySelector('.mobile-nav-toggle');
const mobileNavPanel=document.querySelector('.mobile-nav-panel');
const mobileNavClose=document.querySelector('.mobile-nav-close');
const mobileNavBackdrop=document.querySelector('.mobile-nav-backdrop');
const setMobileNav=(open)=>{
  document.body.classList.toggle('mobile-nav-open',open);
  mobileNavToggle?.setAttribute('aria-expanded',String(open));
  mobileNavPanel?.setAttribute('aria-hidden',String(!open));
};
mobileNavToggle?.addEventListener('click',()=>setMobileNav(true));
mobileNavClose?.addEventListener('click',()=>setMobileNav(false));
mobileNavBackdrop?.addEventListener('click',()=>setMobileNav(false));
document.addEventListener('keydown',e=>{if(e.key==='Escape')setMobileNav(false)});

document.querySelectorAll('a[href^="#"]').forEach(link=>{
  link.addEventListener('click',e=>{
    const id=link.getAttribute('href');
    const target=id&&id.length>1?document.querySelector(id):null;
    if(!target)return;
    e.preventDefault();
    setMobileNav(false);
    target.scrollIntoView({behavior:reduceMotion?'auto':'smooth',block:'start'});
  });
});
