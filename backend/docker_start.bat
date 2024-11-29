@echo off


echo
echo -----------------------------------------------
echo Starting container with PostgreSQL...
echo -----------------------------------------------
echo
docker run -d --name postgres_container --network hospital-network -p 1266:5432 hospital-postgres

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