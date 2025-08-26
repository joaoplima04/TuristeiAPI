document.addEventListener("DOMContentLoaded", function () {
    const loginForm = document.getElementById("loginForm");
    const username = document.getElementById("username");
    const password = document.getElementById("password");
    const loginBtn = document.getElementById("loginBtn");
    const forgotPassword = document.getElementById("forgotPassword");
    const message = document.getElementById("message");

    // Habilitar botão de login quando os campos estiverem preenchidos
    function validateForm() {
        loginBtn.disabled = !(username.value.trim() && password.value.trim());
    }

    username.addEventListener("input", validateForm);
    password.addEventListener("input", validateForm);

    // Exibir mensagem ao clicar em "Esqueci minha senha"
    forgotPassword.addEventListener("click", function () {
        message.className = "alert alert-info";
        message.textContent = "Um código de verificação foi enviado ao seu email";
        message.classList.remove("d-none");
    });

    // Enviar requisição ao backend (simulação)
    loginForm.addEventListener("submit", function (event) {
        event.preventDefault();

        // Exibir um alert com os dados digitados antes do login ser processado
        alert(`Usuário: ${username.value}\nSenha: ${password.value}`);

        // Simulando um login bem-sucedido
        if (username.value === "admin" && password.value === "1234") {
            message.className = "alert alert-success";
            message.textContent = "Login bem-sucedido! Redirecionando...";
            message.classList.remove("d-none");

            setTimeout(() => {
                window.location.href = "welcome.html"; // Página de boas-vindas
            }, 2000);
        } else {
            message.className = "alert alert-danger";
            message.textContent = "Usuário ou senha inválidos!";
            message.classList.remove("d-none");
        }
    });
});
