@echo off

echo
echo -----------------------------------------------
echo Creating network
echo -----------------------------------------------
echo
docker network create hospital-network

echo
echo -----------------------------------------------
echo Building PostgreSQL image...
echo -----------------------------------------------
echo
docker build -t hospital-postgres .\db

echo
echo -----------------------------------------------
echo Starting container with PostgreSQL...
echo -----------------------------------------------
echo
docker run -d --name postgres_container --network hospital-network -p 1266:5432 hospital-postgres

echo
echo -----------------------------------------------
echo Building application image...
echo -----------------------------------------------
echo
docker build -t hospital-app .

echo
echo -----------------------------------------------
echo Starting container with application...
echo -----------------------------------------------
echo
docker run -d --name hospital_app --network hospital-network -p 8000:8000 hospital-app

echo
echo -----------------------------------------------
echo Job done!
pause