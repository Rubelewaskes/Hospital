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
echo Job done!
pause