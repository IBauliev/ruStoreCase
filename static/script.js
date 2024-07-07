async function sendMessage() {
    const userInput = document.getElementById('userInput').value;
    if (userInput.trim() === "") return; // Проверка на пустой ввод

    const chatbox = document.getElementById('chatbox');  // Создание и добавление сообщения пользователя в чат
    const userMessage = document.createElement('div');
    userMessage.className = 'message user-message';
    userMessage.textContent = userInput;
    chatbox.appendChild(userMessage);
    chatbox.scrollTop = chatbox.scrollHeight; // Прокрутка чата вниз

    try {
         // Отправка запроса к API
        const response = await fetch('https://api.', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer sk-115f6cca8d3b4c46bb9739c9387c002b'
            },
            body: JSON.stringify({ message: userInput })
        });

        if (!response.ok) {
            throw new Error(`Error404 ${response.statusText}`); // Обработка ошибки HTTP
        }

        const data = await response.json(); // Парсинг ответа в формате JSON
         // Создание и добавление сообщения бота в чат
        const botMessage = document.createElement('div');
        botMessage.className = 'message bot-message';
        botMessage.textContent = data.reply;
        chatbox.appendChild(botMessage);
        chatbox.scrollTop = chatbox.scrollHeight; // Прокрутка чата вниз

    } catch (error) {
        console.error('Ошибка при выполнении запроса:', error); // Логирование ошибки в консоль
        // Создание и добавление сообщения об ошибке в чат
        const errorMessage = document.createElement('div');
        errorMessage.className = 'message bot-message';
        errorMessage.textContent = `Ошибка: ${error.message}`;
        chatbox.appendChild(errorMessage);
        chatbox.scrollTop = chatbox.scrollHeight; // Прокрутка чата вниз
    }

    document.getElementById('userInput').value = ''; // Очистка поля ввода
}


