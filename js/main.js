(()=>{const $=s=>document.querySelector(s),$$=s=>[...document.querySelectorAll(s)];
const mb=$('.menu-btn'),menu=$('#menu');
if(mb){mb.addEventListener('click',()=>{const o=menu.classList.toggle('open');mb.setAttribute('aria-expanded',o);mb.textContent=o?'Close':'Menu'});
 addEventListener('keydown',e=>{if(e.key==='Escape'&&menu.classList.contains('open')){menu.classList.remove('open');mb.setAttribute('aria-expanded',false);mb.textContent='Menu';mb.focus()}})}
const q=$('#qform');q&&q.addEventListener('submit',e=>{e.preventDefault();$('#qmsg').textContent=q.checkValidity()?'Thanks. On the live site this goes to the Carroll office. (Demo: nothing was sent.)':'Please add your name and phone number.'});
const reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
const count=el=>{const end=parseFloat(el.dataset.count),dec=+(el.dataset.dec||0),t0=performance.now(),d=800;const f=t=>{const k=Math.min((t-t0)/d,1),v=end*(1-Math.pow(1-k,3));el.textContent=v.toFixed(dec);if(k<1)requestAnimationFrame(f)};requestAnimationFrame(f)};
const els=$$('.rv');
if(!('IntersectionObserver' in window)||reduce){els.forEach(e=>e.classList.add('in'));return}
const io=new IntersectionObserver(es=>es.forEach(en=>{if(en.isIntersecting){const t=en.target,s=[...t.parentNode.children].filter(x=>x.classList.contains('rv'));t.style.transitionDelay=Math.min(Math.max(s.indexOf(t),0),5)*70+'ms';t.classList.add('in');t.querySelectorAll('[data-count]').forEach(count);if(t.dataset.count)count(t);io.unobserve(t)}}),{rootMargin:'0px 0px -80px 0px'});
els.forEach(e=>io.observe(e));})();
