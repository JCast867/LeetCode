/* Write your PL/SQL query statement below */
SELECT Customers.name AS Customers FROM Customers
LEFT JOIN Orders ON Customers.id = Orders.customerID
WHERE Orders.customerID IS NULL
ORDER BY Customers.name;