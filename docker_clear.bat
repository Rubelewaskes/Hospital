@echo off

echo
echo -----------------------------------------------
echo Stopping and removing containers...
echo -----------------------------------------------
echo
docker stop hospital_app postgres_container
docker rm hospital_app postgres_container

echo
echo -----------------------------------------------
echo Removing network...
echo -----------------------------------------------
echo
docker network rm hospital-network

echo
echo -----------------------------------------------
echo Removing images...
echo -----------------------------------------------
echo
docker rmi hospital-app hospital-postgres

echo
echo -----------------------------------------------
echo Job done!
pause