// 仮のユーザ情報（Pythonの users = {} と同じ）
const users = {
  "test": "test1234"
};

function login() {
  // 入力値を取得
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;
  const message = document.getElementById("message");

  // ユーザ存在チェック
  if (!(username in users)) {
    message.textContent = "そのユーザ名は存在しません";
    return;
  }

  // パスワードチェック
  if (users[username] !== password) {
    message.textContent = "パスワードが違います";
    return;
  }

  // 成功
  message.textContent = "ログイン成功！";
}
