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

function ensureMobileNav(){
  if(document.querySelector('.mobile-nav-toggle')) return;
  const nav=document.querySelector('.nav');
  const lang=document.querySelector('.lang');
  if(!nav) return;

  const toggle=document.createElement('button');
  toggle.className='mobile-nav-toggle';
  toggle.type='button';
  toggle.setAttribute('aria-expanded','false');
  toggle.setAttribute('aria-label','Menu');
  toggle.textContent='☰';

  const backdrop=document.createElement('div');
  backdrop.className='mobile-nav-backdrop';

  const panel=document.createElement('aside');
  panel.className='mobile-nav-panel';
  panel.setAttribute('aria-hidden','true');

  const close=document.createElement('button');
  close.className='mobile-nav-close';
  close.type='button';
  close.setAttribute('aria-label','Close');
  close.textContent='×';
  panel.appendChild(close);

  nav.querySelectorAll('a').forEach(a=>panel.appendChild(a.cloneNode(true)));
  if(lang){
    const ml=document.createElement('div');
    ml.className='mobile-lang';
    lang.querySelectorAll('a').forEach(a=>ml.appendChild(a.cloneNode(true)));
    panel.appendChild(ml);
  }
  document.body.append(toggle,backdrop,panel);
}
ensureMobileNav();

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

window.addEventListener('resize',()=>{
  if(window.innerWidth>800) setMobileNav(false);
});

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

// Primary business email across all language versions.
const contactInfo=document.querySelector('#contact .contact-info');
if(contactInfo&&!contactInfo.querySelector('a[href^="mailto:"]')){
  const email=document.createElement('p');
  const label=document.documentElement.lang==='fa'?'ایمیل':document.documentElement.lang==='ar'?'البريد الإلكتروني':'EMAIL';
  email.innerHTML=`<b>${label}</b><a href="mailto:business@shakibanameghi.com">business@shakibanameghi.com</a>`;
  contactInfo.appendChild(email);
}
