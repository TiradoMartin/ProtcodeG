@echo off
:menu
cls
color B
title BIENVENIDO AL CREADOR DE DISCO DURO VIRTUAL (JEHODICK)DE JHV.corp
echo.
echo  BIENVENIDO DIOS LE BENDIGA %USERNAME%
ECHO.
ECHO ELIJE UNA OPCION...
ECHO.
ECHO ======================================== ===
ECHO = 1. CREAR UN DISCO DURO VIRTUAL ==
ECHO = 2. BORRAR EL DISCO DURO VIRTUAL ==
ECHO = 3. SALIR DEL PROGRAMA ==
ECHO ======================================== ===
ECHO.
SET /P ver= QUE DESEA HACER?
if %ver%==1 goto crear
if %ver%==2 goto bo
if %ver%==3 goto salir

:crear
md "G:\disco duro de jehodick"
attrib /d /s -r -h -s" "C:\"
subst I: "C:\disco duro de jehodick"
msg * EL DISCO DURO VIRTUAL SE CREO SATISFACTORIAMENTE
goto menu

:bo
attrib -h "C:\disco duro de jehodick"
rd "c:\disco duro extra"
subst I: /d
msg * EL DISCO DURO VIRTUAL SE BORRO SATISFACTORIAMENTE
goto menu

:salir
msg * M23corporation(JHV)...
exit

