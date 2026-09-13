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

document.querySelectorAll('a[href^="#"]').forEach(link=>{
  link.addEventListener('click',e=>{
    const id=link.getAttribute('href');
    const target=id&&id.length>1?document.querySelector(id):null;
    if(!target)return;
    e.preventDefault();
    target.scrollIntoView({behavior:reduceMotion?'auto':'smooth',block:'start'});
  });
});
