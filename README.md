# Telegram Echo Bot for Testing

1. **Клонирование репозитория:**  
    Склонируйте репозиторий с помощью команды:
    ```
    https://github.com/KrisRockDev/tg_echo_bot.git
    ```
2. **Сборка образа:**  
   Выполните следующую команду в терминале для создания Docker-образа:
   ```bash
   sudo docker build -t my-bot .
   ```

3. **Запуск контейнера:**  
   Запустите контейнер, передав переменную окружения `BOT_TOKEN`:
   ```bash
   sudo docker run \ 
   -e BOT_TOKEN=<ваш токен бота> \
   --name tg-bot-container-1 \
   my-bot
   ```