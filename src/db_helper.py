import mysql.connector

try:
    mydb = mysql.connector.connect(host='localhost', user='root',
                                   password='password',
                                   database='Northwind')
    mycursor = mydb.cursor()
except Exception as err:
    print("Error in connecting", err)


class DbHelper:
    def get_maximum_salary(self):
        '''
        Implement the logic to find and return maximum salary from employee table
        '''
        QUERY = 'SELECT max(Salary) FROM Employees;'
        mycursor.execute(QUERY)
        max_data = mycursor.fetchall()
        print("inside max sal")
        return max_data[0][0]

    def get_minimum_salary(self):
        '''
        Implement the logic to find and return minimum salary from employee table
        '''
        QUERY = 'SELECT min(Salary) FROM Employees;'
        mycursor.execute(QUERY)
        min_data = mycursor.fetchall()
        print("inside min sal")
        return min_data[0][0]

if __name__ == "__main__":
    db_helper = DbHelper()
    min_salary = db_helper.get_minimum_salary()
    max_salary = db_helper.get_maximum_salary()
    print(max_salary)
    print(min_salary)