from typing import List, Dict, Any
from db import get_db_connection

def get_customers_by_credit_limit_range():
    """Return customers with credit limits outside the normal range."""
    conn = get_db_connection()
    cursor = conn.cursor()
    query = '''SELECT customerName, creditLimit FROM customers
                WHERE creditLimit < 10000
	                OR creditLimit > 100000'''
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def get_orders_with_null_comments():
    """Return orders that have null comments."""
    conn = get_db_connection()
    cursor = conn.cursor()
    query = '''SELECT orderNumber, comments FROM orders
                WHERE comments IS NULL
                ORDER BY orderDate'''
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def get_first_5_customers():
    """Return the first 5 customers."""
    conn = get_db_connection()
    cursor = conn.cursor()
    query = '''SELECT customerName, contactLastName, contactFirstName FROM customers
                ORDER BY contactLastName
                LIMIT 5'''
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def get_payments_total_and_average():
    """Return total and average payment amounts."""
    conn = get_db_connection()
    cursor = conn.cursor()
    query = 'SELECT AVG(amount), SUM(amount), MIN(amount), MAX(amount) FROM payments'
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def get_employees_with_office_phone():
    """Return employees with their office phone numbers."""
    conn = get_db_connection()
    cursor = conn.cursor()
    query = '''SELECT employees.firstName, employees.lastName, offices.phone
                FROM employees
                INNER JOIN offices ON employees.officeCode = offices.officeCode'''
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def get_customers_with_shipping_dates():
    """Return customers with their order shipping dates."""
    conn = get_db_connection()
    cursor = conn.cursor()
    query = '''SELECT customers.customerName, orders.orderDate FROM customers
                LEFT JOIN orders ON customers.customerNumber = orders.customerNumber'''
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def get_customer_quantity_per_order():
    """Return customer name and quantity for each order."""
    conn = get_db_connection()
    cursor = conn.cursor()
    query = '''SELECT customers.customerName, orderdetails.quantityOrdered FROM customers
                INNER JOIN orders ON customers.customerNumber = orders.customerNumber
                INNER JOIN orderdetails ON orders.orderNumber = orderdetails.orderNumber
                ORDER BY customers.customerName'''
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def get_customers_payments_by_lastname_pattern(pattern: str = "son"):
    """Return customers and payments for last names matching pattern."""
    conn = get_db_connection()
    cursor = conn.cursor()
    query = '''SELECT customers.customerName, customers.contactFirstName, SUM(payments.amount) FROM customers
                INNER JOIN payments ON customers.customerNumber = payments.customerNumber
                WHERE customers.contactFirstName LIKE '%ly%'
                    OR customers.contactFirstName LIKE '%Mu%'
                GROUP BY customers.customerName
                ORDER BY SUM(payments.amount) DESC'''
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result