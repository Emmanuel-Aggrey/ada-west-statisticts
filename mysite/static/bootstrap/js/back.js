
document.querySelector('.back').addEventListener('click',goBack)
function goBack(goback) {
  window.history.back()
//   if (goback.keyCode===8){
//       console.log('')
//    window.history.back()
// }
}


window.addEventListener('keyup',MyBack)
function MyBack(ev) {
  if (ev.keyCode===8){
      console.log('')
   window.history.back()
}
}
