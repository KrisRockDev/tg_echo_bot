# Telegram Echo Bot for Testing

1. **Клонирование репозитория:**  
    Склонируйте репозиторий с помощью команды:
    ```sh
    git clone https://github.com/KrisRockDev/tg_echo_bot.git
    ```
2. **Перейдите в директорию:**  
   Перейдите в директорию tg_echo_bot с помощью команды:
   ```bash
   cd tg_echo_bot
   ```
   
3. **Сборка образа:**  
   Выполните следующую команду в терминале для создания Docker-образа:
   ```bash
   sudo docker build -t my-bot .
   ```

4. **Запуск контейнера:**  
   Запустите контейнер, передав переменную окружения `BOT_TOKEN`:
   ```bash
   sudo docker run \
   --restart on-failure \
   -e BOT_TOKEN='TOKEN' \
   --name tg-bot-container-1 \
   my-bot
   ```
