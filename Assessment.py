# employee class code in Python
# class definition
class Employee:
    __id=0
    __name=""
    __Age=""
	
	# function to set data 
    def setData(self,id,name,Age):
        self.__id= id
        self.__name = name
        self.__Age = Age
	
	# function to get/print data
    def showData(self):
        print("Id\t:",self.__id)
        print("Name\t:", self.__name)
        print("Age\t:", self.__Age)

# main function definition
def main():
    #Employee Object
    emp=Employee()
    emp.setData(1,'syed','26')
    emp.showData()
	
if __name__=="__main__":
    main()
    