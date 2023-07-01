
// js code to show header animated
const text = document.getElementById("gtoup_name");
const words = text.innerText.split("");
text.innerText = "";

for (let i = 0; i < words.length; i++) {
    setTimeout(() => {
    text.innerText += words[i] + " ";}, i * 200);
}

function changeColor(element) {
  const listItems = document.querySelectorAll('.list-group-item');
  listItems.forEach(item => {
    item.classList.remove('active');
  });
  element.classList.add('active');
}
