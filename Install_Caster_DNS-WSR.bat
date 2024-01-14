@echo off
set currentpath=%~dp0
echo Installation path: %currentpath%
echo Using this python/pip:
<<<<<<< HEAD
c:\python27\python -m pip -V

echo Installing Caster Dependencies for DNS/WSR
c:\python27\python -m pip install -r "%currentpath%requirements.txt"
=======
python -m pip -V

echo Installing Caster Dependencies for DNS/WSR
python -m pip install -r "%currentpath%requirements.txt"
>>>>>>> a6644842494eca21366326a82b2af452b38c5977

pause 1
