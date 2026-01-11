const users = {
  "test": "test1234"
};

let currentUser = null;

function login() {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;
  const message = document.getElementById("message");

  if (!(username in users)) {
    message.textContent = "ユーザが存在しません";
    return;
  }

  if (users[username] !== password) {
    message.textContent = "パスワードが違います";
    return;
  }

  currentUser = username;
  message.textContent = "ログイン成功！";
}
