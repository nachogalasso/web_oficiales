/* LANDING PAGE SCRIPTS */
// ACCORDION ELEMENTS
const navBtn = document.querySelectorAll('.accordion__info-bar');
const panels = document.querySelectorAll('.info-bar-panel');


navBtn.forEach(btns => {

  btns.addEventListener('click', (e) => {
    const pics = document.querySelectorAll(".slider");
    e.target.classList.toggle('act')
    img = e.target.id
    let panel = e.target.nextElementSibling
    if(panel.style.maxHeight) {
      panel.style.maxHeight = null;
    }else{
      panel.style.maxHeight = panel.scrollHeight + 'rem'
    }

    if(img === 'slide-1') {
      pics[0].classList.replace('hidden', 'show')
      pics[1].classList.replace('show', 'hidden')
      pics[2].classList.replace('show', 'hidden')
    }else if(img === 'slide-2') {
      pics[1].classList.replace('hidden', 'show')
      pics[2].classList.replace('show', 'hidden')
      pics[0].classList.replace('show', 'hidden')
    }else{
      pics[2].classList.replace('hidden', 'show')
      pics[0].classList.replace('show', 'hidden')
      pics[1].classList.replace('show', 'hidden')
    }
    
  })
})

// AVAILABILITY PAGE
const btns = [...document.querySelectorAll('.tab-btn')]
const forms = [...document.querySelectorAll('.tab-content')]

forms[0].style.display = 'block'
btns.forEach(item => {
  item.addEventListener('click', () => {
    const target = item.getAttribute('data-target');
    forms.forEach(form => {
      if (form.id === target) {
        form.style.display = 'block';
      }else{
        form.style.display = 'none';
      }
    })
  })
})