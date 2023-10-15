echo "" >> ./backend/.env
echo "" >> ./frontend/.env
echo "" >> .env

docker compose down -v --remove-orphans

docker compose build
docker compose up -d
