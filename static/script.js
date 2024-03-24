// dummy storage
const messages = [];

async function submitForm() {
  console.log("---------Function Running-------------");
  const tesxtareaEl = document.getElementById("usrInp");
  const question = tesxtareaEl.value.trim();
  if (tesxtareaEl && question) {
    let isPrevQst = false;
    let prevAnswer = "";
    messages.forEach((msg) => {
      if (msg["question"] == question) {
        isPrevQst = true;
        prevAnswer = msg["answer"];
      }
    });

    const btnEl = document.getElementById("btnSubmit");
    const loaderEL = document.getElementById("loader");
    loaderEL.classList.remove("hidden");
    btnEl.setAttribute("disabled", "");
    btnEl.classList.add("loading");

    let answer = "";
    if (isPrevQst) {
      answer = prevAnswer;
    } else {
      const response = await fetch("/", {
        method: "POST",
        mode: "cors",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          human: question,
        }),
      });
      const res = await response.json();
      answer = res.message;
      console.log({ res });
    }

    console.log({ answer });
    console.log({ question });
    // update UI(
    updateUI({
      question,
      answer,
    });
    loaderEL.classList.add("hidden");
    btnEl.classList.remove("loading");
    btnEl.removeAttribute("disabled");

    tesxtareaEl.textContent = "";
  }
}

const updateUI = ({ question, answer }) => {
  const chatsEl = document.getElementById("chats");
  messages.push({
    question,
    answer,
  });
  let chats = `<div>`;
  messages.forEach((message) => {
    let messageBlock = `<div class="msg-block">`;
    const humanMessage = `<div class="human-msg"> ${message.question} </div>`;
    const aiMessage = `<div class="ai-msg"> ${message.answer} </div>`;
    messageBlock += `${humanMessage} ${aiMessage} </div>`;

    chats += `${messageBlock}`;
  });
  chats += `</div>`;

  chatsEl.innerHTML = chats;
};
