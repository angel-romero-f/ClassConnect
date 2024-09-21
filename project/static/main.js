const announcementNumEl = document.getElementById("announcements-num")
const announcementItemEl = document.querySelectorAll("announcement-item")
const announcementBtnEl = document.getElementById("dismiss-all-btn")
const resetBtnEl = document.getElementById("reset-btn")

dismissBtnEl.addEventListener('click', () => {
    announcementItemEl.forEach(item => {
        item.classList.add('hide')
    })

    announcementNumEl.innerText = '0'
    document.querySelector('.announcements').style.width = "515px"

    dismissBtnEl.classList.add('hide')
    resetBtnEl.classList.add('show')
})

resetBtnEl.addEventListener('click', () => {
    announcementItemEl.forEach(item =>{
        item.classList.remove('hide')
    })

    announcementNumEl.innerText = '2'
    document.querySelector('.announcements').style.width = 'initial'

    dismissBtnEl.classList.remove('hide')
    resetBtnEl.classList.remove('show')
})