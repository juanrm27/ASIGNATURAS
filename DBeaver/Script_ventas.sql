
/* Consultas bd Ventas

Consultas sobre una tabla
1. Devuelve un listado con todos los pedidos que se han realizado. Los pedidos deben estar ordenados por la fecha de realización, mostrando en primer lugar los pedidos más recientes.
2. Devuelve todos los datos de los dos pedidos de mayor valor.
3. Devuelve un listado con los identificadores de los clientes que han realizado algún pedido. Tenga en cuenta que no debe mostrar identificadores que estén repetidos.
4. Devuelve un listado de todos los pedidos que se realizaron durante el año 2017, cuya cantidad total sea superior a 500€.
5. Devuelve un listado con el nombre y los apellidos de los comerciales que tienen una comisión entre 0.05 y 0.11.
6. Devuelve el valor de la comisión de mayor valor que existe en la tabla comercial .
7. Devuelve el identificador, nombre y primer apellido de aquellos clientes cuyo segundo apellido no es NULL . El listado deberá estar ordenado alfabéticamente por apellidos y nombre.
8. Devuelve un listado de los nombres de los clientes que empiezan por A y terminan por n y también los nombres que empiezan por P . El listado deberá estar ordenado alfabéticamente.
9. Devuelve un listado de los nombres de los clientes que no empiezan por A . El listado deberá estar ordenado alfabéticamente.
10. Devuelve un listado con los nombres de los comerciales que terminan por el o o . Tenga en cuenta que se deberán eliminar los nombres repetidos.

Consultas multitabla

1. Devuelve un listado con el identificador, nombre y los apellidos de todos los clientes que han realizado algún pedido. El listado debe estar ordenado alfabéticamente y se deben eliminar los elementos repetidos.
2. Devuelve un listado que muestre todos los pedidos que ha realizado cada cliente. El resultado debe mostrar todos los datos de los pedidos y del cliente. El listado debe mostrar los datos de los clientes ordenados alfabéticamente.
3. Devuelve un listado que muestre todos los pedidos en los que ha participado un comercial. El resultado debe mostrar todos los datos de los pedidos y de los comerciales. El listado debe mostrar los datos de los comerciales ordenados alfabéticamente.
4. Devuelve un listado que muestre todos los clientes, con todos los pedidos que han realizado y con los datos de los comerciales asociados a cada pedido.
5. Devuelve un listado de todos los clientes que realizaron un pedido durante el año 2017 , cuya cantidad esté entre 300 € y 1000 €.
6. Devuelve el nombre y los apellidos de todos los comerciales que ha participado en algún pedido realizado por María Santana Moreno .
7. Devuelve el nombre de todos los clientes que han realizado algún pedido con el comercial Daniel Sáez Vega .
8. Devuelve un listado con todos los clientes junto con los datos de los pedidos que han realizado. Este listado también debe incluir los clientes que no han realizado ningún pedido. El listado debe estar ordenado alfabéticamente por el primer apellido, segundo apellido y nombre de los clientes.
2. Devuelve un listado con todos los comerciales junto con los datos de los pedidos que han realizado. Este listado también debe incluir los comerciales que no han realizado ningún pedido. El listado debe estar ordenado alfabéticamente por el primer apellido, segundo apellido y nombre de los comerciales.
3. Devuelve un listado que solamente muestre los clientes que no han realizado ningún pedido. 
4. Devuelve un listado que solamente muestre los comerciales que no han realizado ningún pedido.
5. Devuelve un listado con los clientes que no han realizado ningún pedido y de los comerciales que no han participado en ningún pedido. Ordene el listado alfabéticamente por los apellidos y el nombre. En en listado deberá diferenciar de algún modo los clientes y los comerciales.

Consultas resumen

1. Calcula la cantidad total que suman todos los pedidos que aparecen en la tabla pedido .
2. Calcula la cantidad media de todos los pedidos que aparecen en la tabla pedido .
3. Calcula el número total de comerciales distintos que aparecen en la tabla pedido .
4. Calcula el número total de clientes que aparecen en la tabla cliente .
5. Calcula cuál es la mayor cantidad que aparece en la tabla pedido .
6. Calcula cuál es la menor cantidad que aparece en la tabla pedido .
7. Calcula cuál es el valor máximo de categoría para cada una de las ciudades que aparece en la tabla cliente .
8. Calcula cuál es el máximo valor de los pedidos realizados durante el mismo día para cada uno de los clientes. Es decir, el mismo cliente puede haber realizado varios pedidos de diferentes cantidades el mismo día. Se pide que se calcule cuál es el pedido de máximo valor para cada uno de los días en los que un cliente ha realizado un pedido. Muestra el identificador del cliente, nombre, apellidos, la fecha y el valor de la cantidad.
9. Calcula cuál es el máximo valor de los pedidos realizados durante el mismo día para cada uno de los clientes, teniendo en cuenta que sólo queremos mostrar aquellos pedidos que superen la cantidad de 2000 €.
10. Calcula el máximo valor de los pedidos realizados para cada uno de los comerciales durante la fecha 2016-08-17 . Muestra el identificador del comercial, nombre, apellidos y total.
11. Devuelve un listado con el identificador de cliente, nombre y apellidos y el número total de pedidos que ha realizado cada uno de clientes. Tenga en cuenta que pueden existir clientes que no han realizado ningún pedido. Estos clientes también deben aparecer en el listado indicando que el número de pedidos realizados es 0 .
12. Devuelve un listado con el identificador de cliente, nombre y apellidos y el número total de pedidos que ha realizado cada uno de clientes durante el año 2017.
*/

-- 1. Devuelve un listado con todos los pedidos que se han realizado. Los pedidos deben estar ordenados por la fecha de realización, mostrando en primer lugar los pedidos más recientes.
SELECT * from pedido p order by p.fecha DESC

-- 2. Devuelve todos los datos de los dos pedidos de mayor valor.
SELECT * from pedido p order by total DESC limit 2

-- 3. Devuelve un listado con los identificadores de los clientes que han realizado algún pedido. Tenga en cuenta que no debe mostrar identificadores que estén repetidos.
SELECT DISTINCT id_cliente from pedido p 

-- 4. Devuelve un listado de todos los pedidos que se realizaron durante el año 2017, cuya cantidad total sea superior a 500€.
SELECT fecha, total from pedido p where YEAR(p.fecha) = 2017 and total >= 500

-- 5. Devuelve un listado con el nombre y los apellidos de los comerciales que tienen una comisión entre 0.05 y 0.11.
SELECT nombre, apellido1, apellido2, comisión from comercial c where c.comisión >= 0.05 and c.comisión <= 0.11

-- 6. Devuelve el valor de la comisión de mayor valor que existe en la tabla comercial .
SELECT c.comisión from comercial c order by c.comisión DESC limit 1

-- 7. Devuelve el identificador, nombre y primer apellido de aquellos clientes cuyo segundo apellido no es NULL . El listado deberá estar ordenado alfabéticamente por apellidos y nombre.
SELECT id, nombre, apellido1 from cliente c where c.apellido2 is not NULL order by apellido1 , nombre

-- 8. Devuelve un listado de los nombres de los clientes que empiezan por A y terminan por n y también los nombres que empiezan por P . El listado deberá estar ordenado alfabéticamente.
SELECT nombre from cliente c where left(nombre,1) = 'A' and RIGHT(nombre,1) = 'N' or left(nombre,1) = 'P' order by nombre

-- 9. Devuelve un listado de los nombres de los clientes que no empiezan por A . El listado deberá estar ordenado alfabéticamente.


-- 10. Devuelve un listado con los nombres de los comerciales que terminan por el o o . Tenga en cuenta que se deberán eliminar los nombres repetidos.










