/*
CONSULTAS
          
    1.  Código y nombre de todos los departamentos.
    2.     Mes y ejercicio de los justificantes de nómina pertenecientes al empleado cuyo código es 1.
    3.     Código y nombre de los empleados ordenados ascendentemente por nombre.
    4.     Código y número de cuenta de los empleados cuyo nombre empieze por 'A' o por 'J'.
    5.     Número de empleados que hay en la base de datos.
    6.     Nombre y número de hijos de los empleados cuya retención es: 8, 10 o 12.
    7.     Número de hijos y número de empleados agrupados por hijos, mostrando sólo los grupos cuyo número de empleados sea mayor que 1.
    8.     Número de hijos, retención máxima, mínima y media de los empleados agrupados por hijos.
    9.     Nombre y función de los empleados que han trabajado en el departamento 1.
    10.     Nombre del empleado y nombre del departamento en el que han trabajado empleados que no tienen hijos.
    11.     Nombre del empleado, mes y ejercicio de sus justificantes de nómina, número de línea y cantidad de las líneas de los justificantes para el empleado cuyo código=1.
    12.     Nombre del empleado e ingresos totales percibidos agrupados por nombre.
    13.     Número de empleados cuyo número de hijos es superior a la media de hijos de los empleados.
    14.     Nombre de los empleados que más hijos tienen o que menos hijos tienen.
    15.     Nombre de los empleados que no tienen justificante de nóminas.
    16.     Nombre de los empleados, nombre de los departamentos en los que ha trabajado y función en mayúsculas que ha realizado en cada departamento.
    17.     Nombre, fecha de nacimiento y nombre del día de la semana de su fecha de nacimiento de todos los empleados.
    18.     Nombre y edad de los empleados.
    19.     Nombre, edad y número de hijos de los empleados que tienen menos de 40 años y tienen hijos.
    20.     Nombre e ingresos percibidos empleado más joven y del más longevo.   

*/

-- 1.  Código y nombre de todos los departamentos.
SELECT * FROM Departamentos d 

-- 2.     Mes y ejercicio de los justificantes de nómina pertenecientes al empleado cuyo código es 1.
SELECT mes, ejercicio FROM Just_nominas jn where cod_emp = 1

-- 3.     Código y nombre de los empleados ordenados ascendentemente por nombre.
SELECT codigo, nombre from Empleados e order by nombre 


-- 4.     Código y número de cuenta de los empleados cuyo nombre empieze por 'A' o por 'J'.
SELECT codigo, cuenta, nombre from Empleados e where left(nombre,1) = 'A' or left(nombre,1) = 'J'

-- 5.     Número de empleados que hay en la base de datos.
SELECT 


-- 6.     Nombre y número de hijos de los empleados cuya retención es: 8, 10 o 12.


-- 7.     Número de hijos y número de empleados agrupados por hijos, mostrando sólo los grupos cuyo número de empleados sea mayor que 1.


-- 8.     Número de hijos, retención máxima, mínima y media de los empleados agrupados por hijos.


-- 9.     Nombre y función de los empleados que han trabajado en el departamento 1.


-- 10.    Nombre del empleado y nombre del departamento en el que han trabajado empleados que no tienen hijos.


















