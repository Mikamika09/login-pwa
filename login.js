// ===============================
// 仮のユーザデータ（DBの代わり）
// ===============================
// Pythonの users = {} と同じ役割
const users = {
  "alice": "alice123",
  "bob": "bob12345",
  "charlie": "charlie999"
};

// ===============================
// ログイン処理
// ===============================
function login() {
  // 入力値を取得
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;
  const message = document.getElementById("message");

  // 何も入力されていない場合
  if (username === "" || password === "") {
    message.textContent = "ユーザ名とパスワードを入力してください";
    return;
  }

  // ユーザ存在チェック
  if (!(username in users)) {
    message.textContent = "そのユーザ名は存在しません";
    return;
  }

  // パスワード照合
  if (users[username] !== password) {
    message.textContent = "パスワードが違います";
    return;
  }

  // ログイン成功
  message.textContent = "ログイン成功！ようこそ " + username;
}

