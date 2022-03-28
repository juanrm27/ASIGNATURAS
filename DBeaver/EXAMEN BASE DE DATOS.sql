

/*1. Crear una consulta que muestre el apellido de todos aquellos empleados cuyo nombre empiece por 'a' o por 'b'*/

SELECT e.last_name FROM employees e
WHERE e.first_name LIKE "a%" or e.first_name LIKE "b%"

/*2. Liste los campos de la tabla productos que tengan un precio exactamente 18, 19 y 10 dolares*/
	
SELECT p.* FROM products p
join order_details od on p.id = od.product_id
where unit_price = '18' or unit_price = '19' or unit_price = '10'

/*3. Genere una lista de selección de la tabla Employees (Empleado) con una sola columna de salida y  
ésta contenga los campos: EmployeeID, LastName y FirstName*/

SELECT CONCAT(id ,' ', last_name ,' ', first_name) as datos_empleado
FROM employees e


/*4. Mostrar el nombre del cliente de todos los clientes que han sido atendidos por aquellos 
empleados con una "A" en su apellido*/
	
select c.first_name FROM customers c
join orders o on c.id = o.customer_id
join employees e on o.employee_id = e.id
WHERE e.last_name like "%a%"


/*5. Crear una consulta que muestre el nombre aquellos clientes cuyo pais es USA, SPAIN o ITALY*/

SELECT first_name FROM customers c
where country_region = 'USA' or country_region = 'SPAIN' or country_region = 'ITALY'